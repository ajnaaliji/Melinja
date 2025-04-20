import streamlit as st
import base64
import pandas as pd
from utils.data_manager import DataManager
from utils.login_manager import LoginManager

# ===== Seiteneinstellungen =====
st.set_page_config(
    page_title="Laborjournal",
    page_icon="🧪",
    layout="centered",
    initial_sidebar_state="collapsed"
)

# ===== Init Block =====
data_manager = DataManager(fs_protocol='webdav', fs_root_folder="App_Melinja")
login_manager = LoginManager(data_manager)
login_manager.login_register()

# ===== Daten laden =====
try:
    data_manager.load_user_data(
        session_state_key='calorie_data_df',
        file_name='data.csv',
        initial_value=pd.DataFrame(),
        parse_dates=['timestamp'],
        date_parser=lambda col: pd.to_datetime(col, errors='coerce')
    )
except UnicodeDecodeError:
    st.warning("⚠️ Die Datei 'data.csv' konnte nicht gelesen werden und wurde zurückgesetzt.")
    st.session_state["calorie_data_df"] = pd.DataFrame()

# ===== Begrüßung oben rechts =====
if "username" in st.session_state:
    st.markdown(f"""
        <div style='text-align: right; font-size: 20px; font-weight: bold; margin-top: 10px;'>
            👋 Schön, dass du wieder da bist, <span style='color:#2c3e50;'>{st.session_state['username']}</span>!
            <div style='font-size: 16px; color: #888;'>Bereit für dein nächstes Praktikum?</div>
        </div>
    """, unsafe_allow_html=True)

# ===== Bild laden =====
with open("assets/labor.png", "rb") as f:
    image_data = f.read()
    encoded_image = base64.b64encode(image_data).decode("utf-8")
    img_html = f'<img src="data:image/png;base64,{encoded_image}" width="36" style="margin-left: 10px; vertical-align: middle;">'

# ===== Style + Layout =====
st.markdown("""
    <style>
        .stApp {
            background: linear-gradient(to bottom, #eaf2f8, #f5f9fc);
        }
        .title-container {
            text-align: center;
            margin-top: 40px;
            margin-bottom: 20px;
        }
        .title-container h1 {
            font-size: 50px;
            font-weight: bold;
            margin-bottom: 10px;
        }
        .title-container p {
            font-size: 22px;
            color: #666;
            margin: 0;
        }
        .intro-box {
            background-color: #dceeff;
            padding: 20px;
            border-radius: 10px;
            font-size: 18px;
            margin-bottom: 30px;
        }
        .subject-title {
            font-size: 28px;
            font-weight: bold;
            margin-top: 30px;
            margin-bottom: 10px;
        }
        .hint-box {
            background-color: #FFF3CD;
            padding: 15px;
            border-radius: 8px;
            font-size: 16px;
            margin-top: 40px;
        }
    </style>
""", unsafe_allow_html=True)

# ===== Titelbereich =====
st.markdown(f"""
    <div class="title-container">
        <p>Dein persönliches</p>
        <h1>Laborjournal {img_html}</h1>
    </div>
""", unsafe_allow_html=True)

# ===== Einführungstext =====
st.markdown("""
<div class="intro-box">
    <p style="margin-bottom: 10px;">Plane, dokumentiere und behalte den Überblick über deine Praktika – alles an einem Ort.</p>
    <p style="margin-bottom: 10px;">Wähle ein Fach – und bring Ordnung ins Versuchswirrwarr.</p>
    <p style="margin-bottom: 0;"><strong>Laborkittel an, Journal starten. 🧪</strong></p>
</div>
""", unsafe_allow_html=True)

# ===== Fachauswahl =====
if st.session_state.get("authentication_status") is True:
    st.markdown('<div class="subject-title">Wähle dein gewünschtes Fach:</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns([1, 1, 1])

    if col1.button("🧪 Chemie"):
        st.session_state["fach"] = "chemie"
        st.session_state["ansicht"] = "start"
        st.switch_page("pages/01_Datei.py")

    if col2.button("🩸 Hämatologie"):
        st.session_state["fach"] = "haematologie"
        st.session_state["ansicht"] = "start"
        st.switch_page("pages/01_Datei.py")

    if col3.button("🧬 Klinische Chemie"):
        st.session_state["fach"] = "klinische chemie"
        st.session_state["ansicht"] = "start"
        st.switch_page("pages/01_Datei.py")

# ===== Hinweis =====
st.markdown("""
<div class="hint-box">
    ⚠️ <strong>Hinweis:</strong> Dieses Journal unterstützt dich bei der Organisation deines Studiums – es ersetzt jedoch keine individuelle Lernstrategie.
</div>
""", unsafe_allow_html=True)
