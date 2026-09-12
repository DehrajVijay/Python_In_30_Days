"""
Restaurant bill calculator — now generates an actual PDF receipt.

Collects the restaurant name, table number, and a list of items
(name, quantity, price), then produces a receipt-style PDF that
looks like what you'd actually get at a restaurant: itemised lines,
subtotal, CGST + SGST split, an optional tip, and a grand total.
"""

import os
from datetime import datetime

from reportlab.lib.pagesizes import mm
from reportlab.lib.units import mm as MM
from reportlab.lib.enums import TA_CENTER, TA_RIGHT
from reportlab.lib.styles import ParagraphStyle
from reportlab.pdfgen import canvas
from reportlab.pdfbase.pdfmetrics import stringWidth

CGST_RATE = 0.025  # 2.5%
SGST_RATE = 0.025  # 2.5% -> combined 5% GST, matches most Indian restaurant bills

PAGE_WIDTH = 80 * MM  # classic 80mm thermal receipt width
MARGIN = 5 * MM
FONT = "Courier"
FONT_BOLD = "Courier-Bold"


def money(n):
    return f"Rs.{n:,.2f}"


def collect_items():
    items = []
    print("Enter items one at a time. Leave the name blank to finish.\n")
    while True:
        name = input("Item name: ").strip()
        if not name:
            break
        try:
            qty = int(input("  Qty: ").strip() or "1")
            price = float(input("  Price per item (Rs.): ").strip())
        except ValueError:
            print("  Invalid number, try that item again.")
            continue
        items.append({"name": name, "qty": qty, "price": price})
    return items


def wrap_name(c, name, max_width, font=FONT, size=9):
    """Wrap an item name to fit max_width, return list of lines."""
    words = name.split()
    lines, cur = [], ""
    for w in words:
        test = (cur + " " + w).strip()
        if stringWidth(test, font, size) <= max_width:
            cur = test
        else:
            if cur:
                lines.append(cur)
            cur = w
    if cur:
        lines.append(cur)
    return lines or [""]


def draw_dashed_line(c, y, width=PAGE_WIDTH):
    c.setDash(1, 2)
    c.setLineWidth(0.5)
    c.line(MARGIN, y, width - MARGIN, y)
    c.setDash()


def render(
    c,
    page_height,
    restaurant_name,
    address,
    table_number,
    items,
    tip_percent,
    subtotal,
    cgst,
    sgst,
    tip,
    grand_total,
):
    """Draws the full bill onto canvas c (of the given page_height) and
    returns the final y position (how far down the content reached)."""
    amt_x = PAGE_WIDTH - MARGIN
    rate_x = amt_x - 17 * MM
    qty_x = rate_x - 16 * MM
    name_col_width = qty_x - 6 * MM - MARGIN
    per_line = 4.2 * MM
    y = page_height - 8 * MM

    # ---- Header ----
    c.setFont(FONT_BOLD, 13)
    c.drawCentredString(PAGE_WIDTH / 2, y, restaurant_name.upper())
    y -= 5.5 * MM

    if address:
        c.setFont(FONT, 7.5)
        for line in wrap_name(c, address, PAGE_WIDTH - 2 * MARGIN, FONT, 7.5):
            c.drawCentredString(PAGE_WIDTH / 2, y, line)
            y -= 3.6 * MM

    c.setFont(FONT, 7.5)
    c.drawCentredString(PAGE_WIDTH / 2, y, "GSTIN: 27ABCDE1234F1Z5")
    y -= 6 * MM

    draw_dashed_line(c, y)
    y -= 5 * MM

    now = datetime.now()
    c.setFont(FONT, 8)
    c.drawString(MARGIN, y, f"Date: {now.strftime('%d-%m-%Y')}")
    c.drawRightString(PAGE_WIDTH - MARGIN, y, f"Time: {now.strftime('%I:%M %p')}")
    y -= 4.5 * MM
    c.drawString(MARGIN, y, f"Table: {table_number}")
    c.drawRightString(PAGE_WIDTH - MARGIN, y, f"Bill No: {now.strftime('%y%m%d%H%M')}")
    y -= 5 * MM

    draw_dashed_line(c, y)
    y -= 5 * MM

    # ---- Items header ----
    c.setFont(FONT_BOLD, 8)
    c.drawString(MARGIN, y, "ITEM")
    c.drawCentredString(qty_x, y, "QTY")
    c.drawRightString(rate_x, y, "RATE")
    c.drawRightString(amt_x, y, "AMT")
    y -= 3.5 * MM
    draw_dashed_line(c, y)
    y -= 4.5 * MM

    # ---- Items ----
    c.setFont(FONT, 8.5)
    for it in items:
        amount = it["qty"] * it["price"]
        lines = wrap_name(c, it["name"], name_col_width, FONT, 8.5)
        c.drawString(MARGIN, y, lines[0])
        c.drawCentredString(qty_x, y, str(it["qty"]))
        c.drawRightString(rate_x, y, f"{it['price']:.2f}")
        c.drawRightString(amt_x, y, f"{amount:.2f}")
        y -= per_line
        for extra in lines[1:]:
            c.drawString(MARGIN, y, extra)
            y -= per_line

    y -= 1 * MM
    draw_dashed_line(c, y)
    y -= 5 * MM

    # ---- Totals ----
    def total_row(label, value, bold=False, size=8.5):
        nonlocal y
        c.setFont(FONT_BOLD if bold else FONT, size)
        c.drawString(MARGIN, y, label)
        c.drawRightString(PAGE_WIDTH - MARGIN, y, money(value))
        y -= 4.5 * MM

    total_row("Subtotal", subtotal)
    total_row("CGST (2.5%)", cgst)
    total_row("SGST (2.5%)", sgst)
    if tip_percent > 0:
        total_row(f"Tip ({tip_percent:.0f}%)", tip)

    y -= 1 * MM
    draw_dashed_line(c, y)
    y -= 5.5 * MM

    total_row("GRAND TOTAL", grand_total, bold=True, size=11)
    y -= 3 * MM

    draw_dashed_line(c, y)
    y -= 8 * MM

    # ---- Footer ----
    c.setFont(FONT, 8)
    c.drawCentredString(PAGE_WIDTH / 2, y, "Thank you, come again!")
    y -= 4 * MM
    c.setFont(FONT, 6.5)
    c.drawCentredString(PAGE_WIDTH / 2, y, "Prices inclusive of applicable taxes")
    y -= 6 * MM

    return y


def build_bill_pdf(
    restaurant_name, address, table_number, items, tip_percent, output_path
):
    subtotal = sum(i["qty"] * i["price"] for i in items)
    cgst = subtotal * CGST_RATE
    sgst = subtotal * SGST_RATE
    tip = subtotal * (tip_percent / 100)
    grand_total = subtotal + cgst + sgst + tip
    args = (
        restaurant_name,
        address,
        table_number,
        items,
        tip_percent,
        subtotal,
        cgst,
        sgst,
        tip,
        grand_total,
    )

    # Pass 1: render onto an oversized dummy page just to measure how much
    # vertical space the content actually needs.
    probe_height = 400 * MM
    probe_path = output_path + ".probe.pdf"
    c_probe = canvas.Canvas(probe_path, pagesize=(PAGE_WIDTH, probe_height))
    final_y = render(c_probe, probe_height, *args)
    c_probe.save()
    os.remove(probe_path)

    content_height = probe_height - final_y  # how much vertical space was used
    page_height = content_height + 4 * MM  # small bottom breathing room

    # Pass 2: render for real at the tightly-fitted page height.
    c = canvas.Canvas(output_path, pagesize=(PAGE_WIDTH, page_height))
    render(c, page_height, *args)
    c.save()

    return {
        "subtotal": subtotal,
        "cgst": cgst,
        "sgst": sgst,
        "tip": tip,
        "grand_total": grand_total,
    }


def main():
    print("=" * 40)
    print("     RESTAURANT BILL GENERATOR")
    print("=" * 40)

    restaurant_name = (
        input("Restaurant name [The Spice Route]: ").strip() or "The Spice Route"
    )
    address = input("Address (optional): ").strip()
    table_number = input("Table number: ").strip()
    items = collect_items()

    if not items:
        print("No items entered. Exiting.")
        return

    tip_input = input("Tip % (0 if none): ").strip()
    tip_percent = float(tip_input) if tip_input else 0.0

    os.makedirs("outputs", exist_ok=True)
    safe_name = restaurant_name.lower().replace(" ", "_")
    output_path = f"outputs/{safe_name}_bill.pdf"

    totals = build_bill_pdf(
        restaurant_name, address, table_number, items, tip_percent, output_path
    )

    print("-" * 40)
    print(f"Subtotal   : {money(totals['subtotal'])}")
    print(f"CGST (2.5%): {money(totals['cgst'])}")
    print(f"SGST (2.5%): {money(totals['sgst'])}")
    if tip_percent > 0:
        print(f"Tip ({tip_percent:.0f}%)  : {money(totals['tip'])}")
    print(f"TOTAL      : {money(totals['grand_total'])}")
    print("=" * 40)
    print(f"PDF saved to: {output_path}")


if __name__ == "__main__":
    main()
