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

### 🛠️ **8 Integrated Tools**

1. **🔍 Web Search** - Real-time web search using DuckDuckGo
2. **🖼️ Image Generation** - AI-powered image creation via HuggingFace Hub
3. **🕐 Timezone Conversion** - Get current time in any timezone worldwide
4. **📝 Text Analysis** - Sentiment analysis, summarization, translation (OpenAI-powered)
5. **💻 Code Review** - Code quality assessment and optimization suggestions (OpenAI-powered)
6. **✍️ Creative Writing** - Stories, poems, articles, marketing copy (OpenAI-powered)
7. **📊 System Status** - Real-time monitoring of all agent capabilities
8. **✅ Final Answer** - Structured response delivery system

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

## 💬 Example Queries

### Web Search & Information
- "What's the latest news about artificial intelligence?"
- "Search for Python programming tutorials"
- "Find information about climate change research"

### Image Generation
- "Generate an image of a sunset over mountains"
- "Create a picture of a futuristic robot"
- "Make an image of a cozy coffee shop"

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
- OpenAI tools use GPT-3.5-turbo for specialized tasks
- Comprehensive error handling and fallback mechanisms
- Real-time system status monitoring

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Test thoroughly
5. Submit a pull request

## 📝 License

This project is open source and available under the MIT License.

## 🙏 Acknowledgments

- HuggingFace for the amazing smolagents framework
- OpenAI for powerful language models
- The open-source community for tools and libraries

---

**Ready to experience the power of multi-tool AI assistance? Launch your agent and start exploring!** 🚀
