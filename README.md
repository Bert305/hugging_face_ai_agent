---
title: HuggingFace + OpenAI Multi-Tool AI Agent
emoji: 🤖
colorFrom: blue
colorTo: purple
sdk: gradio
sdk_version: 5.23.1
app_file: app.py
pinned: false
tags:
- smolagents
- openai
- agent
- multi-tool
- web-search
- image-generation
- text-analysis
- code-review
- creative-writing
---

# 🤖 HuggingFace + OpenAI Multi-Tool AI Agent

A powerful AI agent that combines the best of HuggingFace and OpenAI technologies, featuring 8 integrated tools for comprehensive assistance.

## ✨ Features

### 🧠 **Dual AI Model Support**
- **Premium Mode**: OpenAI GPT-4o-mini for enhanced reasoning and performance
- **Fallback Mode**: HuggingFace Qwen2.5-Coder-32B-Instruct for reliable operation

### 🛠️ **9 Integrated Tools**

1. **🔍 Web Search** - Real-time web search using DuckDuckGo
2. **🖼️ Image Generation** - Custom Stable Diffusion XL implementation via HuggingFace Inference API
3. **🔎 Image Search** - Web-based image search suggestions and resources
4. **🕐 Timezone Conversion** - Get current time in any timezone worldwide
5. **📝 Text Analysis** - Sentiment analysis, summarization, translation (OpenAI-powered)
6. **💻 Code Review** - Code quality assessment and optimization suggestions (OpenAI-powered)
7. **✍️ Creative Writing** - Stories, poems, articles, marketing copy (OpenAI-powered)
8. **📊 System Status** - Real-time monitoring of all agent capabilities
9. **✅ Final Answer** - Structured response delivery system

## 🚀 Quick Start

### Prerequisites
- Python 3.8+
- HuggingFace API token
- OpenAI API key (optional but recommended for enhanced features)

### Installation
1. Clone the repository
2. Create a virtual environment:
   ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # Linux/Mac
   ```
3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```
4. Set up environment variables in `.env`:
   ```
   HUGGINGFACE_API_TOKEN=your_hf_token_here
   OPENAI_API_KEY=your_openai_key_here
   ```
5. Run the agent:
   ```bash
   python app.py
   ```

### Access
The agent will be available at: **http://127.0.0.1:7860**

## 🆕 Recent Updates

### **Image Generation Enhancement (Latest)**
- ✅ **Fixed API Authentication Issues** - Resolved "You must provide an api_key" errors
- 🎨 **Custom Stable Diffusion Integration** - Direct HuggingFace Inference API implementation
- 🖼️ **Enhanced Image Quality** - Automatic prompt enhancement with quality modifiers
- 💾 **Local Image Saving** - Generated images saved to `./temp_images/` directory
- 🔍 **Image Search Fallback** - Alternative image search suggestions when generation fails
- ⚡ **Improved Error Handling** - Better user feedback for various scenarios
- 📁 **File Management** - Organized image storage with unique filenames

### **What's New:**
- **9 Tools Total** (up from 8) - Added dedicated image search tool
- **Robust Image Generation** - Uses `stabilityai/stable-diffusion-xl-base-1.0`
- **No More API Errors** - Proper token authentication and error recovery
- **Enhanced User Experience** - Clear feedback and fallback options

## 💬 Example Queries

### Web Search & Information
- "What's the latest news about artificial intelligence?"
- "Search for Python programming tutorials"
- "Find information about climate change research"

### Image Generation & Search
- "Generate an image of a sunset over mountains"
- "Create a picture of a futuristic robot"
- "Make an image of a cozy coffee shop"
- "Generate a high-resolution image of a peaceful garden"
- "Search for images of dogs if generation fails"
- "Find pictures of modern architecture online"

### Text Analysis (OpenAI-Enhanced)
- "Analyze the sentiment of this text: 'I love this new AI agent!'"
- "Summarize this article: [long text]"
- "Translate this to English: 'Bonjour, comment allez-vous?'"

### Code Review (OpenAI-Enhanced)
- "Review this Python code: `def hello(): print('world')`"
- "Check this JavaScript for bugs"
- "Optimize this SQL query"

### Creative Writing (OpenAI-Enhanced)
- "Write a short story about a robot learning to paint"
- "Create a poem about artificial intelligence"
- "Write a marketing email for a new mobile app"

### System & Utilities
- "Check system status"
- "What time is it in Tokyo?"
- "Show me all available tools"

## 🏗️ Architecture

```
app.py                 # Main application and agent initialization
├── tools/
│   ├── final_answer.py      # Structured response delivery
│   ├── web_search.py        # DuckDuckGo search integration
│   └── openai_tools.py      # OpenAI-powered enhancement tools
├── Gradio_UI.py            # Custom Gradio interface with streaming
├── prompts.yaml            # Agent prompt templates
├── requirements.txt        # Python dependencies
└── .env                    # Environment variables (create this)
```

## 🔧 Technical Details

### Dependencies
- **smolagents**: v1.13.0 - Core agent framework
- **gradio**: v5.23.1 - Web interface
- **openai**: Latest - OpenAI API integration
- **ddgs**: Latest - DuckDuckGo search
- **python-dotenv**: Environment variable management
- **pytz**: Timezone handling
- **pyyaml**: Configuration management

### Model Configuration
- **OpenAI Model**: GPT-4o-mini with 2048 max tokens, 0.1 temperature
- **HuggingFace Model**: Qwen/Qwen2.5-Coder-32B-Instruct with 2096 max tokens, 0.5 temperature

### Tool Enhancement
- **OpenAI Integration** - GPT-3.5-turbo for text analysis, code review, and creative writing
- **Custom Image Generation** - Direct Stable Diffusion XL API implementation
- **Image Processing** - Automatic prompt enhancement and quality optimization
- **Comprehensive Error Handling** - Fallback mechanisms for all tools
- **File Management** - Organized storage for generated images
- **Real-time System Status** - Monitoring of all 9 agent capabilities

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🎓 Learning Journey & Achievements

This project represents the culmination of comprehensive AI agent development training:

### � **Course Documentation**
- **[Complete Course Notes & Documentation](https://docs.google.com/document/d/1vHNgp8yaSmCnY-iqVOGMVTacrMUvZEQNtsszaUe1jK8/edit?usp=sharing)** - Detailed notes and insights from the HuggingFace Agents course

### 🏆 **Certification**
- **[HuggingFace Agents Course Certificate](https://cas-bridge.xethub.hf.co/xet-bridge-us/67a47037749ea2c4b9fafd4b/d8d1a66c162fe3df9d9897b55c2348080aa649f5cff8b2d45170c72e79423e60?X-Amz-Algorithm=AWS4-HMAC-SHA256&X-Amz-Content-Sha256=UNSIGNED-PAYLOAD&X-Amz-Credential=cas%2F20250930%2Fus-east-1%2Fs3%2Faws4_request&X-Amz-Date=20250930T043928Z&X-Amz-Expires=3600&X-Amz-Signature=07907a008a2690ce21f4f20463cf9101294af0633fdebf58ac434e7e89cfafe1&X-Amz-SignedHeaders=host&X-Xet-Cas-Uid=6818393441450cf054a221a2&response-content-disposition=inline%3B+filename*%3DUTF-8%27%272025-09-26.png%3B+filename%3D%222025-09-26.png%22%3B&response-content-type=image%2Fpng&x-id=GetObject&Expires=1759210768&Policy=eyJTdGF0ZW1lbnQiOlt7IkNvbmRpdGlvbiI6eyJEYXRlTGVzc1RoYW4iOnsiQVdTOkVwb2NoVGltZSI6MTc1OTIxMDc2OH19LCJSZXNvdXJjZSI6Imh0dHBzOi8vY2FzLWJyaWRnZS54ZXRodWIuaGYuY28veGV0LWJyaWRnZS11cy82N2E0NzAzNzc0OWVhMmM0YjlmYWZkNGIvZDhkMWE2NmMxNjJmZTNkZjlkOTg5N2I1NWMyMzQ4MDgwYWE2NDlmNWNmZjhiMmQ0NTE3MGM3MmU3OTQyM2U2MCoifV19&Signature=IjfPAyXWkZn-lJ9aKYMRHLj8GFQnoN7NkRGsRHpqZVHmH6pkhB6QRqQbol4UNDyYCV9Qy6whb1QH3vMSHp2b8OJgiiivVFZElh4I%7ErbF41wl439zIS%7EFnMDFGic7RMFvavxoxEmhcIPjwLHsO1DVoRuuwf%7Ez4XvAPgIbNZ2LUYf%7Ec0BCHJlpt6rBKnVKcMurXt5jWY1MueG0mQtlx8madarOEOMv6RhIBAj3IY98WG8bc97GlLwHgaqDN52XlflwBtMxHWzyadCpf6xJk8Irww-zCAh1Fs80SYJJOwYl87OXVmb7ZQ53sAX-TMPQt1l4h1%7E-llJMdJkssPsFN1R3RQ__&Key-Pair-Id=K2L8F4GPSG1IFC)** - Official certificate of achievement for completing the HuggingFace Agents course

### 🎥 **Video Tutorial**
- **[HuggingFace Agents Course YouTube Video](https://www.youtube.com/watch?v=nNIlnKuCNcI)** - Visual walkthrough and demonstration of AI agent development concepts

### 🌟 **What This Represents**
This project demonstrates mastery of:
- **Agent Architecture Design** - Building robust multi-tool AI systems
- **API Integration** - Seamlessly combining HuggingFace and OpenAI services
- **Tool Development** - Creating custom tools for specialized tasks
- **Error Handling** - Implementing fallback mechanisms and robust error management
- **User Experience** - Designing intuitive interfaces with Gradio
- **Production Deployment** - Preparing agents for real-world usage

## �🙏 Acknowledgments

- HuggingFace for the amazing smolagents framework and comprehensive agent development course
- OpenAI for powerful language models and API integration
- The open-source community for tools and libraries
- The AI/ML community for continuous innovation and knowledge sharing

---

**Ready to experience the power of multi-tool AI assistance? Launch your agent and start exploring!** 🚀

*This project represents a journey from learning to implementation - showcasing the practical application of cutting-edge AI agent development techniques.*
