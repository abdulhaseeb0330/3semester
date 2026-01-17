import streamlit as st
import json
import os
from datetime import datetime

# --- CONFIG ---
MESSAGES_FILE = "messages.json"  # file to persist messages
MAX_MESSAGES = 1000  # keep last N messages to avoid file growth

# --- Helpers ---

def load_messages():
    if not os.path.exists(MESSAGES_FILE):
        return []
    try:
        with open(MESSAGES_FILE, "r", encoding="utf-8") as f:
            data = json.load(f)
            if isinstance(data, list):
                return data
            return []
    except Exception:
        return []


def save_message(username, text):
    text = text.strip()
    if not text:
        return
    messages = load_messages()
    messages.append({
        "username": username,
        "text": text,
        "ts": datetime.utcnow().isoformat() + "Z",
    })
    # keep only last MAX_MESSAGES
    if len(messages) > MAX_MESSAGES:
        messages = messages[-MAX_MESSAGES:]
    with open(MESSAGES_FILE, "w", encoding="utf-8") as f:
        json.dump(messages, f, ensure_ascii=False, indent=2)


# --- UI ---

st.set_page_config(page_title="Group Chat (Streamlit)", layout="wide")
st.title("🚀 Simple Group Chat")

# Username input (persist in session state)
if "username" not in st.session_state:
    st.session_state.username = "Guest_" + datetime.utcnow().strftime("%H%M%S")

col1, col2 = st.columns([3, 1])
with col1:
    username = st.text_input("Your name", st.session_state.username, key="username_input")
    if username.strip():
        st.session_state.username = username.strip()

st.markdown("---")

# Message input
msg = st.text_area("Write a message", height=100, key="msg_area")
if st.button("Send", key="send_btn"):
    if not msg.strip():
        st.warning("Cannot send empty message")
    else:
        save_message(st.session_state.username, msg)
        st.success("Message sent")
        # Instead of modifying session_state directly, rerun to clear
        st.experimental_rerun()

st.markdown("### Chat")

# Load and display messages
messages = load_messages()
if not messages:
    st.info("No messages yet — be the first to write!")
else:
    # Show messages newest last
    for m in messages[-200:]:
        ts = m.get("ts", "")
        # convert ISO ts to readable local time if possible
        try:
            pretty_ts = datetime.fromisoformat(ts.replace("Z", "")).strftime("%Y-%m-%d %H:%M:%S")
        except Exception:
            pretty_ts = ts
        st.markdown(f"**{m.get('username','Unknown')}**  ·  *{pretty_ts}*\n\n{m.get('text','')}")
        st.markdown("---")

# Info Sidebar
st.sidebar.header("Info")
st.sidebar.write("Persistent messages file:\n`%s`" % MESSAGES_FILE)
st.sidebar.write("Anyone can open the app URL and send messages. This app stores messages locally on the server in a JSON file.")

st.sidebar.markdown("\n---\n**Notes for production**\n- This app has no authentication. For real use, add login (OAuth) or simple password.\n- For concurrent heavy use, replace JSON with a DB (SQLite/Postgres) or a messaging backend.\n- Consider locking or atomic writes for strict concurrency handling.")
