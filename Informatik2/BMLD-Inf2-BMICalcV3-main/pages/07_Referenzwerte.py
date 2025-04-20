import streamlit as st

st.set_page_config(page_title="Referenzwerte", page_icon="📊")

st.title("📊 Referenzwerte – Klinische Chemie")

# Bildpfade für Klinische Chemie
referenzbilder = {
    "Allgemeine Referenzwerte": ["files/images/0001.png", "files/images/0002.png"],
    "Fett-Kontrolle (HDL, LDL)": ["files/images/0010.png", "files/images/0011.png"],
    "Multikontrolle (Albumin, Bilirubin, Glucose)": [
        "files/images/0003.png", "files/images/0004.png", "files/images/0005.png",
        "files/images/0006.png", "files/images/0007.png", "files/images/0008.png",
        "files/images/0009.png"
    ]
}

# Bilder anzeigen
for titel, bilder in referenzbilder.items():
    with st.expander(f"🗌 {titel}"):
        for pfad in bilder:
            st.image(pfad, use_container_width=True)
            with open(pfad, "rb") as file:
                btn = st.download_button(
                    label="📥 Bild herunterladen",
                    data=file,
                    file_name=pfad.split("/")[-1],
                    mime="image/png"
                )
# Zurück-Button zur Datei-Übersicht (Klinische Chemie)
if st.button("🔙 Zurück"):
    st.switch_page("pages/01_Datei.py")
