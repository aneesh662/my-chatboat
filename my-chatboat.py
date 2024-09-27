import streamlit as st

# Set the title of the app
st.title("Welcome to Our Mizu")

# Add a description
st.write("Feel free to chat with us using our chatbot!")

# Embed the Dialogflow chatbot using a responsive iframe
iframe_code = """
<style>
    /* CSS for responsive iframe */
    .responsive-iframe {
        position: relative;
        width: 100%;
        height: 0;
        padding-bottom: 75%; /* Adjust this for aspect ratio (4:3 here) */
        overflow: hidden;
    }
    .responsive-iframe iframe {
        position: absolute;
        top: 0;
        left: 0;
        width: 100%;
        height: 100%;
        border: 0;
    }
</style>

<div class="responsive-iframe">
    <iframe 
        allow="microphone;" 
        src="https://console.dialogflow.com/api-client/demo/embedded/e4b58c8e-5f3f-448a-b8ab-fa1afd3eb768">
    </iframe>
</div>
"""

# Use Streamlit's components to render the iframe with responsive design
st.components.v1.html(iframe_code, height=500, scrolling=True)
