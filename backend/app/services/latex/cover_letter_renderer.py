from pathlib import Path
from .template_loader import load_template


def render_cover_letter(
    cover_letter_text: str,
    output_path: Path
) -> Path:
    """
    Renders a cover letter LaTeX file.
    """

    template = load_template("cover_letter.tex.j2")

    tex_content = template.render(
        cover_letter=cover_letter_text
    )

    output_path.write_text(tex_content)
    return output_path
