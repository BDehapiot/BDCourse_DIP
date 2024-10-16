#%% Imports -------------------------------------------------------------------

from pathlib import Path

from reportlab.lib.pagesizes import letter, A4
from reportlab.pdfgen import canvas
from reportlab.lib.colors import HexColor
from reportlab.lib import colors
from reportlab.lib.units import inch
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import landscape
from reportlab.graphics import renderPDF

from svglib.svglib import svg2rlg

#%% Comments ------------------------------------------------------------------

'''
- Convert mm to points (1 mm = 2.83465 points)

'''

#%% Inputs --------------------------------------------------------------------

name = "test.pdf"
width, height = 300, 200

#%% Function(s) ---------------------------------------------------------------

def create_canvas(name, width=300, height=200):
    c = canvas.Canvas(name, pagesize=(width * mm, height * mm))
    return c

def add_text(
        c, text="text", 
        x=10, y=10, 
        font="Helvetica",
        size=20,
        color=(0, 0, 0),
        align="left",
        ):
        
    # Setup font
    c.setFont(f"{font}", size) # font type & size
    c.setFillColorRGB(color[0], color[1], color[2]) # font color
        
    # Draw text
    if align == "left":
        c.drawString(
            x * mm, y * mm, text)
    elif align == "center":
        c.drawCentredString(
            x * mm, y * mm, text)
    elif align == "right":
        c.drawRightString(
            x * mm, y * mm, text)
        
def add_image(
    c, image_path, 
    x=10, y=10, 
    width=None, height=None, 
    preserve_aspect_ratio=True, 
    mask="auto",
    ):
    
    if width and height and preserve_aspect_ratio:
        c.drawImage(
            image_path, 
            x * mm, y * mm, 
            width=width * mm, 
            height=height * mm, 
            preserveAspectRatio=True, 
            mask=mask,
            )
    else:
        c.drawImage(
            image_path, 
            x * mm, y * mm, 
            width=width * mm if width else None, 
            height=height * mm if height else None, 
            mask=mask,
            )
        
def add_svg(
        c, svg_path, 
        x=10, y=10, 
        width=None, height=None,
        ):
    
    # Convert SVG to ReportLab's drawing object
    drawing = svg2rlg(svg_path)
    
    # Scale the drawing to the desired width and height
    if width and height:
        scale_x = width / drawing.width
        scale_y = height / drawing.height
        drawing.width = width
        drawing.height = height
        drawing.scale(scale_x, scale_y)
    
    # Translate to the specified (x, y) coordinates
    renderPDF.draw(drawing, c, x * mm, y * mm)
        
def save_pdf(c):
    c.showPage()
    c.save()

#%% Execute -------------------------------------------------------------------

if __name__ == "__main__":
    c = create_canvas(name, width=width, height=height)
    # add_text(c, text="text", x=10, y=10)
    # add_image(c, Path.cwd() / "img.jpg", x=50, y=50, width=100, height=100)
    add_svg(c, Path.cwd() / "test.svg")
    save_pdf(c)