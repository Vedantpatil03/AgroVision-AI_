import streamlit as st

def apply_global_style():
    st.markdown("""
    <style>

    /* App background */
    .stApp {
        background: linear-gradient(180deg, #0b0f19 0%, #0e1525 100%);
        color: #e6e6e6;
    }

    /* Sidebar */
    section[data-testid="stSidebar"] {
        background: #020617;
    }

    /* Sidebar links */
    section[data-testid="stSidebar"] a {
        font-size: 18px !important;
        font-weight: 800 !important;
        text-transform: uppercase;
        padding: 12px 14px !important;
        border-radius: 10px;
    }

    /* Hover */
    section[data-testid="stSidebar"] a:hover {
        background-color: rgba(34,197,94,0.18);
        transform: translateX(6px);
    }

    /* Active page */
    section[data-testid="stSidebar"] a[aria-current="page"] {
        background-color: rgba(34,197,94,0.28);
        border-left: 4px solid #22c55e;
    }

    footer {visibility: hidden;}
    #MainMenu {visibility: hidden;}

    </style>
    """, unsafe_allow_html=True)
