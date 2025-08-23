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


LINKEDIN_POST_PROMPT = PromptTemplate.from_template(
"""
You are a LinkedIn content creator. Based on the transcript, create a LinkedIn post.


Rules:
- Max {max_chars} characters total.
- STYLE: {style}; TONE: {tone}
- Include emojis if {include_emojis}.
- If {add_hashtags}, add {hashtags_n} relevant hashtags at the end.
- Include a call to action if {call_to_action}.


Transcript:
{transcript}


Return a JSON object with keys: hook, body, cta (nullable), hashtags (array).
"""
)

SUMMARY_PROMPT = PromptTemplate.from_template(
    """
You are an expert summarizer. 
Your task is to condense the following transcript segment into a clear, factual summary.

Guidelines:
- Keep it under 3 to 4 sentences.
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
    - "Bullet Points": Return 3–6 concise bullet points capturing the main ideas.
    - "Short Summary": Return 3–5 sentences, clear and to the point.
    - "Detailed Summary": Return 1–2 paragraphs covering all key details, examples, and context.

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
