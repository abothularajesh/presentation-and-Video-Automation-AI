from groq import Groq
client = Groq(api_key="********************************")

def generate_slide_content(topic, slide_count):

    prompt = f"""
    Create {slide_count} presentation slides about {topic}.
    Each slide must contain:
    Title
    3 bullet points

    Format:
    Slide Title:
    - point
    - point
    - point
    """

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}]
    )
    content =response.choices[0].message.content

    return content