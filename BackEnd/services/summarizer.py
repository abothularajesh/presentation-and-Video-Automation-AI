# from utils.text_cleaner import clean_text

# def generate_slide_content(text: str, max_slides: int = 6):
#     text = clean_text(text)
#     sentences = text.split(". ")

#     slides = []
#     slide_size = max(3, len(sentences) // max_slides)

#     for i in range(0, len(sentences), slide_size):
#         chunk = sentences[i:i+slide_size]
#         if len(slides) >= max_slides:
#             break

#         slides.append({
#             "title": f"Slide {len(slides)+1}",
#             "content": chunk[:5]
#         })

#     return slides