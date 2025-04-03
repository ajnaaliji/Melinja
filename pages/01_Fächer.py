import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')  # wie bei deinem Lehrer
# ====== End Login Block ======

# ====== Seiten-Titel ======
st.title("📚 Fächerübersicht")

# ====== Einführung ======
st.markdown("""
<div style="background-color: #E7F3FF; padding: 15px; border-radius: 8px;">
Wähle ein Fach, um Materialien, Notizen oder Lernmethoden zu sehen oder hinzuzufügen.
</div>
""", unsafe_allow_html=True)

st.write("")

# ====== Fachliste ======
fächer = [
    "Chemie",
    "Klinische Chemie",
    "Hämatologie",
    "Histologie",
    "Mikrobiologie"
]

# Auswahlfeld für Fach
ausgewähltes_fach = st.selectbox("🔍 Wähle ein Fach:", fächer)

# Fach anzeigen
st.markdown(f"### 📘 Aktuell ausgewähltes Fach: **{ausgewähltes_fach}**")

# Platzhalter für spätere Inhalte
st.info("Hier kannst du später Fach-spezifische Inhalte anzeigen, z. B. Dateien, Lernpläne, Methoden…")

st.markdown("---")

# ====== Entwicklerinnen ======
st.markdown("""
#### 👩‍💻 Entwicklerinnen:
**Ajna Aliji**  
[alijiajn@students.zhaw.ch](mailto:alijiajn@students.zhaw.ch)  

**Melisa Dedukic**  
[dedukmel@students.zhaw.ch](mailto:dedukmel@students.zhaw.ch)
""")
