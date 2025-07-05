import streamlit as st

# Conversion rules
conversion = {
    "breads": 80,
    "gluten_free": 32,
    "wraps_box": 72,
    "wraps_packet": 18,
    "salad": 24,
}

# For tray conversion (specific to bread)
TRAY_TO_BREAD = 5

import re

def evaluate_expression(expr):
    try:
        # Remove all characters except digits, operators, dot and letters
        expr = expr.strip().upper()

        # Handle "T" in bread — convert "2T" to "2 * TRAY_TO_BREAD"
        if "T" in expr:
            expr = re.sub(r"(\d*\.?\d*)T", lambda m: str(float(m.group(1) or 1) * TRAY_TO_BREAD), expr)

        # Handle "B" for boxes
        expr = re.sub(r"(\d*\.?\d*)B", lambda m: str(float(m.group(1) or 1)), expr)

        # Handle "P" for packets
        expr = re.sub(r"(\d*\.?\d*)P", lambda m: str(float(m.group(1) or 1)), expr)

        # Evaluate the expression safely
        return eval(expr)
    except:
        return 0.0

def convert(val, item_type):
    if not val or val.strip() == "":
        return 0.0

    val = val.strip().upper()

    # Convert based on special cases
    try:
        result = evaluate_expression(val)

        # Apply unit conversion
        if "B" in val:
            result *= conversion[item_type]
        elif "P" in val and item_type == "wraps_box":
            result *= conversion["wraps_packet"]
        elif item_type == "breads" and "T" in val:
            result *= conversion["breads"] / TRAY_TO_BREAD  # Already converted T to # of breads

        return result
    except:
        return 0.0

st.title("Subway Stock Calculator 📦")

items = ["breads", "gluten_free", "wraps_box", "salad"]

# Locations per item
locations_dict = {
    "breads": ["Freezer", "Chiller", "Back Store", "Front Store"],
    "gluten_free": ["Freezer", "Chiller", "Back Store", "Front Store"],
    "wraps_box": ["Freezer", "Chiller", "Back Store", "Front Store"],
    "salad": ["Back Store", "Front Store"],  # Removed Freezer and Chiller
}

for item in items:
    readable_name = item.replace("_box", "").replace("_", " ").title()
    st.subheader(f"{readable_name}")
    total = 0.0

    for loc in locations_dict[item]:
        entry = st.text_input(
            f"{readable_name} in {loc}",
            key=f"{item}_{loc}",
            help="Supports math: e.g. 1B+2.5, 3T (tray for breads), 4P (packets for wraps), etc."
        )
        total += convert(entry, item)

    st.success(f"Total {readable_name}: {round(total, 2)}")
