def build_report_prompt(transcript: str) -> str:
    """
    Creates the prompt that will be sent to the LLM.
    """

    prompt = f"""
You are an experienced equity research analyst.

Analyze the following earnings call transcript and generate a professional investment research report.

Your report should include the following sections:

# Executive Summary

Summarize the quarter in 2-3 paragraphs.

# Financial Highlights

List the most important financial metrics discussed.

# Positive Developments

Identify the company's major strengths, achievements, and positive business developments.

# Negative Developments

Identify challenges, weaknesses, or disappointing results.

# Risks

List the key risks mentioned or implied by management.

# Opportunities

List future growth opportunities discussed during the call.

# Management Guidance

Summarize management's outlook for future quarters.

# Key Quotes

Extract 3-5 important quotes from management.

# Management Confidence

Give a confidence score from 1-10 and explain your reasoning.

Instructions:

- Be objective.
- Do not speculate.
- Base every conclusion only on the transcript.
- If information is not discussed, state "Not discussed."
- Format the report using Markdown headings and bullet points.

Transcript:

{transcript}
"""

    return prompt