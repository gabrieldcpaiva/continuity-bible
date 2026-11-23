"""Print typesetting: document DSL -> reportlab flowables.

Design system
  A4 portrait, 18 mm side margins, 9.6 pt body on 14.2 pt leading.
  Inter for text and tables, Source Serif for display. Deep teal accent, clay
  for change, amber for unresolved, green for fixed, grey for not-applicable.
  Status is always carried by a letter (F / C / U / N/A), never by colour alone.
"""

import os
import re

from reportlab.lib import colors
from reportlab.lib.enums import TA_LEFT, TA_CENTER, TA_RIGHT
from reportlab.lib.pagesizes import A4
from reportlab.lib.styles import ParagraphStyle
from reportlab.lib.units import mm
from reportlab.pdfbase import pdfmetrics
from reportlab.pdfbase.ttfonts import TTFont
from reportlab.platypus import (BaseDocTemplate, Flowable, FrameBreak, KeepTogether,
                                NextPageTemplate, PageBreak, PageTemplate,
                                Paragraph, Spacer, Table, TableStyle)

import plan as PLAN
from schema import PRODUCT, STATUS

HERE = os.path.dirname(os.path.abspath(__file__))
FONT_DIR = os.path.join(os.path.dirname(HERE), "assets", "fonts")

PAGE_W, PAGE_H = A4
MARGIN_L = MARGIN_R = 18 * mm
MARGIN_T = 21 * mm
MARGIN_B = 17 * mm
CONTENT_W = PAGE_W - MARGIN_L - MARGIN_R

INK = colors.HexColor("#17212B")
MUTED = colors.HexColor("#5C6775")
FAINT = colors.HexColor("#8A939E")
RULE = colors.HexColor("#D3D9DF")
ACCENT = colors.HexColor("#13504A")
ACCENT_TINT = colors.HexColor("#E8EFED")
CLAY = colors.HexColor("#A4562A")
CLAY_TINT = colors.HexColor("#F7EBE2")
AMBER = colors.HexColor("#8A5A11")
AMBER_TINT = colors.HexColor("#F8EFDC")
GREEN = colors.HexColor("#1D6B4A")
GREY_TINT = colors.HexColor("#EDEFF1")
PAPER_TINT = colors.HexColor("#F7F8F7")

KIND_COLOR = {
    "tip": (ACCENT, ACCENT_TINT, "TIP"),
    "rule": (ACCENT, ACCENT_TINT, "RULE"),
    "warn": (CLAY, CLAY_TINT, "WATCH OUT"),
    "note": (MUTED, GREY_TINT, "NOTE"),
}


def register_fonts():
    faces = {
        "Inter": "Inter-Regular.ttf",
        "Inter-Italic": "Inter-Italic.ttf",
        "Inter-Medium": "Inter-Medium.ttf",
        "Inter-SemiBold": "Inter-SemiBold.ttf",
        "Inter-Bold": "Inter-Bold.ttf",
        "Serif": "SourceSerif4-Regular.ttf",
        "Serif-SemiBold": "SourceSerif4-SemiBold.ttf",
        "Mono": "JetBrainsMono-Regular.ttf",
        "Mono-Medium": "JetBrainsMono-Medium.ttf",
    }
    for name, fn in faces.items():
        pdfmetrics.registerFont(TTFont(name, os.path.join(FONT_DIR, fn)))
    from reportlab.pdfbase.pdfmetrics import registerFontFamily
    registerFontFamily("Inter", normal="Inter", bold="Inter-Bold",
                       italic="Inter-Italic", boldItalic="Inter-SemiBold")
    registerFontFamily("Mono", normal="Mono", bold="Mono-Medium",
                       italic="Mono", boldItalic="Mono-Medium")
    registerFontFamily("Serif", normal="Serif", bold="Serif-SemiBold",
                       italic="Serif", boldItalic="Serif-SemiBold")


def styles():
    s = {}
    s["body"] = ParagraphStyle("body", fontName="Inter", fontSize=9.6, leading=14.0,
                               textColor=INK, spaceAfter=6, alignment=TA_LEFT)
    s["lead"] = ParagraphStyle("lead", parent=s["body"], fontName="Inter", fontSize=11.4,
                               leading=16.6, textColor=INK, spaceAfter=9)
    s["h1"] = ParagraphStyle("h1", fontName="Inter-Bold", fontSize=17.5, leading=21,
                             textColor=INK, spaceBefore=2, spaceAfter=8, keepWithNext=1)
    s["h2"] = ParagraphStyle("h2", fontName="Inter-Bold", fontSize=12.2, leading=15.5,
                             textColor=INK, spaceBefore=11, spaceAfter=4, keepWithNext=1)
    s["h3"] = ParagraphStyle("h3", fontName="Inter-SemiBold", fontSize=10, leading=13,
                             textColor=ACCENT, spaceBefore=8, spaceAfter=4, keepWithNext=1)
    s["cell"] = ParagraphStyle("cell", fontName="Inter", fontSize=8.3, leading=10.9, textColor=INK)
    s["cell_dense"] = ParagraphStyle("cell_dense", fontName="Inter", fontSize=7.8,
                                     leading=10.1, textColor=INK)
    s["cell_head"] = ParagraphStyle("cell_head", fontName="Inter-SemiBold", fontSize=7.6,
                                    leading=9.6, textColor=ACCENT)
    s["cell_head_dense"] = ParagraphStyle("cell_head_dense", fontName="Inter-SemiBold",
                                          fontSize=7.2, leading=9.2, textColor=ACCENT)
    s["caption"] = ParagraphStyle("caption", fontName="Inter-Italic", fontSize=7.6,
                                  leading=10.2, textColor=MUTED, spaceBefore=4, spaceAfter=10)
    s["mono"] = ParagraphStyle("mono", fontName="Mono", fontSize=7.55, leading=10.4,
                               textColor=INK)
    s["callout_title"] = ParagraphStyle("ct", fontName="Inter-SemiBold", fontSize=7.4,
                                        leading=9.6, textColor=ACCENT, spaceAfter=2.5)
    s["callout_body"] = ParagraphStyle("cb", fontName="Inter", fontSize=9.0, leading=13.2,
                                       textColor=INK)
    s["fill_label"] = ParagraphStyle("fl", fontName="Inter-SemiBold", fontSize=8.4,
                                     leading=11, textColor=INK)
    s["check_label"] = ParagraphStyle("cl", fontName="Inter-SemiBold", fontSize=8.8,
                                      leading=12, textColor=INK)
    s["check_hint"] = ParagraphStyle("ch", fontName="Inter", fontSize=8.0, leading=11,
                                     textColor=MUTED)
    s["ul"] = ParagraphStyle("ul", parent=s["body"], leftIndent=11, bulletIndent=1,
                             spaceAfter=4.5)
    s["toc_item"] = ParagraphStyle("toc", fontName="Inter", fontSize=9.2, leading=15.5,
                                   textColor=INK)
    s["part_kicker"] = ParagraphStyle("pk", fontName="Inter-SemiBold", fontSize=7.6,
                                      leading=10, textColor=ACCENT)
    s["part_title"] = ParagraphStyle("pt", fontName="Serif-SemiBold", fontSize=27, leading=31,
                                     textColor=INK)
    s["part_sub"] = ParagraphStyle("ps", fontName="Inter", fontSize=10.2, leading=14.6,
                                   textColor=MUTED)
    return s


ST = None


# --------------------------------------------------------------- inline markup

def inline(text):
    """Convert the light markup used in the content modules to reportlab tags."""
    t = text
    t = t.replace("&", "&amp;").replace("<", "&lt;").replace(">", "&gt;")
    t = re.sub(r"\*\*(.+?)\*\*", r"<b>\1</b>", t, flags=re.S)
    t = re.sub(r"(?<!\*)\*([^*]+?)\*(?!\*)", r"<i>\1</i>", t, flags=re.S)
    t = re.sub(r"`([^`]+?)`", r'<font name="Mono">\1</font>', t)
    t = re.sub(r"_([^_]+?)_", r"<i>\1</i>", t) if "Answer:" not in t else t
    t = t.replace("\n", "<br/>")
    return t


def P(text, style):
    return Paragraph(inline(text), style)


# ------------------------------------------------------------- small flowables

class HR(Flowable):
    def __init__(self, width=CONTENT_W, thickness=0.7, color=RULE, space_before=2, space_after=6):
        Flowable.__init__(self)
        self.width = width
        self.t = thickness
        self.c = color
        self.sb = space_before
        self.sa = space_after

    def wrap(self, aw, ah):
        return (self.width, self.t + self.sb + self.sa)

    def draw(self):
        self.canv.setStrokeColor(self.c)
        self.canv.setLineWidth(self.t)
        y = self.sa
        self.canv.line(0, y, self.width, y)


class Rules(Flowable):
    """Ruled writing lines, optionally numbered."""

    def __init__(self, n=1, height=15.5, numbered=False, start=1, inset=0):
        Flowable.__init__(self)
        self.n, self.height, self.numbered, self.start, self.inset = n, height, numbered, start, inset
        self.width = CONTENT_W

    def wrap(self, aw, ah):
        self.width = aw
        return (aw, self.n * self.height + 2)

    def draw(self):
        c = self.canv
        c.setLineWidth(0.45)
        for i in range(self.n):
            y = self.n * self.height - (i + 1) * self.height + 4
            c.setStrokeColor(colors.HexColor("#C6CED5"))
            c.line(self.inset + (14 if self.numbered else 0), y, self.width, y)
            if self.numbered:
                c.setFont("Inter-SemiBold", 7.2)
                c.setFillColor(FAINT)
                c.drawString(self.inset, y + 2.6, str(self.start + i))


class CheckBox(Flowable):
    def __init__(self, size=8.4):
        Flowable.__init__(self)
        self.size = size

    def wrap(self, aw, ah):
        return (self.size, self.size)

    def draw(self):
        c = self.canv
        c.setStrokeColor(colors.HexColor("#7C8794"))
        c.setLineWidth(0.8)
        c.setFillColor(colors.white)
        c.roundRect(0, 0, self.size, self.size, 1.4, stroke=1, fill=1)


class StatusPill(Flowable):
    def __init__(self, code, size=7.4):
        Flowable.__init__(self)
        self.code = code
        self.size = size
        self.color = colors.HexColor("#5B6673")
        for s in STATUS:
            if s["code"] == code:
                self.color = colors.HexColor(s["color"])

    def wrap(self, aw, ah):
        self.txt_w = pdfmetrics.stringWidth(self.code, "Inter-Bold", self.size) + 10
        return (self.txt_w, 12)

    def draw(self):
        c = self.canv
        c.setFillColor(self.color)
        c.roundRect(0, 1, self.txt_w, 11, 5.2, stroke=0, fill=1)
        c.setFillColor(colors.white)
        c.setFont("Inter-Bold", self.size)
        c.drawCentredString(self.txt_w / 2, 4.4, self.code)


class Score(Flowable):
    """The five small marks used on the cover to suggest a shot strip."""

    def __init__(self, w, h=26):
        Flowable.__init__(self)
        self.width, self.height = w, h

    def wrap(self, aw, ah):
        return (aw, self.height)

    def draw(self):
        c = self.canv
        n = 6
        gap = 6
        cw = (self.width - gap * (n - 1)) / n
        for i in range(n):
            x = i * (cw + gap)
            c.setStrokeColor(colors.Color(1, 1, 1, 0.55))
            c.setLineWidth(0.7)
            if i == 4:
                c.setFillColor(colors.Color(1, 1, 1, 0.16))
                c.rect(x, 0, cw, self.height, stroke=1, fill=1)
            else:
                c.rect(x, 0, cw, self.height, stroke=1, fill=0)


class StagePlan(Flowable):
    """Vector floor plan, driven by plan.py so it matches the ASCII version."""

    LEGEND_H = 22

    def __init__(self, data=None, height=300):
        Flowable.__init__(self)
        self.data = data or {"kind": "blank"}
        self.height = height

    def wrap(self, aw, ah):
        self.width = aw
        return (aw, self.height + self.LEGEND_H)

    def draw(self):
        c = self.canv
        filled = self.data.get("kind") != "blank"
        pad = 18
        availw = self.width - 2 * pad
        availh = self.height - 2 * pad
        rw, rh = PLAN.ROOM
        scale = min(availw / rw, availh / rh)
        ox = pad + (availw - rw * scale) / 2
        oy = pad + (availh - rh * scale) / 2

        def X(x):
            return ox + x * scale

        def Y(y):
            return oy + y * scale

        # one-metre grid
        c.setStrokeColor(colors.HexColor("#E2E7EA"))
        c.setLineWidth(0.45)
        for i in range(1, int(rw)):
            c.line(X(i), Y(0), X(i), Y(rh))
        for j in range(1, int(rh)):
            c.line(X(0), Y(j), X(rw), Y(j))

        # room
        c.setStrokeColor(INK)
        c.setLineWidth(1.3)
        c.setFillColor(colors.white)
        c.rect(X(0), Y(0), rw * scale, rh * scale, stroke=1, fill=1)

        if not filled:
            self._north(c, X(rw) + 10, Y(rh) + 10)
            c.setFillColor(FAINT)
            c.setFont("Inter", 6.8)
            c.drawString(X(0), Y(1.5), "draw the room from above, one circle per shot")
            return

        # door: gap in the east wall, leaf swinging inwards
        c.setFillColor(colors.white)
        c.rect(X(rw) - 1.2, Y(PLAN.DOOR["y0"]), 2.4, (PLAN.DOOR["y1"] - PLAN.DOOR["y0"]) * scale, stroke=0, fill=1)
        c.setStrokeColor(CLAY)
        c.setLineWidth(1.8)
        c.line(X(rw), Y(PLAN.DOOR["y0"]), X(rw), Y(PLAN.DOOR["y1"]))
        c.setLineWidth(0.7)
        c.setDash(2.2, 2.2)
        r = (PLAN.DOOR["y1"] - PLAN.DOOR["y0"]) * scale
        c.arc(X(rw) - r, Y(PLAN.DOOR["y0"]) - r, X(rw) + r, Y(PLAN.DOOR["y0"]) + r, 0, 90)
        c.setDash()
        c.setFillColor(CLAY)
        c.setFont("Inter-SemiBold", 6.2)
        c.drawString(X(rw) + 5, Y((PLAN.DOOR["y0"] + PLAN.DOOR["y1"]) / 2) - 2, "DOOR")

        # north wall dressing
        c.setFillColor(colors.HexColor("#DCD9CE"))
        c.rect(X(PLAN.CORK["x0"]), Y(rh) - 4, (PLAN.CORK["x1"] - PLAN.CORK["x0"]) * scale, 4, stroke=0, fill=1)
        c.setFillColor(MUTED)
        c.setFont("Inter", 5.6)
        c.drawString(X(PLAN.CORK["x0"]), Y(rh) + 3.5, "corkboard")
        c.setStrokeColor(colors.HexColor("#B9BFC5"))
        c.setDash(2, 2)
        c.setLineWidth(0.7)
        c.rect(X(PLAN.CLOCK["x0"]), Y(rh) - 8, (PLAN.CLOCK["x1"] - PLAN.CLOCK["x0"]) * scale, 8, stroke=1, fill=0)
        c.setDash()
        c.setFillColor(MUTED)
        c.drawString(X(PLAN.CLOCK["x0"]) - 4, Y(rh) + 3.5, "clock ghost")

        # desk, mixer
        d = PLAN.DESK
        c.setFillColor(colors.HexColor("#EFE9DA"))
        c.setStrokeColor(colors.HexColor("#8C7B57"))
        c.setLineWidth(0.8)
        c.rect(X(d["x0"]), Y(d["y0"]), (d["x1"] - d["x0"]) * scale, (d["y1"] - d["y0"]) * scale, stroke=1, fill=1)
        m = PLAN.MIXER
        c.setFillColor(colors.HexColor("#C8CDD2"))
        c.setStrokeColor(colors.HexColor("#9AA3AA"))
        c.rect(X(m["x0"]), Y(m["y0"]), (m["x1"] - m["x0"]) * scale, (m["y1"] - m["y0"]) * scale, stroke=1, fill=1)
        c.setFillColor(MUTED)
        c.setFont("Inter", 5.4)
        c.drawString(X(d["x0"]) + 4, Y(d["y0"]) + 5, "DESK")

        # small objects: dots only, explained in the legend line
        c.setFillColor(INK)
        c.circle(X(PLAN.MIC[0]), Y(PLAN.MIC[1]), 1.9, stroke=0, fill=1)
        c.setFillColor(colors.HexColor("#E8E1D6"))
        c.setStrokeColor(colors.HexColor("#8C7B57"))
        c.circle(X(PLAN.MUG[0]), Y(PLAN.MUG[1]), 2.6, stroke=1, fill=1)
        c.setFillColor(colors.white)
        c.rect(X(PLAN.CLIP[0]) - 3, Y(PLAN.CLIP[1]) - 4, 6, 8, stroke=1, fill=1)
        c.setFillColor(colors.HexColor("#B08D57"))
        c.circle(X(PLAN.LAMP[0]) + 6, Y(PLAN.LAMP[1]), 2.4, stroke=0, fill=1)

        # chair + character
        cx, cy = PLAN.CHAIR
        c.setFillColor(ACCENT_TINT)
        c.setStrokeColor(ACCENT)
        c.setLineWidth(1.0)
        c.circle(X(cx), Y(cy), 9.5, stroke=1, fill=1)
        c.setFillColor(ACCENT)
        c.setFont("Inter-Bold", 5.8)
        c.drawCentredString(X(cx), Y(cy) - 2, "RAE")
        c.setStrokeColor(ACCENT)
        c.setLineWidth(0.9)
        c.line(X(cx), Y(cy) - 10, X(cx), Y(cy) - 20)
        c.line(X(cx), Y(cy) - 20, X(cx) - 2.6, Y(cy) - 16.5)
        c.line(X(cx), Y(cy) - 20, X(cx) + 2.6, Y(cy) - 16.5)
        c.setFillColor(ACCENT)
        c.setFont("Inter", 5.6)
        c.drawString(X(cx) + 4, Y(cy) - 19, "faces south")

        # cameras
        for label, x, y, lens in PLAN.CAMERAS:
            if label.startswith("S3"):
                tx = (PLAN.DESK["x0"] + PLAN.DESK["x1"]) / 2
                ty = (PLAN.DESK["y0"] + PLAN.DESK["y1"]) / 2
            else:
                tx, ty = PLAN.CHAIR
            c.setStrokeColor(colors.Color(0.075, 0.314, 0.290, 0.55))
            c.setLineWidth(0.6)
            c.setDash(1.4, 2.2)
            c.line(X(x), Y(y), X(tx), Y(ty))
            c.setDash()
            c.setFillColor(ACCENT)
            c.circle(X(x), Y(y), 8.5, stroke=0, fill=1)
            c.setFillColor(colors.white)
            c.setFont("Inter-Bold", 5.6)
            c.drawCentredString(X(x), Y(y) - 2, label.replace("S", "").replace(" ", "").replace("/", "·")[:3])

        self._north(c, X(rw) + 10, Y(rh) + 10)

        # legend line under the plan
        c.setFillColor(FAINT)
        c.setFont("Inter", 6.4)
        c.drawString(X(0), oy - 12,
                     "One grid square is one metre. Desk objects: mug (west), mixer and mic (north), clipboard and lamp (east). "
                     "Dotted lines: what each camera is pointed at.")

    def _north(self, c, x, y):
        c.setFillColor(MUTED)
        c.setFont("Inter-SemiBold", 6.6)
        c.drawCentredString(x + 4, y + 9, "N")
        c.setStrokeColor(MUTED)
        c.setLineWidth(0.7)
        c.line(x + 4, y, x + 4, y + 7)
        c.line(x + 4, y + 7, x + 2.4, y + 4.4)
        c.line(x + 4, y + 7, x + 5.6, y + 4.4)


class ThreeLayerDiagram(Flowable):
    """Identity / Variant / Shot state, with the handoff line between shots."""

    def __init__(self, height=132):
        Flowable.__init__(self)
        self.height = height

    def wrap(self, aw, ah):
        self.width = aw
        return (aw, self.height)

    def draw(self):
        c = self.canv
        colw = (self.width - 16) / 3
        rows = [
            ("IDENTITY", "stays for the sequence", ACCENT, ACCENT_TINT,
             "face anchors · landmarks · time band"),
            ("VARIANT", "changes on purpose, with a code", CLAY, CLAY_TINT,
             "V2 cardigan open · P-01b mug tipped · L2 lamp off"),
            ("SHOT STATE", "one shot, checked in 30 seconds", INK, GREY_TINT,
             "action · frame side · hands · framing"),
        ]
        y = self.height - 66
        for i, (name, sub, col, tint, ex) in enumerate(rows):
            x = i * (colw + 8)
            c.setFillColor(tint)
            c.setStrokeColor(col)
            c.setLineWidth(0.7)
            c.roundRect(x, y, colw, 58, 3, stroke=1, fill=1)
            c.setFillColor(col)
            c.setFont("Inter-Bold", 8.2)
            c.drawString(x + 8, y + 44, name)
            c.setFillColor(INK)
            c.setFont("Inter", 6.9)
            c.drawString(x + 8, y + 33, sub)
            c.setFillColor(MUTED)
            c.setFont("Inter-Italic", 6.4)
            for k, line in enumerate(_wrap(ex, colw - 16, "Inter-Italic", 6.4)[:3]):
                c.drawString(x + 8, y + 22 - k * 7.6, line)
        # handoff strip beneath
        c.setFillColor(INK)
        c.setFont("Inter-SemiBold", 7.0)
        c.drawString(0, y - 15, "HANDOFF LINE")
        c.setFillColor(MUTED)
        c.setFont("Inter", 7.0)
        c.drawString(64, y - 15, "inherits  >  changes  >  hands off     repeated between every pair of shots")


def _wrap(text, width, font, size):
    words = text.split()
    lines, cur = [], ""
    for w in words:
        t = (cur + " " + w).strip()
        if pdfmetrics.stringWidth(t, font, size) <= width:
            cur = t
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines


# ------------------------------------------------------------------ converters

def cell(text, dense=False, bold=False, head=False):
    if isinstance(text, Flowable):
        return text
    t = str(text)
    if t.startswith("**") and t.endswith("**") and t.count("**") == 2:
        t = t[2:-2]
        bold = True
    style = ST["cell_head_dense" if dense else "cell_head"] if head else ST["cell_dense" if dense else "cell"]
    if bold and not head:
        style = ParagraphStyle("b", parent=style, fontName="Inter-SemiBold")
    return Paragraph(inline(t), style)


def make_table(b):
    dense = b.get("dense", False)
    cols = b["cols"]
    rows = b["rows"]
    widths = b.get("widths") or [1 / len(cols)] * len(cols)
    colw = [w * CONTENT_W for w in widths]
    nhead = b.get("header_rows", 1)
    has_header = bool(cols) and any(str(c).strip() for c in cols)

    data = []
    if has_header:
        data.append([cell(c, dense, head=True) for c in cols])
    for r in rows:
        data.append([cell(c, dense) for c in r])

    heights = b.get("heights")
    if heights:
        heights = list(heights)
        if has_header:
            heights = [None] + heights

    t = Table(data, colWidths=colw, rowHeights=heights, repeatRows=nhead if has_header else 0)
    style = [
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("TOPPADDING", (0, 0), (-1, -1), 3.8 if not dense else 3.0),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 3.8 if not dense else 3.0),
        ("LEFTPADDING", (0, 0), (-1, -1), 5),
        ("RIGHTPADDING", (0, 0), (-1, -1), 5),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
    ]
    if has_header:
        style += [
            ("BACKGROUND", (0, 0), (-1, 0), ACCENT_TINT),
            ("LINEBELOW", (0, 0), (-1, 0), 0.8, ACCENT),
            ("TOPPADDING", (0, 0), (-1, 0), 5),
            ("BOTTOMPADDING", (0, 0), (-1, 0), 5),
        ]
    if len(cols) >= 5:
        style.append(("LINEBEFORE", (1, 0), (-1, -1), 0.35, colors.HexColor("#E4E8EB")))
    if b.get("first_col_bold") and has_header:
        style.append(("FONTNAME", (0, 1), (0, -1), "Inter-SemiBold"))
    t.setStyle(TableStyle(style))
    if len(rows) <= 8:
        t = KeepTogether([t])
    out = [t]
    if b.get("caption"):
        out.append(P(b["caption"], ST["caption"]))
    else:
        out.append(Spacer(1, 8))
    return out


def make_callout(b):
    col, tint, tag = KIND_COLOR.get(b["kind"], KIND_COLOR["note"])
    para = [Paragraph(inline(b["title"]),
                      ParagraphStyle("ct2", parent=ST["callout_title"], textColor=col))]
    tagp = Paragraph(f'<font name="Inter-Bold" size="6.6" color="{col.hexval()}">{tag}</font>',
                     ParagraphStyle("tag", fontName="Inter-Bold", fontSize=6.6, leading=9))
    body = P(b["body"], ST["callout_body"])
    inner = Table([[tagp], [para[0]], [body]], colWidths=[CONTENT_W - 24])
    inner.setStyle(TableStyle([
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 0),
        ("TOPPADDING", (0, 0), (-1, -1), 0),
        ("BOTTOMPADDING", (0, 1), (-1, 1), 2),
        ("BOTTOMPADDING", (0, 0), (-1, 0), 3),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    wrapper = Table([["", inner]], colWidths=[4, CONTENT_W - 4])
    wrapper.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (0, 0), col),
        ("BACKGROUND", (1, 0), (1, 0), tint),
        ("LEFTPADDING", (0, 0), (0, 0), 0),
        ("RIGHTPADDING", (0, 0), (0, 0), 0),
        ("LEFTPADDING", (1, 0), (1, 0), 10),
        ("RIGHTPADDING", (1, 0), (1, 0), 10),
        ("TOPPADDING", (1, 0), (1, 0), 7),
        ("BOTTOMPADDING", (1, 0), (1, 0), 8),
        ("TOPPADDING", (0, 0), (0, 0), 8),
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
    ]))
    return [Spacer(1, 3), wrapper, Spacer(1, 9)]


def make_fill(b):
    out = []
    slot = 0
    line_h = 13.2 if b.get("tight") else 15.0
    for it in b["items"]:
        lab = it["label"]
        hint = it.get("hint", "")
        n = max(1, it.get("lines", 2))
        head = f'<b>{inline(lab)}</b>'
        if hint:
            head += f' <font name="Inter-Italic" size="7.8" color="{MUTED.hexval()}">— {inline(hint)}</font>'
        p = Paragraph(head, ParagraphStyle("fh", parent=ST["fill_label"], spaceAfter=1))
        rules = Rules(n=n, height=line_h, numbered=b.get("numbered"), start=slot + 1)
        slot += n
        out.append(KeepTogether([p, rules, Spacer(1, 3)]))
    out.append(Spacer(1, 3))
    return out


def make_checklist(b):
    rows = []
    for i, (label, hint) in enumerate(b["items"], 1):
        right = [P(label, ST["check_label"])]
        if hint:
            right.append(P(inline(hint), ST["check_hint"]))
        rows.append([CheckBox(), right])
    t = Table(rows, colWidths=[16, CONTENT_W - 16])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LEFTPADDING", (0, 0), (-1, -1), 0),
        ("RIGHTPADDING", (0, 0), (-1, -1), 4),
        ("TOPPADDING", (0, 0), (-1, -1), 4.2),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4.2),
        ("LINEBELOW", (0, 0), (-1, -2), 0.35, colors.HexColor("#E7EAED")),
        ("TOPPADDING", (0, 0), (0, -1), 7),
    ]))
    return [t, Spacer(1, 8)]


def _sanitise_mono(text):
    """Keep mono blocks to glyphs that are unambiguous in print and in plain text."""
    return (text.replace("\u2192", "->").replace("\u2190", "<-")
                .replace("\u2026", "...").replace("\u2022", "-")
                .replace("\u00b7", "\u00b7"))


def make_formula(b):
    avail = CONTENT_W - 20
    lines = [_sanitise_mono(l) for l in b["lines"]]
    size = 7.6
    while size > 5.6 and max(
            pdfmetrics.stringWidth(l, "Mono", size) for l in lines) > avail:
        size -= 0.2
    style = ParagraphStyle("mono2", parent=ST["mono"], fontSize=size, leading=size * 1.42)
    body = "<br/>".join(
        ('&nbsp;' if not line.strip() else inline(line).replace(" ", "&nbsp;"))
        for line in lines
    )
    para = Paragraph(body, style)
    t = Table([[para]], colWidths=[CONTENT_W])
    t.setStyle(TableStyle([
        ("BACKGROUND", (0, 0), (-1, -1), PAPER_TINT),
        ("LINEBEFORE", (0, 0), (0, -1), 2, ACCENT),
        ("LEFTPADDING", (0, 0), (-1, -1), 10),
        ("RIGHTPADDING", (0, 0), (-1, -1), 8),
        ("TOPPADDING", (0, 0), (-1, -1), 8),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 9),
    ]))
    return [Spacer(1, 2), t, Spacer(1, 11)]


def make_kv(b):
    rows = [[cell(k, bold=True), cell(v)] for k, v in b["pairs"]]
    t = Table(rows, colWidths=[b["widths"][0] * CONTENT_W, b["widths"][1] * CONTENT_W])
    t.setStyle(TableStyle([
        ("VALIGN", (0, 0), (-1, -1), "TOP"),
        ("LINEBELOW", (0, 0), (-1, -1), 0.4, RULE),
        ("TOPPADDING", (0, 0), (-1, -1), 4),
        ("BOTTOMPADDING", (0, 0), (-1, -1), 4),
        ("LEFTPADDING", (0, 0), (-1, -1), 4),
    ]))
    return [t, Spacer(1, 10)]


SMALL_NEXT = {"fill", "checklist", "formula"}


def _render_one(b):
    """Render exactly one block. Used by the grouping pass below."""
    return _render_block(b)


def blocks_to_flowables(blocks):
    out = []
    i = 0
    while i < len(blocks):
        b = blocks[i]
        t = b["t"]
        nxt = blocks[i + 1] if i + 1 < len(blocks) else None
        # keep a heading (and an optional one-line intro) with the small block after it
        if t in ("h1", "h2", "h3") and nxt is not None:
            after = blocks[i + 2] if i + 2 < len(blocks) else None
            if nxt["t"] in SMALL_NEXT:
                out.append(KeepTogether(_render_block(b) + _render_block(nxt)))
                i += 2
                continue
            # a heading must not sit alone at the foot of a page
            if nxt["t"] in ("p", "lead") and len(nxt.get("text", "")) < 420:
                out.append(KeepTogether(_render_block(b) + _render_block(nxt)))
                i += 2
                continue

        out += _render_block(b)
        i += 1
    return out


def _render_block(b):
    out = []
    t = b["t"]
    if t == "h1":
        out.append(P(b["text"], ST["h1"]))
    elif t == "h2":
        out.append(P(b["text"], ST["h2"]))
    elif t == "h3":
        out += [Spacer(1, 2), P(b["text"], ST["h3"])]
    elif t == "p":
        out.append(P(b["text"], ST["body"]))
    elif t == "lead":
        out.append(P(b["text"], ST["lead"]))
    elif t == "ul":
        grp = [Paragraph(inline(it), ST["ul"], bulletText="•") for it in b["items"]]
        out.append(KeepTogether(grp + [Spacer(1, 4)]) if len(grp) <= 6 else grp)
        if len(grp) > 6:
            out.append(Spacer(1, 4))
    elif t == "ol":
        grp = []
        for i, it in enumerate(b["items"], 1):
            st = ParagraphStyle("oli", parent=ST["ul"])
            grp.append(Paragraph(inline(it), st, bulletText=f"{i}."))
        out.append(KeepTogether(grp + [Spacer(1, 4)]) if len(grp) <= 6 else grp)
        if len(grp) > 6:
            out.append(Spacer(1, 4))
    elif t == "table":
        out += make_table(b)
    elif t == "callout":
        out += make_callout(b)
    elif t == "fill":
        out += make_fill(b)
    elif t == "checklist":
        out += make_checklist(b)
    elif t == "kv":
        out += make_kv(b)
    elif t == "formula":
        out += make_formula(b)
    elif t == "keep":
        grp = []
        for child in b["blocks"]:
            grp += _render_block(child)
        out.append(KeepTogether(grp))
    elif t == "stageplan":
        dock = b.get("data") or {}
        out += [Spacer(1, 4), StagePlan(dock, height=dock.get("height", 320)), Spacer(1, 6)]
        if b.get("caption"):
            out.append(P(b["caption"], ST["caption"]))
    elif t == "divider":
        out += [PageBreak(), P(b["title"], ST["h1"])]
    elif t == "spacer":
        out.append(Spacer(1, b.get("h", 6)))
    elif t == "pagebreak":
        out.append(PageBreak())
    elif t == "pdfonly":
        pass
    return out
