from pptx import Presentation
from pptx.util import Inches, Pt

def create_ppt(slide_data, filename):

    prs = Presentation()

    # choose a clean slide layout
    layout = prs.slide_layouts[5]  # title only layout

    for slide in slide_data:

        s = prs.slides.add_slide(layout)

        # TITLE
        title = s.shapes.title
        title.text = slide["title"].replace("*","").strip()

        title.text_frame.paragraphs[0].font.size = Pt(40)

        # LEFT TEXT BOX (points)
        left = Inches(0.5)
        top = Inches(2)
        width = Inches(5)
        height = Inches(4)

        textbox = s.shapes.add_textbox(left, top, width, height)
        tf = textbox.text_frame

        for i, point in enumerate(slide["points"]):

            if i == 0:
                p = tf.paragraphs[0]
            else:
                p = tf.add_paragraph()

            p.text = point
            p.level = 0
            p.font.size = Pt(24)

        # RIGHT IMAGE
        if "image" in slide:

            img_left = Inches(6)
            img_top = Inches(2)

            s.shapes.add_picture(
                slide["image"],
                img_left,
                img_top,
                width=Inches(3.5)
            )

    output_path = f"outputs/slides/{filename}.pptx"
    prs.save(output_path)

    return output_path




# from pptx import Presentation
# import os

# def create_ppt(slides, filename):

#     prs = Presentation()

#     for slide in slides:

#         slide_layout = prs.slide_layouts[1]
#         slide_obj = prs.slides.add_slide(slide_layout)

#         title = slide_obj.shapes.title
#         content = slide_obj.placeholders[1]

#         title.text = slide["title"].replace("*","").strip()
#         content.text = "\n".join(slide["points"])

#         # Add image generation if it exists
#         if "image" in slide:

#             slide_obj.shapes.add_picture(
#                 slide["image"],
#                 left=prs.slide_width * 0.55,
#                 top=prs.slide_height * 0.25,
#                 width=prs.slide_width * 0.35
#             )

#     os.makedirs("outputs/slides", exist_ok=True)

#     path = f"outputs/slides/{filename}.pptx"

#     prs.save(path)

#     return path