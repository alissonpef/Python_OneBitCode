from PyPDF2 import PdfWriter, PdfReader
from reportlab.pdfgen import canvas
from reportlab.lib.pagesizes import A4
from reportlab.lib import colors
from io import BytesIO
import os

def modify_pdf(filename, cpf, position, color, upload_folder):
    packet = BytesIO()
    can = canvas.Canvas(packet, pagesize=A4)

    # Define a posição do texto no PDF
    positions = {
        'top-left': (50, 800),
        'top-right': (500, 800),
        'bottom-left': (50, 50),
        'bottom-right': (500, 50)
    }

    if position not in positions:
        raise ValueError('Invalid position')

    x, y = positions[position]

    # Mapeia as cores para o formato RGB
    color_map = {
        'red': colors.red,
        'blue': colors.blue,
        'black': colors.black
    }

    # Verifica se a cor escolhida é válida
    if color not in color_map:
        raise ValueError('Invalid color')

    # Define a cor do texto
    can.setFillColor(color_map[color])  
    can.setFont("Helvetica", 8)
    can.drawString(x, y, cpf)
    can.save()

    try:
        packet.seek(0)
        new_pdf = PdfReader(packet)
        print("Successfully created new PDF with CPF.")

        existing_pdf_path = os.path.join(upload_folder, filename)

        with open(existing_pdf_path, "rb") as existing_file:
            existing_pdf = PdfReader(existing_file)
            output = PdfWriter()

            print(f"Number of pages in existing PDF: {len(existing_pdf.pages)}")

            for i in range(len(existing_pdf.pages)):
                page = existing_pdf.pages[i]
                page.merge_page(new_pdf.pages[0])  # Adiciona o CPF na página
                output.add_page(page)

            # Salva o novo PDF modificado
            with open(existing_pdf_path, "wb") as outputStream:
                output.write(outputStream)

            print(f"Modified PDF saved at: {existing_pdf_path}")

    except Exception as e:
        print("Error processing PDF: " + str(e))
