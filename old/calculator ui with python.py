# 💊 AI Medicine Recommender (Educational Demo)
# DISCLAIMER: Ye sirf taleemi / research demo hai. Ye medical advice nahi.
# Hamesha licensed doctor se mashwara karein, especially agar symptoms severe ya lambi muddat ke hon.

import re
import streamlit as st

st.set_page_config(page_title="AI Medicine Recommender (Educational)", page_icon="💊")

# -------------------------
# Simple rulebase (OTC-style)
# -------------------------
RULES = [
    # symptom, severity_threshold, min_days, max_days, medicine_key, dosage, tips
    ("fever",      "mild",     0, 3,  "paracetamol",           "500mg har 6–8 ghante (max 3g/day)", "Paani zyada; aaram; lukewarm sponging"),
    ("fever",      "moderate", 0, 5,  "paracetamol",           "500mg har 6–8 ghante (max 3g/day)", "Temp monitor; hydrate"),
    ("cough",      "mild",     0, 7,  "dextromethorphan syrup","10ml har 6–8 ghante",               "Garam fluids; irritants se parhez"),
    ("cough",      "moderate", 0,14,  "dextromethorphan syrup","10ml har 6–8 ghante",               "Room humidify; aaram"),
    ("sore_throat","mild",     0, 5,  "lozenges",              "As directed",                        "Salt-water gargle; garam chai"),
    ("sore_throat","moderate", 0, 7,  "ibuprofen",             "400mg har 8–12 ghante (khane ke sath)", "Thande mashroob se parhez"),
    ("headache",   "mild",     0, 2,  "paracetamol",           "500mg har 6–8 ghante (max 3g/day)", "Hydrate; screen time kam"),
    ("headache",   "moderate", 0, 3,  "ibuprofen",             "400mg har 8–12 ghante (khane ke sath)", "Andhera/khamosh kamra"),
    ("body_pain",  "mild",     0, 3,  "ibuprofen",             "400mg har 8–12 ghante (khane ke sath)", "Stretching/heat-ice"),
    ("body_pain",  "moderate", 0, 5,  "ibuprofen",             "400mg har 8–12 ghante (khane ke sath)", "Heat/ice packs"),
    ("nausea",     "mild",     0, 2,  "oral rehydration (ORS)", "As directed",                       "Chote chote ghont; bland diet"),
    ("nausea",     "moderate", 0, 3,  "oral rehydration (ORS)", "As directed",                       "Ginger/BRAT diet"),
    ("vomiting",   "mild",     0, 1,  "oral rehydration (ORS)", "As directed",                       "Frequently sips"),
    ("vomiting",   "moderate", 0, 2,  "oral rehydration (ORS)", "As directed",                       "Worsen par doctor"),
    ("diarrhea",   "mild",     0, 2,  "oral rehydration (ORS)", "As directed",                       "Zinc 10–20mg/day optional"),
    ("diarrhea",   "moderate", 0, 3,  "oral rehydration (ORS)", "As directed",                       "BRAT diet; dairy se parhez"),
    ("cold",       "mild",     0, 5,  "antihistamine (OTC)",    "As directed",                       "Aaram; steam inhalation"),
    ("cold",       "moderate", 0, 7,  "antihistamine (OTC)",    "As directed",                       "Nasal saline"),
    ("allergy",    "mild",     0, 7,  "antihistamine (OTC)",    "As directed",                       "Triggers se bachao"),
    ("allergy",    "moderate", 0,14,  "antihistamine (OTC)",    "As directed",                       "HEPA/saaf mahal"),
    ("acidity",    "mild",     0, 3,  "antacid (OTC)",          "As directed",                       "Spicy/fatty food se parhez"),
    ("acidity",    "moderate", 0, 7,  "antacid (OTC)",          "As directed",                       "Head elevate during sleep"),
]

SEVERITY_ORDER = {"any": 0, "mild": 1, "moderate": 2, "severe": 3}

# Urdu/English symptom map
SYM_MAP = {
    "bukhar": "fever",
    "khansi": "cough",
    "sar dard": "headache",
    "sar_dard": "headache",
    "gala dard": "sore_throat",
    "gala_dard": "sore_throat",
    "zukaam": "cold",
    "jism dard": "body_pain",
    "jism_dard": "body_pain",
    "seena jalna": "acidity",
    "seena_jalna": "acidity",
    "ulti": "vomiting",
    "dast": "diarrhea",
    "matelee": "nausea",
    "allergy": "allergy",
}

SEV_MAP = {
    "halka": "mild", "light": "mild", "mild": "mild",
    "moderate": "moderate",
    "zyada": "severe", "bohat": "severe", "severe": "severe",
}

DUR_PATTERNS = [
    (re.compile(r"(\d+)\s*(din|day|days)"), 1),
    (re.compile(r"(\d+)\s*(hafta|week|weeks)"), 7),
]

def normalize_symptom(token: str) -> str:
    t = token.strip().lower().replace("-", " ").replace("_", " ")
    return SYM_MAP.get(t, t).replace(" ", "_")

def parse_free_text(text: str):
    text_l = text.lower()
    # duration
    duration_days = 1
    for pat, mult in DUR_PATTERNS:
        m = pat.search(text_l)
        if m:
            duration_days = int(m.group(1)) * mult
            break
    # severity
    severity = "mild"
    for k, v in SEV_MAP.items():
        if k in text_l:
            severity = v
            break
    # symptoms
    known = {r[0] for r in RULES}
    found = set()
    for sym in known:
        key = sym.replace("_", " ")
        if key in text_l:
            found.add(sym)
    for k, v in SYM_MAP.items():
        if k in text_l:
            found.add(v.replace(" ", "_"))
    if not found:
        for w in re.findall(r"[a-zA-Z\u0600-\u06FF_]+", text_l):
            norm = normalize_symptom(w)
            if norm in known:
                found.add(norm)
    return sorted(found), duration_days, severity

def recommend(symptoms, duration_days, severity, age=None, contraindications=None):
    contraindications = contraindications or []
    sev_rank = SEVERITY_ORDER.get(severity, 1)
    notes = []
    recs = {}

    if not symptoms:
        return [], ["Koi symptom samajh nahi aya — zyada wazeh likhen (e.g., '2 din se bukhar aur khansi, halka')."]

    # basic safety flags
    consult = False
    if duration_days >= 5 or sev_rank >= SEVERITY_ORDER["severe"]:
        consult = True
    if age is not None and age < 12:
        consult = True
        notes.append("Bachcha detected (<12y): pediatric mashwara zaroori ho sakta hai.")
    for ci in (c.lower() for c in contraindications):
        if ci in {"pregnancy", "ulcer", "liver_disease"}:
            consult = True
            notes.append(f"Contraindication: {ci}. Doctor se mashwara behtar hai.")

    for (sym, thr, mn, mx, med, dose, tip) in RULES:
        if sym in symptoms and mn <= duration_days <= mx and SEVERITY_ORDER[thr] <= sev_rank:
            if med not in recs:
                recs[med] = {"dosage": dose, "symptoms": set(), "tips": set()}
            recs[med]["symptoms"].add(sym)
            if tip:
                recs[med]["tips"].add(tip)

    result = []
    for med, obj in recs.items():
        result.append({
            "medicine": med,
            "dosage": obj["dosage"],
            "for": ", ".join(sorted(s.replace("_", " ") for s in obj["symptoms"])),
            "tips": sorted(obj["tips"]) if obj["tips"] else [],
        })

    if consult:
        result.append({
            "medicine": "Consult a Doctor",
            "dosage": "—",
            "for": "",
            "tips": ["Severe/long duration ya red flags; clinical review recommended."],
        })
    if not result:
        notes.append("Safe OTC-style match nahi mila — please doctor se mashwara karein.")
    return result, notes

# -------------------------
# UI
# -------------------------
st.markdown("""
# 💊 AI Medicine Recommender (Educational)
**Ye demo sirf taleemi maqsad ke liye hai — medical advice nahi.**
""")

with st.expander("⚠️ Safety Notes"):
    st.write("""
- Adults focus; prescriptions **nahi**. Sirf general OTC-style guidance.
- Agar chronic diseases, pregnancy, drug allergy, ulcers, liver problems, ya severe/lambe arsay ke symptoms hon to **doctor se mashwara** lazmi.
- Emergency signs (saans me takleef, behoshi, khoon, worst-ever headache, chest pain) → **immediate care**.
""")

st.sidebar.header("Patient Context (optional)")
age = st.sidebar.number_input("Age (saal)", min_value=0, max_value=120, value=25)
preg = st.sidebar.checkbox("Pregnancy")
ulcer = st.sidebar.checkbox("Ulcer / GI bleed history")
liver = st.sidebar.checkbox("Liver disease")
contra = []
if preg: contra.append("pregnancy")
if ulcer: contra.append("ulcer")
if liver: contra.append("liver_disease")

if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "Assalam o Alaikum! Apne symptoms free text me likhein (e.g., '2 din se bukhar aur khansi, halka')."}
    ]

for m in st.session_state.messages:
    with st.chat_message(m["role"]):
        st.markdown(m["content"])

user_text = st.chat_input("Type here (Urdu/English supported)…")

if user_text:
    st.session_state.messages.append({"role": "user", "content": user_text})
    with st.chat_message("user"):
        st.markdown(user_text)

    syms, dur, sev = parse_free_text(user_text)
    rec_list, notes = recommend(syms, dur, sev, age=age, contraindications=contra)

    # Build reply
    lines = []
    if syms:
        lines.append(f"**Parsed:** symptoms `{', '.join(syms)}`, duration ~ `{dur}` days, severity `{sev}`")
    else:
        lines.append("Symptoms samajh nahi aaye — behtar parsing ke liye 'din/hafta', 'halka/zyada' use karein.")

    if rec_list:
        lines.append("\n**Suggested (educational only):**")
        for r in rec_list:
            bullet = f"- **{r['medicine']}** — {r['dosage']}"
            if r["for"]:
                bullet += f" _(for: {r['for']})_"
            lines.append(bullet)
            for t in r["tips"]:
                lines.append(f"    • {t}")
    if notes:
        lines.append("\n**Notes:**")
        for n in notes:
            lines.append(f"- {n}")

    reply = "\n".join(lines) if lines else "I couldn't generate a suggestion. Please rephrase."
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.markdown(reply)
