import streamlit as st
from PIL import Image
from utils.soil_utils import load_soil_model, predict_soil
import streamlit as st
from utils.ui_style import apply_global_style

apply_global_style()




# ---------------------------------------------------------
# Page config (important for layout consistency)
# ---------------------------------------------------------
st.set_page_config(
    page_title="Soil Detection",
    layout="wide"
)

# ---------------------------------------------------------
# Custom CSS (same visual language as Vegetation page)
# ---------------------------------------------------------
st.markdown("""
<style>
.main {
    background-color: #0e1117;
}

h1, h2, h3, h4, h5 {
    color: #ffffff;
}

p, span, div {
    color: #cfd8dc;
}

.stat-card {
    background: #161b22;
    padding: 22px;
    border-radius: 14px;
    margin-bottom: 18px;
    box-shadow: 0 0 0 1px rgba(255,255,255,0.04);
}

.stat-title {
    font-size: 15px;
    color: #9aa4ad;
}

.stat-value {
    font-size: 28px;
    font-weight: 700;
    margin-top: 6px;
}

.green {
    color: #3fb950;
}

.blue {
    color: #58a6ff;
}

.orange {
    color: #f0883e;
}

.red {
    color: #ff7b72;
}

.upload-box > div {
    background-color: #161b22 !important;
    border-radius: 12px !important;
    border: 1px dashed #30363d !important;
}
</style>
""", unsafe_allow_html=True)

# ---------------------------------------------------------
# Page Header
# ---------------------------------------------------------
st.markdown("## 🌱 Soil Detection")
st.markdown(
    "Upload a soil image to identify **soil type**, **confidence**, and **coverage** using AI."
)

# ---------------------------------------------------------
# Load model (cached)
# ---------------------------------------------------------
@st.cache_resource
def load_model():
    return load_soil_model()

model = load_model()

# ---------------------------------------------------------
# File uploader
# ---------------------------------------------------------
uploaded_file = st.file_uploader(
    "📤 Upload Soil Image",
    type=["jpg", "png", "jpeg"],
    label_visibility="visible"
)

# ---------------------------------------------------------
# Inference
# ---------------------------------------------------------
if uploaded_file:
    try:
        # Validate and open image
        image = Image.open(uploaded_file)
        
        # Verify image is valid
        image.verify()
        
        # Reopen image after verify (verify closes the file)
        uploaded_file.seek(0)
        image = Image.open(uploaded_file).convert("RGB")
        
        with st.spinner("Analyzing soil image..."):
            annotated_img, soil, conf, regions, coverage = predict_soil(model, image)
            
            # Check if prediction returned valid results
            if annotated_img is None:
                st.warning("⚠️ No soil detected or Invalid image. Please try another image.")
                st.stop()
            
            # Ensure annotated_img is a PIL Image before display
            if not isinstance(annotated_img, Image.Image):
                annotated_img = Image.fromarray(annotated_img.astype('uint8'))
        
        # Display results only if we have valid annotated image
        # Layout: Image (left) | Stats (right)
        col1, col2 = st.columns([1.6, 1])

        # LEFT: Image
        with col1:
            st.image(
                annotated_img,
                caption="Detected Soil Regions",
                use_container_width=True
            )

        # RIGHT: Statistics
        with col2:
            st.markdown("### 📊 Soil Statistics")

            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-title">Dominant Soil Type</div>
                <div class="stat-value green">{soil}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-title">Confidence Score</div>
                <div class="stat-value blue">{conf}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-title">Regions Detected</div>
                <div class="stat-value orange">{regions}</div>
            </div>
            """, unsafe_allow_html=True)

            st.markdown(f"""
            <div class="stat-card">
                <div class="stat-title">Soil Coverage</div>
                <div class="stat-value red">{coverage}%</div>
            </div>
            """, unsafe_allow_html=True)
    
    except Exception as e:
        st.error(f"❌ Invalid image file. Please upload a valid image (JPG, PNG, or JPEG).\n\nError: {str(e)}")

else:
    st.info("⬅️ Upload a soil image to begin analysis.")
