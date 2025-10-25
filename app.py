import streamlit as st
import time
from datetime import datetime

# ---------- Page / theme ----------
st.set_page_config(
    page_title="AI Command Center",
    page_icon="🦁",
    layout="wide",
)

GOLD = "#C7A647"
BLACK = "#0B0B0C"
CSS = f"""
<style>
:root {{
  --bg: {BLACK};
  --card: #121216;
  --border: #27272f;
  --gold: {GOLD};
  --fg: #e9e9ee;
  --muted: #8b8b94;
}}
/* Dark background */
.stApp {{ background: var(--bg); color: var(--fg); }}
/* Cards */
.block-container {{ padding-top: 2rem; }}
.css-1r6slb0, .css-1y4p8pa, .stMarkdown, .stDataFrame {{ color: var(--fg); }}
section[data-testid="stSidebar"] {{ background: #0f0f12; border-right: 1px solid #1e1e25; }}
/* Buttons */
.stButton>button {{ background:var(--gold); color:#111; font-weight:700; border-radius:12px; border:none; }}
.stButton>button:hover {{ filter: brightness(1.05); }}
/* Inputs */
.stTextInput>div>div>input, .stPassword>div>div>input {{
  background: #121216; color: var(--fg); border:1px solid var(--border);
}}
/* Headings */
h1, h2, h3 {{ color: var(--fg); }}
/* Center login card */
.login-card {{ background:#111114; border:1px solid var(--border); border-radius:16px; padding:30px; width:420px; margin:8vh auto; box-shadow:0 12px 40px rgba(0,0,0,.45); }}
.logo {{ width:84px; height:84px; margin:0 auto 10px; display:block; }}
.subtitle {{ color:var(--muted); text-align:center; margin-top:4px; }}
</style>
"""
st.markdown(CSS, unsafe_allow_html=True)

# ---------- Inline lion crest (gold, no text) ----------
LION_SVG = f"""
<svg class="logo" viewBox="0 0 128 128" xmlns="http://www.w3.org/2000/svg" fill="{GOLD}">
  <defs>
    <linearGradient id="g" x1="0" x2="1">
      <stop offset="0%" stop-color="{GOLD}"/><stop offset="100%" stop-color="#9c8031"/>
    </linearGradient>
  </defs>
  <circle cx="64" cy="64" r="58" stroke="url(#g)" stroke-width="6" fill="none"/>
  <path fill="url(#g)" d="M64 28c-9 0-18 6-21 15-7 3-12 10-12 18 0 10 8 19 18 20 1 7 8 12 15 12s14-5 15-12c10-1 18-10 18-20 0-8-5-15-12-18-3-9-12-15-21-15zm-8 26c3 0 6 3 6 6s-3 6-6 6-6-3-6-6 3-6 6-6zm16 0c3 0 6 3 6 6s-3 6-6 6-6-3-6-6 3-6 6-6zm-8 28c-6 0-12-3-15-7 3 1 9 3 15 3s12-2 15-3c-3 4-9 7-15 7z"/>
</svg>
"""

# ---------- Auth (simple) ----------
PASSWORD = "AylaMarie@24"

if "authed" not in st.session_state:
    st.session_state.authed = False

def login_view():
    st.markdown(f'<div class="login-card">{LION_SVG}', unsafe_allow_html=True)
    st.markdown("<h2 style='text-align:center;'>AI Command Center</h2>", unsafe_allow_html=True)
    st.markdown("<div class='subtitle'>Gold & Black • Private</div>", unsafe_allow_html=True)
    pwd = st.text_input("Password", type="password", placeholder="Enter password")
    col1, col2 = st.columns([1,1])
    with col1:
        if st.button("Log in", use_container_width=True):
            if pwd == PASSWORD:
                st.session_state.authed = True
                st.rerun()
            else:
                st.error("Wrong password.")
    with col2:
        if st.button("Forgot?", use_container_width=True):
            st.info("Ask me to change the password anytime.")
    st.markdown("</div>", unsafe_allow_html=True)

def stat_card(title, value, help_text=""):
    with st.container():
        st.markdown(
            f"""
            <div style="background:#111114;border:1px solid #27272f;border-radius:14px;padding:16px;">
              <div style="color:#8b8b94;font-size:12px;">{help_text}</div>
              <div style="font-weight:800;font-size:24px;margin:2px 0 6px 0;">{value}</div>
              <div style="font-size:15px;">{title}</div>
            </div>
            """,
            unsafe_allow_html=True,
        )

# ---------- Main ----------
if not st.session_state.authed:
    login_view()
    st.stop()

st.sidebar.markdown("### Widgets")
widget = st.sidebar.radio(
    "Choose a widget",
    [
        "Overview",
        "Personal Credit Card",
        "Shopify Sales",
        "Stripe Payouts",
        "Bank Balances",
        "Price Tracker",
    ],
    label_visibility="collapsed",
)

st.markdown(LION_SVG, unsafe_allow_html=True)
st.title("AI Command Center")
st.caption(f"Signed in • {datetime.now().strftime('%b %d, %Y %I:%M %p')}")

if widget == "Overview":
    c1, c2, c3, c4 = st.columns(4)
    with c1: stat_card("Personal Credit Card", "$3,240", "30-day net spend")
    with c2: stat_card("Shopify Sales", "$1,980", "Today")
    with c3: stat_card("Stripe Payouts", "$7,420", "This week")
    with c4: stat_card("Bank Balances", "$85,210", "Total")
    st.write("Coming next: live connectors (Plaid, Stripe, Shopify) and web price tracking.")

elif widget == "Personal Credit Card":
    st.subheader("Personal Credit Card — last 30 days")
    st.write("Demo data. We’ll connect your real feed next.")

elif widget == "Shopify Sales":
    st.subheader("Shopify — Today")
    st.write("Demo data. Connect token later.")

elif widget == "Stripe Payouts":
    st.subheader("Stripe — This week")
    st.write("Demo data. Connect key later.")

elif widget == "Bank Balances":
    st.subheader("Bank Balances — Checking + Savings")
    st.write("Demo data. Connect Plaid later.")

elif widget == "Price Tracker":
    st.subheader("Price Tracker")
    st.write("Watching 34 items (demo). Auto updates coming.")
