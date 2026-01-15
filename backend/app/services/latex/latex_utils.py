def escape_latex(text: str) -> str:
    replacements = {
        "&": "\\&",
        "%": "\\%",
        "$": "\\$",
        "#": "\\#",
        "_": "\\_",
        "{": "\\{",
        "}": "\\}",
        "~": "\\textasciitilde{}",
        "^": "\\textasciicircum{}",
        "\\": "\\textbackslash{}"
    }
    for k, v in replacements.items():
        text = text.replace(k, v)
    return text


def bullets_to_latex(bullets: list[str]) -> str:
    return "\n".join([f"\\item {escape_latex(b)}" for b in bullets])