import streamlit as st

from utils.ui_style import apply_global_style
# ================== PAGE CONFIG ==================
st.set_page_config(
    page_title="AGROVISION – AI DRIVEN SOIL & VEGETATION ANALYSIS",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>

/* -------- App Background -------- */
.stApp {
    background: linear-gradient(180deg, #0b0f19 0%, #0e1525 100%);
    color: #e6e6e6;
}

/* -------- Section Heading -------- */
.section-title {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 25px;
}

/* -------- Card Style -------- */
.card {
    background-color: #ffffff;
    border-radius: 18px;
    padding: 26px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.35);
    height: 100%;
}

.card h3 {
    color: #111827 !important;
    font-weight: 800;
    font-size: 22px;
}

.card p {
    color: #374151 !important;
    font-size: 16px;
    line-height: 1.7;
}

/* ================= MOBILE RESPONSIVE ================= */
@media (max-width: 768px) {

    .section-title {
        font-size: 24px;
        text-align: center;
    }

    .card {
        padding: 18px;
        margin-bottom: 16px;
    }

    .card h3 {
        font-size: 20px;
    }

    .card p {
        font-size: 15px;
    }
}

</style>
""", unsafe_allow_html=True)


# ================== SIDEBAR + GLOBAL CSS ==================
st.markdown("""
<style>

/* -------- App Background -------- */
.stApp {
    background: linear-gradient(180deg, #0b0f19 0%, #0e1525 100%);
    color: #e6e6e6;
}

/* -------- Main Title -------- */
.main-title {
    text-align: center;
    font-size: 44px;
    font-weight: 900;
    letter-spacing: 2px;
    text-transform: uppercase;
    margin-top: 10px;
    margin-bottom: 10px;
}

/* -------- Subtitle -------- */
.subtitle {
    text-align: center;
    font-size: 20px;
    color: #cbd5f5;
    margin-bottom: 40px;
}

/* -------- Section Heading -------- */
.section-title {
    font-size: 28px;
    font-weight: 800;
    margin-bottom: 25px;
}

/* -------- Card Style -------- */
.card {
    background-color: #ffffff;
    border-radius: 18px;
    padding: 26px;
    box-shadow: 0 15px 35px rgba(0,0,0,0.35);
    height: 100%;
}

.card h3 {
    color: #111827 !important;
    font-weight: 800;
    font-size: 22px;
}

.card p {
    color: #374151 !important;
    font-size: 16px;
    line-height: 1.7;
}

/* -------- Info Banner -------- */
.info-banner {
    background: linear-gradient(90deg, #2563eb, #1d4ed8);
    color: white;
    padding: 18px;
    border-radius: 14px;
    text-align: center;
    font-size: 18px;
    font-weight: 600;
    margin-top: 45px;
}

/* -------- Sidebar Background -------- */
section[data-testid="stSidebar"] {
    background: #020617;
}

/* -------- Sidebar Navigation Text -------- */
section[data-testid="stSidebar"] a {
    font-size: 18px !important;
    font-weight: 800 !important;
    text-transform: uppercase;
    padding: 12px 14px !important;
    border-radius: 10px;
}

/* -------- Sidebar Hover -------- */
section[data-testid="stSidebar"] a:hover {
    background-color: rgba(34, 197, 94, 0.18);
    transform: translateX(6px);
}

/* -------- Active Sidebar Item -------- */
section[data-testid="stSidebar"] a[aria-current="page"] {
    background-color: rgba(34, 197, 94, 0.28);
    border-left: 4px solid #22c55e;
}

/* -------- Remove Footer -------- */
footer {visibility: hidden;}
#MainMenu {visibility: hidden;}

</style>
""", unsafe_allow_html=True)

# ================== MAIN CONTENT ==================

st.markdown(
    '<div class="main-title">AGROVISION – AI DRIVEN SOIL & VEGETATION ANALYSIS</div>',
    unsafe_allow_html=True
)

st.markdown(
    """
    <div class="subtitle">
    AgroVision AI is a deep learning–based analytical platform designed to evaluate
    <b>soil characteristics</b> and <b>vegetation patterns</b> for
    <b>precision agriculture</b> and <b>environmental monitoring</b>.
    </div>
    """,
    unsafe_allow_html=True
)

st.markdown(
    '<div class="section-title">🚀  CORE FUNCTIONALITIES</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="card">
        <h3>🌿 Vegetation Analysis</h3>
        <p>
        Upload satellite or land images to estimate vegetation and non-vegetation
        coverage using advanced semantic segmentation techniques.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="card">
        <h3>🌱 Soil Detection</h3>
        <p>
        Identify soil types such as <b>Alluvial, Black, Clay, and Red Soil</b>
        using YOLO-based object detection with confidence scoring.
        </p>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="card">
        <h3>📊 Intelligent Insights</h3>
        <p>
        Receive confidence levels, detected regions, and coverage percentages
        to support data-driven agricultural decisions.
        </p>
    </div>
    """, unsafe_allow_html=True)

st.markdown("""
<div class="info-banner">
➡ SELECT A MODULE FROM THE SIDEBAR TO BEGIN ANALYSIS
</div>
""", unsafe_allow_html=True)
