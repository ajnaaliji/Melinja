import streamlit as st
st.set_page_config(page_title="Methoden", page_icon="🧪")

# ====== Start Login Block ======
from utils.login_manager import LoginManager
LoginManager().go_to_login('Start.py')
# ====== End Login Block ======

# ------------------------------------------------------------
# Methodenblatt pro Fach & Praktikum

st.title("📋 Methodenblatt pro Fach")

# Fachauswahl
fächer = ["Chemie", "Klinische Chemie", "Hämatologie", "Histologie", "Mikrobiologie"]
fach = st.selectbox("📚 Wähle ein Fach:", fächer)

# Emoji-Auswahl je Fach
emoji_map = {
    "Chemie": "🧪",
    "Klinische Chemie": "💉",
    "Hämatologie": "🩸",
    "Histologie": "🔬",
    "Mikrobiologie": "🦠"
}
fach_emoji = emoji_map.get(fach, "📘")

# Praktikum / Experiment eingeben
praktikum = st.text_input(" 🔬 Praktikum / Experiment (z.\u202fB. 'Titration', 'Zählung', 'Färbung')")

# Abschnittsdefinitionen je Fach mit Beschreibung und Bonusfeldern
abschnitt_beschreibungen = {
    "Hämatologie": [
        ("1. Ziel / Zweck", "Was ist das Ziel des Versuchs? z. B. Unterscheidung von Leukozytenarten."),
        ("2. Durchführung", "Wie wurde die Methode durchgeführt? z. B. Blutausstrich nach May-Grünwald-Giemsa."),
        ("3. Schritte / Ablauf", "Einzelschritte wie Fixieren, Färben, Auswerten."),
        ("4. Zellmerkmale", "Welche Zellarten erkenne ich? Erys, Leukos, Thrombos, ggf. mit Normwerten."),
        ("5. Material & Geräte", "Was wurde verwendet? Objektträger, Mikroskop, Färbelösungen usw."),
        ("6. Wichtige Hinweise", "Artefakte vermeiden, sauber arbeiten, Fixierzeit beachten."),
        ("7. Interpretation", "Wie sind die Ergebnisse zu deuten? z. B. Anisozytose, Linksverschiebung."),
        ("8. Referenzwerte", "Kleine Normwert-Tabelle z. B. Ery-Anzahl, Hb usw."),
        ("9. Vergleichsmikroskopie", "Unterschiede zwischen gesunden und pathologischen Bildern.")
    ],
    "Histologie": [
        ("1. Ziel / Zweck", "Was soll untersucht werden? z. B. Epithelart erkennen."),
        ("2. Probenvorbereitung", "Fixierung, Entkalkung, Einbettung z. B. in Paraffin."),
        ("3. Färbemethode", "Welche Färbung wurde verwendet? z. B. HE, PAS."),
        ("4. Arbeitsschritte", "Schnitt, Färbung, Spülung, Decken usw."),
        ("5. Mikroskopische Merkmale", "Zellkerne, Strukturen, Epithelarten unter dem Mikroskop."),
        ("6. Materialien & Geräte", "Mikrotom, Objektträger, Färbelösung, Deckgläser."),
        ("7. Hinweise / Artefakte", "Fehlerquellen wie Luftblasen, Quetschartefakte."),
        ("8. Interpretation / Ergebnis", "Deutung der Befunde z. B. entzündlich verändertes Gewebe."),
        ("9. Gewebeart / Organ", "z. B. Niere, Leber, Haut zur Einordnung."),
        ("10. Vergleichspräparate", "Gesundes vs. pathologisches Gewebe."),
        ("11. Färbeergebnis", "z. B. Zellkerne blau, Zytoplasma rosa.")
    ],
    "Mikrobiologie": [
        ("1. Ziel / Fragestellung", "Was soll bestimmt werden? z. B. Nachweis von gramnegativen Bakterien."),
        ("2. Material / Probenart", "Welche Probe? z. B. Urin, Abstrich, Blutkultur."),
        ("3. Kultivierung", "Nährmedien, Temperatur, Inkubationsbedingungen."),
        ("4. Färbemethode", "z. B. Gram, Ziehl-Neelsen, Methylenblau."),
        ("5. Arbeitsschritte", "z. B. Ausstreichen, Inkubieren, Färben."),
        ("6. Beobachtungen", "Kolonieform, Geruch, mikroskopische Merkmale."),
        ("7. Identifikation / Interpretation", "z. B. Morphologie, Katalase-Test, Oxidase-Test."),
        ("8. Hinweise / Fehlerquellen", "z. B. falsche Inkubation, Kontamination."),
        ("9. Antibiogramm", "z. B. Hemmhofbestimmung, Interpretation nach EUCAST."),
        ("10. Sicherheitsmaßnahmen", "z. B. Umgang mit BSL-2-Keimen."),
        ("11. Vergleichstabelle", "z. B. Grampositiv vs. Gramnegativ.")
    ],
    "Klinische Chemie": [
        ("1. Ziel / Fragestellung", "z. B. Glukosebestimmung zur Diabetesdiagnose."),
        ("2. Probenmaterial", "z. B. Serum, Plasma, Urin. Wichtig: Lagerung, Handhabung."),
        ("3. Reagenzien & Geräte", "z. B. Analysegerät, Testkit, Kalibrator."),
        ("4. Methodentyp", "z. B. enzymatisch, photometrisch, turbidimetrisch."),
        ("5. Arbeitsschritte", "Vorbereitung, Gerätebedienung, Kalibrierung."),
        ("6. Berechnung / Ergebnis", "z. B. Konzentration über Extinktion."),
        ("7. Referenzwerte", "Normbereiche angeben, z. B. für Glukose 3.9–5.5 mmol/L."),
        ("8. Interpretation / Bewertung", "Was bedeutet ein Wert außerhalb der Norm?"),
        ("9. Fehlerquellen", "z. B. Hämolyse, Lipämie, falsche Lagerung."),
        ("10. Gerätename / Hersteller", "z. B. Roche Cobas, Beckman Coulter."),
        ("11. Einheit des Parameters", "z. B. mmol/L, mg/dL."),
        ("12. Probenlagerung", "z. B. 4 °C, 24h stabil."),
        ("13. Trend / Verlauf", "z. B. Verlauf über 3 Tage, Tabelle oder Diagramm.")
    ],
    "Chemie": [
        ("1. Ziel / Fragestellung", "Was soll analysiert werden? z. B. Konzentration von HCl."),
        ("2. Reaktionsgleichung / Theorie", "Kurze Reaktionsgleichung oder chemischer Hintergrund."),
        ("3. Chemikalien & Geräte", "NaOH, Indikator, Bürette, Becherglas usw."),
        ("4. Durchführung", "Ablauf wie Probenvorbereitung oder Messung."),
        ("5. Arbeitsschritte", "Detaillierte Schrittfolge."),
        ("6. Beobachtungen", "Farbumschlag, Ausfällung, Gasentwicklung."),
        ("7. Berechnungen", "Konzentration, Stoffmenge, pH usw."),
        ("8. Auswertung / Interpretation", "Was sagen die Ergebnisse aus?"),
        ("9. Sicherheitsaspekte", "z. B. ätzend, reizend, Schutzmaßnahmen."),
        ("10. Vergleich / Trend", "z. B. Serienversuche mit Konzentrationsvergleich.")
    ]
}

# Wenn Praktikum angegeben ist, zeige passende Eingabefelder
if praktikum:
    st.markdown(f"### {fach_emoji} Methodenblatt für **{fach}** – *{praktikum}*")
    
    abschnitte = abschnitt_beschreibungen.get(fach, [])

    for abschnitt, beschreibung in abschnitte:
        st.markdown(f"#### {abschnitt}")
        st.markdown(f"<div style='color:gray; font-size:0.9em'>{beschreibung}</div>", unsafe_allow_html=True)
        key = f"{fach}_{praktikum}_{abschnitt}"
        default = st.session_state.get(key, "")
        st.text_area("", value=default, key=key, height=160)

    if st.button("📏 Alles speichern"):
        st.success("Methodenblatt gespeichert!")
else:
    st.info("Bitte gib zuerst das Praktikum ein, um das Methodenblatt zu bearbeiten.")
