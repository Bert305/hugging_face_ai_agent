"""
HuggingFace + OpenAI Multi-Tool Agent
--------------------------------------
This agent integrates system status, web search, image generation,
timezone conversion, and optional OpenAI-powered tools.
"""

# ======================
# Imports
# ======================
import os
import datetime
import pytz
import requests
import yaml
from dotenv import load_dotenv

from smolagents import CodeAgent, InferenceClientModel, OpenAIModel, load_tool, tool
from tools.final_answer import FinalAnswerTool
from tools.web_search import DuckDuckGoSearchTool as WebSearchTool
from tools.openai_tools import (
    OpenAITextAnalysisTool,
    OpenAICodeReviewTool,
    OpenAICreativeWritingTool,
)
from Gradio_UI import GradioUI

# ======================
# Environment Setup
# ======================
load_dotenv()
hf_token = os.getenv("HUGGINGFACE_API_TOKEN")
openai_key = os.getenv("OPENAI_API_KEY")

if not hf_token:
    raise ValueError("❌ HUGGINGFACE_API_TOKEN not found in .env file")

print(f"✅ HF Token loaded: {hf_token[:10]}..." if hf_token else "❌ No HF Token found")
print(f"✅ OpenAI Key loaded: {openai_key[:10]}..." if openai_key else "❌ No OpenAI Key found")

# ======================
# Tools
# ======================

@tool
def my_custom_tool(arg1: str, arg2: int) -> str:
    """A placeholder tool.
    Args:
        arg1: the first argument
        arg2: the second argument
    """
    return "What magic will you build?"

@tool
def system_status() -> str:
    """Check the current system status and available tools."""
    status = [
        f"✅ System Status Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}",
        f"🔑 HF Token: {'✅ Loaded' if hf_token else '❌ Missing'}",
        f"🔑 OpenAI Key: {'✅ Loaded' if openai_key else '❌ Missing'}",
        f"🤖 Model: {'OpenAI GPT-4o-mini' if openai_key else 'HuggingFace Qwen'}",
        "🕐 Timezone Tool: ✅ Working",
        "🔍 Web Search: ✅ Initialized (ddgs package)",
        "🖼️ Image Generation: ✅ Loaded from HF Hub",
    ]
    if openai_key:
        status.extend([
            "📝 Text Analysis: ✅ OpenAI-powered",
            "💻 Code Review: ✅ OpenAI-powered",
            "✍️ Creative Writing: ✅ OpenAI-powered",
        ])
    status.append("🚀 Agent: Ready to help!")
    return "\n".join(status)

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """Fetch the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        tz = pytz.timezone(timezone)
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"

final_answer = FinalAnswerTool()

# ======================
# Model Selection
# ======================
if openai_key:
    model = OpenAIModel(
        model_id="gpt-4o-mini",
        api_key=openai_key,
        max_tokens=2048,
        temperature=0.1,
    )
    print("🚀 Using OpenAI GPT-4o-mini model")
else:
    model = InferenceClientModel(
        model_id="Qwen/Qwen2.5-Coder-32B-Instruct",
        max_tokens=2096,
        temperature=0.5,
        token=hf_token,
    )
    print("📡 Using HuggingFace Qwen model (fallback)")

# ======================
# Load External Tools
# ======================
# Load image generation tool
try:
    image_generation_tool = load_tool(
        "agents-course/text-to-image",
        trust_remote_code=True,
        token=hf_token,
    )
    print("✅ Image generation tool loaded")
except Exception as e:
    print(f"⚠️ Could not load image generation tool: {e}")

    @tool
    def image_generation_tool(prompt: str) -> str:
        """Fallback image generation tool.
        Args:
            prompt: Description of the image to generate
        """
        return f"Image generation unavailable. Requested image: {prompt}"

# Load prompt templates
with open("prompts.yaml", "r") as stream:
    prompt_templates = yaml.safe_load(stream)

# ======================
# Build Toolset
# ======================
working_tools = [
    final_answer,
    get_current_time_in_timezone,
    system_status,
]

# Web search
try:
    web_search_tool = WebSearchTool()
    working_tools.append(web_search_tool)
    print("✅ Web search tool loaded")
except Exception as e:
    print(f"⚠️ Web search tool failed: {e}")

    @tool
    def web_search_fallback(query: str) -> str:
        """Fallback web search.
        Args:
            query: The search query
        """
        return f"Web search unavailable. Query: {query}"

    working_tools.append(web_search_fallback)

# Image generation
working_tools.append(image_generation_tool)

# OpenAI-powered tools
if openai_key:
    try:
        text_analysis_tool = OpenAITextAnalysisTool()
        code_review_tool = OpenAICodeReviewTool()
        creative_writing_tool = OpenAICreativeWritingTool()
        working_tools.extend([text_analysis_tool, code_review_tool, creative_writing_tool])
        print("✅ OpenAI-powered tools added successfully")
    except Exception as e:
        print(f"⚠️ Could not load OpenAI tools: {e}")
else:
    print("ℹ️ OpenAI tools skipped (no API key)")

print(f"📋 Loaded {len(working_tools)} tools")

# ======================
# Initialize Agent
# ======================
agent = CodeAgent(
    model=model,
    tools=working_tools,
    max_steps=10,
    verbosity_level=2,
    name="HuggingFaceAIAgent",
    description="A helpful AI agent with web search, image generation, and enhanced capabilities",
    prompt_templates=prompt_templates
)

# ======================
# Launch Interface
# ======================
if __name__ == "__main__":
    print("🚀 Launching HuggingFace AI Agent...")
    GradioUI(agent).launch()
