# AI Content Generator

## Project Summary
**AI Content Generator** is a Generative AI platform that transforms raw YouTube videos into multiple types of content including:  
- Transcripts  
- Summaries  
- Blog posts  
- Social media content

This tool leverages advanced AI to save time, boost productivity, and enhance content creation for creators and marketers.

## Problem Definition
Creating high-quality content from videos manually is time-consuming and requires multiple steps. Content creators need a tool that can automatically convert video content into readable, shareable, and engaging formats. **AI Content Generator** solves this problem by automating content generation while maintaining style, tone, and context.

## Input Variables
The application requires the following inputs:  
- **YouTube Video Link**: URL of the video to process  
- **Content Preferences** (for social media outputs):  
  - Style  
  - Tone  
  - Hashtags  
  - Call to Action  
  - Word Count  

These inputs allow the platform to generate content that is tailored to the user’s needs and platform requirements.

## Technology
- **Model**: Gemma LLM (Large Language Model)  
- **Backend**: FAST API, Python, LangChain, Prompt, RAG  
- **Frontend**: Stramlit

## Features
- Automatic transcription of YouTube videos  
- AI-generated summaries
- Social media post creation with customizable style and tone  
- Configurable word count and hashtags  

## Usage
1. Provide a YouTube video link.  
2. Set your preferences (style, tone, hashtags, CTA, word count).  
3. Click **Generate Content**.  
4. Copy the output for your platforms.

## Future Enhancements
- Support for multiple video platforms  
- Multi-language content generation  
- Integration with scheduling tools for automatic posting  

## Follow Step to execute the application

-  **Step 1. Create Virtual Environment using Conda**  
conda crete -p <<virtual_env_folder_name>> python=<<python_version>> -y  
conda create -p virtual_env python==3.11 -y

-  **Step 2. Activate vitual enviroment**  
conda acitvate <<virtual_env_folder_name>>/  
conda activate virtual_env/  

-  **Step 4. Install Packages**  
pip install -r requirements.txt

-  **Step 3. Run Streamlit App**  
streamlit run <<file_name>>  
streamlit run streamlit.py  
