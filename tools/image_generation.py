import os
import requests
from smolagents.tools import Tool
from dotenv import load_dotenv

load_dotenv()

class HuggingFaceImageGenerationTool(Tool):
    name = "image_generation"
    description = "Generate images from text descriptions using Stable Diffusion via HuggingFace Inference API"
    inputs = {
        'prompt': {'type': 'string', 'description': 'Description of the image to generate'}
    }
    output_type = "string"

    def __init__(self):
        super().__init__()
        self.api_token = os.getenv('HUGGINGFACE_API_TOKEN')
        self.api_url = "https://api-inference.huggingface.co/models/stabilityai/stable-diffusion-xl-base-1.0"
        self.headers = {"Authorization": f"Bearer {self.api_token}"}

    def forward(self, prompt: str) -> str:
        """Generate an image from a text prompt using HuggingFace Inference API"""
        try:
            if not self.api_token:
                return "❌ Image generation unavailable: HuggingFace API token not found"
            
            # Clean and enhance the prompt
            enhanced_prompt = f"{prompt}, high quality, detailed, professional"
            
            payload = {
                "inputs": enhanced_prompt,
                "parameters": {
                    "num_inference_steps": 30,
                    "guidance_scale": 7.5,
                    "width": 512,
                    "height": 512
                }
            }
            
            response = requests.post(self.api_url, headers=self.headers, json=payload, timeout=60)
            
            if response.status_code == 200:
                # Save the image temporarily (in a real deployment, you'd want to save to a proper location)
                image_filename = f"generated_image_{hash(prompt) % 10000}.png"
                image_path = f"./temp_images/{image_filename}"
                
                # Create temp directory if it doesn't exist
                os.makedirs("./temp_images", exist_ok=True)
                
                with open(image_path, "wb") as f:
                    f.write(response.content)
                
                return f"✅ Image generated successfully! Saved as: {image_filename}\n📝 Prompt used: {enhanced_prompt}\n📁 Location: {image_path}"
            
            elif response.status_code == 503:
                return f"⏳ Image generation service is loading. Please try again in a few moments.\n📝 Prompt: {prompt}"
            
            else:
                return f"❌ Image generation failed (Status: {response.status_code})\n📝 Prompt: {prompt}\n💡 Try a different description or wait a moment"
                
        except requests.exceptions.Timeout:
            return f"⏰ Image generation timed out. The service might be busy.\n📝 Prompt: {prompt}\n💡 Try again with a simpler prompt"
        
        except Exception as e:
            return f"❌ Image generation error: {str(e)}\n📝 Prompt: {prompt}\n💡 Please check your HuggingFace API token and try again"

# Alternative simple tool for web search of images
class ImageSearchTool(Tool):
    name = "image_search"
    description = "Search for existing images on the web related to your query"
    inputs = {
        'query': {'type': 'string', 'description': 'What kind of image to search for'}
    }
    output_type = "string"

    def forward(self, query: str) -> str:
        """Provide suggestions for finding images online"""
        search_suggestions = [
            f"🔍 **Image Search Suggestions for '{query}':**",
            "",
            f"📸 **Recommended Sources:**",
            f"• Unsplash: https://unsplash.com/s/photos/{query.replace(' ', '-')}",
            f"• Pexels: https://www.pexels.com/search/{query.replace(' ', '%20')}/",
            f"• Pixabay: https://pixabay.com/images/search/{query.replace(' ', '-')}/",
            f"• Wikimedia Commons: https://commons.wikimedia.org/wiki/Special:Search?search={query}",
            "",
            f"🎨 **For AI-Generated Images:**",
            f"• Try generating with a more specific prompt",
            f"• Consider style keywords: 'photorealistic', 'artistic', 'cartoon', 'sketch'",
            f"• Add quality modifiers: 'high resolution', 'detailed', 'professional'",
            "",
            f"💡 **Alternative Approach:**",
            f"If image generation fails, you can describe the image in detail instead!"
        ]
        
        return "\n".join(search_suggestions)