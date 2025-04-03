import streamlit as st

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')
# ====== End Login Block ======

st.set_page_config(page_title="StudyJournal", page_icon="📘")

# ====== Titel ======
st.title("📘 StudyJournal – Dein persönliches Studienjournal")

# ====== Einführung ======
st.markdown("""
<div style="background-color: #E7F3FF; padding: 15px; border-radius: 8px;">
Das <strong>StudyJournal</strong> unterstützt dich bei der Organisation deines Studiums. Wähle ein Fach, erfasse deine Notizen, lade Lernunterlagen hoch und dokumentiere deinen Fortschritt.
</div>
""", unsafe_allow_html=True)

st.write("")

# ====== Funktionen ======
st.markdown("### 🔧 Funktionen im Überblick:")
st.markdown("""
1. 📚 **Fächerübersicht** – Füge deine aktuellen Fächer hinzu  
2. 📝 **Zusammenfassungen & Dateien** – Speichere PDFs, Bilder oder Texte  
3. 🎯 **Lernziele & Methoden** – Plane, wie du den Stoff angehst  
4. 🧪 **Materialien & Tools** – Was du brauchst, um dich vorzubereiten  
5. ✅ **Checkliste für Prüfungen** – Was du bereits erledigt hast  
""")

st.write("")

# ====== Hinweis ======
st.markdown("""
<div style="background-color: #FFF3CD; padding: 15px; border-radius: 8px;">
ℹ️ <strong>Hinweis:</strong> Dieses Journal hilft dir, strukturiert durchs Studium zu gehen – es ersetzt aber keine individuelle Lernstrategie.
</div>
""", unsafe_allow_html=True)

st.write("")

# ====== Navigation ======
st.markdown("## 🚀 Starte hier:")

# Button-Stil
st.markdown("""
<style>
.stButton>button {
    background-color: #007BFF !important;
    color: white !important;
    font-size: 18px !important;
    font-weight: bold !important;
    border-radius: 8px !important;
    padding: 10px !important;
    width: 100% !important;
}
.stButton>button:hover {
    background-color: #0056b3 !important;
}
</style>
""", unsafe_allow_html=True)

col1, col2 = st.columns(2)
with col1:
    if st.button("📚 Fächerübersicht"):
        st.switch_page("pages/01_Faecher.py")
with col2:
    if st.button("📁 Dateien & Notizen"):
        st.switch_page("pages/02_Dateien.py")

st.markdown("---")

# ====== Entwicklerinnen ======
st.markdown("""
#### Entwicklerinnen:
**Ajna Aliji**  
[alijiajn@students.zhaw.ch](mailto:alijiajn@students.zhaw.ch)  

**Melisa Dedukic**  
[dedukmel@students.zhaw.ch](mailto:dedukmel@students.zhaw.ch)
""")