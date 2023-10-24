import PyPDF2
from langchain.text_splitter import CharacterTextSplitter


class TextExtractor:
    @staticmethod
    def extract_text_from_pdf(pdf_path):
        text = ""
        with open(pdf_path, "rb") as pdf_file:
            pdf_reader = PyPDF2.PdfReader(pdf_file)
            for page_num in range(len(pdf_reader.pages)):
                page = pdf_reader.pages[page_num]
                text += page.extract_text()
            return text

    @staticmethod
    def chunk_text(raw_text):
        text_splitter = CharacterTextSplitter(
            separator="\n",
            chunk_size=500,
            chunk_overlap=200,
            length_function=len
        )
        chunks = text_splitter.split_text(raw_text)
        return chunks