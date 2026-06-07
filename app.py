import streamlit as st
import pandas as pd
import joblib

# 1. Load the trained model
# The @st.cache_resource decorator ensures we only load the model once (speed boost)
@st.cache_resource
def load_model():
    return joblib.load('ad_sales_model.pkl')

model = load_model()

# 2. App Title & Description
st.title(" AI Marketing Optimizer")
st.write("""
**Stop guessing your ad budget.** Enter your planned spend for each channel, and this AI will predict your revenue 
based on historical performance data.
""")

# 3. Sidebar for User Inputs
st.sidebar.header("Configure Your Budget")
st.sidebar.write("Adjust the sliders to set your monthly spend.")

fb_spend = st.sidebar.slider("Facebook Spend ($)", 0, 20000, 5000)
insta_spend = st.sidebar.slider("Instagram Spend ($)", 0, 20000, 5000)
tiktok_spend = st.sidebar.slider("TikTok Spend ($)", 0, 20000, 5000)

# 4. Main Panel: The "Brain" Logic
# We organize the input into a DataFrame just like the model expects
input_data = pd.DataFrame({
    'Facebook_Spend': [fb_spend],
    'Instagram_Spend': [insta_spend],
    'TikTok_Spend': [tiktok_spend]
})

# Run the prediction
prediction = model.predict(input_data)[0]
total_spend = fb_spend + insta_spend + tiktok_spend
roi = ((prediction - total_spend) / total_spend) * 100 if total_spend > 0 else 0

# 5. Display Results
st.markdown("---")
col1, col2 = st.columns(2)

with col1:
    st.subheader(" Predicted Revenue")
    st.metric(label="Revenue", value=f"${prediction:,.2f}", delta=f"ROI: {roi:.1f}%")

with col2:
    st.subheader(" Total Cost")
    st.metric(label="Ad Spend", value=f"${total_spend:,.2f}")

# 6. Visualization
st.markdown("### Budget Allocation vs. Return")
chart_data = pd.DataFrame({
    'Metric': ['Cost', 'Revenue'],
    'Amount': [total_spend, prediction]
})
st.bar_chart(chart_data.set_index('Metric'))

# 7. "AI Consultant" Advice
st.info(" **AI Tip:** Our model shows that **TikTok** has the highest ROI coefficient (4.33). "
        "Consider shifting more budget there to maximize profit!")
