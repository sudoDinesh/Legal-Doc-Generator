from Knowledge import knowledge
from Templates import templates
from Htmlgen import htmls
import pdfkit
from test import fillin
import streamlit as st

import Advisor
import TemplateEngine
import HtmlGen

def html_to_pdf(html_string, output_pdf_path):

    try:
        # Configure pdfkit options
        options = {
            'page-size': 'A4',
            'margin-top': '20mm',
            'margin-right': '20mm',
            'margin-bottom': '20mm',
            'margin-left': '20mm',
            'encoding': 'UTF-8',
        }
        config = pdfkit.configuration(wkhtmltopdf="C:\Program Files\wkhtmltopdf\Bin\wkhtmltopdf.exe")

        # Create a PDF from the HTML string and save it to the output path
        pdfkit.from_string(html_string, output_pdf_path, options=options, configuration=config)


        print(f"PDF saved to: {output_pdf_path}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    
    if 'conversation1' not in st.session_state:
        st.session_state.conversation1 = None
    if 'conversation2' not in st.session_state:
        st.session_state.conversation2 = None
    if 'conversation3' not in st.session_state:
        st.session_state.conversation3 = None
        
    st.title('Legal Documentation Assistant')

    with st.spinner("Loading..."):
            
        knowledge.Develop()
        templates.Develop()
        htmls.Develop()
    
    query = st.text_input('Explain elaborately what do you need to document legally: ')
        

    # query = input('Explain elaborately what do you need to document legally: ')
    if query:
        with st.spinner('Processing'):
            st.session_state.conversation1 = Advisor.get()
            response = st.session_state.conversation1({'question':f'Tell me the name of one legal document related to the need {query}. Give the name alone do not give a sentence'})

            print('\n\n'+response['answer']+'\n\n')
            document = response['answer']

            response = st.session_state.conversation1({'question':f'Find the laws or acts related to the below details\n Document : {document}\n User query: {query}'})
            laws = response['answer']
            print(laws)
            prompt = f'''
            Give a , Very long template for the '{document}' and it should be very elaborate and explained so that a layman could understand 
            considering' {query}' 
            also include these laws {laws}
            use good understandable placeholders enclosed with square brackets for every information that has to be filled before taking print
            leave empty space for signatures
            Dont give any disclaimers
            Make it very elaborate as if you are explaining to a illiterates
            '''

            st.session_state.conversation2 = TemplateEngine.get()
            response = st.session_state.conversation2({'question':prompt})
            
            template = response['answer']
            print(template)
            result = fillin(template)

            st.session_state.conversation3 = HtmlGen.get()
            prompt2 = f'''
            I want you to convert document into a html enclosing the appropriate field with appropriate tags based on your knowledge of how legal documents should look.
            I want the first heading to be aligned centre and all the headings to be bold and all the font must be Times New roman and the font must be clear 
            The alignment should look formal for a legal document and use seperate div classes if needed to align 
            here is the content of the document document
            {result}
            '''
            print(prompt2)
            response = st.session_state.conversation3({'question':prompt2})
            htmlresult = response['answer']
            print(htmlresult)

            html_to_pdf(htmlresult,f'st.pdf')

if __name__=='__main__':
    main()

