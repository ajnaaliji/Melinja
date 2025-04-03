# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py') 
# ====== End Login Block ======

# ------------------------------------------------------------
# Fachseite für StudyJournal
import streamlit as st

st.title("📚 Fächerübersicht")

# ====== Emoji-Zuweisung pro Fach ======
fach_emojis = {
    "Chemie": "🧪",
    "Klinische Chemie": "💉",
    "Hämatologie": "🩸",
    "Histologie": "🔬",
    "Mikrobiologie": "🦠"
}

# ====== Liste deiner Fächer ======
fächer = list(fach_emojis.keys())

# ====== Auswahl eines Fachs ======
ausgewähltes_fach = st.selectbox("🔍 Wähle ein Fach:", fächer)

# ====== Anzeige mit Emoji ======
emoji = fach_emojis.get(ausgewähltes_fach, "")
st.markdown(f"### Fach: {emoji} **{ausgewähltes_fach}**")

# ====== Eingabe für persönliche Notiz oder Lernstand ======
notiz_key = f"notiz_{ausgewähltes_fach}"
default_notiz = st.session_state.get(notiz_key, "")

notiz = st.text_area("📝 Deine Notiz zu diesem Fach:", value=default_notiz)

if st.button("💾 Notiz speichern"):
    st.session_state[notiz_key] = notiz
    st.success("Notiz gespeichert!")

# ====== Hinweisbox ======
st.info("Dies ist ein einfacher Einstieg. Später kannst du z. B. Lernpläne, Dateien oder Checklisten pro Fach speichern.")
