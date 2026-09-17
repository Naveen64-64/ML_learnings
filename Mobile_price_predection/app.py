from pathlib import Path

import streamlit as st
import pandas as pd
import joblib

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "model" / "model.pkl"


# =========================================================
# PAGE CONFIGURATION
# =========================================================

st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# =========================================================
# LOAD MODEL
# =========================================================

if not MODEL_PATH.exists():
    raise FileNotFoundError(f"Model file not found: {MODEL_PATH}")

model = joblib.load(MODEL_PATH)


# =========================================================
# CUSTOM CSS
# =========================================================

st.markdown(
    """
    <style>

    /* =====================================================
       MAIN PAGE
       ===================================================== */

    .stApp {
        background-color: #f5f7fb;
    }

    .block-container {
        max-width: 1180px;
        padding-top: 30px;
        padding-bottom: 30px;
    }


    /* =====================================================
       TITLE
       ===================================================== */

    h1 {
        text-align: center;
        color: #111827 !important;
        font-size: 40px !important;
        font-weight: 800 !important;
        margin-bottom: 5px !important;
    }

    .subtitle {
        text-align: center;
        color: #64748b;
        font-size: 15px;
        margin-bottom: 38px;
        font-weight: 500;
    }


    /* =====================================================
       SECTION HEADINGS
       ===================================================== */

    h2, h3 {
        color: #111827 !important;
    }

    .section-heading {
        color: #1011827;
        font-size: 20px;
        font-weight: 700;
        margin-bottom: 15px;
    }

    /* Input boxes similar to mockup */
    [data-testid="stNumberInput"] {
        margin-bottom: 18px;
    }

    [data-testid="stNumberInput"] > div {
        background: #1f2937;
        border-radius: 12px;
        border: none;
        height: 50px;
        box-shadow: none;
    }

    [data-testid="stNumberInput"] label {
        color: #000000 !important;
        font-size: 12px !important;
        font-weight: 600 !important;
        margin-bottom: 6px;
        display: block;
    }

    [data-testid="stNumberInput"] input {
        color: #f8fafc !important;
        font-size: 15px !important;
        font-weight: 600 !important;
        background: transparent !important;
        border: none !important;
        box-shadow: none !important;
    }

    [data-testid="stNumberInput"] small {
        color: #94a3b8 !important;
    }

    [data-testid="stNumberInput"] button {
        background: transparent !important;
        border: none !important;
        color: #f8fafc !important;
    }

    /* =====================================================
       PREDICT BUTTON
       ===================================================== */

    .stButton > button {
        width: 100%;
        height: 50px;
        background-color: #111827;
        color: white;
        border: none;
        border-radius: 12px;
        font-size: 15px;
        font-weight: 700;
        margin-top: 10px;
    }

    .stButton > button:hover {
        background-color: #1f2937;
        color: white;
    }


    /* =====================================================
       METRIC CARDS
       ===================================================== */

    div[data-testid="stMetric"] {
        background-color: #ffffff;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px;
        box-shadow: 0 3px 12px rgba(15, 23, 42, 0.04);
        min-height: 90px;
    }

    div[data-testid="stMetricLabel"] {
        color: #64748b !important;
        font-size: 12px !important;
        font-weight: 500 !important;
    }

    div[data-testid="stMetricValue"] {
        color: #111827 !important;
        font-size: 21px !important;
        font-weight: 750 !important;
    }

    .price-section div[data-testid="stMetric"] {
        background: #f3f4f6;
        border: 1px solid #e2e8f0;
        border-radius: 12px;
        padding: 18px 20px;
        text-align: center;
        box-shadow: none;
        min-height: 110px;
        display: flex;
        justify-content: center;
        align-items: center;
    }

    .price-section div[data-testid="stMetricLabel"] {
        color: #475569 !important;
        font-size: 14px !important;
        justify-content: center;
    }

    .price-section div[data-testid="stMetricValue"] {
        color: #111827 !important;
        font-size: 42px !important;
        font-weight: 800 !important;
        justify-content: center;
    }

    .price-section [data-testid="stCaptionContainer"] {
        text-align: center;
        color: #94a3b8 !important;
        margin-top: 5px;
    }


    /* =====================================================
       DIVIDER
       ===================================================== */

    hr {

        border-color: #e5e7eb !important;

        margin-top: 25px !important;

        margin-bottom: 25px !important;

    }


    /* =====================================================
       INFO MESSAGE
       ===================================================== */

    div[data-testid="stAlert"] {

        border-radius: 14px;

        border: 1px solid #e2e8f0;

    }


    /* =====================================================
       HIDE STREAMLIT BRANDING
       ===================================================== */

    #MainMenu {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# =========================================================
# HEADER
# =========================================================

st.title("Mobile Price Predictor")

st.markdown(
    """
    <div class="subtitle">
        Estimate a mobile phone price using Multiple Linear Regression
    </div>
    """,
    unsafe_allow_html=True
)


# =========================================================
# MAIN LAYOUT
# =========================================================

left_column, right_column = st.columns(
    [1, 1],
    gap="large"
)


# =========================================================
# LEFT COLUMN - INPUTS
# =========================================================

with left_column:

    st.markdown(
        '<div class="section-heading">Mobile Specifications</div>',
        unsafe_allow_html=True
    )

    with st.container(border=True):

        # -------------------------------------------------
        # RAM + STORAGE
        # -------------------------------------------------

        col1, col2 = st.columns(2)

        with col1:

            ram = st.number_input(
                "RAM (GB)",
                min_value=1.0,
                max_value=32.0,
                value=8.0,
                step=1.0,
                help="Memory capacity of the mobile phone"
            )

        with col2:

            storage = st.number_input(
                "Storage (GB)",
                min_value=16.0,
                max_value=1024.0,
                value=128.0,
                step=16.0,
                help="Internal storage capacity"
            )


        # -------------------------------------------------
        # BATTERY + CAMERA
        # -------------------------------------------------

        col3, col4 = st.columns(2)

        with col3:

            battery = st.number_input(
                "Battery (mAh)",
                min_value=1000.0,
                max_value=10000.0,
                value=5000.0,
                step=100.0,
                help="Battery capacity"
            )

        with col4:

            camera = st.number_input(
                "Camera (MP)",
                min_value=2.0,
                max_value=250.0,
                value=50.0,
                step=1.0,
                help="Main camera resolution"
            )


        # -------------------------------------------------
        # SCREEN + PROCESSOR
        # -------------------------------------------------

        col5, col6 = st.columns(2)

        with col5:

            screen_size = st.number_input(
                "Screen Size (inches)",
                min_value=4.0,
                max_value=8.0,
                value=6.5,
                step=0.1,
                help="Display size"
            )

        with col6:

            processor_speed = st.number_input(
                "Processor Speed (GHz)",
                min_value=1.0,
                max_value=5.0,
                value=2.8,
                step=0.1,
                help="CPU clock speed"
            )


    # -----------------------------------------------------
    # PREDICT BUTTON
    # -----------------------------------------------------

    predict_button = st.button(
        "Predict Mobile Price"
    )


# =========================================================
# RIGHT COLUMN - OUTPUT
# =========================================================

with right_column:

    st.markdown(
        '<div class="section-heading">Prediction Result</div>',
        unsafe_allow_html=True
    )

    if predict_button:
        new_mobile = pd.DataFrame({
            "ram": [ram],
            "storage": [storage],
            "battery": [battery],
            "camera": [camera],
            "screen_size": [screen_size],
            "processor_speed": [processor_speed]
        })

        prediction = model.predict(new_mobile)
        predicted_price = prediction[0]

        st.markdown('<div class="price-section">', unsafe_allow_html=True)
        st.metric(label="Estimated Mobile Price", value=f"₹{predicted_price:,.0f}")
        st.caption("Estimated using Multiple Linear Regression")
        st.markdown('</div>', unsafe_allow_html=True)

        st.divider()
        st.markdown("### Selected Specifications")

        spec1, spec2 = st.columns(2)
        with spec1:
            st.metric(label="RAM", value=f"{ram:.0f} GB")
        with spec2:
            st.metric(label="Storage", value=f"{storage:.0f} GB")

        spec3, spec4 = st.columns(2)
        with spec3:
            st.metric(label="Battery", value=f"{battery:.0f} mAh")
        with spec4:
            st.metric(label="Camera", value=f"{camera:.0f} MP")

        spec5, spec6 = st.columns(2)
        with spec5:
            st.metric(label="Screen Size", value=f"{screen_size:.1f} inches")
        with spec6:
            st.metric(label="Processor Speed", value=f"{processor_speed:.1f} GHz")

    else:
        st.markdown("### Ready to Predict")
        st.write("Enter the mobile specifications on the left and click **Predict Mobile Price**.")
        st.info("Your estimated mobile price will appear here.")


# =========================================================
# HOW IT WORKS
# =========================================================

st.markdown('<div class="section-heading" style="margin-top: 40px;">How It Works</div>', unsafe_allow_html=True)

step1, step2, step3 = st.columns(3)

with step1:
    st.markdown(
        """
        <div style="background: rgba(255,255,255,0.45); border: 1px solid #e5e7eb; border-radius: 16px; padding: 22px 18px; min-height: 180px; box-shadow: 0 5px 15px rgba(15, 23, 42, 0.03);">
            <h4 style="margin: 0 0 18px; color: #111827; font-size: 28px; font-weight: 700;">01. Enter Details</h4>
            <p style="margin: 0; color: #64748b; font-size: 18px; line-height: 1.6;">Provide RAM, storage, battery, camera, screen size and processor speed.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with step2:
    st.markdown(
        """
        <div style="background: rgba(255,255,255,0.45); border: 1px solid #e5e7eb; border-radius: 16px; padding: 22px 18px; min-height: 180px; box-shadow: 0 5px 15px rgba(15, 23, 42, 0.03);">
            <h4 style="margin: 0 0 18px; color: #111827; font-size: 28px; font-weight: 700;">02. ML Prediction</h4>
            <p style="margin: 0; color: #64748b; font-size: 18px; line-height: 1.6;">The trained Multiple Linear Regression model analyzes the specifications.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

with step3:
    st.markdown(
        """
        <div style="background: rgba(255,255,255,0.45); border: 1px solid #e5e7eb; border-radius: 16px; padding: 22px 18px; min-height: 180px; box-shadow: 0 5px 15px rgba(15, 23, 42, 0.03);">
            <h4 style="margin: 0 0 18px; color: #111827; font-size: 28px; font-weight: 700;">03. Get Price</h4>
            <p style="margin: 0; color: #64748b; font-size: 18px; line-height: 1.6;">The system displays the estimated mobile price instantly.</p>
        </div>
        """,
        unsafe_allow_html=True,
    )

st.markdown(
    """
    <div style="border-top: 1px solid #dfe5ee; margin-top: 32px; padding-top: 22px; text-align: center; color: #64748b; line-height: 1.8; font-size: 15px;">
        <div style="font-size: 20px; color: #111827; font-weight: 600; margin-bottom: 4px;">Mobile Price Prediction System</div>
        <div>Machine Learning Mini Project</div>
    </div>
    """,
    unsafe_allow_html=True,
)