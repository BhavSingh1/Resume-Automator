import os
import subprocess
from datetime import date

TEMPLATE_DIR = "backend/templates/latex"
OUTPUT_DIR = "backend/generated"

def render_latex(template_name: str, replacements: dict, output_filename: str):
    """
    Renders a LaTeX template and compiles it to PDF.
    """
    template_path = os.path.join(TEMPLATE_DIR, template_name)
    with open(template_path, "r") as f:
        tex = f.read()

    for key, value in replacements.items():
        tex = tex.replace(f"{{{key}}}", value)

    output_tex_path = os.path.join(OUTPUT_DIR, output_filename + ".tex")

    with open(output_tex_path, "w") as f:
        f.write(tex)

    subprocess.run(
        ["pdflatex", "-interaction=nonstopmode", output_tex_path],
        cwd=OUTPUT_DIR,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
        check=True
    )

    return os.path.join(OUTPUT_DIR, output_filename + ".pdf")