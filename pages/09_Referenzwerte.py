import streamlit as st

st.set_page_config(page_title="Referenzwerte", page_icon="📊")

st.title("📊 Referenzwerte – Hämatologie & Klinische Chemie")

# Auswahl des Fachbereichs
bereich = st.selectbox("Wähle einen Bereich:", ["Klinische Chemie", "Hämatologie"])

# Bildpfade pro Bereich und Kategorie
referenzbilder = {
    "Klinische Chemie": {
        "Allgemeine Referenzwerte": ["files/images/0001.png", "files/images/0002.png"],
        "Fett-Kontrolle (HDL, LDL)": ["files/images/0010.png", "files/images/0011.png"],
        "Multikontrolle (Albumin, Bilirubin, Glucose)": [
            "files/images/0003.png", "files/images/0004.png", "files/images/0005.png",
            "files/images/0006.png", "files/images/0007.png", "files/images/0008.png",
            "files/images/0009.png"
        ]
    },
    "Hämatologie": {
        # Du kannst hier später eigene Bilder einfügen
    }
}

# Bilder anzeigen
if bereich in referenzbilder:
    kategorien = referenzbilder[bereich]
    for titel, bilder in kategorien.items():
        with st.expander(f"🗌 {titel}"):
            for pfad in bilder:
                st.image(pfad, use_container_width=True)
else:
    st.info("Für diesen Bereich sind aktuell keine Referenzwerte als Bilder hinterlegt.")
