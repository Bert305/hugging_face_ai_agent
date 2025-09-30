import os
from smolagents.tools import Tool
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

class OpenAITextAnalysisTool(Tool):
    name = "text_analysis"
    description = "Analyze text for sentiment, summarization, translation, or other advanced text processing using OpenAI"
    inputs = {
        'text': {'type': 'string', 'description': 'The text to analyze'},
        'task': {'type': 'string', 'description': 'Type of analysis: sentiment, summary, translate, grammar_check, etc.', 'nullable': True}
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def forward(self, text: str, task: str = "summary") -> str:
        try:
            if task == "sentiment":
                prompt = f"Analyze the sentiment of this text and provide a detailed explanation:\n\n{text}"
            elif task == "summary":
                prompt = f"Provide a concise summary of this text:\n\n{text}"
            elif task == "translate":
                prompt = f"Translate this text to English:\n\n{text}"
            elif task == "grammar_check":
                prompt = f"Check and correct grammar in this text:\n\n{text}"
            else:
                prompt = f"Analyze this text for {task}:\n\n{text}"

            response = self.client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1000,
                temperature=0.3
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error in text analysis: {str(e)}"

class OpenAICodeReviewTool(Tool):
    name = "code_review"
    description = "Review and improve code quality, suggest optimizations, and find bugs using OpenAI"
    inputs = {
        'code': {'type': 'string', 'description': 'The code to review'},
        'language': {'type': 'string', 'description': 'Programming language (python, javascript, etc.)', 'nullable': True}
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def forward(self, code: str, language: str = "python") -> str:
        try:
            prompt = f"""
            Please review this {language} code and provide:
            1. Code quality assessment
            2. Potential bugs or issues
            3. Performance optimizations
            4. Best practice suggestions
            5. Improved version if needed

            Code:
            ```{language}
            {code}
            ```
            """

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[{"role": "user", "content": prompt}],
                max_tokens=1500,
                temperature=0.2
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error in code review: {str(e)}"

class OpenAICreativeWritingTool(Tool):
    name = "creative_writing"
    description = "Generate creative content like stories, poems, articles, or marketing copy using OpenAI"
    inputs = {
        'prompt': {'type': 'string', 'description': 'What you want to create (e.g., "write a story about a robot")'},
        'style': {'type': 'string', 'description': 'Writing style: story, poem, article, marketing, technical, etc.', 'nullable': True}
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.client = OpenAI(api_key=os.getenv('OPENAI_API_KEY'))

    def forward(self, prompt: str, style: str = "story") -> str:
        try:
            if style == "story":
                system_prompt = "You are a creative storyteller. Write engaging, well-structured stories with vivid descriptions and compelling characters."
            elif style == "poem":
                system_prompt = "You are a poet. Create beautiful, meaningful poetry with good rhythm and imagery."
            elif style == "article":
                system_prompt = "You are a professional writer. Create informative, well-researched articles with clear structure."
            elif style == "marketing":
                system_prompt = "You are a marketing copywriter. Create persuasive, engaging marketing content that drives action."
            else:
                system_prompt = f"You are a {style} writer. Create high-quality content in the {style} style."

            response = self.client.chat.completions.create(
                model="gpt-4o-mini",
                messages=[
                    {"role": "system", "content": system_prompt},
                    {"role": "user", "content": prompt}
                ],
                max_tokens=1500,
                temperature=0.7
            )
            
            return response.choices[0].message.content
            
        except Exception as e:
            return f"Error in creative writing: {str(e)}"