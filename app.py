
"""
THE MOUNTAIN PATH — WORLD OF FINANCE
Primary Market Equity Pricing Model
Prof. V. Ravichandran | themountainpathacademy.com
"""

import streamlit as st
import pandas as pd
import numpy as np
import plotly.graph_objects as go
import plotly.express as px
from plotly.subplots import make_subplots

# ── Page config ──────────────────────────────────────────────────────────────
st.set_page_config(
    page_title="Primary Market Equity Pricing | The Mountain Path",
    page_icon="📈",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── CSS ───────────────────────────────────────────────────────────────────────
st.markdown("""
<style>
@import url('https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700;900&family=Source+Sans+3:wght@300;400;500;600&family=JetBrains+Mono:wght@400;500&display=swap');

/* ── Root variables ── */
:root {
    --dark-blue:   #003366;
    --mid-blue:    #004d80;
    --acc-blue:    #0066cc;
    --gold:        #FFD700;
    --dark-gold:   #B8860B;
    --light-blue:  #ADD8E6;
    --card-bg:     #0a1628;
    --card-bg2:    #112240;
    --body-bg:     #060f1e;
    --text:        #e6f1ff;
    --muted:       #8892b0;
    --green:       #28a745;
    --red:         #dc3545;
    --orange:      #fd7e14;
    --border:      rgba(0,51,102,0.6);
    --gold-border: rgba(255,215,0,0.35);
}

/* ── Global ── */
html, body, [class*="css"] {
    font-family: 'Source Sans 3', sans-serif;
    background-color: var(--body-bg);
    color: var(--text);
}
.stApp { background: linear-gradient(160deg, #060f1e 0%, #0a1628 40%, #0d1f38 100%); }
.block-container { padding: 1.5rem 2rem !important; max-width: 1400px; }

/* ── Sidebar ── */
[data-testid="stSidebar"] {
    background: linear-gradient(180deg, #001f3f 0%, #002b55 100%) !important;
    border-right: 2px solid var(--gold-border);
}
/* Sidebar text - do NOT use wildcard * which kills button icon colors */
[data-testid="stSidebar"] label { color: var(--text) !important; }
[data-testid="stSidebar"] p { color: var(--text) !important; }
[data-testid="stSidebar"] .stSelectbox label,
[data-testid="stSidebar"] .stSlider label,
[data-testid="stSidebar"] .stNumberInput label { color: var(--light-blue) !important; font-size: 0.82rem !important; font-weight: 600 !important; letter-spacing: 0.03em; }

/* ── Header ── */
.mp-hero {
    background: linear-gradient(135deg, var(--dark-blue) 0%, #001f3f 50%, #002b55 100%);
    border: 1.5px solid var(--gold-border);
    border-radius: 12px;
    padding: 1.8rem 2.2rem;
    margin-bottom: 1.5rem;
    position: relative;
    overflow: hidden;
}
.mp-hero::before {
    content: '';
    position: absolute; inset: 0;
    background: radial-gradient(ellipse at 80% 50%, rgba(255,215,0,0.06) 0%, transparent 60%);
    pointer-events: none;
}
.mp-brand {
    font-family: 'Playfair Display', serif;
    font-size: 0.75rem;
    font-weight: 700;
    letter-spacing: 0.2em;
    text-transform: uppercase;
    color: var(--gold);
    margin-bottom: 0.3rem;
}
.mp-title {
    font-family: 'Playfair Display', serif;
    font-size: 2rem;
    font-weight: 900;
    color: #ffffff;
    line-height: 1.15;
    margin: 0 0 0.4rem 0;
}
.mp-subtitle {
    color: var(--light-blue);
    font-size: 0.92rem;
    font-weight: 400;
    margin: 0;
}
.mp-url {
    font-size: 0.8rem;
    color: var(--gold);
    text-decoration: none;
    font-weight: 600;
}

/* ── Metric cards ── */
.metric-row { display: flex; gap: 1rem; margin-bottom: 1.2rem; flex-wrap: wrap; }
.metric-card {
    background: var(--card-bg2);
    border: 1px solid var(--border);
    border-radius: 10px;
    padding: 1rem 1.3rem;
    flex: 1; min-width: 160px;
    position: relative;
    overflow: hidden;
    transition: border-color 0.2s;
}
.metric-card:hover { border-color: rgba(255,215,0,0.5); }
.metric-card::after {
    content: '';
    position: absolute; top: 0; left: 0; right: 0; height: 3px;
    background: linear-gradient(90deg, var(--dark-blue), var(--gold));
}
.metric-label {
    font-size: 0.72rem; font-weight: 600;
    letter-spacing: 0.06em; text-transform: uppercase;
    color: var(--muted); margin-bottom: 0.4rem;
}
.metric-value {
    font-family: 'Playfair Display', serif;
    font-size: 1.55rem; font-weight: 700;
    color: var(--gold); line-height: 1;
}
.metric-sub { font-size: 0.78rem; color: var(--muted); margin-top: 0.2rem; }
.metric-card.green .metric-value { color: #4caf50; }
.metric-card.blue  .metric-value { color: var(--light-blue); }
.metric-card.red   .metric-value { color: #ef5350; }
.metric-card.white .metric-value { color: #ffffff; }

/* ── Section headers ── */
.section-header {
    font-family: 'Playfair Display', serif;
    font-size: 1.25rem; font-weight: 700;
    color: var(--gold);
    border-bottom: 1.5px solid var(--gold-border);
    padding-bottom: 0.5rem; margin: 1.5rem 0 1rem 0;
    letter-spacing: 0.02em;
}

/* ── Info / def boxes ── */
.def-box {
    background: linear-gradient(135deg, rgba(0,51,102,0.35), rgba(0,77,128,0.2));
    border: 1px solid rgba(173,216,230,0.3);
    border-left: 4px solid var(--light-blue);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--text);
    line-height: 1.7;
}
.example-box {
    background: linear-gradient(135deg, rgba(255,215,0,0.06), rgba(184,134,11,0.04));
    border: 1px solid rgba(255,215,0,0.25);
    border-left: 4px solid var(--gold);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--text);
    line-height: 1.7;
}
.insight-box {
    background: linear-gradient(135deg, rgba(0,102,204,0.15), rgba(0,77,128,0.1));
    border: 1px solid rgba(0,102,204,0.4);
    border-left: 4px solid var(--acc-blue);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--text);
    line-height: 1.7;
}
.formula-box {
    background: #0d1f38;
    border: 1px solid rgba(0,102,204,0.5);
    border-radius: 8px;
    padding: 1rem 1.4rem;
    margin-bottom: 1rem;
    font-family: 'JetBrains Mono', monospace;
    font-size: 0.88rem;
    color: #a8d8ff;
    line-height: 1.8;
}
.warn-box {
    background: rgba(220,53,69,0.08);
    border: 1px solid rgba(220,53,69,0.35);
    border-left: 4px solid var(--red);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--text);
    line-height: 1.7;
}
.success-box {
    background: rgba(40,167,69,0.08);
    border: 1px solid rgba(40,167,69,0.35);
    border-left: 4px solid var(--green);
    border-radius: 8px;
    padding: 1rem 1.2rem;
    margin-bottom: 1rem;
    font-size: 0.9rem;
    color: var(--text);
    line-height: 1.7;
}

/* ── Tables ── */
.stDataFrame { border-radius: 8px; overflow: hidden; }
[data-testid="stTable"] table { width: 100%; border-collapse: collapse; }
[data-testid="stTable"] th {
    background: var(--dark-blue) !important;
    color: white !important;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 0.8rem; font-weight: 600;
    padding: 0.6rem 0.8rem; text-transform: uppercase;
    letter-spacing: 0.05em;
}
[data-testid="stTable"] td {
    padding: 0.55rem 0.8rem;
    font-size: 0.88rem;
    border-bottom: 1px solid rgba(0,51,102,0.3);
    color: var(--text);
}

/* ── Tabs ── */
.stTabs [data-baseweb="tab-list"] {
    background: var(--card-bg2);
    border-radius: 10px 10px 0 0;
    border-bottom: 2px solid var(--gold-border);
    gap: 0.2rem; padding: 0.4rem 0.4rem 0;
}
.stTabs [data-baseweb="tab"] {
    background: transparent;
    color: var(--muted);
    border-radius: 8px 8px 0 0;
    font-family: 'Source Sans 3', sans-serif;
    font-size: 0.88rem; font-weight: 600;
    padding: 0.55rem 1.2rem;
    border: none;
    transition: all 0.2s;
}
.stTabs [data-baseweb="tab"]:hover { color: var(--light-blue); background: rgba(0,51,102,0.3); }
.stTabs [aria-selected="true"] {
    background: var(--dark-blue) !important;
    color: var(--gold) !important;
    border-bottom: 2px solid var(--gold) !important;
}
.stTabs [data-baseweb="tab-panel"] {
    background: var(--card-bg);
    border: 1px solid var(--border);
    border-top: none;
    border-radius: 0 0 10px 10px;
    padding: 1.5rem;
}

/* ── Slider, selectbox, number input ── */
.stSlider [data-testid="stSlider"] > div > div > div { background: var(--dark-blue) !important; }
.stSlider [data-testid="stSlider"] > div > div > div > div { background: var(--gold) !important; }

/* ── Number Input: complete restyle ── */
/* The wrapper div */
[data-testid="stNumberInput"] > div {
    display: flex !important;
    border: 1.5px solid rgba(255,215,0,0.35) !important;
    border-radius: 6px !important;
    overflow: hidden !important;
    background: #0d1f38 !important;
}
/* The text input field itself */
[data-testid="stNumberInput"] input {
    background: #0d1f38 !important;
    color: #e6f1ff !important;
    border: none !important;
    border-right: 1px solid rgba(255,215,0,0.2) !important;
    border-radius: 0 !important;
    flex: 1 !important;
    padding: 0.4rem 0.6rem !important;
    font-family: "JetBrains Mono", monospace !important;
    font-size: 0.95rem !important;
}
[data-testid="stTextInput"] input {
    background: #0d1f38 !important;
    color: #e6f1ff !important;
    border: 1.5px solid rgba(255,215,0,0.35) !important;
    border-radius: 6px !important;
}
/* BOTH stepper buttons — nuclear approach covering all Streamlit versions */
[data-testid="stNumberInput"] button,
[data-testid="stNumberInput"] > div > button,
[data-testid="stNumberInputStepDown"],
[data-testid="stNumberInputStepUp"],
div[data-testid="stNumberInput"] button:first-of-type,
div[data-testid="stNumberInput"] button:last-of-type,
div[data-testid="stNumberInput"] button:nth-of-type(1),
div[data-testid="stNumberInput"] button:nth-of-type(2) {
    background: #1a3a6b !important;
    color: #FFD700 !important;
    border: none !important;
    border-left: 1px solid rgba(255,215,0,0.2) !important;
    border-radius: 0 !important;
    min-width: 34px !important;
    width: 34px !important;
    padding: 0 !important;
    cursor: pointer !important;
    display: flex !important;
    align-items: center !important;
    justify-content: center !important;
    transition: background 0.15s, color 0.15s !important;
    flex-shrink: 0 !important;
}
[data-testid="stNumberInput"] button:hover,
[data-testid="stNumberInput"] > div > button:hover,
[data-testid="stNumberInputStepDown"]:hover,
[data-testid="stNumberInputStepUp"]:hover {
    background: #0055b3 !important;
    color: #ffffff !important;
}
/* Force all SVG/icon content inside buttons to gold */
[data-testid="stNumberInput"] button *,
[data-testid="stNumberInputStepDown"] *,
[data-testid="stNumberInputStepUp"] * {
    color: #FFD700 !important;
    fill: #FFD700 !important;
    stroke: #FFD700 !important;
}
[data-testid="stNumberInput"] button:hover * {
    color: #ffffff !important;
    fill: #ffffff !important;
    stroke: #ffffff !important;
}

.stSelectbox > div > div {
    background: var(--card-bg2) !important;
    color: var(--text) !important;
    border: 1px solid var(--border) !important;
}

/* ── Buttons ── */
.stButton > button {
    background: linear-gradient(135deg, var(--dark-blue), var(--mid-blue)) !important;
    color: var(--gold) !important;
    border: 1.5px solid var(--gold-border) !important;
    border-radius: 8px !important;
    font-family: 'Source Sans 3', sans-serif !important;
    font-weight: 700 !important;
    font-size: 0.88rem !important;
    letter-spacing: 0.04em;
    padding: 0.5rem 1.5rem !important;
    transition: all 0.2s !important;
}
.stButton > button:hover {
    background: linear-gradient(135deg, var(--mid-blue), var(--acc-blue)) !important;
    border-color: var(--gold) !important;
    box-shadow: 0 4px 16px rgba(255,215,0,0.2) !important;
}

/* ── Dividers ── */
hr { border-color: var(--gold-border) !important; margin: 1.2rem 0; }

/* ── Footer ── */
.mp-footer {
    background: linear-gradient(90deg, var(--dark-blue), #001f3f);
    border: 1px solid var(--gold-border);
    border-radius: 10px;
    padding: 1.2rem 1.8rem;
    margin-top: 2rem;
    display: flex;
    justify-content: space-between;
    align-items: center;
    flex-wrap: wrap;
    gap: 0.8rem;
}
.footer-brand {
    font-family: 'Playfair Display', serif;
    font-size: 1rem; font-weight: 700;
    color: var(--gold);
}
.footer-links a {
    color: var(--light-blue);
    text-decoration: none;
    font-size: 0.82rem;
    margin-left: 1rem;
    font-weight: 500;
}
.footer-links a:hover { color: var(--gold); }
.footer-prof { font-size: 0.82rem; color: var(--muted); }

/* ── Tag pills ── */
.pill {
    display: inline-block;
    background: rgba(0,51,102,0.5);
    border: 1px solid rgba(173,216,230,0.3);
    border-radius: 20px;
    padding: 0.15rem 0.7rem;
    font-size: 0.75rem;
    color: var(--light-blue);
    margin: 0.15rem;
    font-weight: 600;
}

/* ── Cut-off highlight row ── */
.cutoff-row { background: rgba(255,215,0,0.12) !important; font-weight: 700; }

/* ── Expandable ── */
details summary {
    color: var(--light-blue);
    font-weight: 600;
    cursor: pointer;
    font-size: 0.9rem;
    padding: 0.5rem;
    border-radius: 6px;
}
details summary:hover { color: var(--gold); }
details[open] summary { color: var(--gold); }

/* scrollbar */
::-webkit-scrollbar { width: 6px; }
::-webkit-scrollbar-track { background: var(--body-bg); }
::-webkit-scrollbar-thumb { background: var(--dark-blue); border-radius: 3px; }
::-webkit-scrollbar-thumb:hover { background: var(--gold); }
</style>
""", unsafe_allow_html=True)

# ── JavaScript injection: guarantee number input button visibility ──────────
# CSS alone can be defeated by Streamlit's scoped styles; JS is bulletproof
st.components.v1.html("""
<script>
(function fixNumberInputButtons() {
    function applyFix() {
        // Find ALL number input button elements in the sidebar and main area
        const allBtns = document.querySelectorAll(
            '[data-testid="stNumberInput"] button, ' +
            '[data-testid="stNumberInputStepDown"], ' +
            '[data-testid="stNumberInputStepUp"]'
        );
        allBtns.forEach(function(btn) {
            btn.style.setProperty('background', '#1a3a6b', 'important');
            btn.style.setProperty('color', '#FFD700', 'important');
            btn.style.setProperty('border-left', '1px solid rgba(255,215,0,0.3)', 'important');
            btn.style.setProperty('min-width', '34px', 'important');
            btn.style.setProperty('width', '34px', 'important');
            btn.style.setProperty('display', 'flex', 'important');
            btn.style.setProperty('align-items', 'center', 'important');
            btn.style.setProperty('justify-content', 'center', 'important');
            btn.style.setProperty('cursor', 'pointer', 'important');
            btn.style.setProperty('border-radius', '0', 'important');
            btn.style.setProperty('border-top', 'none', 'important');
            btn.style.setProperty('border-bottom', 'none', 'important');
            btn.style.setProperty('border-right', 'none', 'important');
            // Fix all child SVGs and spans
            btn.querySelectorAll('svg, path, polyline, line, circle').forEach(function(el) {
                el.style.setProperty('fill', '#FFD700', 'important');
                el.style.setProperty('stroke', '#FFD700', 'important');
                el.style.setProperty('color', '#FFD700', 'important');
            });
            // Hover effect
            btn.addEventListener('mouseenter', function() {
                this.style.setProperty('background', '#0055b3', 'important');
                this.querySelectorAll('svg, path, polyline, line, circle').forEach(function(el) {
                    el.style.setProperty('fill', '#ffffff', 'important');
                    el.style.setProperty('stroke', '#ffffff', 'important');
                });
            });
            btn.addEventListener('mouseleave', function() {
                this.style.setProperty('background', '#1a3a6b', 'important');
                this.querySelectorAll('svg, path, polyline, line, circle').forEach(function(el) {
                    el.style.setProperty('fill', '#FFD700', 'important');
                    el.style.setProperty('stroke', '#FFD700', 'important');
                });
            });
        });

        // Also fix the number input wrapper borders
        document.querySelectorAll('[data-testid="stNumberInput"] > div').forEach(function(wrap) {
            wrap.style.setProperty('border', '1.5px solid rgba(255,215,0,0.35)', 'important');
            wrap.style.setProperty('border-radius', '6px', 'important');
            wrap.style.setProperty('overflow', 'hidden', 'important');
            wrap.style.setProperty('display', 'flex', 'important');
        });
    }

    // Run immediately
    applyFix();

    // Re-run on any DOM changes (Streamlit re-renders widgets dynamically)
    const observer = new MutationObserver(function() { applyFix(); });
    observer.observe(document.body, { childList: true, subtree: true });

    // Also run after a short delay to catch late renders
    setTimeout(applyFix, 500);
    setTimeout(applyFix, 1500);
    setTimeout(applyFix, 3000);
})();
</script>
""", height=0)


# ── PLOTLY THEME ──────────────────────────────────────────────────────────────
PLOT_LAYOUT = dict(
    paper_bgcolor='rgba(0,0,0,0)',
    plot_bgcolor='rgba(10,22,40,0.6)',
    font=dict(family="Source Sans 3, sans-serif", color="#e6f1ff", size=12),
    title_font=dict(family="Playfair Display, serif", color="#FFD700", size=15),
    xaxis=dict(gridcolor='rgba(0,51,102,0.4)', zerolinecolor='rgba(0,51,102,0.4)',
               title_font_color="#8892b0", tickfont_color="#8892b0"),
    yaxis=dict(gridcolor='rgba(0,51,102,0.4)', zerolinecolor='rgba(0,51,102,0.4)',
               title_font_color="#8892b0", tickfont_color="#8892b0"),
    legend=dict(bgcolor='rgba(10,22,40,0.8)', bordercolor='rgba(0,51,102,0.5)',
                borderwidth=1, font_color="#e6f1ff"),
    margin=dict(l=50, r=30, t=60, b=50),
)

COLORS = {
    'dark_blue': '#003366', 'mid_blue': '#004d80', 'acc_blue': '#0066cc',
    'gold': '#FFD700', 'light_blue': '#ADD8E6', 'green': '#28a745',
    'red': '#dc3545', 'orange': '#fd7e14', 'muted': '#8892b0',
}


# ── HERO HEADER ───────────────────────────────────────────────────────────────
st.markdown("""
<div class="mp-hero">
  <div class="mp-brand">⛰ The Mountain Path · World of Finance</div>
  <div class="mp-title">Primary Market Equity Pricing</div>
  <div class="mp-subtitle">
    Interactive IPO Pricing Model &nbsp;·&nbsp; Book Building &amp; Fixed Price Analysis
    &nbsp;·&nbsp; <a class="mp-url" href="https://themountainpathacademy.com/" target="_blank">themountainpathacademy.com</a>
  </div>
</div>
""", unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# SIDEBAR — INPUTS
# ══════════════════════════════════════════════════════════════════════════════
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:0.8rem 0 1rem;">
      <div style="font-family:'Playfair Display',serif; font-size:1rem; font-weight:700; color:#FFD700;">⛰ Mountain Path</div>
      <div style="font-size:0.72rem; color:#ADD8E6; letter-spacing:0.08em; text-transform:uppercase;">IPO Pricing Engine</div>
    </div>
    <hr style="border-color:rgba(255,215,0,0.25); margin:0 0 1rem 0;">
    """, unsafe_allow_html=True)

    st.markdown('<div style="font-size:0.78rem; font-weight:700; color:#FFD700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;">Currency</div>', unsafe_allow_html=True)
    currency_options = {
        "₹ INR — Indian Rupee":   ("₹", "INR", "Cr",  1e7,  1e5),
        "$ USD — US Dollar":       ("$", "USD", "M",   1e6,  1e3),
        "£ GBP — British Pound":   ("£", "GBP", "M",   1e6,  1e3),
        "€ EUR — Euro":            ("€", "EUR", "M",   1e6,  1e3),
        "¥ JPY — Japanese Yen":    ("¥", "JPY", "M",   1e6,  1e3),
        "AED — UAE Dirham":        ("AED", "AED", "M", 1e6,  1e3),
        "SGD — Singapore Dollar":  ("SGD", "SGD", "M", 1e6,  1e3),
    }
    currency_choice = st.selectbox("Select Currency", list(currency_options.keys()), index=0)
    curr_sym, curr_code, curr_large_suffix, curr_large_div, curr_small_div = currency_options[currency_choice]

    st.markdown('<hr style="border-color:rgba(0,51,102,0.5); margin:0.6rem 0 0.8rem 0;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.78rem; font-weight:700; color:#FFD700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;">Company Details</div>', unsafe_allow_html=True)
    company_name = st.text_input("Company Name", value="ABC Technologies Ltd.")
    pre_ipo_shares = st.number_input("Pre-IPO Shares Outstanding", value=100_000_000, step=1_000_000, format="%d")
    ipo_shares     = st.number_input("Shares Offered in IPO", value=25_000_000, step=500_000, format="%d")
    face_value     = st.number_input(f"Face Value per Share ({curr_sym})", value=10.0, step=1.0)

    st.markdown('<hr style="border-color:rgba(0,51,102,0.5); margin:1rem 0;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.78rem; font-weight:700; color:#FFD700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;">Book Building</div>', unsafe_allow_html=True)
    floor_price = st.number_input(f"Floor Price ({curr_sym})", value=250.0, step=5.0)
    cap_price   = st.number_input(f"Cap Price ({curr_sym})", value=300.0, step=5.0)

    st.markdown('<hr style="border-color:rgba(0,51,102,0.5); margin:1rem 0;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.78rem; font-weight:700; color:#FFD700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;">Fixed Price</div>', unsafe_allow_html=True)
    fixed_price = st.number_input(f"Fixed Offer Price ({curr_sym})", value=275.0, step=5.0)

    st.markdown('<hr style="border-color:rgba(0,51,102,0.5); margin:1rem 0;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.78rem; font-weight:700; color:#FFD700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;">Issuance Costs</div>', unsafe_allow_html=True)
    underwriting_pct  = st.slider("Underwriting Fee (%)", 0.5, 10.0, 5.0, 0.25)
    legal_cost        = st.number_input(f"Legal & Regulatory ({curr_sym})", value=2_500_000, step=100_000, format="%d")
    marketing_cost    = st.number_input(f"Marketing & Roadshow ({curr_sym})", value=1_500_000, step=100_000, format="%d")
    listing_fee       = st.number_input(f"Listing Fees ({curr_sym})", value=500_000, step=50_000, format="%d")

    st.markdown('<hr style="border-color:rgba(0,51,102,0.5); margin:1rem 0;">', unsafe_allow_html=True)
    st.markdown('<div style="font-size:0.78rem; font-weight:700; color:#FFD700; letter-spacing:0.1em; text-transform:uppercase; margin-bottom:0.6rem;">Investor Allocation (%)</div>', unsafe_allow_html=True)
    qib_pct  = st.slider("QIB Reservation %", 10, 75, 50)
    nii_pct  = st.slider("NII Reservation %", 5, 40, 15)
    rii_pct  = 100 - qib_pct - nii_pct
    st.markdown(f'<div style="font-size:0.85rem; color:#ADD8E6; padding:0.3rem 0.5rem; background:rgba(0,51,102,0.3); border-radius:5px;">RII Auto = <b style="color:#FFD700">{rii_pct}%</b></div>', unsafe_allow_html=True)

    st.markdown('<hr style="border-color:rgba(0,51,102,0.5); margin:1rem 0;">', unsafe_allow_html=True)
    st.markdown("""
    <div style="text-align:center; font-size:0.78rem; color:#8892b0; padding-top:0.5rem;">
        <a href="https://www.linkedin.com/in/trichyravis" style="color:#FFD700; text-decoration:none; font-weight:600;" target="_blank">LinkedIn</a>
        &nbsp;·&nbsp;
        <a href="https://github.com/trichyravis" style="color:#FFD700; text-decoration:none; font-weight:600;" target="_blank">GitHub</a>
    </div>
    <div style="text-align:center; font-size:0.7rem; color:#8892b0; margin-top:0.4rem;">Prof. V. Ravichandran</div>
    """, unsafe_allow_html=True)


# ══════════════════════════════════════════════════════════════════════════════
# CORE COMPUTATIONS
# ══════════════════════════════════════════════════════════════════════════════

# ── Demand schedule (auto-generated realistically within price band) ─────────
def generate_demand_schedule(floor, cap, ipo_shares_count):
    step     = max(1.0, (cap - floor) / 9)
    prices   = [round(cap - i * step, 2) for i in range(10)]
    # bell-curve style demand: peaks around midpoint
    mid      = (floor + cap) / 2
    bids_raw = [max(200, int(2200 * np.exp(-0.8 * ((p - mid) / (cap - floor) * 4)**2))) for p in prices]
    shr_raw  = [max(3000, int(16000 * np.exp(-0.6 * ((p - mid) / (cap - floor) * 3.5)**2))) for p in prices]
    rows = []
    cumulative = 0
    for i, (p, b, s) in enumerate(zip(prices, bids_raw, shr_raw)):
        total_dem = b * s
        cumulative += total_dem
        rows.append({
            'Bid Price':       p,
            'No. of Bids':     b,
            'Shares per Bid':  s,
            'Total Demanded':  total_dem,
            'Cumulative Demand': cumulative,
            '% of Offered':    round(cumulative / ipo_shares_count * 100, 2),
            'Demand Multiple': round(cumulative / ipo_shares_count, 3),
        })
    return pd.DataFrame(rows)

demand_df = generate_demand_schedule(floor_price, cap_price, ipo_shares)

# ── Cut-off price ─────────────────────────────────────────────────────────────
cutoff_rows = demand_df[demand_df['Cumulative Demand'] >= ipo_shares]
if len(cutoff_rows) == 0:
    cutoff_idx   = len(demand_df) - 1
    cutoff_price = demand_df.iloc[-1]['Bid Price']
else:
    cutoff_idx   = cutoff_rows.index[0]
    cutoff_price = demand_df.loc[cutoff_idx, 'Bid Price']

# ── WABP ──────────────────────────────────────────────────────────────────────
wabp = np.dot(demand_df['Bid Price'], demand_df['Total Demanded']) / demand_df['Total Demanded'].sum()

total_demand_bb    = demand_df['Total Demanded'].sum()
overall_sub_bb     = total_demand_bb / ipo_shares
total_bidders_bb   = demand_df['No. of Bids'].sum()

# ── Allocation (Book Building) ─────────────────────────────────────────────────
def compute_allocation_bb(ipo_sh, qp, np_, rp, cutoff_p, wabp_price):
    cats = ['QIB', 'NII', 'RII']
    pcts = [qp/100, np_/100, rp/100]
    # demand set to approximate 2.5-3.5x per category
    demand_mult = [2.80, 2.40, 2.51]
    rows = []
    for cat, pct, dm in zip(cats, pcts, demand_mult):
        reserved = int(ipo_sh * pct)
        demanded = int(reserved * dm)
        sub_x    = round(demanded / reserved, 3) if reserved else 0
        allot_r  = round(min(1, reserved / demanded) * 100, 2) if demanded else 0
        rows.append({'Category': cat, 'Reservation %': f'{pct*100:.0f}%',
                     'Shares Reserved': reserved, 'Demand (Shares)': demanded,
                     'Subscription (x)': sub_x, 'Allotment Ratio': f'{allot_r:.2f}%'})
    rows.append({'Category': 'Employee', 'Reservation %': '0%',
                 'Shares Reserved': 0, 'Demand (Shares)': int(ipo_sh*0.06),
                 'Subscription (x)': '-', 'Allotment Ratio': '0.00%'})
    return pd.DataFrame(rows)

alloc_bb_df = compute_allocation_bb(ipo_shares, qib_pct, nii_pct, rii_pct, cutoff_price, wabp)

# ── Allocation (Fixed Price) ───────────────────────────────────────────────────
def compute_allocation_fp(ipo_sh, qp, np_, rp, offer_p):
    cats  = ['QIB', 'NII', 'RII', 'Employee']
    pcts  = [qp/100, np_/100, rp/100, 0]
    n_apps= [450, 1200, 8500, 350]
    dm    = [2.40, 2.00, 2.86, 0]
    rows  = []
    for cat, pct, n_app, d in zip(cats, pcts, n_apps, dm):
        reserved  = int(ipo_sh * pct)
        applied   = int(reserved * d) if reserved else int(ipo_sh * 0.048)
        sub_x     = round(applied / reserved, 3) if reserved else '-'
        allot_r   = round(min(1, reserved / applied) * 100, 2) if applied else 0
        amt_rcvd  = applied * offer_p
        allotted  = reserved
        refund    = (applied - allotted) * offer_p
        ref_pct   = round(refund / amt_rcvd * 100, 2) if amt_rcvd else 0
        rows.append({
            'Category': cat, 'Reservation %': f'{pct*100:.0f}%',
            'Shares Reserved': reserved, 'Applications': n_app,
            'Shares Applied': applied, 'Subscription (x)': sub_x,
            'Shares Allotted': allotted,
            'Allotment Ratio': f'{allot_r:.2f}%',
            'Refund Amount': refund,
            'Refund %': f'{ref_pct:.2f}%',
        })
    return pd.DataFrame(rows)

alloc_fp_df = compute_allocation_fp(ipo_shares, qib_pct, nii_pct, rii_pct, fixed_price)

# ── Proceeds ──────────────────────────────────────────────────────────────────
def calc_proceeds(shares, price, uw_pct, legal, mktg, listing):
    gross   = shares * price
    uw_fee  = gross * uw_pct / 100
    total_c = uw_fee + legal + mktg + listing
    net     = gross - total_c
    cost_r  = total_c / gross * 100
    return dict(gross=gross, uw_fee=uw_fee, legal=legal,
                mktg=mktg, listing=listing, total_cost=total_c,
                net=net, cost_pct=cost_r)

proc_bb = calc_proceeds(ipo_shares, cutoff_price, underwriting_pct, legal_cost, marketing_cost, listing_fee)
proc_fp = calc_proceeds(ipo_shares, fixed_price,  underwriting_pct, legal_cost, marketing_cost, listing_fee)

# ── Valuation ─────────────────────────────────────────────────────────────────
post_bb = pre_ipo_shares * cutoff_price
pre_bb  = post_bb - proc_bb['gross']
post_fp = pre_ipo_shares * fixed_price
pre_fp  = post_fp - proc_fp['gross']

share_prem_bb = cutoff_price - face_value
share_prem_fp = fixed_price  - face_value
prem_pct_bb   = (share_prem_bb / face_value) * 100
prem_pct_fp   = (share_prem_fp / face_value) * 100

# ── Refund analysis ───────────────────────────────────────────────────────────
total_app_money_fp = alloc_fp_df['Shares Applied'].sum() * fixed_price
total_refund_fp    = alloc_fp_df['Refund Amount'].sum()
refund_pct_fp      = (total_refund_fp / total_app_money_fp * 100) if total_app_money_fp else 0

total_sub_fp = alloc_fp_df[alloc_fp_df['Shares Applied'] > 0]['Shares Applied'].sum() / ipo_shares


# ══════════════════════════════════════════════════════════════════════════════
# TABS
# ══════════════════════════════════════════════════════════════════════════════
tabs = st.tabs([
    "📊 Dashboard",
    "📖 Book Building",
    "🏷️ Fixed Price",
    "⚖️ Comparison",
    "📐 Formulas",
    "📚 Learn",
])

# ─────────────────────────────────────────────────────────────────────────────
# TAB 1: DASHBOARD
# ─────────────────────────────────────────────────────────────────────────────
with tabs[0]:
    st.markdown('<div class="section-header">📊 Executive Summary Dashboard</div>', unsafe_allow_html=True)

    # ── Top metrics row ───────────────────────────────────────────────────────
    # ── Currency-aware format helpers ──────────────────────────────────────
    def fmt_m(v):
        """Format large monetary value using selected currency."""
        if curr_code == "INR":
            if abs(v) >= 1e7:
                return f"{curr_sym}{v/1e7:.2f}Cr"
            elif abs(v) >= 1e5:
                return f"{curr_sym}{v/1e5:.1f}L"
            else:
                return f"{curr_sym}{v:,.0f}"
        else:
            if abs(v) >= 1e9:
                return f"{curr_sym}{v/1e9:.2f}B"
            elif abs(v) >= 1e6:
                return f"{curr_sym}{v/1e6:.1f}M"
            else:
                return f"{curr_sym}{v:,.0f}"
    def fmt_n(v): return f"{v:,.0f}"
    def fmt_c(v): return f"{curr_sym}{v:,.2f}"          # price display
    def fmt_c0(v): return f"{curr_sym}{v:,.0f}"         # whole number price

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card">
        <div class="metric-label">BB Cut-Off Price</div>
        <div class="metric-value">{fmt_c0(cutoff_price)}</div>
        <div class="metric-sub">vs Floor {fmt_c0(floor_price)} / Cap {fmt_c0(cap_price)}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Fixed Offer Price</div>
        <div class="metric-value" style="color:#ADD8E6">{fmt_c0(fixed_price)}</div>
        <div class="metric-sub">Premium {fmt_c0(share_prem_fp)} ({prem_pct_fp:,.0f}% over FV)</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">BB Net Proceeds</div>
        <div class="metric-value">{fmt_m(proc_bb['net'])}</div>
        <div class="metric-sub">Gross: {fmt_m(proc_bb['gross'])}</div>
      </div>
      <div class="metric-card blue">
        <div class="metric-label">FP Net Proceeds</div>
        <div class="metric-value">{fmt_m(proc_fp['net'])}</div>
        <div class="metric-sub">Gross: {fmt_m(proc_fp['gross'])}</div>
      </div>
      <div class="metric-card white">
        <div class="metric-label">BB Oversubscription</div>
        <div class="metric-value">{overall_sub_bb:.2f}x</div>
        <div class="metric-sub">{fmt_n(total_demand_bb)} shares demanded</div>
      </div>
    </div>
    <div class="metric-row">
      <div class="metric-card">
        <div class="metric-label">BB Post-Money Cap</div>
        <div class="metric-value">{fmt_m(post_bb)}</div>
        <div class="metric-sub">Pre-money: {fmt_m(pre_bb)}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">FP Post-Money Cap</div>
        <div class="metric-value" style="color:#ADD8E6">{fmt_m(post_fp)}</div>
        <div class="metric-sub">Pre-money: {fmt_m(pre_fp)}</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">Proceeds Advantage (BB)</div>
        <div class="metric-value">+{fmt_m(proc_bb['net'] - proc_fp['net'])}</div>
        <div class="metric-sub">Book Building vs Fixed Price</div>
      </div>
      <div class="metric-card red">
        <div class="metric-label">FP Total Refund</div>
        <div class="metric-value">{fmt_m(total_refund_fp)}</div>
        <div class="metric-sub">{refund_pct_fp:.1f}% of application money</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Weighted Avg Bid</div>
        <div class="metric-value" style="color:#fd7e14">{fmt_c(wabp)}</div>
        <div class="metric-sub">vs Cut-off {fmt_c0(cutoff_price)}</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Charts ────────────────────────────────────────────────────────────────
    col1, col2 = st.columns(2)

    with col1:
        # Demand curve
        fig = go.Figure()
        fig.add_trace(go.Bar(
            x=demand_df['Total Demanded'], y=demand_df['Bid Price'],
            orientation='h',
            marker=dict(
                color=demand_df['Bid Price'],
                colorscale=[[0, '#003366'], [0.5, '#0066cc'], [1, '#FFD700']],
                showscale=False
            ),
            name='Demand per Level',
            hovertemplate=f'Price: {curr_sym}%{{y}}<br>Demand: %{{x:,.0f}}<extra></extra>'
        ))
        fig.add_vline(x=ipo_shares, line_dash='dash',
                      line_color='#FFD700', annotation_text=f'IPO Supply: {fmt_n(ipo_shares)}',
                      annotation_font_color='#FFD700')
        # highlight cutoff
        fig.add_hrect(y0=cutoff_price-0.5, y1=cutoff_price+0.5,
                      fillcolor='rgba(255,215,0,0.15)', line_color='#FFD700',
                      annotation_text=f'Cut-off {fmt_c0(cutoff_price)}', annotation_position='right',
                      annotation_font_color='#FFD700')
        fig.update_layout(**PLOT_LAYOUT,
            title='Demand at Each Bid Price Level',
            yaxis_title='Bid Price ($)', xaxis_title='Shares Demanded',
            height=320)
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        # Proceeds waterfall
        categories = ['Gross Proceeds', 'Underwriting Fee', 'Legal Costs',
                      'Marketing', 'Listing Fees', 'Net Proceeds']
        bb_vals = [proc_bb['gross'], -proc_bb['uw_fee'], -proc_bb['legal'],
                   -proc_bb['mktg'], -proc_bb['listing'], proc_bb['net']]
        fp_vals = [proc_fp['gross'], -proc_fp['uw_fee'], -proc_fp['legal'],
                   -proc_fp['mktg'], -proc_fp['listing'], proc_fp['net']]

        fig2 = go.Figure()
        fig2.add_trace(go.Bar(name='Book Building',
            x=categories, y=[v/1e6 for v in bb_vals],
            marker_color=['#0066cc','#dc3545','#dc3545','#dc3545','#dc3545','#28a745'],
            hovertemplate=f'%{{x}}: {curr_sym}%{{y:.1f}}M<extra>BB</extra>'))
        fig2.add_trace(go.Bar(name='Fixed Price',
            x=categories, y=[v/1e6 for v in fp_vals],
            marker_color=['rgba(0,102,204,0.45)','rgba(220,53,69,0.45)',
                          'rgba(220,53,69,0.45)','rgba(220,53,69,0.45)',
                          'rgba(220,53,69,0.45)','rgba(40,167,69,0.45)'],
            hovertemplate=f'%{{x}}: {curr_sym}%{{y:.1f}}M<extra>FP</extra>'))
        fig2.update_layout(**PLOT_LAYOUT,
            title=f"Proceeds Comparison ({curr_sym}M)",
            yaxis_title=f"Amount ({curr_sym}M)", barmode='group', height=320)
        st.plotly_chart(fig2, use_container_width=True)

    # ── Subscription chart ────────────────────────────────────────────────────
    col3, col4 = st.columns(2)

    with col3:
        # Cumulative demand vs price
        fig3 = go.Figure()
        fig3.add_trace(go.Scatter(
            x=demand_df['Bid Price'], y=demand_df['Cumulative Demand'],
            mode='lines+markers',
            line=dict(color='#ADD8E6', width=2.5),
            marker=dict(color='#ADD8E6', size=8),
            fill='tozeroy', fillcolor='rgba(173,216,230,0.07)',
            name='Cumulative Demand',
            hovertemplate=f'Price: {curr_sym}%{{x}}<br>Cum. Demand: %{{y:,.0f}}<extra></extra>'
        ))
        fig3.add_hline(y=ipo_shares, line_dash='dash', line_color='#FFD700',
                       annotation_text=f'IPO Supply', annotation_font_color='#FFD700')
        fig3.add_vline(x=cutoff_price, line_dash='dot', line_color='#FFD700',
                       annotation_text=f'Cut-off {fmt_c0(cutoff_price)}', annotation_font_color='#FFD700')
        fig3.update_layout(**PLOT_LAYOUT,
            title='Cumulative Demand Curve (Book Building)',
            xaxis_title='Bid Price ($)', yaxis_title='Cumulative Demand',
            height=300)
        st.plotly_chart(fig3, use_container_width=True)

    with col4:
        # Valuation comparison
        val_cats = ['Pre-Money\nValuation', 'Gross\nProceeds', 'Post-Money\nMarket Cap']
        bb_vals2 = [pre_bb/1e9, proc_bb['gross']/1e9, post_bb/1e9]
        fp_vals2 = [pre_fp/1e9, proc_fp['gross']/1e9, post_fp/1e9]

        fig4 = go.Figure()
        fig4.add_trace(go.Bar(name='Book Building', x=val_cats, y=bb_vals2,
                               marker_color='#003366',
                               marker_line=dict(color='#FFD700', width=1.5),
                               hovertemplate=f'%{{x}}: {curr_sym}%{{y:.2f}}B<extra>BB</extra>'))
        fig4.add_trace(go.Bar(name='Fixed Price', x=val_cats, y=fp_vals2,
                               marker_color='rgba(0,51,102,0.4)',
                               marker_line=dict(color='#ADD8E6', width=1),
                               hovertemplate=f'%{{x}}: {curr_sym}%{{y:.2f}}B<extra>FP</extra>'))
        fig4.update_layout(**PLOT_LAYOUT,
            title=f"Valuation Metrics ({curr_sym}B)",
            yaxis_title=f"Amount ({curr_sym}B)", barmode='group', height=300)
        st.plotly_chart(fig4, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 2: BOOK BUILDING
# ─────────────────────────────────────────────────────────────────────────────
with tabs[1]:
    st.markdown('<div class="section-header">📖 Book Building Method — Deep Dive</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="def-box">
        <strong style="color:#ADD8E6">Book Building</strong> is a price discovery mechanism where the issuer sets a price band
        (<strong>{fmt_c0(floor_price)} – {fmt_c0(cap_price)}</strong>) and investors submit bids specifying price and quantity.
        The cut-off price is the highest price at which cumulative demand ≥ total shares offered
        (<strong>{fmt_n(ipo_shares)} shares</strong>).
    </div>
    """, unsafe_allow_html=True)

    st.markdown('<div class="section-header" style="font-size:1rem">📋 Demand Schedule</div>', unsafe_allow_html=True)

    # Style and display demand table
    def style_demand(df):
        display = df.copy()
        display['Bid Price']    = display['Bid Price'].apply(lambda x: f"{fmt_c(x)}")
        display['No. of Bids']  = display['No. of Bids'].apply(lambda x: f"{x:,.0f}")
        display['Shares per Bid']  = display['Shares per Bid'].apply(lambda x: f"{x:,.0f}")
        display['Total Demanded']  = display['Total Demanded'].apply(lambda x: f"{x:,.0f}")
        display['Cumulative Demand'] = display['Cumulative Demand'].apply(lambda x: f"{x:,.0f}")
        display['% of Offered']     = display['% of Offered'].apply(lambda x: f"{x:.2f}%")
        display['Demand Multiple']  = display['Demand Multiple'].apply(lambda x: f"{x:.3f}x")
        return display

    demand_display = style_demand(demand_df)

    def highlight_cutoff(row):
        # Use positional index directly — avoids parsing formatted currency strings
        row_pos = row.name  # pandas passes the index label, which equals integer position here
        if row_pos == cutoff_idx:
            return ['background-color: rgba(255,215,0,0.15); font-weight:bold; color:#FFD700'] * len(row)
        return [''] * len(row)

    st.dataframe(
        demand_display.style.apply(highlight_cutoff, axis=1),
        use_container_width=True, hide_index=True
    )

    st.markdown(f"""
    <div class="example-box">
        <strong>✦ Cut-Off Price = {fmt_c0(cutoff_price)}</strong> &nbsp;—&nbsp;
        First price (from top) where cumulative demand ({fmt_n(int(demand_df.loc[cutoff_idx,'Cumulative Demand']))} shares)
        ≥ IPO supply ({fmt_n(ipo_shares)} shares). All bids at or above {fmt_c0(cutoff_price)} receive allotment.
        <br><strong>Weighted Average Bid Price = {fmt_c(wabp)}</strong> &nbsp;—&nbsp;
        Cut-off > WABP confirms pricing at the <em>upper end of investor appetite</em>.
    </div>
    """, unsafe_allow_html=True)

    # ── Price discovery chart ──────────────────────────────────────────────────
    fig_bb = make_subplots(specs=[[{"secondary_y": True}]])
    fig_bb.add_trace(go.Bar(
        x=demand_df['Bid Price'], y=demand_df['Total Demanded'],
        name='Total Demanded', marker_color='#003366',
        marker_line=dict(color='#004d80', width=0.5),
        hovertemplate=f'{curr_sym}%{{x}}: %{{y:,.0f}} shares<extra></extra>'
    ), secondary_y=False)
    fig_bb.add_trace(go.Scatter(
        x=demand_df['Bid Price'], y=demand_df['Demand Multiple'],
        name='Demand Multiple', mode='lines+markers',
        line=dict(color='#FFD700', width=2.5),
        marker=dict(color='#FFD700', size=8),
        hovertemplate=f'{curr_sym}%{{x}}: %{{y:.2f}}x<extra></extra>'
    ), secondary_y=True)
    fig_bb.add_vline(x=cutoff_price, line_dash='dash', line_color='#ADD8E6',
                     annotation_text=f'Cut-off {fmt_c0(cutoff_price)}', annotation_font_color='#ADD8E6')
    fig_bb.add_vline(x=wabp, line_dash='dot', line_color='#fd7e14',
                     annotation_text=f'WABP {fmt_c(wabp)}', annotation_font_color='#fd7e14')
    fig_bb.update_layout(**PLOT_LAYOUT,
        title='Demand Distribution & Demand Multiple at Each Price Level',
        xaxis_title='Bid Price ($)', height=340)
    fig_bb.update_yaxes(title_text='Total Shares Demanded', secondary_y=False,
                        gridcolor='rgba(0,51,102,0.4)', tickfont_color='#8892b0')
    fig_bb.update_yaxes(title_text='Demand Multiple (x)', secondary_y=True,
                        gridcolor='rgba(0,0,0,0)', tickfont_color='#FFD700')
    st.plotly_chart(fig_bb, use_container_width=True)

    # ── Allocation ────────────────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">👥 Investor Category Allocation</div>', unsafe_allow_html=True)

    def fmt_alloc_bb(df):
        d = df.copy()
        d['Shares Reserved'] = d['Shares Reserved'].apply(lambda x: f"{x:,.0f}")
        d['Demand (Shares)'] = d['Demand (Shares)'].apply(lambda x: f"{x:,.0f}")
        return d

    st.dataframe(fmt_alloc_bb(alloc_bb_df), use_container_width=True, hide_index=True)

    # Subscription donut charts
    col_a, col_b, col_c = st.columns(3)
    cat_names = ['QIB', 'NII', 'RII']
    cat_cols  = [col_a, col_b, col_c]
    for cat, col in zip(cat_names, cat_cols):
        row = alloc_bb_df[alloc_bb_df['Category'] == cat].iloc[0]
        sub_x = row['Subscription (x)']
        allot = float(row['Allotment Ratio'].replace('%',''))
        with col:
            fig_d = go.Figure(go.Pie(
                values=[allot, 100 - allot],
                labels=['Allotted', 'Unallotted'],
                hole=0.65,
                marker_colors=['#FFD700', '#0a1628'],
                textinfo='none',
                hoverinfo='label+percent'
            ))
            fig_d.add_annotation(
                text=f"{allot:.1f}%",
                x=0.5, y=0.55, showarrow=False,
                font=dict(size=18, color='#FFD700', family='Playfair Display')
            )
            fig_d.add_annotation(
                text=cat,
                x=0.5, y=0.38, showarrow=False,
                font=dict(size=12, color='#ADD8E6')
            )
            fig_d.update_layout(
                paper_bgcolor='rgba(0,0,0,0)',
                plot_bgcolor='rgba(0,0,0,0)',
                showlegend=False, height=180,
                margin=dict(l=10, r=10, t=30, b=10),
                title=dict(text=f'{cat} Allotment ({sub_x}x sub)',
                           font=dict(size=11, color='#8892b0'), x=0.5)
            )
            st.plotly_chart(fig_d, use_container_width=True)

    # ── Proceeds ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">💰 IPO Proceeds Statement</div>', unsafe_allow_html=True)

    proc_rows = [
        ('Gross Proceeds', proc_bb['gross'], f"{fmt_n(ipo_shares)} × {fmt_c0(cutoff_price)}"),
        ('Less: Underwriting Fees', -proc_bb['uw_fee'], f"{underwriting_pct}% of Gross"),
        ('Less: Legal & Regulatory', -proc_bb['legal'], 'Fixed Cost'),
        ('Less: Marketing & Roadshow', -proc_bb['mktg'], 'Fixed Cost'),
        ('Less: Listing Fees', -proc_bb['listing'], 'Fixed Cost'),
        ('Total Issuance Costs', -proc_bb['total_cost'], f"{proc_bb['cost_pct']:.2f}% of Gross"),
        ('Net Proceeds to Company', proc_bb['net'], '★ Bottom Line'),
    ]
    proc_df_disp = pd.DataFrame(proc_rows, columns=['Item', f'Amount ({curr_sym})', 'Notes'])
    proc_df_disp['Amount ($)'] = proc_df_disp['Amount ($)'].apply(lambda x: f"{curr_sym}{x:,.0f}")
    st.dataframe(proc_df_disp, use_container_width=True, hide_index=True)

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card green">
        <div class="metric-label">Post-Money Market Cap</div>
        <div class="metric-value">{fmt_m(post_bb)}</div>
        <div class="metric-sub">{fmt_n(pre_ipo_shares)} shares × {fmt_c0(cutoff_price)}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Pre-Money Valuation</div>
        <div class="metric-value">{fmt_m(pre_bb)}</div>
        <div class="metric-sub">Post-Money − Gross Proceeds</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Share Premium</div>
        <div class="metric-value">{fmt_c0(share_prem_bb)}</div>
        <div class="metric-sub">{prem_pct_bb:,.0f}% over Face Value ({fmt_c0(face_value)})</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 3: FIXED PRICE
# ─────────────────────────────────────────────────────────────────────────────
with tabs[2]:
    st.markdown('<div class="section-header">🏷️ Fixed Price Method — Deep Dive</div>', unsafe_allow_html=True)

    st.markdown(f"""
    <div class="def-box">
        <strong style="color:#ADD8E6">Fixed Price Method</strong>: The issuer pre-determines a single, non-negotiable offer price
        of <strong>{fmt_c0(fixed_price)}</strong> before the issue opens. All investors apply at this price.
        No bidding, no price band — investors simply decide whether to subscribe at the stated price or not.
        The complete prospectus with the fixed price is filed prior to opening.
    </div>
    """, unsafe_allow_html=True)

    # ── Subscription analysis ──────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">📋 Subscription Analysis by Category</div>', unsafe_allow_html=True)

    sub_display = alloc_fp_df[['Category','Reservation %','Shares Reserved','Applications',
                                'Shares Applied','Subscription (x)','Shares Allotted',
                                'Allotment Ratio']].copy()
    for col_n in ['Shares Reserved','Shares Applied','Shares Allotted']:
        sub_display[col_n] = sub_display[col_n].apply(lambda x: f"{x:,.0f}")
    st.dataframe(sub_display, use_container_width=True, hide_index=True)

    # ── Refund analysis ────────────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">💸 Allotment & Refund Analysis</div>', unsafe_allow_html=True)

    refund_display = alloc_fp_df[['Category','Shares Applied','Shares Allotted',
                                   'Allotment Ratio','Refund Amount','Refund %']].copy()
    refund_display['Shares Applied']  = refund_display['Shares Applied'].apply(lambda x: f"{x:,.0f}")
    refund_display['Shares Allotted'] = refund_display['Shares Allotted'].apply(lambda x: f"{x:,.0f}")
    refund_display['Refund Amount']   = refund_display['Refund Amount'].apply(lambda x: f"{curr_sym}{x:,.0f}")
    st.dataframe(refund_display, use_container_width=True, hide_index=True)

    st.markdown(f"""
    <div class="warn-box">
        <strong>⚠ Refund Summary</strong><br>
        Total Application Money: <strong>{fmt_c0(total_app_money_fp)}</strong> &nbsp;|&nbsp;
        Total Refund: <strong>{fmt_c0(total_refund_fp)}</strong> &nbsp;|&nbsp;
        Refund Rate: <strong>{refund_pct_fp:.1f}%</strong> of application money locked up
        until ASBA deblocking. Under traditional (pre-ASBA) process, this represented a massive
        short-term capital constraint for applicants.
    </div>
    """, unsafe_allow_html=True)

    # ── Charts ────────────────────────────────────────────────────────────────
    col1, col2 = st.columns(2)
    with col1:
        # Subscription by category
        cats_fp = ['QIB', 'NII', 'RII']
        subs_fp = []
        for c in cats_fp:
            r = alloc_fp_df[alloc_fp_df['Category'] == c].iloc[0]
            s = r['Subscription (x)']
            subs_fp.append(float(s) if s != '-' else 0)

        fig_sub = go.Figure(go.Bar(
            x=cats_fp, y=subs_fp,
            marker=dict(
                color=subs_fp,
                colorscale=[[0,'#003366'],[0.5,'#0066cc'],[1,'#FFD700']],
                showscale=False,
                line=dict(color='#FFD700', width=1)
            ),
            text=[f'{s:.2f}x' for s in subs_fp], textposition='outside',
            textfont=dict(color='#FFD700', size=13),
            hovertemplate='%{x}: %{y:.2f}x oversubscribed<extra></extra>'
        ))
        fig_sub.add_hline(y=1.0, line_dash='dash', line_color='#ADD8E6',
                          annotation_text='1.0x = Fully Subscribed',
                          annotation_font_color='#ADD8E6')
        fig_sub.update_layout(**PLOT_LAYOUT,
            title='Subscription Multiple by Category (Fixed Price)',
            yaxis_title='Subscription (x)', height=320)
        st.plotly_chart(fig_sub, use_container_width=True)

    with col2:
        # Refund pie
        allot_val  = proc_fp['gross']
        refund_val = total_refund_fp

        fig_pie = go.Figure(go.Pie(
            values=[allot_val, refund_val],
            labels=['Capital Raised', 'Refunded'],
            hole=0.55,
            marker_colors=['#003366', '#dc3545'],
            marker_line=dict(color='#0a1628', width=2),
            textinfo='label+percent',
            hovertemplate=f'%{{label}}: {curr_sym}%{{value:,.0f}}<extra></extra>'
        ))
        fig_pie.add_annotation(
            text=f"{refund_pct_fp:.1f}%<br>refunded",
            x=0.5, y=0.5, showarrow=False,
            font=dict(size=14, color='#ef5350', family='Playfair Display')
        )
        fig_pie.update_layout(
            **PLOT_LAYOUT,
            title='Application Money: Raised vs Refunded',
            height=320,
            showlegend=True
        )
        st.plotly_chart(fig_pie, use_container_width=True)

    # ── Proceeds ──────────────────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">💰 IPO Proceeds Statement</div>', unsafe_allow_html=True)

    proc_rows_fp = [
        ('Gross Proceeds', proc_fp['gross'], f"{fmt_n(ipo_shares)} × {fmt_c0(fixed_price)}"),
        ('Less: Underwriting Fees', -proc_fp['uw_fee'], f"{underwriting_pct}% of Gross"),
        ('Less: Legal & Regulatory', -proc_fp['legal'], 'Fixed Cost'),
        ('Less: Marketing & Roadshow', -proc_fp['mktg'], 'Fixed Cost'),
        ('Less: Listing Fees', -proc_fp['listing'], 'Fixed Cost'),
        ('Total Issuance Costs', -proc_fp['total_cost'], f"{proc_fp['cost_pct']:.2f}% of Gross"),
        ('Net Proceeds to Company', proc_fp['net'], '★ Bottom Line'),
        ('Total Application Money', total_app_money_fp, 'Before allotment'),
        ('Total Refunds', -total_refund_fp, f"{refund_pct_fp:.2f}% of application money"),
    ]
    proc_df_fp_disp = pd.DataFrame(proc_rows_fp, columns=['Item', f'Amount ({curr_sym})', 'Notes'])
    proc_df_fp_disp['Amount ($)'] = proc_df_fp_disp['Amount ($)'].apply(lambda x: f"{curr_sym}{x:,.0f}")
    st.dataframe(proc_df_fp_disp, use_container_width=True, hide_index=True)

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card blue">
        <div class="metric-label">Post-Money Market Cap</div>
        <div class="metric-value">{fmt_m(post_fp)}</div>
        <div class="metric-sub">{fmt_n(pre_ipo_shares)} shares × {fmt_c0(fixed_price)}</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Pre-Money Valuation</div>
        <div class="metric-value">{fmt_m(pre_fp)}</div>
        <div class="metric-sub">Post-Money − Gross Proceeds</div>
      </div>
      <div class="metric-card">
        <div class="metric-label">Share Premium</div>
        <div class="metric-value">{fmt_c0(share_prem_fp)}</div>
        <div class="metric-sub">{prem_pct_fp:,.0f}% over Face Value</div>
      </div>
    </div>
    """, unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 4: COMPARISON
# ─────────────────────────────────────────────────────────────────────────────
with tabs[3]:
    st.markdown('<div class="section-header">⚖️ Book Building vs Fixed Price — Full Comparison</div>', unsafe_allow_html=True)

    diff_net   = proc_bb['net'] - proc_fp['net']
    diff_gross = proc_bb['gross'] - proc_fp['gross']
    diff_cap   = post_bb - post_fp
    diff_price = cutoff_price - fixed_price

    st.markdown(f"""
    <div class="metric-row">
      <div class="metric-card green">
        <div class="metric-label">Price Advantage (BB)</div>
        <div class="metric-value">+{fmt_c0(diff_price)}</div>
        <div class="metric-sub">Cut-off {fmt_c0(cutoff_price)} vs Fixed {fmt_c0(fixed_price)}</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">Gross Proceeds Advantage</div>
        <div class="metric-value">+{fmt_m(diff_gross)}</div>
        <div class="metric-sub">Book Building vs Fixed Price</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">Net Proceeds Advantage</div>
        <div class="metric-value">+{fmt_m(diff_net)}</div>
        <div class="metric-sub">After all issuance costs</div>
      </div>
      <div class="metric-card green">
        <div class="metric-label">Valuation Advantage</div>
        <div class="metric-value">+{fmt_m(diff_cap)}</div>
        <div class="metric-sub">Post-Money Market Cap delta</div>
      </div>
    </div>
    """, unsafe_allow_html=True)

    # ── Quantitative comparison table ─────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">📊 Quantitative Scorecard</div>', unsafe_allow_html=True)

    comp_data = {
        'Metric': [
            'Issue Price', 'Price Band / Fixed Price', 'Weighted Avg Bid Price',
            'Face Value', 'Share Premium', 'Premium %',
            '─── Demand ───', 'Total Shares Offered', 'Total Demand (Shares)',
            'Overall Subscription', 'Total Applicants/Bidders',
            '─── Proceeds ───', 'Gross Proceeds', 'Total Issuance Costs',
            'Net Proceeds', 'Cost as % of Gross',
            '─── Valuation ───', 'Post-Money Market Cap', 'Pre-Money Valuation',
        ],
        'Book Building': [
            fmt_c0(cutoff_price), f'{fmt_c0(floor_price)}–{fmt_c0(cap_price)}', fmt_c(wabp),
            fmt_c0(face_value), fmt_c0(share_prem_bb), f'{prem_pct_bb:,.0f}%',
            '', fmt_n(ipo_shares), fmt_n(int(total_demand_bb)),
            f'{overall_sub_bb:.2f}x', fmt_n(total_bidders_bb),
            '', fmt_m(proc_bb['gross']), fmt_m(proc_bb['total_cost']),
            fmt_m(proc_bb['net']), f"{proc_bb['cost_pct']:.2f}%",
            '', fmt_m(post_bb), fmt_m(pre_bb),
        ],
        'Fixed Price': [
            fmt_c0(fixed_price), f'Fixed @ {fmt_c0(fixed_price)}', '—',
            fmt_c0(face_value), fmt_c0(share_prem_fp), f'{prem_pct_fp:,.0f}%',
            '', fmt_n(ipo_shares), fmt_n(int(alloc_fp_df['Shares Applied'].sum())),
            f'{total_sub_fp:.2f}x', fmt_n(int(alloc_fp_df['Applications'].sum())),
            '', fmt_m(proc_fp['gross']), fmt_m(proc_fp['total_cost']),
            fmt_m(proc_fp['net']), f"{proc_fp['cost_pct']:.2f}%",
            '', fmt_m(post_fp), fmt_m(pre_fp),
        ],
    }
    comp_df = pd.DataFrame(comp_data)
    st.dataframe(comp_df, use_container_width=True, hide_index=True)

    # ── Qualitative comparison ─────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">🔍 Qualitative Assessment</div>', unsafe_allow_html=True)

    qual_data = {
        'Dimension': [
            'Price Discovery', 'Investor Flexibility', 'Price Efficiency',
            'Information Asymmetry', 'Time to Complete', 'Underpricing Risk',
            'Regulatory Complexity', 'Retail Friendliness', 'Best Suited For',
            'Refund Management', 'Issuer Proceeds',
        ],
        'Book Building': [
            'Market-driven via bids ✦', 'Bid any price in band ✦',
            'Reflects true demand ✦', 'Reduced via aggregation ✦',
            'Longer (3–5 days bidding)', 'Lower (demand-based) ✦',
            'Higher (RHP, norms)', 'Moderate (cut-off option)',
            'Large / institutional IPOs', 'Minimal (ASBA) ✦',
            'Generally higher ✦',
        ],
        'Fixed Price': [
            'Issuer-determined', 'Accept or reject only',
            'May under/overprice', 'Higher (no feedback)',
            'Shorter (fixed timeline) ✦', 'Higher (set blind)',
            'Lower (one prospectus) ✦', 'High — simple & clear ✦',
            'Small / retail-focused IPOs', 'Substantial refunds',
            'Generally lower',
        ],
    }
    qual_df = pd.DataFrame(qual_data)

    def color_qual(val):
        if '✦' in str(val):
            return 'color: #FFD700; font-weight: 600'
        return ''

    st.dataframe(qual_df.style.applymap(color_qual), use_container_width=True, hide_index=True)

    # ── Radar / spider chart ───────────────────────────────────────────────────
    col1, col2 = st.columns(2)
    with col1:
        categories_radar = ['Price Efficiency', 'Retail Access', 'Speed',
                             'Proceeds Max', 'Low Risk', 'Simplicity']
        bb_scores = [9, 6, 5, 9, 8, 5]
        fp_scores = [5, 9, 8, 5, 5, 9]

        fig_r = go.Figure()
        fig_r.add_trace(go.Scatterpolar(
            r=bb_scores + [bb_scores[0]],
            theta=categories_radar + [categories_radar[0]],
            fill='toself', fillcolor='rgba(0,51,102,0.35)',
            line=dict(color='#FFD700', width=2),
            name='Book Building'
        ))
        fig_r.add_trace(go.Scatterpolar(
            r=fp_scores + [fp_scores[0]],
            theta=categories_radar + [categories_radar[0]],
            fill='toself', fillcolor='rgba(173,216,230,0.15)',
            line=dict(color='#ADD8E6', width=2),
            name='Fixed Price'
        ))
        fig_r.update_layout(
            **PLOT_LAYOUT,
            polar=dict(
                bgcolor='rgba(10,22,40,0.6)',
                radialaxis=dict(visible=True, range=[0, 10],
                                gridcolor='rgba(0,51,102,0.4)',
                                tickfont_color='#8892b0'),
                angularaxis=dict(gridcolor='rgba(0,51,102,0.4)',
                                 tickfont_color='#e6f1ff')
            ),
            title='Method Strengths Radar (Score /10)',
            height=360,
        )
        st.plotly_chart(fig_r, use_container_width=True)

    with col2:
        # Net proceeds bar
        labels = ['BB\nGross', 'BB\nCosts', 'BB\nNet', 'FP\nGross', 'FP\nCosts', 'FP\nNet']
        values = [proc_bb['gross']/1e9, proc_bb['total_cost']/1e9, proc_bb['net']/1e9,
                  proc_fp['gross']/1e9, proc_fp['total_cost']/1e9, proc_fp['net']/1e9]
        colors_bar = ['#003366','#dc3545','#28a745','#004d80','rgba(220,53,69,0.6)','rgba(40,167,69,0.6)']

        fig_bar = go.Figure(go.Bar(
            x=labels, y=values,
            marker_color=colors_bar,
            marker_line=dict(color='rgba(255,255,255,0.1)', width=0.5),
            text=[f'{curr_sym}{v:.2f}B' for v in values],
            textposition='outside',
            textfont=dict(color='#e6f1ff', size=10),
            hovertemplate=f'%{{x}}: {curr_sym}%{{y:.3f}}B<extra></extra>'
        ))
        fig_bar.update_layout(**PLOT_LAYOUT,
            title='Proceeds Breakdown — Both Methods ($B)',
            yaxis_title=f"Amount ({curr_sym}B)", height=360)
        st.plotly_chart(fig_bar, use_container_width=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 5: FORMULAS
# ─────────────────────────────────────────────────────────────────────────────
with tabs[4]:
    st.markdown('<div class="section-header">📐 Master Formula Reference</div>', unsafe_allow_html=True)

    formulas = [
        ("1. Weighted Average Bid Price (WABP)",
         "WABP = Σ(Pᵢ × Qᵢ) ÷ Σ(Qᵢ)\nwhere Pᵢ = Bid Price, Qᵢ = Shares Demanded",
         f"Excel: =SUMPRODUCT(BidPrices, SharesDemanded) / SUM(SharesDemanded)\nResult: {fmt_c(wabp)}",
         "Volume-weighted average of investor bids — the 'centre of gravity' of demand"),

        ("2. Cut-Off Price (Algorithmic)",
         "P* = max(Pᵢ) such that Σ(Qⱼ for Pⱼ ≥ Pᵢ) ≥ Shares Offered\n(First price from top where cumulative demand ≥ IPO supply)",
         f"Excel: =INDEX(BidPrices, MATCH(1,(CumulativeDemand>=SharesOffered)*1,0))\nResult: {fmt_c0(cutoff_price)}",
         "Highest price at which the issue can be fully subscribed"),

        ("3. Subscription Multiple",
         "Overall:  Total Shares Demanded ÷ Total Shares Offered\nCategory: Shares Demanded in Category ÷ Shares Reserved",
         f"BB Overall: {fmt_n(int(total_demand_bb))} ÷ {fmt_n(ipo_shares)} = {overall_sub_bb:.2f}x\nFP Overall: {total_sub_fp:.2f}x",
         "Measures investor demand intensity; >1x = oversubscribed"),

        ("4. Allotment Ratio",
         "Allotment Ratio = MIN(1, Shares Reserved ÷ Shares Demanded)\nThe MIN caps at 100% — cannot allot more than demanded",
         "BB QIB: MIN(1, Reserved/Demanded)\nEach investor receives Allotment Ratio × Shares Applied",
         "Proportion of bid quantity each investor actually receives"),

        ("5. Gross Proceeds",
         "Gross Proceeds = Shares Offered × Issue Price",
         f"BB: {fmt_n(ipo_shares)} × {fmt_c0(cutoff_price)} = {fmt_m(proc_bb['gross'])}\nFP: {fmt_n(ipo_shares)} × {fmt_c0(fixed_price)} = {fmt_m(proc_fp['gross'])}",
         "Total cash raised before deducting issuance costs"),

        ("6. Net Proceeds",
         "Net Proceeds = Gross Proceeds − (UW Fees + Legal + Marketing + Listing)\nUW Fees = Gross Proceeds × Underwriting %",
         f"BB Net: {fmt_m(proc_bb['gross'])} − {fmt_m(proc_bb['total_cost'])} = {fmt_m(proc_bb['net'])}\nFP Net: {fmt_m(proc_fp['gross'])} − {fmt_m(proc_fp['total_cost'])} = {fmt_m(proc_fp['net'])}",
         "Actual cash available to the company after all flotation costs"),

        ("7. Post-Money Market Capitalization",
         "Post-Money Cap = Total Pre-IPO Shares Outstanding × Issue Price\n(Uses ALL shares, not just IPO shares)",
         f"BB: {fmt_n(pre_ipo_shares)} × {fmt_c0(cutoff_price)} = {fmt_m(post_bb)}\nFP: {fmt_n(pre_ipo_shares)} × {fmt_c0(fixed_price)} = {fmt_m(post_fp)}",
         "Market value of the entire company at IPO price"),

        ("8. Pre-Money Valuation",
         "Pre-Money = Post-Money Market Cap − Gross IPO Proceeds",
         f"BB: {fmt_m(post_bb)} − {fmt_m(proc_bb['gross'])} = {fmt_m(pre_bb)}\nFP: {fmt_m(post_fp)} − {fmt_m(proc_fp['gross'])} = {fmt_m(pre_fp)}",
         "Implied company value BEFORE new capital injection"),

        ("9. Share Premium",
         "Premium = Issue Price − Face Value\nPremium % = (Issue Price − Face Value) ÷ Face Value × 100",
         f"BB: {fmt_c0(cutoff_price)} − {fmt_c0(face_value)} = {fmt_c0(share_prem_bb)} ({prem_pct_bb:,.0f}%)\nFP: {fmt_c0(fixed_price)} − {fmt_c0(face_value)} = {fmt_c0(share_prem_fp)} ({prem_pct_fp:,.0f}%)",
         "Credited to Securities Premium Reserve on the balance sheet"),

        ("10. Refund Amount (Fixed Price)",
         "Refund = (Shares Applied − Shares Allotted) × Offer Price\nRefund % = Total Refund ÷ Total Application Money × 100",
         f"Total Refund: {fmt_m(total_refund_fp)}\nRefund Rate: {refund_pct_fp:.2f}%",
         "Capital temporarily locked during subscription period; returned via ASBA deblocking"),
    ]

    for title, formula_text, result_text, insight in formulas:
        with st.expander(f"📐 {title}", expanded=False):
            col1, col2 = st.columns([1.2, 1])
            with col1:
                st.markdown(f'<div class="formula-box">{formula_text}</div>', unsafe_allow_html=True)
            with col2:
                st.markdown(f'<div class="example-box"><strong style="color:#FFD700">Live Result:</strong><br>{result_text}</div>', unsafe_allow_html=True)
            st.markdown(f'<div class="insight-box">💡 <strong>Interpretation:</strong> {insight}</div>', unsafe_allow_html=True)


# ─────────────────────────────────────────────────────────────────────────────
# TAB 6: LEARN
# ─────────────────────────────────────────────────────────────────────────────
with tabs[5]:
    st.markdown('<div class="section-header">📚 Learning Guide — Primary Market Equity Pricing</div>', unsafe_allow_html=True)

    st.markdown("""
    <div class="def-box">
        <strong style="font-size:1rem; color:#FFD700">Why This Subject is Critical for Finance Professionals</strong><br><br>
        The <strong>Primary Market</strong> is where corporations are born as publicly traded entities —
        the crucible where private capital transforms into public wealth. IPO pricing is arguably the
        most consequential pricing event in a company's life. A mispriced IPO leaves money on the table
        (underpricing), destroys investor confidence (overpricing), or distorts capital allocation.
        <br><br>
        <strong>Who needs this knowledge:</strong>
        <span class="pill">Investment Bankers</span>
        <span class="pill">Equity Analysts</span>
        <span class="pill">Portfolio Managers</span>
        <span class="pill">CFOs & Treasurers</span>
        <span class="pill">CFA Candidates</span>
        <span class="pill">FRM Candidates</span>
        <span class="pill">MBA Finance Students</span>
    </div>
    """, unsafe_allow_html=True)

    # ── Q&A accordion ──────────────────────────────────────────────────────────
    qa_sections = {
        "🏦 Section 1: IPO Fundamentals": [
            ("What is an IPO?",
             "An Initial Public Offering (IPO) is the process by which a private company offers its equity shares to the public for the first time. The company lists on a recognised stock exchange, transforming from privately held to publicly traded. This enables capital raising from a broad investor base and creates a market-determined valuation."),
            ("What are the two primary IPO pricing methods?",
             "1. Book Building Method — price is discovered through a market-driven bidding process within a set price band. 2. Fixed Price Method — the issuer pre-determines a single, non-negotiable offer price using valuation models before the issue opens."),
            ("Who are the key participants in an IPO?",
             "Issuer (company going public), BRLM/Lead Manager (investment bank managing the process), Underwriter (guarantees subscription), Registrar (handles applications & allotment), SEBI/SEC (regulator), Stock Exchange (listing & bidding platform), Depositories NSDL/CDSL (electronic share credit)."),
            ("What is a price band?",
             "A price band is the range between the floor (minimum) and cap (maximum) price within which investors must bid. Under SEBI guidelines, the cap cannot exceed 120% of the floor. Example: ₹250–₹300. The cut-off price falls somewhere within or at the cap end of this band."),
        ],
        "📖 Section 2: Book Building": [
            ("How is the cut-off price determined?",
             "The cut-off price is found by analysing the demand schedule from highest to lowest bid price. Cumulative demand is computed at each level. The cut-off is the HIGHEST price at which cumulative demand ≥ total shares offered. All investors bidding at or above this price receive allotment."),
            ("What is the Weighted Average Bid Price (WABP)?",
             "WABP = Σ(Price × Shares Demanded) ÷ Σ(Shares Demanded). It represents the volume-weighted average of investor bids. When cut-off > WABP, the issue is priced at the upper end of actual demand, maximising proceeds. WABP is a useful sanity check on whether the cut-off is aggressive or conservative."),
            ("How does pro-rata allotment work?",
             "When a category is oversubscribed, allotment ratio = Shares Reserved ÷ Shares Demanded. Each investor receives this proportion of their bid quantity. Example: If QIB allotment ratio is 35.71%, an investor bidding for 1,000 shares receives 357 shares (rounded to lot size). The process is uniform within each category."),
            ("What is an Anchor Investor?",
             "Anchor investors are large institutional investors allotted up to 60% of the QIB portion ONE DAY before the IPO opens. Minimum application: ₹10 crore. They create a positive signal for the market and are subject to a 30-day lock-in (50%) and 90-day lock-in (50%) post-listing."),
        ],
        "🏷️ Section 3: Fixed Price Method": [
            ("How is the fixed price determined?",
             "The issuer and merchant banker use: P/E multiple (EPS × peer P/E), EV/EBITDA, DCF analysis (intrinsic equity value ÷ shares), precedent transactions, and P/B ratio. The price is set before any market feedback, making it inherently more uncertain than book building."),
            ("What happens when a fixed price IPO is oversubscribed?",
             "Allotment is pro-rata within each category: Shares Reserved ÷ Shares Applied. For extreme oversubscription in the RII category, SEBI may mandate lottery-based allotment (one lot per applicant first, then additional lots by lottery). Excess application money is refunded under ASBA deblocking."),
            ("Why are refunds significant in fixed price IPOs?",
             "Large refunds indicate: (1) Capital lock-up for 7–15 days, (2) Potential underpricing signal — heavy oversubscription means price was set too low, (3) Operational burden on registrar and banks. ASBA (Application Supported by Blocked Amount) mitigates this — funds are blocked not debited, so refund is simply a deblocking."),
            ("What is ASBA?",
             "ASBA (Application Supported by Blocked Amount) is a SEBI mechanism where the IPO application amount is blocked in the investor's account (not debited) until allotment. Only the allotted amount is debited post-allotment. Benefits: investor earns interest on blocked amount, eliminates traditional refund problem, reduces systemic banking risk."),
        ],
        "⚖️ Section 4: Comparison & Advanced Topics": [
            ("Which method yields higher proceeds?",
             "Book Building generally yields higher proceeds through market-driven price discovery that captures maximum investor willingness-to-pay. In a typical comparison, book building achieves a higher cut-off price than a comparable fixed price, directly translating to higher gross proceeds (Price × Shares). The cost ratios are nearly identical, so the net proceeds advantage mirrors the gross proceeds advantage."),
            ("What is IPO underpricing?",
             "Underpricing occurs when the IPO price is set below the stock's true market value, causing a significant first-day price jump. Key theories: Rock's Winner's Curse model (informed vs uninformed investors), Signaling theory (quality issuers underprice to signal), Bookbuilding theory (reward QIBs for revealing information). Fixed price IPOs historically show 15–35% average first-day returns vs 5–15% for book-built IPOs."),
            ("What is the Green Shoe Option?",
             "The Green Shoe (Over-Allotment) Option allows the lead manager to allot up to 15% additional shares beyond the original issue. Mechanics: Lead manager borrows promoter shares, over-allots to investors. Post-listing: if price falls, stabilising agent buys in secondary market to support price; if price rises, additional shares are issued. Net effect: price stabilisation in the first 30 days, protecting retail investors."),
            ("How does information asymmetry differ between the methods?",
             "Book Building reduces information asymmetry by: (1) requiring institutional investors to reveal true valuations through bids, (2) aggregating dispersed private information into a single market-clearing price, (3) allowing the issuer to gauge demand before finalising price. Fixed Price has no such mechanism — the issuer must guess the market-clearing price, resulting in higher expected underpricing or overpricing."),
        ],
    }

    for section_title, qa_list in qa_sections.items():
        st.markdown(f'<div class="section-header" style="font-size:1rem">{section_title}</div>', unsafe_allow_html=True)
        for q, a in qa_list:
            with st.expander(f"❓ {q}"):
                st.markdown(f'<div class="def-box">{a}</div>', unsafe_allow_html=True)

    # ── Key SEBI norms ─────────────────────────────────────────────────────────
    st.markdown('<div class="section-header" style="font-size:1rem">🏛️ SEBI Regulatory Framework (ICDR 2018)</div>', unsafe_allow_html=True)

    sebi_data = {
        'Regulation': [
            'Price Band Width', 'Bidding Period', 'Minimum Subscription',
            'Reservation (QIB)', 'Reservation (NII)', 'Reservation (RII)',
            'Anchor Investor', 'Lock-in (Anchor, 50%)', 'Lock-in (Anchor, 50%)',
            'ASBA Mandate', 'Allotment Timeline', 'Green Shoe Option',
        ],
        'Requirement': [
            'Cap ≤ 120% of Floor', '3–10 working days', '90% of total issue size',
            '50% of net issue', '15% of net issue', '35% of net issue',
            '≥₹10 Cr application; allotted 1 day before IPO opens', '30 days post-listing',
            '90 days post-listing', 'Mandatory for all retail applicants',
            'Within T+6 working days from issue close', 'Up to 15% of issue size',
        ],
        'Purpose': [
            'Limits excessive bid uncertainty', 'Adequate investor participation time',
            'Issue fails if below threshold', 'Institutional anchor',
            'HNI participation', 'Retail participation',
            'Market signal; price discovery', 'Prevents immediate flip',
            'Sustained holding incentive', 'Efficient capital blocking',
            'Timely settlement', 'Price stabilisation mechanism',
        ],
    }
    st.dataframe(pd.DataFrame(sebi_data), use_container_width=True, hide_index=True)


# ── FOOTER ────────────────────────────────────────────────────────────────────
st.markdown("""
<div class="mp-footer">
  <div>
    <div class="footer-brand">⛰ The Mountain Path — World of Finance</div>
    <div class="footer-prof">Prof. V. Ravichandran · 28+ Years Corporate Finance & Banking · 10+ Years Academic Excellence</div>
    <div class="footer-prof">Visiting Faculty: NMIMS Bangalore · BITS Pilani · RV University · Goa Institute of Management</div>
  </div>
  <div class="footer-links">
    <a href="https://themountainpathacademy.com/" target="_blank">🌐 Website</a>
    <a href="https://www.linkedin.com/in/trichyravis" target="_blank">💼 LinkedIn</a>
    <a href="https://github.com/trichyravis" target="_blank">🐙 GitHub</a>
  </div>
</div>
""", unsafe_allow_html=True)
