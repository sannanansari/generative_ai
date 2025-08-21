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