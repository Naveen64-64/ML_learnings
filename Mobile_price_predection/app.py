import streamlit as st
import pandas as pd
import joblib

# ---------------------------------------------------
# PAGE CONFIGURATION
# ---------------------------------------------------

st.set_page_config(
    page_title="Mobile Price Predictor",
    page_icon="📱",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# ---------------------------------------------------
# LOAD MODEL
# ---------------------------------------------------

model = joblib.load("model/model.pkl")

# ---------------------------------------------------
# CUSTOM CSS
# ---------------------------------------------------

st.markdown(
    """
    <style>

    /* Main page */
    .stApp {
        background-color: #f5f7fb;
    }

    /* Remove top padding */
    .block-container {
        padding-top: 2rem;
        padding-bottom: 3rem;
        max-width: 1200px;
    }

    /* Header */
    .main-header {
        text-align: center;
        padding: 20px 0 30px 0;
    }

    .main-header h1 {
        font-size: 42px;
        font-weight: 700;
        color: #111827;
        margin-bottom: 8px;
    }

    .main-header p {
        font-size: 17px;
        color: #6b7280;
    }

    /* Section title */
    .section-title {
        font-size: 24px;
        font-weight: 650;
        color: #111827;
        margin-top: 10px;
        margin-bottom: 15px;
    }

    /* Cards */
    .info-card {
        background: white;
        padding: 22px;
        border-radius: 16px;
        border: 1px solid #e5e7eb;
        box-shadow: 0 4px 15px rgba(0,0,0,0.04);
        margin-bottom: 20px;
    }

    /* Prediction card */
    .prediction-card {
        background: linear-gradient(135deg, #111827, #1f2937);
        padding: 35px;
        border-radius: 20px;
        text-align: center;
        margin-top: 20px;
        margin-bottom: 25px;
    }

    .prediction-label {
        color: #d1d5db;
        font-size: 16px;
        margin-bottom: 8px;
    }

    .prediction-price {
        color: white;
        font-size: 42px;
        font-weight: 750;
        margin: 0;
    }

    .prediction-description {
        color: #9ca3af;
        font-size: 14px;
        margin-top: 10px;
    }

    /* Specification cards */
    .spec-card {
        background: white;
        border: 1px solid #e5e7eb;
        border-radius: 14px;
        padding: 18px;
        margin-bottom: 12px;
    }

    .spec-name {
        color: #6b7280;
        font-size: 13px;
        margin-bottom: 5px;
    }

    .spec-value {
        color: #111827;
        font-size: 18px;
        font-weight: 650;
    }

    /* Button */
    .stButton > button {
        width: 100%;
        height: 50px;
        border-radius: 10px;
        border: none;
        background-color: #111827;
        color: white;
        font-size: 16px;
        font-weight: 600;
    }

    .stButton > button:hover {
        background-color: #374151;
        color: white;
    }

    /* Footer */
    .footer {
        text-align: center;
        color: #9ca3af;
        font-size: 13px;
        margin-top: 40px;
        padding-top: 20px;
        border-top: 1px solid #e5e7eb;
    }

    /* Hide Streamlit branding */
    #MainMenu {
        visibility: hidden;
    }

    footer {
        visibility: hidden;
    }

    header {
        visibility: hidden;
    }

    </style>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# HEADER
# ---------------------------------------------------

st.markdown(
    """
    <div class="main-header">
        <h1>Mobile Price Predictor</h1>
        <p>AI-powered mobile price estimation using Multiple Linear Regression</p>
    </div>
    """,
    unsafe_allow_html=True
)

# ---------------------------------------------------
# MAIN LAYOUT
# ---------------------------------------------------

left_column, right_column = st.columns([1.1, 1], gap="large")

# ===================================================
# LEFT COLUMN - INPUTS
# ===================================================

with left_column:

    st.markdown(
        '<div class="section-title">Mobile Specifications</div>',
        unsafe_allow_html=True
    )

    st.markdown(
        '<div class="info-card">',
        unsafe_allow_html=True
    )

    # Row 1
    col1, col2 = st.columns(2)

    with col1:
        ram = st.number_input(
            "RAM (GB)",
            min_value=1.0,
            max_value=32.0,
            value=8.0,
            step=1.0
        )

    with col2:
        storage = st.number_input(
            "Storage (GB)",
            min_value=16.0,
            max_value=1024.0,
            value=128.0,
            step=16.0
        )

    # Row 2
    col3, col4 = st.columns(2)

    with col3:
        battery = st.number_input(
            "Battery (mAh)",
            min_value=1000.0,
            max_value=10000.0,
            value=5000.0,
            step=100.0
        )

    with col4:
        camera = st.number_input(
            "Camera (MP)",
            min_value=2.0,
            max_value=250.0,
            value=50.0,
            step=1.0
        )

    # Row 3
    col5, col6 = st.columns(2)

    with col5:
        screen_size = st.number_input(
            "Screen Size (inches)",
            min_value=4.0,
            max_value=8.0,
            value=6.5,
            step=0.1
        )

    with col6:
        processor_speed = st.number_input(
            "Processor Speed (GHz)",
            min_value=1.0,
            max_value=5.0,
            value=2.8,
            step=0.1
        )

    st.markdown("</div>", unsafe_allow_html=True)

    # Predict button
    predict_button = st.button(
        "Predict Mobile Price"
    )


# ===================================================
# RIGHT COLUMN - RESULT
# ===================================================

with right_column:

    st.markdown(
        '<div class="section-title">Prediction Result</div>',
        unsafe_allow_html=True
    )

    if predict_button:

        # Create dataframe
        new_mobile = pd.DataFrame({
            "ram": [ram],
            "storage": [storage],
            "battery": [battery],
            "camera": [camera],
            "screen_size": [screen_size],
            "processor_speed": [processor_speed]
        })

        # Prediction
        prediction = model.predict(new_mobile)

        predicted_price = prediction[0]

        # Prediction card
        st.markdown(
            f"""
            <div class="prediction-card">
                <div class="prediction-label">
                    Estimated Mobile Price
                </div>

                <div class="prediction-price">
                    ₹{predicted_price:,.0f}
                </div>

                <div class="prediction-description">
                    Estimated using Multiple Linear Regression
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

        # Specifications
        st.markdown(
            '<div class="section-title">Selected Specifications</div>',
            unsafe_allow_html=True
        )

        spec1, spec2 = st.columns(2)

        with spec1:

            st.markdown(
                f"""
                <div class="spec-card">
                    <div class="spec-name">RAM</div>
                    <div class="spec-value">{ram:.0f} GB</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="spec-card">
                    <div class="spec-name">Battery</div>
                    <div class="spec-value">{battery:.0f} mAh</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="spec-card">
                    <div class="spec-name">Screen Size</div>
                    <div class="spec-value">{screen_size:.1f} inches</div>
                </div>
                """,
                unsafe_allow_html=True
            )

        with spec2:

            st.markdown(
                f"""
                <div class="spec-card">
                    <div class="spec-name">Storage</div>
                    <div class="spec-value">{storage:.0f} GB</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="spec-card">
                    <div class="spec-name">Camera</div>
                    <div class="spec-value">{camera:.0f} MP</div>
                </div>
                """,
                unsafe_allow_html=True
            )

            st.markdown(
                f"""
                <div class="spec-card">
                    <div class="spec-name">Processor</div>
                    <div class="spec-value">{processor_speed:.1f} GHz</div>
                </div>
                """,
                unsafe_allow_html=True
            )

    else:

        # Initial state
        st.markdown(
            """
            <div class="info-card" style="text-align:center; padding:60px 25px;">

                <div style="font-size:45px;">
                    📱
                </div>

                <h3 style="color:#111827;">
                    Ready to Predict
                </h3>

                <p style="color:#6b7280;">
                    Enter the mobile specifications and
                    click the prediction button.
                </p>

            </div>
            """,
            unsafe_allow_html=True
        )


# ---------------------------------------------------
# HOW IT WORKS
# ---------------------------------------------------

st.markdown(
    '<div class="section-title">How It Works</div>',
    unsafe_allow_html=True
)

info1, info2, info3 = st.columns(3)

with info1:

    st.markdown(
        """
        <div class="info-card">
            <h4 style="color:#111827;">01. Enter Details</h4>
            <p style="color:#6b7280;">
                Provide RAM, storage, battery, camera,
                screen size and processor speed.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with info2:

    st.markdown(
        """
        <div class="info-card">
            <h4 style="color:#111827;">02. ML Prediction</h4>
            <p style="color:#6b7280;">
                The trained Multiple Linear Regression
                model analyzes the specifications.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )

with info3:

    st.markdown(
        """
        <div class="info-card">
            <h4 style="color:#111827;">03. Get Price</h4>
            <p style="color:#6b7280;">
                The system displays the estimated
                mobile price instantly.
            </p>
        </div>
        """,
        unsafe_allow_html=True
    )


# ---------------------------------------------------
# FOOTER
# ---------------------------------------------------

st.markdown(
    """
    <div class="footer">
        Mobile Price Prediction System
        <br>
        Machine Learning Mini Project
    </div>
    """,
    unsafe_allow_html=True
)