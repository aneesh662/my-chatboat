import streamlit as st

# Set the title of the app
st.title("Welcome to Mizu")

# Add a description
st.write("Feel free to chat with us using our chatbot!")

# Embed the Dialogflow chatbot using an iframe
iframe_code = """
<iframe 
    width="350" 
    height="430" 
    allow="microphone;" 
    src="https://console.dialogflow.com/api-client/demo/embedded/e4b58c8e-5f3f-448a-b8ab-fa1afd3eb768">
</iframe>
"""

# Use Streamlit's components to render the iframe
st.components.v1.html(iframe_code, height=450, scrolling=True)


