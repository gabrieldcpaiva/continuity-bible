"""Small document DSL + Markdown renderer.

Documents are lists of blocks. The Markdown renderer writes the editable source
files; src/typeset.py writes the same blocks to a print-ready PDF. Keeping one
content source means the two editions cannot disagree.
"""

# ---------------------------------------------------------------- constructors

def h1(t):            return {"t": "h1", "text": t}
def h2(t):            return {"t": "h2", "text": t}
def h3(t):            return {"t": "h3", "text": t}
def p(t):             return {"t": "p", "text": t}
def lead(t):          return {"t": "lead", "text": t}
def ul(items):        return {"t": "ul", "items": list(items)}
def ol(items):        return {"t": "ol", "items": list(items)}
def pagebreak():      return {"t": "pagebreak"}


def keep(*blocks):
    """Bind blocks so the PDF never splits them across pages (prose + its writing space)."""
    return {"t": "keep", "blocks": list(blocks)}
def spacer(h=6):      return {"t": "spacer", "h": h}


def table(cols, rows, widths=None, caption=None, dense=False, heights=None,
          first_col_bold=False, header_rows=1):
    return {"t": "table", "cols": list(cols), "rows": [list(r) for r in rows],
            "widths": widths, "caption": caption, "dense": dense,
            "heights": heights, "first_col_bold": first_col_bold,
            "header_rows": header_rows}


def callout(kind, title, body):
    """kind: tip | rule | warn | note"""
    return {"t": "callout", "kind": kind, "title": title, "body": body}


def fill(items, numbered=False, tight=False):
    """items: list of dicts with label, hint (optional), lines (default 2)"""
    return {"t": "fill", "items": items, "numbered": numbered, "tight": tight}


def checklist(items, numbered=False):
    """items: list of (label, hint) tuples or plain strings."""
    norm = []
    for it in items:
        if isinstance(it, str):
            norm.append((it, ""))
        else:
            norm.append((it[0], it[1] if len(it) > 1 else ""))
    return {"t": "checklist", "items": norm, "numbered": numbered}


def kv(pairs, widths=(0.32, 0.68)):
    return {"t": "kv", "pairs": list(pairs), "widths": list(widths)}


def divider(kicker, title, body=""):
    return {"t": "divider", "kicker": kicker, "title": title, "body": body}


def stageplan(ascii_art, caption="", data=None):
    """ASCII plan for Markdown; `data` lets the PDF draw a vector version."""
    return {"t": "stageplan", "ascii": ascii_art, "caption": caption, "data": data}


def formula(lines):
    return {"t": "formula", "lines": list(lines)}


# PDF-only custom flowables (Markdown gets a short placeholder note)
def pdf_only(kind, note="", data=None):
    return {"t": "pdfonly", "kind": kind, "note": note, "data": data}


def doc(title, subtitle, meta, blocks, filename):
    return {"title": title, "subtitle": subtitle, "meta": meta,
            "blocks": blocks, "filename": filename}


# ------------------------------------------------------------------ markdown

CALLOUT_TAG = {"tip": "Tip", "rule": "Rule", "warn": "Watch out", "note": "Note"}


def _cell(s):
    return str(s).replace("|", "\\|").replace("\n", "<br>")


def _md_table(b):
    cols, rows = b["cols"], b["rows"]
    out = ["| " + " | ".join(_cell(c) for c in cols) + " |",
           "|" + "|".join(["---"] * len(cols)) + "|"]
    for r in rows:
        cells = [_cell(c) for c in r]
        while len(cells) < len(cols):
            cells.append("")
        out.append("| " + " | ".join(cells) + " |")
    md = "\n".join(out)
    if b.get("caption"):
        md += "\n\n*" + b["caption"] + "*"
    return md


WRITE_LINE = "_" * 78


def _md_fill(b):
    """Writing space for the Markdown edition.

    A run of underscores on its own line renders as a horizontal rule in
    CommonMark, so the write-in line is a run of dots after "Answer:" instead —
    it survives every Markdown renderer and is easy to type over.
    """
    out = []
    slot = 0
    for it in b["items"]:
        label = it["label"]
        hint = it.get("hint", "")
        lines = it.get("lines", 2)
        head = "**" + label + "**"
        if hint:
            head += " — _" + hint + "_"
        out.append(head + "  ")          # two trailing spaces = markdown line break
        for _ in range(max(1, lines)):
            if b.get("numbered"):
                slot += 1
                out.append(f"{slot}. " + "." * 62)
            else:
                out.append("Answer: " + "." * 62)
        out.append("")
    return "\n".join(out).rstrip()


def _md_checklist(b):
    out = []
    for i, (label, hint) in enumerate(b["items"], 1):
        if b.get("numbered"):
            out.append(f"{i}. [ ] **{label}**" + (f" — {hint}" if hint else ""))
        else:
            out.append(f"- [ ] **{label}**" + (f" — {hint}" if hint else ""))
    return "\n".join(out)


def _md_kv(b):
    rows = [f"| **{_cell(k)}** | {_cell(v)} |" for k, v in b["pairs"]]
    return "| Field | State |\n|---|---|\n" + "\n".join(rows)


def _flatten(blocks):
    out = []
    for b in blocks:
        if b["t"] == "keep":
            out += _flatten(b["blocks"])
        else:
            out.append(b)
    return out


def render_markdown(d):
    parts = []
    title = d["title"]
    parts.append(f"# {title}\n")
    if d.get("subtitle"):
        parts.append(f"*{d['subtitle']}*\n")
    if d.get("meta"):
        parts.append("\n".join(d["meta"]) + "\n")
    parts.append("\n---\n")

    for b in _flatten(d["blocks"]):
        t = b["t"]
        if t == "h1":
            parts.append(f"\n# {b['text']}\n")
        elif t == "h2":
            parts.append(f"\n## {b['text']}\n")
        elif t == "h3":
            parts.append(f"\n### {b['text']}\n")
        elif t in ("p", "lead"):
            parts.append(b["text"] + "\n")
        elif t == "ul":
            parts.append("\n".join("- " + i for i in b["items"]) + "\n")
        elif t == "ol":
            parts.append("\n".join(f"{i}. {x}" for i, x in enumerate(b["items"], 1)) + "\n")
        elif t == "table":
            parts.append(_md_table(b) + "\n")
        elif t == "callout":
            tag = CALLOUT_TAG.get(b["kind"], "Note")
            parts.append(f"> **{tag} — {b['title']}**  \n> {b['body']}\n")
        elif t == "fill":
            parts.append(_md_fill(b) + "\n")
        elif t == "checklist":
            parts.append(_md_checklist(b) + "\n")
        elif t == "kv":
            parts.append(_md_kv(b) + "\n")
        elif t == "formula":
            parts.append("```\n" + "\n".join(b["lines"]) + "\n```\n")
        elif t == "stageplan":
            parts.append("```\n" + b["ascii"].rstrip("\n") + "\n```\n")
            if b.get("caption"):
                parts.append("*" + b["caption"] + "*\n")
        elif t == "divider":
            parts.append(f"\n---\n\n## {b['title']}\n")
            if b.get("body"):
                parts.append(b["body"] + "\n")
        elif t == "spacer":
            pass
        elif t == "pagebreak":
            parts.append("\n---\n")
        elif t == "pdfonly":
            if b.get("note"):
                parts.append(b["note"] + "\n")
    return "\n".join(parts).replace("\n\n\n", "\n\n").rstrip() + "\n"
