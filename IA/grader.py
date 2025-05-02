import fitz  # PyMuPDF
import subprocess

def extract_text_from_pdf(path):
    doc = fitz.open(path)
    return " ".join(page.get_text() for page in doc)

def grade_submission(pdf_path):
    text = extract_text_from_pdf(pdf_path)
    
    prompt = f"""
Tu es un correcteur expert. Voici une copie d'étudiant à noter sur 20.
Corrige et donne une note, puis un feedback détaillé.
Copie de l'étudiant :
{text}
Réponds sous la forme :
NOTE: <note sur 20>
FEEDBACK: <commentaire détaillé>
"""
    result = subprocess.run(
        ["ollama", "run", "mistral", prompt],
        capture_output=True,
        text=True
    )
    output = result.stdout
    try:
        note_line = next(line for line in output.splitlines() if line.startswith("NOTE"))
        feedback_line = next(line for line in output.splitlines() if line.startswith("FEEDBACK"))
        grade = float(note_line.replace("NOTE:", "").strip())
        feedback = feedback_line.replace("FEEDBACK:", "").strip()
    except Exception as e:
        grade = 0.0
        feedback = f"Erreur d'analyse: {str(e)}"
    return grade, feedback
