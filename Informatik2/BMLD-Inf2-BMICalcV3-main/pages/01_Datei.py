import streamlit as st
import pandas as pd

st.set_page_config(page_title="Fachansicht", page_icon="📂")

# ==== Session-Parameter auslesen ====
fach_key = st.session_state.get("fach", "").lower().strip()
ansicht = st.session_state.get("ansicht", "start").lower().strip()

fach_namen = {
    "chemie": "⚗️ Chemie",
    "haematologie": "🩸 Hämatologie",
    "klinische chemie": "🧬 Klinische Chemie"
}
fach = fach_namen.get(fach_key, "📁 Unbekannt")

# ==== Überschrift ====
st.markdown(f"# {fach}")

# ==== Navigation innerhalb der Seite ====
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
            st.session_state["ansicht"] = "neu"
            st.rerun()

with col3:
    if fach_key == "haematologie":
        if st.button("🧬 Zellatlas"):
            st.switch_page("pages/08_Referenz_Haematologie.py")
    elif fach_key == "klinische chemie":
        if st.button("📊 Referenzwerte"):
            st.switch_page("pages/07_Referenzwerte.py")

# ==== Startansicht ====
if ansicht == "start":
    st.markdown("### Was möchtest du tun?")

    eintraege = pd.DataFrame({
        "datum": ["2025-04-10", "2025-04-05", "2025-03-28"],
        "titel": [f"{fach} – Versuch A", f"{fach} – Analyse B", f"{fach} – Versuch C"]
    })

    suche = st.text_input("🔍 Suche nach Titel oder Datum")

    gefiltert = eintraege[
        eintraege["titel"].str.contains(suche, case=False) |
        eintraege["datum"].str.contains(suche)
    ]

    st.markdown("### Vergangene Einträge")
    for _, row in gefiltert.iterrows():
        if st.button(f"{row['datum']} – {row['titel']}"):
            st.success(f"👉 Du hast **{row['titel']}** ausgewählt.")

# ==== Nur Chemie: Placeholder für Neuansicht ====
elif ansicht == "neu":
    st.markdown("### ✍️ Neuer Eintrag")
    st.info(f"Hier kannst du bald neue Einträge für **{fach}** hinzufügen.")
