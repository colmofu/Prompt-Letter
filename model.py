import openai
import os
import PyPDF2

openai.api_key = os.environ.get('OPENAI_API_KEY')

def get_completion(prompt, model="gpt-4"):
    """
    Helper function to get completion from model based on a prompt input
    """
    
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=0, # this is the degree of randomness of the model's output
    )
    return response.choices[0].message["content"]

def write_letter(job_posting: str, resume: str, lang = 'en', field = 'tech/data', *args, **kwargs):
    """
    Write cover letter for a job post in either English (default) or German.
    """
    languages = {'en': 'English',
                 'de': 'German'}
    
    prompt_topic = f"""
    You are an assistant for writing cover letters for job applications in the {field} field. You will receive the /
    job posting (`job_posting`) and applicant's resume (`resume`) as arguments. Using these documents and your expertise as a career specialist, /
    write a professional cover letter using sharp and field-relevant language. 

    Provide the output in string format in the {languages[lang]} language. The cover letter should be 300-350 words in total. The letter should /
    consist of a conventional format for a cover letter: /
    - An empty skeleton area for the user to enter the mailing information of the recruiter, /
    followed by a conventional greeting and the body split into three paragraphs.
     - A first paragraph consisting of 2-3 sentences, mentioning the position, the company, /
    and what attracted the applicant to the role. It should grasp the readers attention.
     - A second paragraph convincing the reader that the applicant is the perfect fit for the role, highlighting relevant experience. Here, /
    the letter should link relevant skills in the job-posting to compatible items found in the readers resume. It should be fact driven /
    and lean heavily on who the applicant is.
     - A third paragraph explaining what attracted the applicant to the company and position. Use what is provided about the role and company in the /
    job posting, and if provided, the additional arguments.
     - A concluding paragraph thanking the reader for their time and following a standard conclusion. 
        

    Review job_posting: '''{job_posting}'''
    Review resume: '''{resume}'''
    """

    letter = get_completion(prompt_topic)

    return letter

def text_to_pdf(text):
    """
    return pdf for written text from a txt to pdf
    """
    pdf = []
    return pdf

def pdf_to_text(pdf_file_name: str):
    """
    return text for pdf file path provided
    """
    file_name = pdf_file_name
    file_obj = open(os.path.abspath(os.path.join("pdf_files", file_name)), 'rb')
    
    reader = PyPDF2.PdfReader(file_obj)
    
    num_pages = len(reader.pages)
    
    # Extract text for each page
    text = ''
    for page in range(0, num_pages):
        obj = reader.pages[page]
        page_text = obj.extract_text()
        text = '\n'.join([text, page_text])
    
    # closing the pdf file object
    file_obj.close()
    
    return text
        

