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