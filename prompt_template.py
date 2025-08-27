from langchain.prompts import PromptTemplate
summerize_template = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text: {text}"
)

# Prompt for chunk-level summarization ("map step")
map_prompt = PromptTemplate(
    template="""
    You are an expert summarizer. Summarize the following text clearly and concisely.
    Focus on the **key ideas**, remove filler words, and keep context.

    Text:
    {text}

    Summary:
    """,
    input_variables=["text"]
)

# Prompt for combining summaries ("reduce step")
combine_prompt = PromptTemplate(
    template="""
    You are an expert summarizer. Combine the following partial summaries into a
    single well-structured summary. Make it concise but comprehensive,
    and preserve important details.

    Partial summaries:
    {text}

    Final summary:
    """,
    input_variables=["text"]
)


# LINKEDIN_POST_PROMPT = PromptTemplate.from_template(
#     """
# You are a LinkedIn content creator. Based on the transcript, create a LinkedIn post. 
# Do not hallicinate. If you do not know the content just say I dont know the answer.


# Rules:
# - Max {max_words} words total.
# - STYLE: {style}; TONE: {tone}
# - Include emojis if {include_emojis}.
# - If {add_hashtags}, add {hashtags_n} relevant hashtags at the end with hashtag key.
# - Include a call to action if {call_to_action}.


# Transcript:
# {transcript}


# Return a JSON object with keys : hook, body, call_to_action, and hashtags (array). Do NOT include any explanations, quotes, markdown, or code fences. 
# """
    
# )



LINKEDIN_POST_PROMPT = prompt_template = PromptTemplate(
    input_variables=[
        "transcript",
        "style",
        "tone",
        "include_emojis",
        "add_hashtags",
        "hashtags_n",
        "call_to_action",
        "max_words",
    ],
    template="""
Consider you are professional content creator. Your task is to generate a linkedin post content from below Transcript with following Instructions and fullfill the below requirements.

Transcript (source material):
{transcript}

Instructions:
- Style: {style}
- Tone: {tone}
- Include emojis: {include_emojis}
- Add hashtags: {add_hashtags} (limit: {hashtags_n})
- Call to Action: {call_to_action}
- Maximum words: {max_words}

Requirements:
1. Create an engaging post using transcript in the specified style and tone.  
2. Respect the maximum word limit.  
3. If include_emojis = "Yes", add relevant emojis naturally in the content.  
4. If add_hashtags = "Yes", generate up to {hashtags_n} relevant hashtags with hashtag key at the end.  
5. Ensure the call-to-action is included smoothly.  

Return a JSON object with keys : hook, body, call_to_action, and hashtags (array). Do NOT include any explanations, quotes, markdown, or code fences.
"""
)



SUMMARY_PROMPT = PromptTemplate.from_template(
    """
You are an expert summarizer. 
Your task is to condense the following transcript segment into a clear, factual summary.

Guidelines:
- Keep it under 7 to 8 sentences.
- Preserve key ideas, facts, examples, and numbers.
- Avoid unnecessary details, filler words, or repetition.
- Do not add personal opinions or commentary.
- Ensure the summary is coherent on its own.

Transcript segment:
{transcript_segment}

Summary:
"""
)


CUSTOM_SUMMARY_PROMPT  = PromptTemplate.from_template(
        """
    You are an expert summarizer. 
    Summarize the following text based on the requested summary type.

    Summary Types:
    - "Bullet Points": Return 3–4 concise bullet points capturing the main ideas.
    - "Short Summary": Return 4–5 sentences, clear and to the point.
    - "Detailed Summary": Return 5-6 paragraphs covering all key details, examples, and context.

    Guidelines:
    - Stay factual and neutral (no opinions).
    - Keep it coherent and avoid repetition.
    - Preserve important numbers, names, and facts.
    - Do not exceed what is asked for in the summary type.

    Summary Type: {summary_type}

    Text:
    {summerized_transcript}

    Summary:
    """
)


