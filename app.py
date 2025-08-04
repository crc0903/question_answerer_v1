
import streamlit as st
import openai

st.set_page_config(page_title="Ask AI", page_icon="🤖", layout="centered")

st.title("🤖 Ask AI (Powered by GPT-3.5-Turbo)")

openai.api_key = "your-api-key-here"  # Replace with your OpenAI API key

question = st.text_input("Ask a question:")

if st.button("Get Answer") and question:
    with st.spinner("Thinking..."):
        try:
            response = openai.ChatCompletion.create(
                model="gpt-3.5-turbo",
                messages=[{"role": "user", "content": question}],
                temperature=0.7,
                max_tokens=300
            )
            st.markdown("**Answer:**")
            st.write(response['choices'][0]['message']['content'].strip())
        except Exception as e:
            st.error(f"Error: {e}")
