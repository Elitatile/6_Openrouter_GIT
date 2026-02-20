import streamlit as st
from openai import OpenAI
import requests

# Initialize session state variables
if "generated_summary" not in st.session_state:
    st.session_state.generated_summary = None
if "rewritten_summary" not in st.session_state:
    st.session_state.rewritten_summary = None
if "original_text" not in st.session_state:
    st.session_state.original_text = None
if "show_rewrite_options" not in st.session_state:
    st.session_state.show_rewrite_options = False

# Set up page configuration
st.set_page_config(
    page_title="AI Summary Generator",
    page_icon="📝",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        padding: 10px;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("📝 AI Summary Generator")
st.markdown("Advanced Text Summarization with OpenRouter & Ollama")
st.markdown("---")

# Status indicators
with st.sidebar:
    st.markdown("### ℹ️ System Status")
    st.success("✅ OpenRouter connected")
    
    # Check Ollama connection
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={"model": "gemma3:4b", "prompt": "test", "stream": False},
            timeout=2
        )
        st.success("✅ Ollama (gemma3:4b) running")
    except:
        st.warning("⚠️ Ollama not detected (rewriting features may not work)")
    
    st.markdown("---")

# Load API key from file
api_key_file = "openrouter_api_key.txt"

try:
    with open(api_key_file, "r") as f:
        api_key = f.read().strip()
    if not api_key:
        st.error(f"❌ Error: {api_key_file} is empty. Please provide your OpenRouter API key.")
        st.stop()
except FileNotFoundError:
    st.error(f"❌ Error: {api_key_file} not found. Please create this file with your OpenRouter API key.")
    st.stop()

# Initialize OpenRouter client
try:
    openrouter_client = OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
        default_headers={
            "HTTP-Referer": "http://localhost:8501",
            "X-Title": "Summary Generator",
        }
    )
except Exception as e:
    st.error(f"❌ Failed to initialize OpenRouter client: {str(e)}")
    st.stop()

# Function to call Ollama gemma3:4b model
def call_ollama_model(prompt):
    """Call Ollama gemma3:4b model for local processing"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            }
        )
        if response.status_code == 200:
            return response.json().get("response", "")
        else:
            return None
    except Exception as e:
        st.warning(f"⚠️ Ollama connection failed: {str(e)}. Make sure Ollama is running on localhost:11434")
        return None

# Function to generate summary using OpenRouter
def generate_summary_openrouter(text, length="medium"):
    """Generate summary using OpenRouter's stepfun/step-3.5-flash:free model"""
    
    length_instructions = {
        "short": "Summarize this text in 1-3 sentences.",
        "medium": "Summarize this text in 3-5 sentences.",
        "long": "Summarize this text in 5-10 sentences."
    }
    
    system_prompt = f"""You are a professional text summarizer. {length_instructions.get(length, length_instructions['medium'])}
Keep the summary clear, concise, and capture the main points. Do not add any comments or explanations."""
    
    try:
        # Debug: Check if client is initialized
        if not openrouter_client:
            st.error("❌ OpenRouter client not initialized. Please check your API key.")
            return None
            
        response = openrouter_client.chat.completions.create(
            model="stepfun/step-3.5-flash:free",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
            top_p=0.9,
            max_tokens=500
        )
        
        if response and response.choices:
            return response.choices[0].message.content
        else:
            st.error("❌ Empty response from OpenRouter API")
            return None
            
    except requests.exceptions.ConnectionError:
        st.error("❌ Connection Error: Cannot reach OpenRouter API. Please check your internet connection.")
        return None
    except ValueError as e:
        if "403" in str(e) or "Forbidden" in str(e):
            st.error("❌ API Key Error: Your OpenRouter API key is invalid or expired. Please check 'openrouter_api_key.txt'")
        elif "401" in str(e) or "Unauthorized" in str(e):
            st.error("❌ Authentication Error: Invalid API key. Please verify 'openrouter_api_key.txt'")
        else:
            st.error(f"❌ API Error: {str(e)}")
        return None
    except Exception as e:
        error_msg = str(e)
        st.error(f"❌ Error generating summary: {error_msg}")
        with st.expander("📋 Troubleshooting"):
            st.markdown("""
            **Possible causes:**
            - Invalid or expired OpenRouter API key
            - API rate limit exceeded
            - Model not available
            - No internet connection
            
            **Solutions:**
            1. Verify your API key in `openrouter_api_key.txt`
            2. Check OpenRouter account for available credits
            3. Try again in a few moments
            """)
        return None

# Function to rewrite summary
def rewrite_summary(text, action):
    """Rewrite summary using Ollama gemma3:4b model with specified action"""
    
    action_prompts = {
        "Shorten": "Make this text shorter and more concise while keeping the main points:",
        "Expand": "Expand this text with more details and explanations:",
        "More polite": "Rewrite this text to be more polite and courteous:",
        "More direct": "Rewrite this text to be more direct and assertive:",
        "Fix grammar": "Fix all grammar and spelling errors in this text:"
    }
    
    prompt = f"{action_prompts.get(action, action)}\n\n{text}"
    
    result = call_ollama_model(prompt)
    
    if result:
        return result.strip()
    else:
        st.error("❌ Failed to rewrite summary. Make sure Ollama with gemma3:4b is running on localhost:11434")
        return None


# Main content area
st.markdown("### Enter your text to summarize:")

# Text input
user_text = st.text_area(
    "Text to summarize:",
    height=200,
    placeholder="Paste your text here...",
    label_visibility="collapsed"
)

# Generate button
if st.button("✨ Generate Summary", type="primary", use_container_width=True):
    if not user_text.strip():
        st.warning("⚠️ Please enter some text to summarize.")
    else:
        st.session_state.original_text = user_text
        with st.spinner("🔄 Generating summary from OpenRouter API..."):
            st.info("📡 Sending to OpenRouter API (stepfun/step-3.5-flash:free)...")
            summary = generate_summary_openrouter(user_text, "medium")
            if summary:
                st.session_state.generated_summary = summary
                st.success("✅ Summary generated successfully!")
                st.rerun()
            else:
                st.error("❌ Failed to generate summary. Please check the error details above.")

# Display summary if generated
if st.session_state.generated_summary:
    st.markdown("---")
    st.markdown("### 📋 Generated Summary:")
    st.info(st.session_state.generated_summary)
    
    # Buttons in a line (stacked vertically)
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Generate from Scratch", use_container_width=True):
            with st.spinner("🔄 Regenerating summary from scratch..."):
                new_summary = generate_summary_openrouter(st.session_state.original_text, "medium")
                if new_summary:
                    st.session_state.generated_summary = new_summary
                    st.session_state.rewritten_summary = None
                    st.rerun()
    
    with col2:
        if st.button("✏️ Rewrite my Draft", use_container_width=True):
            st.session_state.show_rewrite_options = True
            st.rerun()
    
    # Show rewrite options if button was clicked
    if st.session_state.show_rewrite_options:
        st.markdown("### Choose Rewrite Action:")
        
        col1, col2 = st.columns([2, 1])
        with col1:
            rewrite_action = st.selectbox(
                "How would you like to rewrite the summary?",
                ["Shorten", "Expand", "More polite", "More direct", "Fix grammar"],
                key="rewrite_action_select"
            )
        
        with col2:
            if st.button("Apply", type="primary"):
                with st.spinner(f"✏️ {rewrite_action}ing summary..."):
                    rewritten = rewrite_summary(st.session_state.generated_summary, rewrite_action)
                    if rewritten:
                        st.session_state.rewritten_summary = rewritten
                        st.session_state.show_rewrite_options = False
                        st.rerun()
                    else:
                        st.error("❌ Failed to rewrite summary. Make sure Ollama with gemma3:4b is running.")

# Create tabs for viewing
if st.session_state.generated_summary or st.session_state.rewritten_summary:
    st.markdown("---")
    
    if st.session_state.rewritten_summary:
        tab1, tab2 = st.tabs(["📝 Original Summary", "🎯 Final Result"])
    else:
        tab1 = st.tabs(["📝 Summary"])[0]
    
    with tab1:
        st.markdown("### Original Generated Summary")
        st.code(st.session_state.generated_summary, language="text")
        st.metric("Length", f"{len(st.session_state.generated_summary)} characters")
    
    if st.session_state.rewritten_summary:
        with tab2:
            st.markdown("### Final Result")
            st.code(st.session_state.rewritten_summary, language="text")
            st.metric("Length", f"{len(st.session_state.rewritten_summary)} characters")
    
    st.markdown("---")
    
    # Email sending section
    st.markdown("### 📧 Send Summary by Email")
    
    col1, col2 = st.columns(2)
    
    with col1:
        summary_receiver_name = st.text_input(
            "Summary receiver's name:",
            placeholder="Enter recipient's name...",
            key="summary_receiver_name"
        )
    
    with col2:
        letter_receiver_name = st.text_input(
            "Letter receiver's name:",
            placeholder="Enter letter receiver's name...",
            key="letter_receiver_name"
        )
    
    summary_receiver_email = st.text_input(
        "Recipient's email address:",
        placeholder="name@example.com",
        key="summary_receiver_email"
    )
    
    if st.button("📤 Send Summary by Email", type="primary", use_container_width=True):
        if not summary_receiver_name.strip():
            st.warning("⚠️ Please enter the recipient's name.")
        elif not letter_receiver_name.strip():
            st.warning("⚠️ Please enter the letter receiver's name.")
        elif not summary_receiver_email.strip():
            st.warning("⚠️ Please enter the recipient's email address.")
        else:
            # Use rewritten summary if available, otherwise use original
            final_summary = st.session_state.rewritten_summary or st.session_state.generated_summary
            
            formatted_email = f"""Dear {letter_receiver_name},

To: {summary_receiver_name}
Email: {summary_receiver_email}

---

Summary:

{final_summary}

---

Best regards"""
            
            st.success(f"✅ Summary prepared for: {summary_receiver_name} ({summary_receiver_email})")
            
            st.markdown("### 📧 Email Preview:")
            st.code(formatted_email, language="text")
            
            st.download_button(
                label="⬇️ Download Email",
                data=formatted_email,
                file_name=f"summary_for_{summary_receiver_name.replace(' ', '_')}.txt",
                mime="text/plain"
            )
    
    # Clear button
    if st.button("🗑️ Clear All", use_container_width=True):
        st.session_state.generated_summary = None
        st.session_state.rewritten_summary = None
        st.session_state.original_text = None
        st.session_state.show_rewrite_options = False
        st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Powered by OpenRouter (Summary) & Ollama (Rewriting) | 
    Using Step 3.5 Flash & Gemma3:4b Models
</div>
""", unsafe_allow_html=True)
