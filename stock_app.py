import streamlit as st

# Conversion rules
conversion = {
    "breads": 80,
    "gluten_free": 32,
    "wraps_box": 72,
    "wraps_packet": 18,
    "salad": 24,
}

def convert(val, item_type):
    if val == "":
        return 0
    val = val.upper()
    try:
        if val.endswith("B"):
            return float(val[:-1]) * conversion[item_type]
        elif val.endswith("P") and item_type == "wraps_box":
            return float(val[:-1]) * conversion["wraps_packet"]
        else:
            return float(val)
    except:
        return 0

st.title("Subway Stock Calculator 📦")

items = ["breads", "gluten_free", "wraps_box", "salad"]
locations = ["Freezer", "Chiller", "Back Store", "Front Store"]

for item in items:
    readable_name = item.replace("_box", "").replace("_", " ").title()
    st.subheader(f"{readable_name}")
    total = 0
    for loc in locations:
        entry = st.text_input(f"{readable_name} in {loc}", key=f"{item}_{loc}")
        total += convert(entry, item)
    st.success(f"Total {readable_name}: {int(total)}")
