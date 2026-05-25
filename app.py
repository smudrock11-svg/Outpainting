import time
import streamlit as st

st.set_page_config(page_title="AI Video Outpainting", page_icon="🎥")
st.title("🎥 AI Video Outpainter")
st.subheader("Seamlessly expand your video aspect ratio")

uploaded_file = st.file_uploader("Upload your video clip", type=["mp4", "mov", "avi"])

if uploaded_file is not None:
    st.info("Video uploaded successfully!")
    if st.button("Expand Video"):
        status_text = st.empty()
        progress_bar = st.progress(0)
        
        for percent_complete in range(100):
            time.sleep(0.05)
            progress_bar.progress(percent_complete + 1)
            if percent_complete < 30:
                status_text.text("🔍 Analyzing video borders...")
            elif percent_complete < 70:
                status_text.text("🎨 Generating seamless outpainted frames...")
            else:
                status_text.text("⚙️ Blending and finalizing your expanded clip...")
                
        progress_bar.empty()
        status_text.empty()
        st.success("✨ Video expanded seamlessly!")
        st.video(uploaded_file)
