from youtube_transcript_api import YouTubeTranscriptApi
from langchain.schema import Document
from langchain.text_splitter import RecursiveCharacterTextSplitter
#from langchain_huggingface import HuggingFaceEndpoint
from langchain_groq import ChatGroq
from langchain.chains.summarize import load_summarize_chain
import streamlit as st
import validators
from prompt_template import LINKEDIN_POST_PROMPT, SUMMARY_PROMPT, CUSTOM_SUMMARY_PROMPT
from datetime import datetime
from langchain_core.output_parsers import StrOutputParser



def generate_linkedin_post(youtube_url):

    transcript = fetch_youtube_transcript(youtube_url)
    chunks_documents = text_splitter(transcript)
    compact_trascript = summarize_content(chunks_documents)
    llm = get_llm()

    generate_post_chain = LINKEDIN_POST_PROMPT | llm | StrOutputParser()

    inputs = {
        "transcript": compact_trascript,
        "style": "educational",
        "tone": "professional",
        "include_emojis": True,
        "add_hashtags": True,
        "hashtags_n": 6,
        "call_to_action": True,
        "max_chars": 3000,
    }

    raw_data = generate_post_chain.invoke(inputs)
    print(raw_data)

def summarize_content(chunks_documents):
    llm = get_llm()
    chain = SUMMARY_PROMPT | llm | StrOutputParser()

    summaries = []
    for i, chunk in enumerate(chunks_documents, 1):
        summary = chain.invoke({"transcript_segment": chunk})
        summaries.append(summary)
    return " ".join(summaries)


    
def generate_yt_summerization(youtube_url, summary_type="bullet_points"):
    """
    Generate a summary based on the summary_type for the given YouTube video URL.
    """
    # Get current timestamp
    timestamp = datetime.now()
    print(f"Before: Current timestamp: {timestamp}")
    # Step 1: Fetch the transcript of the YouTube video
    transcript = fetch_youtube_transcript(youtube_url)

    # Step 2: Split the document into smaller chunks
    chunks_documents = text_splitter(transcript)

    # Step 3: Summerize the each document chunks so that we can avoid pass the entire tokens to the llm
    compact_transcript_summary = summarize_content(chunks_documents)

    # Step 3: select the LLM
    llm = get_llm()

    # Step 4: Generate the summary
    generate_summary_chain = CUSTOM_SUMMARY_PROMPT | llm | StrOutputParser()
    output_summary = generate_summary_chain.invoke({"summerized_transcript": compact_transcript_summary, "summary_type": summary_type})

    # summarize_chain = load_summarize_chain(
    #     llm,
    #     chain_type="map_reduce",
    #     map_prompt=map_prompt,
    #     combine_prompt=combine_prompt
    # )
    # output_summary = summarize_chain.run(chunks_documents)
    print(output_summary)

    timestamp = datetime.now()
    print(f"after: Current timestamp: {timestamp}")
    
    # llm = ChatGroq(model_name="groq/groq-llama-3-8b")
    # summarize_chain = load_summarize_chain(llm, chain_type=summary_type, prompt=prompt_template)

    # # Step 5: Generate the summary
    # summary = summarize_chain.run(chunks_documents)
    
    #return summary


def fetch_youtube_transcript(youtube_url):
    """ Fetch the transcript of a YouTube video given its URL."""
    try:
        # Step 1: Validate the YouTube URL
        validate_youtube_url(youtube_url)
        # Step 2: Extract video ID from the URL
        video_id = youtube_url.split("v=")[-1].split("&")[0]
        ytt_api = YouTubeTranscriptApi()
        fetched_transcript = ytt_api.fetch(video_id)
        if fetched_transcript:
            # Step 3: Convert the fetched transcript to a Document object
            document = convert_snippet_to_document(fetched_transcript)
            return document
        else:
            raise ValueError("No Transcript Found for particular Video")
    except Exception as e:
        st.error(f"Error fetching transcript: {str(e)}")
        return None


def validate_youtube_url(youtube_url):
    """ Validate the YouTube URL format."""
    try:
        if not (validators.url(youtube_url) and "youtube.com/watch?v=" in youtube_url):
            raise ValueError("Invalid YouTube URL format.")
    except Exception as e:
        st.error(f"Error validating YouTube URL: {str(e)}")
        raise Exception("Invalid YouTube URL format.")

def convert_snippet_to_document(fetched_transcript):
    """ Convert a text snippet to a Document object."""
    documents = []
    for snippet in fetched_transcript.snippets:
        document = Document(
            page_content=snippet.text,  # the actual transcript text
            #metadata={'start': snippet.start, 'duration': snippet.duration}  # optional metadata
        )
        documents.append(document)
        full_text = " ".join([document.page_content for document in documents])
        full_document = Document(page_content=full_text)
    return full_document

def text_splitter(full_document):
    """ Split the full document into smaller chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=2000,  # Adjust chunk size as needed
        chunk_overlap=200  # Adjust overlap as needed
    )
    return text_splitter.split_documents([full_document])

def get_llm():
    llm =ChatGroq(model="Gemma2-9b-It", groq_api_key="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", temperature=0.5)
    return llm

#https://www.youtube.com/watch?v=p4pHsuEf4Ms
generate_yt_summerization("https://www.youtube.com/watch?v=3T3bR8sxnmo", summary_type="Short Summary")

#generate_linkedin_post("https://www.youtube.com/watch?v=3T3bR8sxnmo")












#  """
#     Generate a summary based on the summary_type for the given YouTube video URL.
#     """
#     from youtube_transcript_api import YouTubeTranscriptApi
#     from langchain_core.prompts import PromptTemplate
#     from langchain_groq import GroqLLM

#     # Extract video ID from the URL
#     video_id = youtube_url.split("v=")[-1].split("&")[0]

#     # Fetch transcript
#     try:
#         transcript = YouTubeTranscriptApi.get_transcript(video_id)
#         text = " ".join([entry['text'] for entry in transcript])
#     except Exception as e:
#         return f"Error fetching transcript: {str(e)}"

#     # Define prompt template
#     prompt_template = PromptTemplate(
#         input_variables=["text"],
#         template="Summarize the following text: {text}"
#     )

#     # Initialize Groq LLM
#     llm = GroqLLM(model_name="groq/groq-llama-3-8b")

#     # Generate summary
#     summary = llm(prompt_template.format(text=text))

#     return summary