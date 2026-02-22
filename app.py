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
if "show_rewrite_menu" not in st.session_state:
    st.session_state.show_rewrite_menu = False
if "rewrite_option_selected" not in st.session_state:
    st.session_state.rewrite_option_selected = None

# Set up page configuration
st.set_page_config(
    page_title="Summary Generator",
    page_icon="📝",
    layout="wide"
)

# Custom styling for justified text and red/green buttons
st.markdown("""
    <style>
    .justified-text {
        text-align: justify;
        font-size: 16px;
        line-height: 1.6;
        padding: 20px;
        background-color: #f8f9fa;
        border-radius: 8px;
    }
    .main {
        padding: 2rem;
    }
    /* Red buttons with green hover */
    .stButton > button {
        background-color: #dc3545 !important;
        color: white !important;
        border: 2px solid #dc3545 !important;
    }
    .stButton > button:hover {
        background-color: #28a745 !important;
        border-color: #28a745 !important;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("Summary Generator")

# Load API key from file
api_key_file = "openrouter_api_key.txt"

try:
    with open(api_key_file, "r") as f:
        api_key = f.read().strip()
    if not api_key:
        st.error("Error: openrouter_api_key.txt is empty. Please provide your OpenRouter API key.")
        st.stop()
except FileNotFoundError:
    st.error("Error: openrouter_api_key.txt not found. Please create this file with your OpenRouter API key.")
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
    st.error(f"Failed to initialize OpenRouter client: {str(e)}")
    st.stop()

# Function to call OpenRouter API for summarization
def generate_summary(text):
    """Generate summary using OpenRouter stepfun/step-3.5-flash:free model"""
    try:
        response = openrouter_client.chat.completions.create(
            model="stepfun/step-3.5-flash:free",
            messages=[
                {
                    "role": "user",
                    "content": f"Please provide a concise summary of the following text:\n\n{text}"
                }
            ],
            max_tokens=500
        )
        return response.choices[0].message.content
    except Exception as e:
        st.error(f"Error generating summary: {str(e)}")
        return None

# Function to call Ollama gemma3:4b model for rewriting
def call_ollama_model(prompt):
    """Call Ollama gemma3:4b model for local processing"""
    try:
        response = requests.post(
            "http://localhost:11434/api/generate",
            json={
                "model": "gemma3:4b",
                "prompt": prompt,
                "stream": False
            },
            timeout=30
        )
        if response.status_code == 200:
            return response.json().get("response", "").strip()
        else:
            st.error("Ollama connection failed. Make sure Ollama is running on localhost:11434 with gemma3:4b model")
            return None
    except Exception as e:
        st.error(f"Error connecting to Ollama: {str(e)}")
        return None

# Function to rewrite summary with specific action using Ollama
def rewrite_summary(text, action):
    """Rewrite summary according to the selected action using Ollama gemma3:4b"""
    try:
        if action == "Shorten":
            prompt = f"Make this text much shorter while keeping the key points. Provide only the shortened text:\n\n{text}"
        elif action == "Expand":
            prompt = f"Expand this text with more details and explanation. Provide only the expanded text:\n\n{text}"
        elif action == "More polite":
            prompt = f"Rewrite this text in a more polite and courteous way. Provide only the rewritten text:\n\n{text}"
        elif action == "More direct":
            prompt = f"Rewrite this text in a more direct and assertive way. Provide only the rewritten text:\n\n{text}"
        elif action == "Fix grammar":
            prompt = f"Fix all grammar, spelling, and punctuation errors in this text. Provide only the corrected text:\n\n{text}"
        else:
            return text
        
        result = call_ollama_model(prompt)
        if result:
            # Clean up any AI comments at the beginning
            lines = result.strip().split('\n')
            filtered_lines = [line for line in lines if line.strip()]
            return '\n'.join(filtered_lines).strip()
        return None
    except Exception as e:
        st.error(f"Error rewriting summary: {str(e)}")
        return None

# Main UI
st.markdown("---")

st.markdown("### Enter your text to summarize:")

# Text input
user_text = st.text_area(
    "Text to summarize:",
    height=250,
    placeholder="Paste your text here...",
    label_visibility="collapsed"
)

# Generate button
if st.button("✨ Generate Summary", type="primary", use_container_width=True):
    if not user_text.strip():
        st.warning("Please enter some text to summarize.")
    else:
        st.session_state.original_text = user_text
        with st.spinner("Generating summary..."):
            summary = generate_summary(user_text)
            if summary:
                st.session_state.generated_summary = summary
                st.session_state.rewritten_summary = None
                st.rerun()

# Display generated summary if available
if st.session_state.generated_summary:
    st.markdown("---")
    st.markdown("### Summary Generated:")
    
    # Display editable summary
    edited_summary = st.text_area(
        "Edit the summary if needed:",
        value=st.session_state.generated_summary,
        height=200,
        label_visibility="collapsed",
        key="summary_edit"
    )
    
    # Update summary if user edits it
    st.session_state.generated_summary = edited_summary
    
    st.markdown("---")
    
    # Buttons in a line - Generate from Scratch and Rewrite my draft
    col1, col2 = st.columns(2)
    
    with col1:
        if st.button("🔄 Generate from Scratch", use_container_width=True, key="gen_scratch"):
            with st.spinner("Regenerating summary..."):
                new_summary = generate_summary(st.session_state.original_text)
                if new_summary:
                    st.session_state.generated_summary = new_summary
                    st.session_state.rewritten_summary = None
                    st.rerun()
    
    with col2:
        if st.button("✏️ Rewrite my draft", use_container_width=True, key="rewrite_btn"):
            st.session_state.show_rewrite_menu = not st.session_state.show_rewrite_menu
            st.rerun()
    
    # Show rewrite options menu if button was clicked
    if st.session_state.show_rewrite_menu:
        col_menu1, col_menu2 = st.columns([3, 1])
        with col_menu1:
            selected_option = st.selectbox(
                "Select rewrite option:",
                ["Shorten", "Expand", "More polite", "More direct", "Fix grammar"],
                key="rewrite_option_dropdown",
                label_visibility="collapsed"
            )
        with col_menu2:
            if st.button("Apply", use_container_width=True, key="apply_rewrite"):
                with st.spinner(f"Rewriting summary ({selected_option})..."):
                    rewritten = rewrite_summary(st.session_state.generated_summary, selected_option)
                    if rewritten:
                        st.session_state.rewritten_summary = rewritten
                        st.session_state.show_rewrite_menu = False
                        st.rerun()
                    else:
                        st.error("Failed to rewrite summary. Make sure Ollama with gemma3:4b is running on localhost:11434")
                        st.session_state.show_rewrite_menu = False
    
    st.markdown("---")
    
    # Final result section (on same page, below buttons)
    st.markdown("### Final Result")
    
    if st.session_state.rewritten_summary:
        result_text = st.session_state.rewritten_summary
    else:
        result_text = st.session_state.generated_summary
    
    # Display editable result with justified text
    edited_result = st.text_area(
        "Final result (editable):",
        value=result_text,
        height=250,
        label_visibility="collapsed",
        key="result_edit"
    )
    
    # Update result if user edits it
    if st.session_state.rewritten_summary:
        st.session_state.rewritten_summary = edited_result
    else:
        st.session_state.generated_summary = edited_result
    
    st.markdown("---")
    
    # Email sending section
    st.markdown("### 📧 Send Summary")
    
    col1, col2 = st.columns(2)
    
    with col1:
        email_receiver_name = st.text_input(
            "Name:",
            placeholder="Enter name",
            key="email_receiver_name"
        )
    
    with col2:
        email_receiver_address = st.text_input(
            "Email address:",
            placeholder="name@domain.com",
            key="email_receiver_address"
        )
    
    if st.button("Send Summary by Email", type="primary", use_container_width=True):
        if not email_receiver_name.strip():
            st.warning("Please enter the name.")
        elif not email_receiver_address.strip():
            st.warning("Please enter email address.")
        else:
            final_summary = st.session_state.rewritten_summary or st.session_state.generated_summary
            
            email_preview = f"""To: {email_receiver_name}
Email: {email_receiver_address}

---

{final_summary}

---"""
            
            st.success(f"✅ Summary ready to send to: {email_receiver_name}")
            st.markdown("### Email Preview:")
            st.text(email_preview)
