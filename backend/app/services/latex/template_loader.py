from jinja2 import Environment, FileSystemLoader, select_autoescape
from pathlib import Path

TEMPLATE_DIR = Path(__file__).resolve().parents[3] / "templates" / "latex"

env = Environment(
    loader=FileSystemLoader(TEMPLATE_DIR),
    autoescape=select_autoescape([])  # disable HTML escaping
)

def load_template(template_name: str):
    return env.get_template(template_name)
