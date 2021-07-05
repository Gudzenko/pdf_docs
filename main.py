import pdfkit
import mammoth

# for windows install package from https://wkhtmltopdf.org/downloads.html


class FormatConverter:
    def __init__(self):
        self.config = pdfkit.configuration(wkhtmltopdf="C:\\Program Files\\wkhtmltopdf\\bin\\wkhtmltopdf.exe")
        self.options = {
            'encoding': "UTF-8"
        }

    def from_string_to_pdf(self, html, pdf, css=None):
        pdfkit.from_string(html, pdf, configuration=self.config, css=css, options=self.options)

    def from_file_to_pdf(self, name, pdf, css=None):
        with open('index.html') as f:
            self.from_string_to_pdf(html=f.read(), pdf=pdf, css=css)

    @staticmethod
    def from_doc_to_html(docx, html):
        with open(docx, "rb") as docx_file:
            result = mammoth.convert_to_html(docx_file)
        with open(html, "w") as html_file:
            html_file.write(result.value)

    def from_template_to_pdf(self, html, params, pdf):
        with open(html) as html_file:
            result = html_file.read()
            self.from_string_to_pdf(html=result.format(**params), pdf=pdf)


if __name__ == '__main__':
    body = """
        <!DOCTYPE html>
        <html>
          <body>
            <div id="header"></div>
            <div class="left"></div>
            <div class="stuff">
              <br><br>
              <h1>Resume</h1>
              <h2>{name}</h2>
              <hr />
              <br>
              <p class="head">Interests</p>
              <ul>
                <li>Drawing</li>
                <li>Photography</li>
                <li>Design</li>
                <li>Programming</li>
                <li>Computer Science</li>
              </ul>
              <p class="head">Skills</p>
              <ul>
                <li>Web Design with HTML & CSS</li>
              </ul>
              <p class="head">Education</p>
              <ul>
                <a href="http://www.wiltonhighschool.org/pages/Wilton_High_School">
                  <li>Wilton High School</li>
                </a>
                <!--Link-->
                <a href="https://www.silvermineart.org/">
                  <li>Silvermine School of Arts</li>
                </a>
                <li>Codeacademy</li>
              </ul>
              <p class="head">Experience</p>
              <ul>
                <li>Student Technology Intern for Wilton School District</li>
                <li>Babysitter</li>
              </ul>
              <p class="head">Extracurriculars</p>
              <ul>
                <li>Recycling Club</li>
                <li>Gardening Club</li>
                <li>Book Club</li>
              </ul>
            </div>
            <div class="right"></div>
            <div id="footer">
              <h2 id="name">{name}</h2>
            </div>
        </body>
        </html>
        """.format(name="John Smith")

    converter = FormatConverter()
    converter.from_string_to_pdf(html=body, css='style.css', pdf='cv.pdf')
    with open('index.html', 'w') as file:
        file.write(body)
    converter.from_file_to_pdf(name='index.html', css='style.css', pdf='cv2.pdf')
    FormatConverter.from_doc_to_html(docx="Events.docx", html='index_doc.html')
    converter.from_template_to_pdf(html='index_doc.html', params={'event_name': 'Event1', 'location': 'London', 'robots': 'Robot'}, pdf='Event.pdf')
