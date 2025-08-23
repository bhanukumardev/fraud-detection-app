import streamlit as st
import pandas as pd
import numpy as np
import joblib
import matplotlib.pyplot as plt

# Set wide page layout to use full screen width
st.set_page_config(layout="wide")

# ----- PAGE STYLE -----
custom_css = """
    <style>
        body { background: #101010 !important; color: #39FF14 !important; }
        .main, .block-container, .css-18e3th9 {
            max-width: 100vw !important;
            padding-left: 1.5vw !important;
            padding-right: 1.5vw !important;
        }
        .main { background: #18181a !important; }
        .stButton>button {
            background-color: #39FF14;
            color: #18181a;
            font-weight: bold;
            border-radius: 7px;
            border: 2px solid #39FF14;
            font-size: 22px;
        }
        .css-1v0mbdj { border: none !important; }
        .st-bf, st-at, .css-145kmo2 { color: #39FF14!important; }
        .st-bb {
            background: linear-gradient(90deg, #39FF14 0%, #00c3ff 100%);
            color: #18181a !important;
        }
        .element-container h1, h2, h3, h4 { color: #00ffea; }
        .stMarkdown { color: #39FF14!important;}
        .stCheckbox>div>div { border-color: #39FF14;}
        /* Dropdown with gradient */
        .stSelectbox > div > div {
            background: linear-gradient(90deg, #39FF14, #00c3ff);
            color: #18181a;
            border-radius: 8px;
            padding-left: 10px;
        }
        /* Slider track */
        .stSlider > div > div > input {
            accent-color: #39FF14;
        }
        /* Radio buttons */
        .stRadio > div > label {
            color: #39FF14 !important;
            font-weight: bold;
        }
    </style>
"""
st.markdown(custom_css, unsafe_allow_html=True)

# ----- TOP TWO-COLUMN LAYOUT WITH WIDER SPREAD -----
left, right = st.columns([1, 2], gap="large")

with left:
    st.markdown("""
    <div style="background: #134e2b; padding: 24px 30px 22px 30px; border-radius: 18px; margin-bottom: 18px; 
                border:2.4px solid #39FF14; box-shadow:0 0 10px #00ffea;">
        <h2 style="color:#fff;margin-bottom:0;">4. Fraud Detection in Finance – Finance & Inclusion</h2>
        <p style="color:#ffea00; margin-bottom:8px;font-size:1.18em;">
            <b>Problem Statement:</b> Fraudulent transactions often mimic normal financial activity, making anomaly detection highly complex.<br>
            Standard detection methods fail against these <b>“hidden”</b> anomalies.
        </p>
        <p style="color:#00ffea; margin-bottom:0;font-size:1.14em;">
            <b>Hackathon Challenge:</b> Design an AI/ML-based anomaly detection system that identifies paradoxical fraud patterns within UPI or credit transaction datasets and provides explainable insights.
        </p>
    </div>
    """, unsafe_allow_html=True)

with right:
    st.markdown("""
    <div style="border-radius:20px;background: linear-gradient(120deg, #1a1a2e 60%, #0f3460 100%);
                padding:30px; margin-bottom:22px; border:3px solid #39FF14; box-shadow:0 0 16px #00ffea;">
        <h1 style="color:#39FF14; font-size:2.3em; margin-bottom:0;">🟢 Binary Brains</h1>
        <h3 style="color:#00ffea; margin-top:8px; margin-bottom:0;">
            <span style="color:#ffea00;">Team ID: 629257</span> | 
            <span style="color:#39ff14;">Track: Advanced</span>
        </h3>
        <h4 style="color:#fff;margin-top:12px;">Bhanu Kumar Dev, Srijan, Ayush Ansh, Atul Kumar, Harsh Bhardwaj</h4>
        <span style="color:#aaa;font-size:1.07em;letter-spacing:1px;">Pandora Paradox @ KIIT E-Summit 2025 • Credit Card Fraud Detection HackApp</span>
    </div>
    """, unsafe_allow_html=True)

    st.markdown("## Enter Transaction Details", unsafe_allow_html=True)

    # --- INPUT FIELDS BELOW TEAM DISPLAY ---
    with st.form("fraud_form"):
        amount = st.number_input("💸 Transaction Amount (₹)", min_value=0.0, format="%.2f", value=100.0)
        location = st.selectbox("🌍 Transaction Location", ["Mumbai", "Delhi", "Bangalore", "Pune", "Hyderabad", "Other"])
        txn_type = st.selectbox("💳 Transaction Type", ["E-Commerce", "UPI", "ATM Withdrawal", "POS Swipe", "Bank Transfer"])
        hour = st.slider("🕒 Transaction Hour", 0, 23, 12)
        day = st.selectbox("📆 Day of Week", ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"])
        is_new_location = st.radio("🛰️ Is New Location?", [0, 1], index=0, horizontal=True)
        is_high_amount = st.radio("⚡High Amount?", [0, 1], index=0, horizontal=True)
        submit_btn = st.form_submit_button("⚡ Predict Fraud")

    # --- PIPELINE & PREDICTION ---
    pipe = joblib.load("fraud_detection_pipeline.pkl")

    if submit_btn:
        input_dict = {
            "Amount": amount,
            "Location": location,
            "Type": txn_type,
            "Hour": hour,
            "Day": day,
            "Is_New_Location": int(is_new_location),
            "Is_High_Amount": int(is_high_amount)
        }
        input_df = pd.DataFrame([input_dict])

        pred = pipe.predict(input_df)[0]
        proba = pipe.predict_proba(input_df)[:, 1][0]
        proba_scalar = float(proba)

        st.markdown("### :alien: Prediction Hack Result")
        if pred == 1:
            st.markdown(
                f"""
                <div style='padding:1em; background:#1a202c; border:3px solid #ff3131; border-radius:12px;'>
                    <span style='font-size:2em;color:#ff3131;font-weight:bold;text-shadow:0 0 5px #fff;'>⚠️ FRAUD DETECTED!</span>
                    <br><span style='color:#ffea00;font-size:1.4em;'>Probability: {proba_scalar:.2%}</span>
                </div>
                """, unsafe_allow_html=True
            )
        else:
            st.markdown(
                f"""
                <div style='padding:1em; background:#102512; border:3px solid #39FF14; border-radius:12px;'>
                    <span style='font-size:2em;color:#39FF14;font-weight:bold;text-shadow:0 0 8px #00ffea;'>✔️ Transaction is Legitimate</span>
                    <br><span style='color:#00ffea;font-size:1.4em;'>Probability of Fraud: {proba_scalar:.2%}</span>
                </div>
                """, unsafe_allow_html=True
            )

        st.markdown("---")
        st.markdown("##### <span style='color:#aaa;'>Explainable Insights:</span>", unsafe_allow_html=True)
        xp = ""
        if bool(is_high_amount):
            xp += "- 💸 Unusually high amount for user<br>"
        if bool(is_new_location):
            xp += f"- 🛰️ New/unfamiliar location used: <b>{location}</b><br>"
        st.markdown(xp or "<span style='color:#39FF14'>No suspicious attributes detected.</span>", unsafe_allow_html=True)

# After the prediction code
if submit_btn:
    import streamlit.components.v1 as components
    # Scroll to see the new result
    st.markdown(
        """
        <script>
            window.scrollTo({ top: document.body.scrollHeight, behavior: "smooth" });
        </script>
        """, unsafe_allow_html=True,
    )

    # Show result box (as before, but bolder)
    st.markdown("### :alien: Prediction Hack Result")
    highlight_color = "#00ff66" if pred == 0 else "#ff3131"
    text_shadow = "0 0 16px #00ff99" if pred == 0 else "0 0 12px #ff4531"
    result_icon = "✅" if pred == 0 else "⚠️"
    result_msg = "Transaction is Legitimate" if pred == 0 else "FRAUD DETECTED!"
    
    st.markdown(
        f"""
        <div style='padding:1.6em;
                    margin-top:0.8em;
                    margin-bottom:1.2em;
                    background:#18181a;
                    border:4px solid {highlight_color};
                    border-radius:16px;
                    box-shadow:0 0 40px {highlight_color};
                    display:flex;
                    flex-direction:column;
                    align-items:center;'>
            <span style='font-size:2.4em;
                         color:{highlight_color};
                         font-weight:bold;
                         text-shadow:{text_shadow};'>{result_icon} {result_msg}</span>
            <br>
            <span style='color:#00ffea;font-size:1.7em;'>
                Probability of Fraud: {proba_scalar:.2%}
            </span>
        </div>
        """, unsafe_allow_html=True
    )
    st.toast("Prediction complete!", icon="⚡")

# --- MATRIX / VISUAL EFFECTS ---
st.markdown("""
<div style='display:flex;flex-direction:column;align-items:center;'>
    <h2 style="color:#fff;letter-spacing:2px;margin-bottom:10px;font-size:2.0em;">🔎 Live Hackathon Matrix 🔎</h2>
    <img src="Assets/snake.webp"
         style="
            width:320px;
            max-width:90vw;
            border-radius:18px;
            border:3px solid #39FF14;
            box-shadow:0 0 18px #00ffea;
            margin-bottom:12px;"
         alt="Live Matrix Snake"/>
</div>
""", unsafe_allow_html=True)

# --- FUN FOOTER ---
st.markdown("""
<hr style='border-top:2px solid #39FF14'>
<p style='color:#aaa;text-align:center;margin-top:24px;'>
    <span style="color:#ff3131;font-weight:bold;">Binary Brains</span> | Powered by <b>Pandora Paradox, KIIT E-Summit 2025</b>
</p>
""", unsafe_allow_html=True)
