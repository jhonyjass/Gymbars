from flask import render_template, make_response
from decouple import config
import pdfkit

ruta_wkhtmltopdf = config('WKHTMLTOPDF_BIN_PATH')

def generar_reporte(template, nombre_archivo, **kwargs):
    rendered = render_template(template, **kwargs)
    
    pdf_options = {
        'page-size': 'LETTER',
        'margin-top': '0.75in',
        'margin-right': '0.75in',
        'margin-bottom': '0.75in',
        'margin-left': '0.75in',
        'orientation': 'Portrait',
        'encoding': 'UTF-8',
        'no-outline': None,
        'quiet': '',
        'zoom': '0.7',
        'dpi': 96,
        'disable-smart-shrinking': ''
    }
    
    pdf = pdfkit.from_string(rendered, False, options=pdf_options, configuration=pdfkit.configuration(wkhtmltopdf=ruta_wkhtmltopdf))
    
    reporte_pdf = make_response(pdf)
    reporte_pdf.headers['Content-Type'] = 'application/pdf'
    reporte_pdf.headers['Content-Disposition'] = f'inline; filename={nombre_archivo}.pdf'
    
    return reporte_pdf