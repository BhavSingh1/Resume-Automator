from pathlib import Path
from .template_loader import load_template


def render_resume(bullets: list[str], output_path: Path) -> Path:
    """
    Renders a resume LaTeX file from bullets.
    """

    template = load_template("resume.tex.j2")

    tex_content = template.render(
        bullets=bullets
    )

    output_path.write_text(tex_content)
    return output_path
