
import pdfkit


def html_to_pdf(html_string, output_pdf_path):

    try:
        # Configure pdfkit options
        options = {
            'page-size': 'A4',
            'margin-top': '8mm',
            'margin-right': '8mm',
            'margin-bottom': '8mm',
            'margin-left': '8mm',
            'encoding': 'UTF-8',
        }
        config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\Bin\wkhtmltopdf.exe")

        # Create a PDF from the HTML string and save it to the output path
        pdfkit.from_string(html_string, output_pdf_path, options=options, configuration=config)


        print(f"PDF saved to: {output_pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

data = '''
<!DOCTYPE html>
<html>
<head>
<title>NON-DISCLOSURE AGREEMENT (NDA)</title>
<style>
h1 {
  text-align: center;
}
h2, h3, h4, h5, h6 {
  font-weight: bold;
}
</style>
</head>
<body>
<h1>NON-DISCLOSURE AGREEMENT (NDA)</h1>

<h2>PARTIES</h2>

<p>- This Non-Disclosure Agreement (hereinafter referred to as the "Agreement") is entered into on 12.09.2023, by and between QuiTech, with an address of Chennai,India (hereinafter referred to as the "Company"), and TCS, with an address of Chennai,India (hereinafter referred to as the "Partner") (collectively referred to as the "Parties").</p>

<h2>CONFIDENTIAL INFORMATION</h2>

<p>The Partner agrees not to disclose, copy, clone, or modify any confidential information related to the Company and agrees not to use any such information without obtaining consent.</p>

<p>"Confidential information" refers to any data and/or information that is related to the Company, in any form, including, but not limited to, oral or written. Such confidential information includes, but is not limited to, any information related to the business or industry of the Company, such as discoveries, processes, techniques, programs, knowledge bases, customer lists, potential customers, business partners, affiliated partners, leads, know-how, or any other services related to the Company.</p>

<h2>OBLIGATIONS</h2>

<p>The Partner agrees to the following obligations:</p>

<ol>
  <li>Not to use confidential information in any way that deviates from authorized purposes.</li>
  <li>Not to disclose the object and scope of any discussions between the Parties, except where required by law.</li>
  <li>Not to disclose confidential information to any third party without written consent of the Company.</li>
  <li>That upon termination of the partnership, all records pertaining to confidential information be returned to the Company.</li>
</ol>

<h2>EXCEPTIONS</h2>

<p>The obligations outlined above shall not apply to material that:</p>

<ol>
  <li>Through no act of the Partner becomes part of the public domain.</li>
  <li>Can be proven to be owned by the Partner before this Agreement.</li>
  <li>Is disclosed by court order.</li>
  <li>Is authorized for release in writing by the Company.</li>
</ol>

<h2>COURT ORDERS AND NOTIFICATION</h2>

<p>Should the Partner receive a court order to turn over any confidential information, the Company must be immediately notified in order to either seek a protective order or waive this Agreement according to the Company's discretion.</p>

<h2>OWNERSHIP</h2>

<p>Both parties understand that confidential information is owned by the Company, and any disclosure of such to the Partner does not convey any manner of license, title, or right to this information and may not appropriate any portion of it for unauthorized uses.</p>

<h2>TERMINATION AND RETURN OF RECORDS</h2>

<p>Termination of the relationship between the Company and the Partner does not relieve the Partner and associates of their obligations outlined in this Agreement, including the return of all records.</p>

<h2>GOVERNING LAW</h2>

<p>This Agreement shall be governed under the jurisdiction of the state of India.</p>

<h2>SIGNATURE AND DATE</h2>

<p>The Parties hereby agree to the terms and conditions set forth in this Agreement and such is demonstrated by their signatures below:</p>

<h3>COMPANY</h3>

<p>Name:____________________________</p>
<p>Signature:_________________________</p>
<p>Date:_____________________________</p>

<h3>PARTNER</h3>

<p>Name:____________________________</p>
<p>Signature:_________________________</p>
<p>Date:_____________________________</p>

</body>
</html>
'''

html_to_pdf(data,'Test.pdf')
