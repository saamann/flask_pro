from flask import render_template, Flask, send_file
import pdfkit
from PyPDF2 import PdfMerger

options = {
    'margin-top': '0mm',
    'margin-right': '0mm',
    'margin-bottom': '0mm',
    'margin-left': '0mm',
    'quiet': '',
    'no-outline': None,
    'enable-local-file-access': '',
    'dpi': 400,
    'disable-smart-shrinking': '',
    'enable-local-file-access': None,
    'page-size': 'A4',
    'encoding': 'UTF-8',
    'orientation': 'Landscape',
}

app = Flask(__name__, template_folder='templates')

@app.route('/pdf')
def generate_pdf():
    merger = PdfMerger()
    static_page_num = [1]

    for i in static_page_num:
        # Render the HTML template to a string
        html_content = render_template(f'page{i}.html')

        # Generate PDF from the HTML content
        pdf_filename = f'page{i}.pdf'
        pdfkit.from_string(html_content, pdf_filename, options=options, css='static/styles.css')

        merger.append(pdf_filename)

    # Merge PDFs and save the final PDF
    output_filename = 'output.pdf'
    merger.write(output_filename)
    merger.close()

    return send_file(output_filename, as_attachment=True)

@app.route('/page1')
def page1():
    return render_template('page1.html')
@app.route('/page6')
def page6():
    return render_template('page6.html')

@app.route('/page7')
def page7():
    return render_template('page7.html')

@app.route('/page8')
def page8():
    return render_template('page8.html')
@app.route('/page9')
def page9():
    return render_template('page9.html')
@app.route('/page10')
def page10():
    return render_template('page10.html')

@app.route('/page11')
def page11():
    return render_template('page11.html')

@app.route('/page12')
def page12():
    return render_template('page12.html')
@app.route('/page13')
def page13():
    return render_template('page13.html')

@app.route('/page14')
def page14():
    return render_template('page14.html')


@app.route('/page15')
def page15():
    return render_template('page15.html')

if __name__ == '__main__':
    app.run(debug=True)
