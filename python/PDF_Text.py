import PyPDF2
import os

def extract_text_from_pdf(pdf_path):
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text = ''
        for page_num in range(len(pdf_reader.pages)):
            text += pdf_reader.pages[page_num].extract_text()
    return text

def create_html_from_text(text):
    # Add your HTML structure and styling here
    html_content = f"""
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>Converted Resume</title>
        <style>
            /* Add your CSS styling here */
            body {{
                font-family: Arial, sans-serif;
                line-height: 1.6;
                margin: 20px;
            }}
            /* Add more styling as needed */
        </style>
    </head>
    <body>
        <div>
            {text}
        </div>
    </body>
    </html>
    """
    return html_content

# Specify the file path to your PDF resume
pdf_path = r'C:\Users\17574\Downloads\Resume GEOG 572.pdf'

# Extract text from the PDF
text_from_pdf = extract_text_from_pdf(pdf_path)

# Specify the output HTML path
output_html_path = r'C:\Users\17574\Documents\GEOG 572\Final\roberta-rothers-portfolio-v5-1\roberta-rothers-portfolio-v5\Output\converted_resume.html'

# Create HTML content
html_content = create_html_from_text(text_from_pdf)

# Save the HTML content to the specified output path
with open(output_html_path, 'w', encoding='utf-8') as html_file:
    html_file.write(html_content)

print(f"HTML file saved at: {output_html_path}")
