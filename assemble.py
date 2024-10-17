#%% Imports -------------------------------------------------------------------

import os
import fitz
from pathlib import Path

# reportlab
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfgen.canvas import Canvas
from reportlab.pdfbase.ttfonts import TTFont

#%% Function(s) ---------------------------------------------------------------

def ai2pdf(slides_path, canvas_path, pdf_path, skip_empty=True):
    
    # Nested function(s) ------------------------------------------------------
    
    def is_empty(page):
        if page.get_text("text").strip() != "":
            return False  # Page contains text
        if len(page.get_images(full=True)) > 0:
            return False  # Page contains images
        return True
    
    def draw_text(c, text, x, y, size=12, color=(0, 0, 0), align="left"):
        
        # Bahnschrift font
        font_path = Path("C:/Windows/Fonts/Bahnschrift.ttf")
        pdfmetrics.registerFont(TTFont("Bahnschrift", str(font_path)))
        
        # Setup canvas
        c.setFont("Bahnschrift", size) # type & size
        c.setFillColorRGB(
            color[0] / 255, color[1] / 255, color[2] / 255) # color
        
        # Draw text
        if align == "left":
            c.drawString(x * mm, y * mm, text)
        elif align == "center":
            c.drawCentredString(x * mm, y * mm, text)
        elif align == "right":
            c.drawRightString(x * mm, y * mm, text)
        
    def get_canvas():
        
        # Define text & style 
        title_01 = "Digital image processing"
        title_02 = "Basic concepts"
        title_02m = title_01 + " - " + title_02
        title_03 = "Images are made of pixels"
        title_cr = "© Benoit Dehapiot, 2024"
        
        # 
        canvas = fitz.open(Path("local", "canvas", "canvas.ai"))
        cPage = canvas.load_page(0)
        
        # 
        
        text = Canvas("text.pdf", pagesize=(300 * mm, 200 * mm))
        draw_text(
            text, title_03, 
            10, 176, size=36, color=(0, 0, 0), align="left"
            )
        draw_text(
            text, title_02m, 
            10, 8, size=14, color=(0, 0, 0), align="left"
            )
        draw_text(
            text, title_cr, 
            282, 8, size=14, color=(218, 218, 218), align="right"
            )
        text.save()
        
        text = fitz.open("text.pdf")
        tPage = text.load_page(0)
                
        return canvas, text, cPage, tPage
    
    # Execute -----------------------------------------------------------------

    # Create PDF
    pdf = fitz.open()
    
    # Get canvas
    canvas, text, cPage, tPage = get_canvas()

    # Read Adobe Illustrator slides
    slides = fitz.open(slides_path)
    for page_num in range(len(slides)):
        sPage = slides.load_page(page_num)
        if skip_empty and is_empty(sPage):
            continue
        new_page = pdf.new_page(
            width=sPage.rect.width,
            height=sPage.rect.height
            )
        new_page.show_pdf_page(cPage.rect, canvas, 0)
        new_page.show_pdf_page(tPage.rect, text, 0)
        new_page.show_pdf_page(sPage.rect, slides, page_num)

    # Save PDF
    if len(pdf) > 0:
        pdf.save(pdf_path)

    pdf.close()
    canvas.close()
    text.close()
    slides.close()
    
    os.remove("text.pdf")

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    
    # Inputs
    slides_name = "DIP_1.1_Basic-Concepts_Pixels"
    slides_path = Path("local", slides_name, slides_name + ".ai")
    canvas_path = Path("local", "canvas", "canvas.ai")
    pdf_path = "test.pdf"
    
    # Assemble
    ai2pdf(slides_path, canvas_path, pdf_path)
    
#%%

