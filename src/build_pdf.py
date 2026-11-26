"""Build the print-ready A4 PDF edition of The Continuity Bible."""

import os
import sys

sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from reportlab.lib import colors
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfgen import canvas as pdfcanvas
from reportlab.platypus import (BaseDocTemplate, Flowable, Frame, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

import docs_00, docs_01, docs_02, docs_03, docs_04, docs_05, docs_06
import typeset as T
from schema import PRODUCT, STATUS

ROOT = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
OUT = os.path.join(ROOT, "product/The-Continuity-Bible-v1.0.pdf")

DOCS = [docs_00, docs_01, docs_02, docs_03, docs_04, docs_05, docs_06]
PART_TITLES = [m.DOC["title"] for m in DOCS]

INK, MUTED, FAINT, RULE = T.INK, T.MUTED, T.FAINT, T.RULE
ACCENT, ACCENT_TINT = T.ACCENT, T.ACCENT_TINT
CLAY, AMBER, GREEN, GREY_TINT = T.CLAY, T.AMBER, T.GREEN, T.GREY_TINT


class PartHeader(Flowable):
    """Part opening block; also carries the table-of-contents entry."""

    def __init__(self, number, title, subtitle, meta, total=7):
        Flowable.__init__(self)
        self.number = number
        self.title = title
        self.subtitle = subtitle
        self.meta = meta
        self.total = total
        self.toc = (number, title)
        self.width = T.CONTENT_W

    def wrap(self, aw, ah):
        self.width = aw
        self.h = 104 + (12 * len(self.meta))
        return (aw, self.h)

    def draw(self):
        c = self.canv
        w = self.width
        c.setFillColor(ACCENT)
        c.rect(0, self.h - 3, 34, 3, stroke=0, fill=1)
        c.setFont("Inter-SemiBold", 7.4)
        c.setFillColor(ACCENT)
        c.drawString(0, self.h - 17, f"PART {self.number} OF {self.total}")
        y = self.h - 46
        for line in _serif_lines(self.title, w, 27, "Serif-SemiBold"):
            c.setFont("Serif-SemiBold", 27)
            c.setFillColor(INK)
            c.drawString(0, y, line)
            y -= 30
        y -= 2
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.line(0, y + 8, w, y + 8)
        y -= 4
        c.setFont("Inter", 9.6)
        c.setFillColor(MUTED)
        for line in _lines(self.subtitle, w, 9.6, "Inter"):
            c.drawString(0, y, line)
            y -= 13
        y -= 3
        c.setFont("Inter", 7.4)
        c.setFillColor(FAINT)
        for line in self.meta:
            plain = line.replace("**", "")
            c.drawString(0, y, plain)
            y -= 10.4


def _lines(text, width, size, font):
    from reportlab.pdfbase import pdfmetrics
    words = text.split()
    out, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            cur = t
        else:
            if cur:
                out.append(cur)
            cur = w
    if cur:
        out.append(cur)
    return out


def _serif_lines(text, width, size, font):
    return _lines(text, width, size, font)


class Book(BaseDocTemplate):
    def __init__(self, path, **kw):
        BaseDocTemplate.__init__(self, path, pagesize=A4,
                                 leftMargin=T.MARGIN_L, rightMargin=T.MARGIN_R,
                                 topMargin=T.MARGIN_T, bottomMargin=T.MARGIN_B,
                                 title="The Continuity Bible — a six-shot handoff system for independent AI filmmakers",
                                 author="The Continuity Bible", subject="Continuity handoff system v1.0",
                                 creator="reportlab")
        self.section_by_page = kw.get("section_by_page", {})
        self.collect = kw.get("collect")
        cover_frame = Frame(0, 0, A4[0], A4[1], id="cover",
                            leftPadding=0, rightPadding=0, topPadding=0, bottomPadding=0)
        body_frame = Frame(T.MARGIN_L, T.MARGIN_B, T.CONTENT_W,
                           A4[1] - T.MARGIN_T - T.MARGIN_B, id="body")
        self.addPageTemplates([
            PageTemplate(id="cover", frames=[cover_frame], onPage=self._no_deco),
            PageTemplate(id="body", frames=[body_frame], onPage=self._deco),
        ])

    def _no_deco(self, canv, doc):
        pass

    def _deco(self, canv, doc):
        p = canv.getPageNumber()
        canv.saveState()
        # header
        canv.setFont("Inter", 7.2)
        canv.setFillColor(FAINT)
        sec = self.section_by_page.get(p, "")
        canv.drawString(T.MARGIN_L, A4[1] - 14 * mm, sec.upper())
        canv.drawRightString(A4[0] - T.MARGIN_R, A4[1] - 14 * mm,
                             "THE CONTINUITY BIBLE  ·  V1.0")
        canv.setStrokeColor(colors.HexColor("#DFE4E7"))
        canv.setLineWidth(0.5)
        canv.line(T.MARGIN_L, A4[1] - 16.4 * mm, A4[0] - T.MARGIN_R, A4[1] - 16.4 * mm)
        # footer
        canv.line(T.MARGIN_L, 12.6 * mm, A4[0] - T.MARGIN_R, 12.6 * mm)
        canv.setFont("Inter", 7.2)
        canv.setFillColor(FAINT)
        canv.drawString(T.MARGIN_L, 8.6 * mm,
                        "Six-shot handoff system for independent AI filmmakers")
        canv.setFont("Inter-SemiBold", 7.6)
        canv.setFillColor(MUTED)
        canv.drawRightString(A4[0] - T.MARGIN_R, 8.6 * mm, str(p))
        canv.restoreState()

    def afterFlowable(self, flowable):
        if hasattr(flowable, "toc"):
            num, title = flowable.toc
            p = self.page
            if self.collect is not None:
                self.collect.append((num, title, p))
            for i in range(p, p + 2):
                self.section_by_page.setdefault(p, f"Part {num} — {title}")


# --------------------------------------------------------------------- pieces

def cover_flowables():
    f = []
    f.append(CoverBlock())
    return f


class CoverBlock(Flowable):
    def wrap(self, aw, ah):
        return (A4[0], A4[1])

    def draw(self):
        c = self.canv
        W, H = A4
        band_h = H * 0.535
        c.setFillColor(ACCENT)
        c.rect(0, H - band_h, W, band_h, stroke=0, fill=1)
        x = 20 * mm
        y = H - 42 * mm
        c.setFillColor(colors.Color(1, 1, 1, 0.72))
        c.setFont("Inter-SemiBold", 8.2)
        c.drawString(x, y, "A SHOT HANDOFF SYSTEM")
        y -= 16 * mm
        c.setFillColor(colors.white)
        for line in ("The", "Continuity", "Bible"):
            c.setFont("Serif-SemiBold", 46)
            c.drawString(x, y, line)
            y -= 15.2 * mm
        y += 4 * mm
        c.setStrokeColor(colors.Color(1, 1, 1, 0.55))
        c.setLineWidth(0.8)
        c.line(x, y, x + 46 * mm, y)
        y -= 9 * mm
        c.setFillColor(colors.Color(1, 1, 1, 0.94))
        c.setFont("Inter", 11.4)
        c.drawString(x, y, "Six generated shots that feel like one film.")
        c.setFillColor(colors.Color(1, 1, 1, 0.70))
        c.setFont("Inter", 10.2)
        c.drawString(x, y - 6.4 * mm, "Identity · variant · shot state · handoff")

        # shot strip motif
        c.setStrokeColor(colors.Color(1, 1, 1, 0.35))
        c.setFillColor(colors.Color(1, 1, 1, 0.10))
        bw, gap = (56 * mm - 5 * 6 * 0.6) / 6, 5
        bx = W - 20 * mm - 56 * mm
        by = H - band_h + 18 * mm
        for i in range(6):
            c.rect(bx + i * (bw + gap), by, bw, 20 * mm, stroke=1, fill=1 if i in (4,) else 0)
            if i == 4:
                c.setFillColor(CLAY)
                c.rect(bx + i * (bw + gap), by, bw, 1.6 * mm, stroke=0, fill=1)
                c.setFillColor(colors.Color(1, 1, 1, 0.10))
        c.setFont("Inter", 6.4)
        c.setFillColor(colors.Color(1, 1, 1, 0.55))
        c.drawRightString(W - 20 * mm, by - 5 * mm, "SIX SHOTS · ONE ROOM · ONE LOOK")

        # lower editorial block
        y = H - band_h - 20 * mm
        c.setFillColor(INK)
        c.setFont("Serif-SemiBold", 17)
        c.drawString(20 * mm, y, "A production handoff you can fill in this weekend.")
        y -= 12 * mm
        c.setFillColor(MUTED)
        c.setFont("Inter", 9.6)
        intro = [
            "Write down what has to survive the cut before you generate a single frame: the five face",
            "anchors, the five fixed landmarks, the three panels that carry state from one shot to the next,",
            "and one line between every pair of shots that says what the next shot must inherit.",
        ]
        for line in intro:
            c.drawString(20 * mm, y, line)
            y -= 5.6 * mm

        y -= 4 * mm
        # three layer diagram
        c.saveState()
        c.translate(20 * mm, y - 34 * mm)
        d = T.ThreeLayerDiagram(height=62)
        d.wrap(W - 40 * mm, 100)
        d.drawOn(c, 0, 0)
        c.restoreState()

        # footer of cover
        c.setStrokeColor(RULE)
        c.setLineWidth(0.6)
        c.line(20 * mm, 26 * mm, W - 20 * mm, 26 * mm)
        c.setFillColor(INK)
        c.setFont("Inter-SemiBold", 8.6)
        c.drawString(20 * mm, 19.5 * mm, "EDITABLE TEMPLATES  ·  PRINT-READY PDF  ·  COMPLETE SIX-SHOT WORKED EXAMPLE")
        c.setFillColor(MUTED)
        c.setFont("Inter", 8)
        c.drawString(20 * mm, 14 * mm, f"Version 1.0  ·  November 2026  ·  {PRODUCT['price_line']}")
        c.setFont("Inter", 8)
        c.setFillColor(FAINT)
        c.drawRightString(W - 20 * mm, 14 * mm, "The Continuity Bible")


def contents_page(entries):
    f = [Paragraph("Contents", T.ST["h1"] if T.ST else ParagraphStyle("x")), ]
    f.append(Spacer(1, 2))
    rows = []
    for num, title, page in entries:
        rows.append([
            Paragraph(f'<font name="Inter-SemiBold" size="7.6" color="{ACCENT.hexval()}">PART {num}</font>',
                      ParagraphStyle("tocn", fontName="Inter", fontSize=7.6, leading=13)),
            Paragraph(f'<font name="Inter-Bold" size="9.4">{title}</font>', ParagraphStyle("toct", fontName="Inter", fontSize=9.4, leading=13)),
            Paragraph(f'<font name="Inter" size="9.0" color="{MUTED.hexval()}">{page}</font>',
                      ParagraphStyle("tocp", fontName="Inter", fontSize=9, leading=13, alignment=2)),
        ])
    t = Table(rows, colWidths=[16 * mm, T.CONTENT_W - 32 * mm, 16 * mm])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "BOTTOM"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.35, colors.HexColor("#E4E8EB")),
        ("TOPPADDING", (0, 0), (-1, -1), 6),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 6),
        ("LEFTPADDING", (0, 0), (0, -1), 0),
    ]))
    f.append(t)
    f.append(Spacer(1, 9))

    f.append(Paragraph("What is in the folder", T.ST["h2"]))
    body = (
        "This PDF is the print edition of seven editable Markdown files, kept in one folder. Both editions carry the same "
        "content, generated from one source, so you can print this book and still edit the sheets digitally. The Markdown "
        "files are the templates you will actually write in; this PDF is the version to read, annotate and keep at the desk."
    )
    f.append(Paragraph(T.inline(body), T.ST["body"]))
    f.append(Paragraph(
        "Also in the folder: a six-shot spreadsheet tracker (CSV) that opens in Google Sheets, Excel or Numbers, an offline "
        "HTML form for typing the same fields with no connection, and the validation and research notes for anyone who wants "
        "to see what has and has not been tested.", T.ST["body"]))

    f.append(Paragraph("How to read it", T.ST["h2"]))
    items = [
        "**Part 1** is the twenty-minute workflow. Read it first, even if you skip everything else.",
        "**Parts 3 to 6** are the blank templates. Print them, or copy the Markdown into your notes app.",
        "**Part 7** is a complete six-shot example. Read it before you fill in your own scene; it is the fastest way to see "
        "what a good row looks like.",
        "**Part 2** is the field dictionary. Keep it nearby for your first scene, then you will stop needing it.",
    ]
    for it in items:
        f.append(Paragraph(T.inline(it), T.ST["ul"], bulletText="•"))
    f.append(Spacer(1, 6))
    f.append(T.make_callout({
        "kind": "note", "title": "An honest note about what this can do",
        "body": "Continuity is a production judgment supported by a useful record, not an automatic guarantee. This system makes "
                "intentional changes explicit and makes accidental ones easier to catch. It does not prevent drift by itself, and "
                "no document can promise a consistent result. This edition is new, and it is free. Feedback from the first real "
                "scenes is welcome.",
    })[1])
    return f


def colophon_page():
    f = [PageBreak(), Paragraph("The fine print", T.ST["h1"]), Spacer(1, 2)]
    f.append(Paragraph(T.inline(
        "**The Continuity Bible**, version 1.0, November 2026. A six-shot continuity handoff system for independent AI filmmakers. "
        + PRODUCT["price_line"] + ". Print it, edit the sheets, and use them on your own productions. Nothing is sold from these pages."
    ), T.ST["body"]))
    f.append(Paragraph("How you may use it", T.ST["h2"]))
    for it in [
        "Use the sheets, tables and checklists on as many of your own productions as you like, commercial or not.",
        "Print, copy, edit and rename the files for your own work and for the people you collaborate with on a production.",
        "Do not resell the files, publish them as your own template product, or redistribute them as a download.",
        "Quote it, teach with it and link to it, with credit to The Continuity Bible.",
    ]:
        f.append(Paragraph(T.inline(it), T.ST["ul"], bulletText="•"))
    f.append(Spacer(1, 4))
    f.append(Paragraph("What it is not", T.ST["h2"]))
    f.append(Paragraph(T.inline(
        "It is not a prompt library, a model integration, a collaboration platform, or a promise that generated shots will match. "
        "It contains no footage, no images and no third-party content. Every example is invented for this product. "
        "“Night Signal” is a fictional film; it was not shot, generated or tested with anyone."
    ), T.ST["body"]))
    f.append(Paragraph("Type and tooling", T.ST["h2"]))
    f.append(Paragraph(T.inline(
        "Set in Inter (SIL Open Font License 1.1) for text and tables, Source Serif 4 (SIL Open Font License 1.1) for display, "
        "and JetBrains Mono (SIL Open Font License 1.1) for the fixed-width examples. All three are embedded in this file. "
        "Font files and licences are included in the folder. Typeset from the field schema in src/schema.py with Python and reportlab, so the "
        "print edition and the editable files cannot disagree. The Markdown is generated from that schema."
    ), T.ST["body"]))
    f.append(Paragraph("Status of validation", T.ST["h2"]))
    f.append(Paragraph(T.inline(
        "This edition is new. The worked example was checked by script for internal consistency. A two-person usability session "
        "is written and not yet run. The commercial price test is retired: the work is free for everyone. If a field fails you "
        "on a real scene, that feedback is welcome."
    ), T.ST["body"]))
    return f


# ------------------------------------------------------------------------ build

def build(path, section_by_page=None, collect=None):
    T.register_fonts()
    T.register_fonts()
    T.ST = T.styles()
    doc = Book(path, section_by_page=section_by_page or {}, collect=collect)
    story = []
    story.append(CoverBlock())
    story.append(NextPageTemplate("body"))
    story.append(PageBreak())
    story += contents_page(PREVIEW_ENTRIES if collect is not None else collect_entries)
    for i, m in enumerate(DOCS, 1):
        story.append(PageBreak())
        d = m.DOC
        story.append(PartHeader(i, d["title"], d["subtitle"], d["meta"]))
        story.append(Spacer(1, 10))
        story += T.blocks_to_flowables(d["blocks"])
    story += colophon_page()
    doc.build(story)
    return doc


# entries used before the first pass has run
PREVIEW_ENTRIES = [(i, t, "--") for i, t in enumerate(PART_TITLES, 1)]
collect_entries = PREVIEW_ENTRIES


def main():
    # pass 1: collect pagination
    collect = []
    build("/tmp/cb_pass1.pdf", section_by_page={}, collect=collect)
    global collect_entries
    collect_entries = collect
    # pass 2: same story, but the contents page now knows its page numbers
    sections = {}
    for num, title, page in collect:
        for p in range(page, page + 2):
            sections.setdefault(p, f"Part {num} — {title}")
    build(OUT, section_by_page=sections, collect=None)
    print(f"  wrote {os.path.relpath(OUT, ROOT)}")
    for num, title, page in collect:
        print(f"    part {num}  {title:24s} p.{page}")


if __name__ == "__main__":
    main()
