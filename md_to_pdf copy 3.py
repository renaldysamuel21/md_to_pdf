import os
import markdown
import pdfkit

def md_to_pdf(input_md, output_pdf):
    # Baca file markdown
    with open(input_md, "r", encoding="utf-8") as f:
        text = f.read()

    # Konversi markdown → HTML
    html_content = markdown.markdown(
        text, extensions=["fenced_code", "tables", "toc", "attr_list"]
    )

    # HTML + CSS untuk PDF
    html_template = f"""
    <html>
    <head>
      <meta charset="utf-8">
      <style>
        body {{
          font-family: "Times New Roman", serif;
          font-size: 13pt;
          line-height: 1.5;
          margin: 0;
        }}
        h1 {{
          font-size: 22pt;
          text-align: center;
          font-weight: bold;
          margin-bottom: 0.6em;
        }}
        h2 {{
          font-size: 18pt;
          margin-top: 1em;
          font-weight: bold;
        }}
        h3 {{
          font-size: 15pt;
          margin-top: 0.8em;
          font-weight: bold;
        }}
        hr {{
          border: none;
          border-top:1px solid #000;
          margin: 1em 0;
        }}
        ul, ol {{
          margin-left: 1.5em;
          margin-bottom: 0.6em;
        }}
        code {{
            background: #f4f4f4;
            padding: 2px 4px;
            border-radius: 3px;
            font-size: 90%;
        }}
      </style>
    </head>
    <body>
      {html_content}
    </body>
    </html>
    """

    # Konfigurasi wkhtmltopdf
    path_wkhtmltopdf = r"S:\Program Files\wkhtmltopdf\bin\wkhtmltopdf.exe"
    config = pdfkit.configuration(wkhtmltopdf=path_wkhtmltopdf)

    # Margin 2.54cm & footer nomor halaman
    options = {
        'margin-top': '25.4mm',
        'margin-bottom': '25.4mm',
        'margin-left': '25.4mm',
        'margin-right': '25.4mm',
        'footer-center': 'Halaman [page] dari [toPage]',
        'footer-font-size': '9'
    }

    pdfkit.from_string(html_template, output_pdf, configuration=config, options=options)
    print(f"PDF berhasil dibuat: {output_pdf}")


if __name__ == "__main__":
    base = r"S:\Python Projects\md_to_pdf"
    md_to_pdf(
        os.path.join(base, "USER_GUIDE.md"),
        os.path.join(base, "USER_GUIDE.pdf")
    )
