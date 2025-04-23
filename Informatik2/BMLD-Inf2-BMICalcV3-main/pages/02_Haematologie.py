import streamlit as st
import math
import base64

st.set_page_config(page_title="Blutbilddifferenzierung", page_icon="🩸")

fach = st.query_params.get("fach", "Hämatologie")

def load_icon_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

img_rbb = load_icon_base64("assets/red-blood-cells.png")
img_neutro = load_icon_base64("assets/neutrophil.png")
img_lympho = load_icon_base64("assets/lymphocyte.png")
img_platelet = load_icon_base64("assets/platelet.png")
img_title = load_icon_base64("assets/blood-count.png")
img_blood = load_icon_base64("assets/blood.png")

st.markdown(f"""
<h1 style='display: flex; align-items: center; gap: 24px;'>
    Zellzählung {fach}
    <img src='data:image/png;base64,{img_blood}' width='50'>
</h1>
""", unsafe_allow_html=True)

zelltypen = [
    "Blasten", "Promyelozyten", "Myelozyten", "Metamyelozyten",
    "Stabkernige Granulozyten", "Segmentkernige Granulozyten",
    "Eosinophile", "Basophile", "Monozyten", "Lymphozyten", "Plasmazellen",
    "Erythroblasten", "Unbekannt / Diverses"
]

st.markdown("""
<style>
.zell-header {
    font-weight: bold;
    background-color: #f2f2f2;
    padding: 6px;
    border: 1px solid #ccc;
    text-align: center;
}
.zell-row {
    border-bottom: 1px solid #eee;
    padding: 8px 0;
}
.zell-cell {
    padding: 4px;
    text-align: center;
}
</style>
""", unsafe_allow_html=True)

# Header manuell
st.markdown("""
<div class="zell-row">
    <div class="zell-cell" style="display: inline-block; width: 20%;"><div class="zell-header">Zelltyp</div></div>
    <div class="zell-cell" style="display: inline-block; width: 30%;"><div class="zell-header">Zählung 1</div></div>
    <div class="zell-cell" style="display: inline-block; width: 30%;"><div class="zell-header">Zählung 2</div></div>
    <div class="zell-cell" style="display: inline-block; width: 15%;"><div class="zell-header">Durchschnitt</div></div>
</div>
""", unsafe_allow_html=True)

for zelltyp in zelltypen:
    z1_key = f"{zelltyp}_z1"
    z2_key = f"{zelltyp}_z2"

    if z1_key not in st.session_state:
        st.session_state[z1_key] = 0
    if z2_key not in st.session_state:
        st.session_state[z2_key] = 0

    col1, col2, col3, col4 = st.columns([2, 3, 3, 2])

    with col1:
        st.markdown(f"**{zelltyp}**")

    with col2:
        c1, c2, c3 = st.columns([1, 1, 1])
        if c1.button("➖", key=f"sub_{zelltyp}_z1"):
            st.session_state[z1_key] = max(0, st.session_state[z1_key] - 1)
        c2.markdown(f"<div style='text-align: center; padding-top: 8px;'>{st.session_state[z1_key]}</div>", unsafe_allow_html=True)
        if c3.button("➕", key=f"add_{zelltyp}_z1"):
            st.session_state[z1_key] += 1

    with col3:
        c4, c5, c6 = st.columns([1, 1, 1])
        if c4.button("➖", key=f"sub_{zelltyp}_z2"):
            st.session_state[z2_key] = max(0, st.session_state[z2_key] - 1)
        c5.markdown(f"<div style='text-align: center; padding-top: 8px;'>{st.session_state[z2_key]}</div>", unsafe_allow_html=True)
        if c6.button("➕", key=f"add_{zelltyp}_z2"):
            st.session_state[z2_key] += 1

    with col4:
        avg = (st.session_state[z1_key] + st.session_state[z2_key]) / 2
        st.markdown(f"**{avg:.1f}**")

st.markdown("---")

# Untere Zusatzbereiche
st.markdown(f"""
<h3 style='display: flex; align-items: center; gap: 10px;'>
    Rotes Blutbild
    <img src='data:image/png;base64,{img_rbb}' width='30'>
</h3>
""", unsafe_allow_html=True)

rb_felder = [
    "Anisozytose", "Mikrozyten", "Makrozyten", "Anisochromasie",
    "Hypochrom", "Hyperchrom", "Polychromasie", "Poikilozytose",
    "Ovalozyten", "Akanthozyten", "Sphärozyten", "Stomatozyten",
    "Echinozyten", "Targetzellen", "Tränenformen", "Sichelzellen",
    "Fragmentozyten", "Baso. Punktierung", "Howell Jollies", "Pappenheim",
]
for feld in rb_felder:
    st.selectbox(feld, ["", "+", "++", "+++"] , key=f"rb_{feld}")
st.text_area("Sonstiges:", key="rb_sonstiges", height=80)

st.markdown(f"""
<h3 style='display: flex; align-items: center; gap: 10px;'>
    Neutrophile Granulozyten
    <img src='data:image/png;base64,{img_neutro}' width='30'>
</h3>
""", unsafe_allow_html=True)

gb_felder = [
    "vergröberte Granula", "basophile Schlieren",
    "Zytoplasmavakuolen", "Fehlende Granula", "Kernpyknose", "Pseudopelger",
    "Linksverschiebung", "Kerne hoch-/übersegmentiert"
]
for feld in gb_felder:
    st.selectbox(feld, ["", "+", "++", "+++"] , key=f"gb_{feld}")
st.text_area("Sonstiges:", key="ng_sonstiges", height=80)

st.markdown(f"""
<h3 style='display: flex; align-items: center; gap: 10px;'>
    Lymphozytenveränderungen
    <img src='data:image/png;base64,{img_lympho}' width='30'>
</h3>
""", unsafe_allow_html=True)

ly_felder = [">10% LGL", "reaktiv", "pathologisch", "lymphoplasmozytoid"]
for feld in ly_felder:
    st.selectbox(feld, ["", "+", "++", "+++"] , key=f"ly_{feld}")
st.text_area("Sonstiges:", key="lc_sonstiges", height=80)

st.markdown(f"""
<h3 style='display: flex; align-items: center; gap: 10px;'>
    Thrombozyten
    <img src='data:image/png;base64,{img_platelet}' width='30'>
</h3>
""", unsafe_allow_html=True)

th_felder = ["Grosse Formen", "Riesenformen", "Agranulär"]
for feld in th_felder:
    st.selectbox(feld, ["", "+", "++", "+++"] , key=f"th_{feld}")
st.text_area("Sonstiges:", key="tc_sonstiges", height=80)

st.markdown("---")
# ==== Zurück-Button ====
if st.button("🔙 Zurück"):
    st.switch_page("pages/01_Datei.py")