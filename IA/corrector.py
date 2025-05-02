# myapp/ai/corrector.py
from myapp.utils.pdf_utils import extract_text_from_pdf  # à créer
from myapp.ai.mistral import get_correction_from_ai       # à créer

def correct_with_ai(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    return get_correction_from_ai(text)
