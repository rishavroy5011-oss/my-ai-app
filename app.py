import streamlit as st
import requests

st.set_page_config(page_title="AI Multi-Tool Hub", layout="centered")

st.title("🚀 All-In-One AI Creator Hub")
st.write("Bina kisi kharch ke apni scripts, blogs aur resumes generate karein.")

option = st.sidebar.selectbox(
    "Aapko kya kaam karna hai?",
    ("YouTube Script Writer", "SEO Blog Post Writer", "Resume Optimizer")
)

# Free Open AI Worker Function
def ask_free_ai(prompt_text):
    try:
        url = f"https://pollinations.ai{requests.utils.quote(prompt_text)}"
        response = requests.get(url)
        if response.status_code == 200:
            return response.text
        else:
            return "Server thoda busy hai, please ek baar dubara generate button dabayein!"
    except:
        return "Connection error! Please internet check karein."

# 1. YouTube Script
if option == "YouTube Script Writer":
    st.subheader("🎥 YouTube Script Generator")
    topic = st.text_input("Video ka Topic/Idea dalein:")
    duration = st.slider("Video kitne minute ki chahiye?", 1, 15, 5)
    
    if st.button("Generate Script"):
        if topic:
            with st.spinner("AI Script likh raha hai..."):
                prompt = f"Write a viral YouTube script in Hinglish for a {duration}-minute video on the topic: '{topic}'. Include a catchy intro hook and engaging storytelling tone."
                result = ask_free_ai(prompt)
                st.success("Aapki Script Taiyar Hai! 👇")
                st.write(result)
        else:
            st.error("Please enter a topic first!")

# 2. SEO Blog
elif option == "SEO Blog Post Writer":
    st.subheader("✍️ SEO Blog Post Writer")
    blog_topic = st.text_input("Blog ka Keyword ya Topic dalein:")
    
    if st.button("Generate Blog"):
        if blog_topic:
            with st.spinner("Blog content create ho raha hai..."):
                prompt = f"Write a 500-word SEO optimized blog post in Hinglish on the topic: '{blog_topic}'. Use proper headings, subheadings, and a professional yet conversational tone."
                result = ask_free_ai(prompt)
                st.success("Blog Post Taiyar Hai! 👇")
                st.write(result)
        else:
            st.error("Please enter a blog topic!")

# 3. Resume Enhancer
elif option == "Resume Optimizer":
    st.subheader("📄 AI Resume Enhancer")
    current_resume = st.text_area("Apna current resume text copy-paste karein:")
    job_desc = st.text_area("Jis job ke liye apply karna hai uska Job Description (JD) dalein:")
    
    if st.button("Optimize Resume"):
        if current_resume and job_desc:
            with st.spinner("Resume optimize ho raha hai..."):
                prompt = f"Analyze this resume: '{current_resume}' against this Job Description: '{job_desc}'. Rewrite the resume bullets to match the core skills required, making it 100% ATS-friendly. Output in Hinglish mixed with professional English terms."
                result = ask_free_ai(prompt)
                st.success("Optimized Resume Points! 👇")
                st.write(result)
        else:
            st.error("Dono fields bharna zaroori hai!")
