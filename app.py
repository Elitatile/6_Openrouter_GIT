import streamlit as st
from openai import OpenAI
import os

# Initialize session state variables
if "generated_summary" not in st.session_state:
    st.session_state.generated_summary = None
if "generated_letter" not in st.session_state:
    st.session_state.generated_letter = None

# Set up page configuration
st.set_page_config(
    page_title="AI Assistant",
    page_icon="🤖",
    layout="centered",
    initial_sidebar_state="expanded"
)

# Custom styling
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stButton > button {
        width: 100%;
        padding: 10px;
        background-color: #0000FF;
        color: white;
        font-weight: bold;
    }
    .stTabs [data-baseweb="tab-list"] button {
        font-weight: bold;
    }
    </style>
    """, unsafe_allow_html=True)

# Title
st.title("🤖 AI Assistant")
st.markdown("Text Summarizer & Email Response Generator")
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
client = OpenAI(
    base_url="https://openrouter.ai/api/v1",
    api_key=api_key,
    default_headers={
        "HTTP-Referer": "http://localhost:8501",
        "X-Title": "Text Summarizer",
    }
)

# Sidebar
with st.sidebar:
    st.header("⚙️ Settings")
    
    st.markdown("### Summary Settings")
    summary_length = st.radio(
        "Select summary length:",
        ["Short (1-3 sentences)", "Medium (3-5 sentences)", "Long (5-10 sentences)"],
        index=1
    )
    
    st.markdown("### Email Settings")
    email_tone = st.selectbox(
        "Select email tone:",
        ["Professional", "Friendly", "Formal", "Casual", "Apologetic"]
    )
    
    email_length = st.radio(
        "Select email length:",
        ["Brief (2-3 lines)", "Medium (3-5 lines)", "Detailed (5-8 lines)"],
        index=1
    )
    
    st.markdown("---")
    st.markdown("### 📚 About")
    st.markdown("""
    This app uses **OpenRouter** with the **Step 3.5 Flash** model 
    for:
    - Text summarization
    - Email response generation
    
    **Features:**
    - Adjustable summary length
    - Multiple email tones
    - Fast processing
    - Clean interface
    """)

# Map selection to prompts
length_mapping = {
    "Short (1-3 sentences)": "Summarize this text in 1-3 sentences.",
    "Medium (3-5 sentences)": "Summarize this text in 3-5 sentences.",
    "Long (5-10 sentences)": "Summarize this text in 5-10 sentences."
}

email_length_mapping = {
    "Brief (2-3 lines)": "Write a brief response in 2-3 lines.",
    "Medium (3-5 lines)": "Write a response in 3-5 lines.",
    "Detailed (5-8 lines)": "Write a detailed response in 5-8 lines."
}

email_tone_mapping = {
    "Professional": "professional and business-appropriate",
    "Friendly": "warm and friendly",
    "Formal": "formal and respectful",
    "Casual": "casual and relaxed",
    "Apologetic": "apologetic and understanding"
}

# Create tabs for different features
tab1, tab2 = st.tabs(["📝 Summarizer", "📧 Email Response"])

# TAB 1: SUMMARIZER
with tab1:
    st.markdown("### Summarize Text")
    st.markdown("Paste or type the text you want to summarize:")
    
    user_text = st.text_area(
        "Text to summarize:",
        height=200,
        placeholder="Paste your text here...",
        label_visibility="collapsed"
    )
    
    # Create columns for buttons
    col1, col2 = st.columns([3, 1])
    
    with col1:
        summarize_button = st.button("✨ Summarize", type="primary", use_container_width=True, key="summarize_btn")
    
    with col2:
        clear_button = st.button("🗑️ Clear", key="clear_btn")
    
    # Clear functionality
    if clear_button:
        st.rerun()
    
    # Summarize functionality
    if summarize_button:
        if not user_text.strip():
            st.warning("⚠️ Please enter some text to summarize.")
        else:
            with st.spinner("🔄 Generating summary..."):
                try:
                    # Prepare the prompt
                    length_instruction = length_mapping[summary_length]
                    system_prompt = f"""You are a professional text summarizer. 
{length_instruction}
Keep the summary clear, concise, and capture the main points."""
                    
                    # Call OpenRouter API
                    response = client.chat.completions.create(
                        model="stepfun/step-3.5-flash:free",
                        messages=[
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            {
                                "role": "user",
                                "content": user_text
                            }
                        ],
                        temperature=0.7,
                        top_p=0.9,
                        max_tokens=500
                    )
                    
                    # Display results
                    summary = response.choices[0].message.content
                    
                    # Store in session state to persist across reruns
                    st.session_state.generated_summary = summary
                    
                    st.markdown("---")
                    st.markdown("### 📋 Generated Summary:")
                    st.info(st.session_state.generated_summary)
                    
                    # Input for receiver name - These will persist now
                    st.markdown("### 📬 Send Summary by Email:")
                    summary_receiver_name = st.text_input(
                        "Summary receiver's name:",
                        placeholder="Enter the name of the recipient...",
                        key="summary_receiver_name"
                    )
                    
                    summary_receiver_email = st.text_input(
                        "Recipient's email address:",
                        placeholder="name@example.com",
                        key="summary_receiver_email"
                    )
                    
                    # Send button
                    col1, col2, col3 = st.columns([1, 1, 2])
                    
                    with col1:
                        send_summary_button = st.button("📧 Send Summary", type="primary", key="send_summary_btn")
                    
                    with col2:
                        copy_summary_button = st.button("📋 Copy", key="copy_summary_btn")
                    
                    # Send functionality
                    if send_summary_button:
                        if not summary_receiver_name.strip():
                            st.warning("⚠️ Please enter the recipient's name.")
                        elif not summary_receiver_email.strip():
                            st.warning("⚠️ Please enter the recipient's email address.")
                        else:
                            # Create formatted summary with receiver details
                            formatted_summary = f"To: {summary_receiver_name}\nEmail: {summary_receiver_email}\n\n---\n\nSummary:\n\n{st.session_state.generated_summary}"
                            
                            st.success(f"✅ Summary prepared for: {summary_receiver_name} ({summary_receiver_email})")
                            
                            # Show formatted summary
                            st.markdown("### 📝 Summary to Send:")
                            st.code(formatted_summary, language="text")
                            
                            # Download option
                            st.download_button(
                                label="⬇️ Download Summary",
                                data=formatted_summary,
                                file_name=f"summary_for_{summary_receiver_name.replace(' ', '_')}.txt",
                                mime="text/plain"
                            )
                    
                    # Copy to clipboard
                    if copy_summary_button:
                        st.success("📋 Summary copied!")
                        st.download_button(
                            label="📄 Download Summary",
                            data=st.session_state.generated_summary,
                            file_name="summary.txt",
                            mime="text/plain"
                        )
                    
                    # Show metadata
                    with st.expander("📊 Details"):
                        col1, col2, col3 = st.columns(3)
                        with col1:
                            st.metric("Original length", f"{len(user_text)} chars")
                        with col2:
                            st.metric("Summary length", f"{len(st.session_state.generated_summary)} chars")
                        with col3:
                            compression_ratio = round((len(st.session_state.generated_summary) / len(user_text)) * 100, 1)
                            st.metric("Compression", f"{compression_ratio}%")
                    
                except Exception as e:
                    st.error(f"❌ Error generating summary: {str(e)}")
                    st.markdown("**Please ensure:**")
                    st.markdown("- Your OpenRouter API key is valid")
                    st.markdown("- You have enough API credits")
                    st.markdown("- You have internet connectivity")
    
    # Display stored summary if it exists (for persistent display)
    elif st.session_state.generated_summary and not summarize_button:
        st.markdown("---")
        st.markdown("### 📋 Generated Summary:")
        st.info(st.session_state.generated_summary)
        
        # Input for receiver name - These will persist now
        st.markdown("### 📬 Send Summary by Email:")
        summary_receiver_name = st.text_input(
            "Summary receiver's name:",
            placeholder="Enter the name of the recipient...",
            key="summary_receiver_name"
        )
        
        summary_receiver_email = st.text_input(
            "Recipient's email address:",
            placeholder="name@example.com",
            key="summary_receiver_email"
        )
        
        # Send button
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            send_summary_button = st.button("📧 Send Summary", type="primary", key="send_summary_btn")
        
        with col2:
            copy_summary_button = st.button("📋 Copy", key="copy_summary_btn")
        
        # Send functionality
        if send_summary_button:
            if not summary_receiver_name.strip():
                st.warning("⚠️ Please enter the recipient's name.")
            elif not summary_receiver_email.strip():
                st.warning("⚠️ Please enter the recipient's email address.")
            else:
                # Create formatted summary with receiver details
                formatted_summary = f"To: {summary_receiver_name}\nEmail: {summary_receiver_email}\n\n---\n\nSummary:\n\n{st.session_state.generated_summary}"
                
                st.success(f"✅ Summary prepared for: {summary_receiver_name} ({summary_receiver_email})")
                
                # Show formatted summary
                st.markdown("### 📝 Summary to Send:")
                st.code(formatted_summary, language="text")
                
                # Download option
                st.download_button(
                    label="⬇️ Download Summary",
                    data=formatted_summary,
                    file_name=f"summary_for_{summary_receiver_name.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
        
        # Copy to clipboard
        if copy_summary_button:
            st.success("📋 Summary copied!")
            st.download_button(
                label="📄 Download Summary",
                data=st.session_state.generated_summary,
                file_name="summary.txt",
                mime="text/plain"
            )
        
        # Show metadata
        with st.expander("📊 Details"):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Summary length", f"{len(st.session_state.generated_summary)} chars")
            with col2:
                st.button("🔄 Generate New Summary", key="new_summary_btn")
                if st.session_state.get("new_summary_btn"):
                    st.session_state.generated_summary = None
                    st.rerun()

# TAB 2: EMAIL RESPONSE GENERATOR
with tab2:
    st.markdown("### Generate Email Response")
    st.markdown("Paste or type the email you want to respond to:")
    
    email_text = st.text_area(
        "Email to respond to:",
        height=200,
        placeholder="Paste the email you received here...",
        label_visibility="collapsed",
        key="email_input"
    )
    
    # Create columns for buttons
    col1, col2 = st.columns([3, 1])
    
    with col1:
        generate_button = st.button("✉️ Generate Response", type="primary", use_container_width=True, key="generate_btn")
    
    with col2:
        clear_email_button = st.button("🗑️ Clear", key="clear_email_btn")
    
    # Clear functionality
    if clear_email_button:
        st.rerun()
    
    # Generate email response functionality
    if generate_button:
        if not email_text.strip():
            st.warning("⚠️ Please enter an email to respond to.")
        else:
            with st.spinner("🔄 Generating email response..."):
                try:
                    # Prepare the prompt
                    length_instruction = email_length_mapping[email_length]
                    tone_instruction = email_tone_mapping[email_tone]
                    
                    system_prompt = f"""You are a professional email writer. 
Write an email response that is {tone_instruction}.
{length_instruction}
Be polite, clear, and address all points from the original email."""
                    
                    # Call OpenRouter API
                    response = client.chat.completions.create(
                        model="stepfun/step-3.5-flash:free",
                        messages=[
                            {
                                "role": "system",
                                "content": system_prompt
                            },
                            {
                                "role": "user",
                                "content": f"Original email:\n\n{email_text}\n\nPlease generate an appropriate response."
                            }
                        ],
                        temperature=0.7,
                        top_p=0.9,
                        max_tokens=600
                    )
                    
                    # Display results
                    email_response = response.choices[0].message.content
                    
                    # Store in session state for later use
                    st.session_state.generated_letter = email_response
                    
                    st.markdown("---")
                    st.markdown("### 📧 Generated Email Response:")
                    st.info(email_response)
                    
                    # Input for receiver name
                    st.markdown("### 📬 Email Details:")
                    letter_receiver_name = st.text_input(
                        "Letter receiver's name:",
                        placeholder="Enter the name of the letter receiver...",
                        key="letter_receiver_name"
                    )
                    
                    # Send button
                    col1, col2, col3 = st.columns([1, 1, 2])
                    
                    with col1:
                        send_button = st.button("📤 Send Letter", type="primary", key="send_btn")
                    
                    with col2:
                        copy_button = st.button("📋 Copy Letter", key="copy_btn")
                    
                    # Send functionality
                    if send_button:
                        if not letter_receiver_name.strip():
                            st.warning("⚠️ Please enter the receiver's name.")
                        else:
                            # Create formatted letter with receiver name
                            formatted_letter = f"To: {letter_receiver_name}\n\n{email_response}"
                            
                            # Here you can add actual sending logic (email API, database, etc.)
                            st.success(f"✅ Letter prepared to send to: {letter_receiver_name}")
                            
                            # Show formatted letter
                            st.markdown("### 📝 Formatted Letter to Send:")
                            st.code(formatted_letter, language="text")
                            
                            # Download option
                            st.download_button(
                                label="⬇️ Download Letter",
                                data=formatted_letter,
                                file_name=f"letter_to_{letter_receiver_name.replace(' ', '_')}.txt",
                                mime="text/plain"
                            )
                    
                    # Copy to clipboard button
                    if copy_button:
                        st.success("📋 Letter copied to clipboard!")
                        st.download_button(
                            label="📄 Download Letter",
                            data=email_response,
                            file_name="email_response.txt",
                            mime="text/plain"
                        )
                    
                    # Show metadata
                    with st.expander("📊 Details"):
                        col1, col2 = st.columns(2)
                        with col1:
                            st.metric("Original email length", f"{len(email_text)} chars")
                        with col2:
                            st.metric("Response length", f"{len(email_response)} chars")
                    
                except Exception as e:
                    st.error(f"❌ Error generating email response: {str(e)}")
                    st.markdown("**Please ensure:**")
                    st.markdown("- Your OpenRouter API key is valid")
                    st.markdown("- You have enough API credits")
                    st.markdown("- You have internet connectivity")
    
    # Display stored letter if it exists (persistent display for input fields)
    elif st.session_state.generated_letter:
        st.markdown("---")
        st.markdown("### 📧 Generated Email Response:")
        st.info(st.session_state.generated_letter)
        
        # Input for receiver name (persists after filling)
        st.markdown("### 📬 Email Details:")
        letter_receiver_name = st.text_input(
            "Letter receiver's name:",
            placeholder="Enter the name of the letter receiver...",
            key="letter_receiver_name_persist"
        )
        
        # Send button
        col1, col2, col3 = st.columns([1, 1, 2])
        
        with col1:
            send_button = st.button("📤 Send Letter", type="primary", key="send_btn_persist")
        
        with col2:
            copy_button = st.button("📋 Copy Letter", key="copy_btn_persist")
        
        # Send functionality
        if send_button:
            if not letter_receiver_name.strip():
                st.warning("⚠️ Please enter the receiver's name.")
            else:
                # Create formatted letter with receiver name
                formatted_letter = f"To: {letter_receiver_name}\n\n{st.session_state.generated_letter}"
                
                # Here you can add actual sending logic (email API, database, etc.)
                st.success(f"✅ Letter prepared to send to: {letter_receiver_name}")
                
                # Show formatted letter
                st.markdown("### 📝 Formatted Letter to Send:")
                st.code(formatted_letter, language="text")
                
                # Download option
                st.download_button(
                    label="⬇️ Download Letter",
                    data=formatted_letter,
                    file_name=f"letter_to_{letter_receiver_name.replace(' ', '_')}.txt",
                    mime="text/plain"
                )
        
        # Copy to clipboard
        if copy_button:
            st.success("📋 Letter copied!")
            st.download_button(
                label="📄 Download Letter",
                data=st.session_state.generated_letter,
                file_name="email_response.txt",
                mime="text/plain"
            )
        
        # Show metadata
        with st.expander("📊 Details"):
            col1, col2 = st.columns(2)
            with col1:
                st.metric("Response length", f"{len(st.session_state.generated_letter)} chars")
            with col2:
                if st.button("🔄 Generate New Response"):
                    st.session_state.generated_letter = None
                    st.rerun()

# Footer
st.markdown("---")
st.markdown("""
<div style='text-align: center; color: gray; font-size: 12px;'>
    Powered by OpenRouter | Using Step 3.5 Flash Model | Text Summarizer & Email Response Generator
</div>
""", unsafe_allow_html=True)
