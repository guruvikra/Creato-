import streamlit as st
from dotenv import load_dotenv
import os
import requests
from services import enhance_prompt,generate_hd_images


load_dotenv()
def main():
    # api_key = os.getenv("BRIA_API_KEY")
    # prompt = enhance_prompt(api_key=api_key, prompt="a bathing soap")
    # generated_img = generate_hd_images(api_key=api_key, prompt=prompt['enhanced_prompt'],model_version='2.2', num_results=1)
    # print(prompt)
    # print(generated_img)
    st.set_page_config(page_title="creato", layout="centered")
    st.title("creato")
    if "enhanced_prompt" not in st.session_state:
        st.session_state.enhanced_prompt = ""
    
    api_key = st.text_input("API Key", type="password")
    prompt = st.text_input("Enter Prompt")
    if st.button("Enhance Prompt"):
        if not api_key or not prompt:
            st.warning("Please enter both API Key and Prompt.")
        else:
            enhanced = enhance_prompt(api_key, prompt)
            st.session_state.enhanced_prompt = enhanced
            st.success("Enhanced Prompt:")
            st.write("Output", enhanced, height=100)
    if st.button("generate HD image"):
        print(st.session_state.enhanced_prompt.get("enhanced_prompt"))
        generated_img = generate_hd_images(api_key=api_key, prompt=st.session_state.enhanced_prompt.get("enhanced_prompt"),model_version='2.2', num_results=1)
        st.write("image_url",generated_img)

        
        # generated_img = generate_hd_images(api_key=api_key, prompt=st.session_state.enhanced_prompt.get("enhanced_prompt"), model_version='2.2', num_results=1)
        # st.text_area(generated_img)
            # st.image(generated_img, caption="Generated HD Image", use_column_width=True)


if __name__ == "__main__":
    main()