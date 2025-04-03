from generate_caption_and_hashtags import generate_caption_and_hashtags
import gradio as gr

# Gradio interface
demo = gr.Interface(
    fn=generate_caption_and_hashtags,
    inputs=[gr.Image(label="Upload Image", type="numpy")],
    outputs=[
        gr.Textbox(label="Generated Caption", lines=2),
        gr.Textbox(label="Generated Hashtags", lines=2)
    ],
    title="📷 Image Captioning and Hashtag Generator",
    description="Upload an image to generate a caption and relevant hashtags for social media. 🚀",
    theme="soft",  # Use a modern theme
    allow_flagging="never"  # Disable flagging for simplicity
)

# Launch the interface
if __name__ == "__main__":
    demo.launch()