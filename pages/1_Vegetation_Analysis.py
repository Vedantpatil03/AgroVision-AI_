import streamlit as st
import tensorflow as tf
from PIL import Image
from utils.vegetation_utils import vegetation_percentage
import streamlit as st
from utils.ui_style import apply_global_style


apply_global_style()






st.title("🌿 Vegetation Analysis")

st.markdown("Upload a satellite or land image to analyze vegetation coverage.")

@st.cache_resource
def load_model():
    # Load TensorFlow SavedModel for Keras 3 compatibility
    return tf.saved_model.load("models/vegetation_saved_model")

model = load_model()

uploaded_file = st.file_uploader(
    "📤 Upload Image",
    type=["jpg", "png"]
)

if uploaded_file:
    image = Image.open(uploaded_file).convert("RGB")

    col1, col2 = st.columns([1.2, 1])

    with col1:
        st.image(image, caption="Uploaded Image", use_container_width=True)

    with st.spinner("Analyzing vegetation..."):
        veg, nonveg, _ = vegetation_percentage(model, image)

    with col2:
        st.markdown("### 📊 Vegetation Statistics")

        st.markdown(f"""
        <div class="metric-card">
            <h2>🌿 {veg}%</h2>
            <p>Vegetation Area</p>
        </div>
        """, unsafe_allow_html=True)

        st.markdown(f"""
        <div class="metric-card" style="margin-top:15px;">
            <h2>🏜️ {nonveg}%</h2>
            <p>Non-Vegetation Area</p>
        </div>
        """, unsafe_allow_html=True)
       

