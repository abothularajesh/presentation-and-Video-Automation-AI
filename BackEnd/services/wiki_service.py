# import wikipedia

# def get_wikipedia_content(topic: str):
#     try:
#         page = wikipedia.page(topic, auto_suggest=True)
#         return page.content
#     except wikipedia.exceptions.DisambiguationError as e:
#         return f"Topic is ambiguous. Suggestions: {e.options[:5]}"
#     except wikipedia.exceptions.PageError:
#         return None
#     except Exception:
#         return None