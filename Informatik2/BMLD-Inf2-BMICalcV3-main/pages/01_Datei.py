import streamlit as st
import pandas as pd
import os
import base64

# ===== Login-Schutz =====
if "authentication_status" not in st.session_state or not st.session_state["authentication_status"]:
    st.switch_page("Start")

# ===== Bilder laden =====
def load_icon_base64(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")

icons = {
    "chemie": load_icon_base64("assets/adrenaline.png"),
    "haematologie": load_icon_base64("assets/blood.png"),
    "klinische chemie": load_icon_base64("assets/rna.png")
}

# ===== Seiteneinstellungen =====
st.set_page_config(page_title="Fachansicht", page_icon="📂")

# ===== Session-Parameter auslesen =====
fach_key = st.session_state.get("fach", "").lower().strip()
ansicht = st.session_state.get("ansicht", "start").lower().strip()

fach_namen = {
    "chemie": "Chemie",
    "haematologie": "Hämatologie",
    "klinische chemie": "Klinische Chemie"
}

csv_pfade = {
    "chemie": "data/data_chemie.csv",
    "haematologie": "data/data_haematologie.csv",
    "klinische chemie": "data/data_klinische_chemie.csv"
}

fach = fach_namen.get(fach_key, "Unbekannt")
dateipfad = csv_pfade.get(fach_key)
fach_icon = icons.get(fach_key)

# ===== Fachüberschrift mit Bild-Icon =====
st.markdown(f"""
<h1 style='display: flex; align-items: center; gap: 20px; font-size: 36px;'>
    {fach}
    <img src="data:image/png;base64,{fach_icon}" width="42">
</h1>
""", unsafe_allow_html=True)

# ===== Navigation =====
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("🏠 Start"):
        st.switch_page("Start.py")

with col2:
    if st.button("📝 Neuer Eintrag"):
        if fach_key == "haematologie":
            st.switch_page("pages/02_Haematologie.py")
        elif fach_key == "klinische chemie":
            st.switch_page("pages/04_Klinische Chemie.py")
        elif fach_key == "chemie":
            st.switch_page("pages/03_Chemie.py")

with col3:
    if fach_key == "haematologie":
        if st.button("🧬 Zellatlas"):
            st.switch_page("pages/08_Referenz_Haematologie.py")
    elif fach_key == "klinische chemie":
        if st.button("📊 Referenzwerte"):
            st.switch_page("pages/07_Referenzwerte.py")

# ===== Ansicht: Start (Eintragsübersicht) =====
if ansicht == "start":
    st.markdown("### Vergangene Einträge anzeigen und bearbeiten")

    if dateipfad and os.path.exists(dateipfad):
        df = pd.read_csv(dateipfad)

        titel_filter = st.text_input("🔍 Suche nach Titel")
        datum_filter = st.date_input("📅 Filter nach Datum", format="YYYY-MM-DD")
        datum_str = datum_filter.strftime("%Y-%m-%d") if datum_filter else None

        gefiltert = df.copy()
        if titel_filter:
            gefiltert = gefiltert[gefiltert["titel"].str.contains(titel_filter, case=False)]
        if datum_str and "datum" in gefiltert.columns:
            gefiltert = gefiltert[gefiltert["datum"] == datum_str]

        st.markdown("#### Gefundene Einträge")
        for index, row in gefiltert.iterrows():
            col1, col2 = st.columns([6, 2])
            with col1:
                st.markdown(f"**{row['datum']} – {row['titel']}**")
            with col2:
                if st.button(f"✏️ Bearbeiten {index}", key=f"edit_{index}"):
                    zielseite = {
                        "chemie": "03_Chemie.py",
                        "haematologie": "02_Haematologie.py",
                        "klinische chemie": "04_Klinische Chemie.py"
                    }.get(fach_key)
                    st.query_params["edit"] = index
                    st.query_params["fach"] = fach_key
                    st.switch_page(f"pages/{zielseite}")
    else:
        st.info("Noch keine gespeicherten Einträge für dieses Fach.")
