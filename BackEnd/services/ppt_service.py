# from pptx import Presentation
# from pptx.util import Pt
# from pptx.enum.text import PP_ALIGN
# from pptx.dml.color import RGBColor
# import os
# from datetime import datetime

# GENERATED_FOLDER = "generated"

# def create_presentation(topic: str, slides_data: list):
#     if not os.path.exists(GENERATED_FOLDER):
#         os.makedirs(GENERATED_FOLDER)

#     prs = Presentation()

#     # Title Slide
#     title_slide_layout = prs.slide_layouts[0]
#     slide = prs.slides.add_slide(title_slide_layout)
#     slide.shapes.title.text = topic
#     slide.placeholders[1].text = "AI Generated Presentation"

#     # Content Slides
#     for slide_data in slides_data:
#         slide_layout = prs.slide_layouts[1]
#         slide = prs.slides.add_slide(slide_layout)

#         slide.shapes.title.text = slide_data["title"]

#         content = slide.placeholders[1]
#         content.text = ""

#         for point in slide_data["content"]:
#             p = content.text_frame.add_paragraph()
#             p.text = point
#             p.level = 1

#     timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
#     file_name = f"{topic}_{timestamp}.pptx"
#     file_path = os.path.join(GENERATED_FOLDER, file_name)

#     prs.save(file_path)

#     return file_path