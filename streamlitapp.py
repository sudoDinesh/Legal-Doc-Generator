from Knowledge import knowledge
from Templates import templates
from Htmlgen import htmls
import streamlit as st
import pdfkit
import Advisor
import TemplateEngine
import HtmlGen

# Define a function to convert HTML to PDF
def html_to_pdf(html_string):
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
        config = pdfkit.configuration(wkhtmltopdf="C:/Program Files/wkhtmltopdf/bin/wkhtmltopdf.exe")

        # Create a PDF from the HTML string and save it to the output path
        a = pdfkit.from_string(html_string, options=options, configuration=config)
        st.write('Click the button below to download your document and for further queries kindly mail : reddyrajan@law.gov.in')
        st.download_button(label="Download",data=a,file_name="Document.pdf",mime='application/octet-stream')
        # st.write(f"PDF saved to: {output_pdf_path}")
    except Exception as e:
        st.error(f"Error: {e}")

# Function to find all placeholders enclosed in squared brackets
def find_placeholders(template):
    import re
    return re.findall(r'\[([^]]+)\]', template)

# Streamlit app
def main():
    st.title('Legal Documentation Assistant')
    page_bg_img = """
    <style>
    [data-testid="stAppViewContainer"]{
        background-image: url("https://firebasestorage.googleapis.com/v0/b/notjayanth.appspot.com/o/unsplash-img.jpg?alt=media&token=80212a15-3d47-4596-ad6c-b28c11e5a5ff");
        background-size: cover;
    }
    [data-testid="stHeader"]{
        background-color: rgba(0,0,0,0);
    }
    </style>
    """
    st.markdown(page_bg_img,unsafe_allow_html=True)
    if 'conversation1' not in st.session_state:
        st.session_state.conversation1 = None
    if 'conversation2' not in st.session_state:
        st.session_state.conversation2 = None
    if 'conversation3' not in st.session_state:
        st.session_state.conversation3 = None
    if 'advisor_response' not in st.session_state:
        st.session_state.advisor_response = None  # Initialize the session state variable
    if 'template' not in st.session_state:
        st.session_state.template = None
    if 'k' not in st.session_state:
        st.session_state.k = None
    if 'dic' not in st.session_state:
        st.session_state.dic = None

    # with st.spinner("Loading..."):
        # Your code for loading modules...
    with st.spinner('Getting things ready..'):
        knowledge.Develop()
        templates.Develop()
        htmls.Develop()
    query = st.text_input('Explain elaborately what do you need to document legally: ')
    col1,col2 = st.columns(2)
    if query:
        if st.session_state.advisor_response is None:
            with st.spinner('Processing Advisor...'):
                st.session_state.conversation1 = Advisor.get()
                response = st.session_state.conversation1({'question':f'Tell me the name of one legal document related to the need {query}'})
                st.session_state.advisor_response = response  # Store the advisor's response

            st.write(st.session_state.advisor_response['answer'])
            document = st.session_state.advisor_response['answer']

            response = st.session_state.conversation1({'question':f'Find any legal information about this and explain it like I am a kid\n Document : {document}\n User query: {query}'})
            laws = response['answer']
            st.write(laws)

            prompt = f'''
            Give a very long template (details to be filled before taking print enclosed by squared brackets) for the {document} 
            in simple words that a layman can understand and detailed, without any disclaimers, and also consider that the user has said '{query}' 
            Rules: Use a unique names for placeholder names like address 1,address 2. No two placeholders must be containing same names
            Leave a blank space for signatures
            you dont have to provide disclaimers in the bottom
            {laws}
            '''

            st.session_state.conversation2 = TemplateEngine.get()
            response = st.session_state.conversation2({'question':prompt})
            template = response['answer']
            st.session_state.template = template
            with col1:
                st.write(template)

    # Check if template is available
        if st.session_state.template:
            placeholders = find_placeholders(st.session_state.template)
            filled_template = st.session_state.template
            st.session_state.k = 1
            
            with col2:
                with st.form(key='template_form'):
                    st.session_state.dic={}
                    for placeholder in placeholders:
                        user_input = st.text_input(f"Enter value for '{placeholder}':", key=f"{placeholder}_input{st.session_state.k}")
                        st.session_state.k+=1
                        # filled_template = filled_template.replace(f"[{placeholder}]", user_input)
                        st.session_state.dic[placeholder]=user_input
                    st.form_submit_button("Generate PDF")
        if st.session_state.dic:
            filled_template = st.session_state.template
            for placeholder, response in st.session_state.dic.items():
                filled_template = filled_template.replace(f"[{placeholder}]", response)
            print(filled_template)

            st.session_state.conversation3 = HtmlGen.get()
            prompt2 = f'''
            I want you to convert the document as it is into HTML enclosing the appropriate field with appropriate tags based on your knowledge.
            I want the first heading to be aligned center and all the headings to be bold, and all the fonts must be Times New Roman and formally spaced.
            Here is the document:
            {filled_template}
            '''
            
            response = st.session_state.conversation3({'question': prompt2})
            htmlresult = response['answer']
            
            # Generate the PDF with the filled template
            
            html_to_pdf(htmlresult)
            

if __name__=='__main__':
    main()
