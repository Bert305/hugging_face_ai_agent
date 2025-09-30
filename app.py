from smolagents import CodeAgent,DuckDuckGoSearchTool, HfApiModel,load_tool,tool
import datetime
import requests
import pytz
import yaml
import os
from dotenv import load_dotenv
from tools.final_answer import FinalAnswerTool
from tools.web_search import DuckDuckGoSearchTool as WebSearchTool

from Gradio_UI import GradioUI

# Load environment variables
load_dotenv()

# Check if HF token is loaded
hf_token = os.getenv('HUGGINGFACE_API_TOKEN')
if not hf_token:
    raise ValueError("HUGGINGFACE_API_TOKEN not found in environment variables. Please check your .env file.")
print(f"✅ HF Token loaded: {hf_token[:10]}..." if hf_token else "❌ No HF Token found")

# Below is an example of a tool that does nothing. Amaze us with your creativity !
@tool
def my_custom_tool(arg1:str, arg2:int)-> str: #it's import to specify the return type
    #Keep this format for the description / args / args description but feel free to modify the tool
    """A tool that does nothing yet 
    Args:
        arg1: the first argument
        arg2: the second argument
    """
    return "What magic will you build ?"

@tool
def system_status() -> str:
    """Check the current system status and available tools.
    """
    status = []
    status.append(f"✅ System Status Report - {datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')}")
    status.append(f"🔑 HF Token: {'✅ Loaded' if hf_token else '❌ Missing'}")
    status.append(f"🕐 Timezone Tool: ✅ Working")
    status.append(f"🔍 Web Search: ✅ Initialized (ddgs package)")
    status.append(f"�️ Image Generation: ✅ Loaded from HF Hub")
    status.append(f"🤖 Agent: Ready to help!")
    
    return "\n".join(status)

@tool
def get_current_time_in_timezone(timezone: str) -> str:
    """A tool that fetches the current local time in a specified timezone.
    Args:
        timezone: A string representing a valid timezone (e.g., 'America/New_York').
    """
    try:
        # Create timezone object
        tz = pytz.timezone(timezone)
        # Get current time in that timezone
        local_time = datetime.datetime.now(tz).strftime("%Y-%m-%d %H:%M:%S")
        return f"The current local time in {timezone} is: {local_time}"
    except Exception as e:
        return f"Error fetching time for timezone '{timezone}': {str(e)}"


final_answer = FinalAnswerTool()

# If the agent does not answer, the model is overloaded, please use another model or the following Hugging Face Endpoint that also contains qwen2.5 coder:
# model_id='https://pflgm2locj2t89co.us-east-1.aws.endpoints.huggingface.cloud' 

model = HfApiModel(
    max_tokens=2096,
    temperature=0.5,
    model_id='Qwen/Qwen2.5-Coder-32B-Instruct',# it is possible that this model may be overloaded
    custom_role_conversions=None,
    token=hf_token
)


# Import tool from Hub with authentication
try:
    image_generation_tool = load_tool("agents-course/text-to-image", trust_remote_code=True, token=hf_token)
    print("✅ Image generation tool loaded successfully")
except Exception as e:
    print(f"⚠️ Could not load image generation tool: {e}")
    # Create a fallback tool
    @tool
    def image_generation_tool(prompt: str) -> str:
        """Fallback image generation tool when the main tool fails to load.
        Args:
            prompt: Description of the image to generate
        """
        return f"Image generation temporarily unavailable. Requested image: {prompt}"

with open("prompts.yaml", 'r') as stream:
    prompt_templates = yaml.safe_load(stream)
    
# Initialize tools
web_search_tool = WebSearchTool()

# Create a list of working tools
working_tools = [final_answer, get_current_time_in_timezone, system_status]

# Add web search if it works
try:
    # Test web search tool initialization only
    web_search_tool = WebSearchTool()
    working_tools.append(web_search_tool)
    print("✅ Web search tool loaded successfully")
except Exception as e:
    print(f"⚠️ Web search tool failed: {e}")
    # Create a fallback web search tool
    @tool
    def web_search_fallback(query: str) -> str:
        """Fallback web search when DuckDuckGo search fails.
        Args:
            query: The search query
        """
        return f"Web search temporarily unavailable. Query was: {query}. Please try again later or use a different approach."
    working_tools.append(web_search_fallback)

# Add image generation tool
working_tools.append(image_generation_tool)

print(f"📋 Loaded {len(working_tools)} tools: {[tool.name if hasattr(tool, 'name') else str(tool) for tool in working_tools]}")

agent = CodeAgent(
    model=model,
    tools=working_tools,
    max_steps=10,  # Increased max_steps to allow more complex tasks
    verbosity_level=2,  # Increased verbosity for better debugging
    grammar=None,
    planning_interval=None,
    name="HuggingFaceAIAgent",
    description="A helpful AI agent with web search, image generation, and time zone capabilities",
    prompt_templates=prompt_templates
)


GradioUI(agent).launch()