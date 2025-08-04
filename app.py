import streamlit as st
from openai import OpenAI

# Set Streamlit page config
st.set_page_config(page_title="Ask AI", page_icon="🤖", layout="centered")

# Title
st.title("🤖 Ask AI (Powered by GPT-3.5-Turbo)")

# Initialize OpenAI client using API key from Streamlit secrets
client = OpenAI(api_key=st.secrets["openai_api_key"])

# User input
question = st.text_input("Ask a question:")

# Get Answer button
if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        try:
            # Call GPT-3.5-Turbo
            response = client.chat.completions.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=300
            )
            # Display result
            st.markdown("**Answer:**")
            st.write(response.choices[0].message.content.strip())
        except Exception as e:
            st.error(f"Error: {e}")
