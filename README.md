# AI Text Summarizer & Email Response Generator

A web-based AI assistant application powered by **OpenRouter** and the **Step 3.5 Flash** AI model. Built with Streamlit for an intuitive and user-friendly interface. Features both text summarization and intelligent email response generation.

## 🌟 Features

- **AI-Powered Text Summarization**: Uses OpenRouter's `stepfun/step-3.5-flash:free` model for fast and accurate text summaries
- **Email Response Generation**: Intelligent email response generator with customizable tone and length
- **Adjustable Summary Length**: Choose between short (1-3 sentences), medium (3-5 sentences), or long (5-10 sentences) summaries
- **Multiple Email Tones**: Select from Professional, Friendly, Formal, Casual, or Apologetic tones
- **Clean Web Interface**: Built with Streamlit for easy access via browser with two main features in separate tabs
- **Real-time Processing**: Get summaries and email responses instantly
- **Compression Metrics**: View statistics on text compression ratio for summaries
- **Secure API Key Management**: API key loaded from local file, never hardcoded

## 📋 Requirements

- Python 3.8+
- OpenRouter API key (get one at [openrouter.ai](https://openrouter.ai))
- Internet connection for API calls

## 🚀 Installation

### 1. Clone or download this project
```bash
cd 6_Openrouter_GIT
```

### 2. Create a virtual environment (recommended)
```bash
python3 -m venv .venv
source .venv/bin/activate  # On Windows: .venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install streamlit openai
```

### 4. Set up your OpenRouter API key
Create a file named `openrouter_api_key.txt` in the project root and paste your OpenRouter API key:

```bash
echo "your_openrouter_api_key_here" > openrouter_api_key.txt
```

**Security Note**: The `openrouter_api_key.txt` file is listed in `.gitignore` to prevent accidental commits of sensitive data.

## 🎯 Usage

Start the application:
```bash
streamlit run app.py
```

The app will open in your default browser at `http://localhost:8501`

### Text Summarizer Tab:
1. **Paste your text** in the text area
2. **Select summary length** from the sidebar (Short, Medium, or Long)
3. **Click "✨ Summarize"** button
4. **View your summary** with compression statistics

### Email Response Tab:
1. **Paste the email** you want to respond to in the text area
2. **Select email tone** from the sidebar (Professional, Friendly, Formal, Casual, or Apologetic)
3. **Select email length** from the sidebar (Brief, Medium, or Detailed)
4. **Click "✉️ Generate Response"** button
5. **Review and copy** your generated email response

## 📁 Project Structure

```
6_Openrouter_GIT/
├── app.py                          # Main Streamlit application
├── README.md                        # This file
├── program_streamlit_description.md # Project requirements
├── openrouter_api_key.txt          # Your API key (not in git)
└── docs/
    ├── ollama_documentation.md
    └── streamlit_documentation.md
```

## 🔧 Configuration

### Environment Variables
- `OPENROUTER_API_KEY`: Loaded from `openrouter_api_key.txt`
- HTTP-Referer: Set to `http://localhost:8501`
- X-Title: Set to `Text Summarizer`

### Model Settings
- **Model**: `stepfun/step-3.5-flash:free`
- **Temperature**: 0.7 (balanced creativity and consistency)
- **Top P**: 0.9 (high diversity)
- **Max Tokens**: 500 (sufficient for summaries)

## 🐛 Troubleshooting

### Error: "openrouter_api_key.txt not found"
- **Solution**: Create the file with your OpenRouter API key:
```bash
echo "your_api_key" > openrouter_api_key.txt
```

### Error: "openrouter_api_key.txt is empty"
- **Solution**: Make sure your API key is properly saved in the file without extra whitespace

### Error: "Error generating summary"
- **Possible causes**:
  - Invalid or expired API key
  - Insufficient API credits
  - Model temporarily unavailable
  - No internet connection
- **Solution**: Verify your API key at [openrouter.ai](https://openrouter.ai) and check your account balance

### App not opening in browser
- **Solution**: Manually open `http://localhost:8501` in your web browser

## 💡 Usage Examples

### Text Summarization Examples:

**Example 1: News Article Summary**
Paste a longer news article and get a quick 3-5 sentence summary to understand the key points.

**Example 2: Document Review**
Use "Long" summary option to capture more details from lengthy documents or reports.

**Example 3: Quick Digest**
Use "Short" option to get the most critical information in bullet-point form.

### Email Response Examples:

**Example 1: Customer Inquiry Response**
Paste a professional customer inquiry and generate a friendly, helpful response.

**Example 2: Formal Business Reply**
Use the "Formal" tone to craft a professional business email response.

**Example 3: Apologetic Reply**
Select "Apologetic" tone for situations where you need to apologize and offer solutions.

**Example 4: Casual Follow-up**
Use "Casual" tone for friendly follow-up emails to colleagues or acquaintances.

## 🌐 OpenRouter Integration

This application uses OpenRouter's unified API to access the Step 3.5 Flash model. OpenRouter provides:
- **Cost-effective pricing** with `free` tier models
- **Unified interface** to multiple AI providers
- **Reliable fallback** system
- **Usage tracking** and analytics

Learn more at [OpenRouter Documentation](https://openrouter.ai/docs)

## 📝 Dependencies

| Package | Version | Purpose |
|---------|---------|---------|
| streamlit | Latest | Web interface |
| openai | Latest | OpenRouter API client |

## 🔐 Security

- API key is stored locally in `openrouter_api_key.txt` (not committed to git)
- HTTPS used for all API communications
- No data is stored on the server
- User inputs are discarded after processing

## 📄 License

This project is for educational purposes.

## 🤝 Support

For issues with:
- **Streamlit**: Visit [streamlit.io](https://streamlit.io)
- **OpenRouter**: Visit [openrouter.ai/docs](https://openrouter.ai/docs)
- **OpenAI Python SDK**: Visit [github.com/openai/openai-python](https://github.com/openai/openai-python)

## 📚 Documentation

Additional documentation is available in the `docs/` folder:
- `streamlit_documentation.md` - Streamlit API references and examples
- `ollama_documentation.md` - Ollama-related documentation

---

**Created**: February 2026  
**Tech Stack**: Python • Streamlit • OpenRouter • AI  
**Status**: ✅ Production Ready
