import streamlit as st
import requests

# page config
st.set_page_config(
    page_title="Sentiment Analysis",
    page_icon="Amazon🛒🛍",
    layout="centered"
)

st.title("Amazon Reviews Sentiment Analyzer")
st.write("Enter a product review andget instant sentiment prediction!")

# Input box
review=st.text_area("Enter your product review here:",height=150)

#Predict button
if st.button("Analyze sentiment"):
    if review.strip() =="":
        st.warning("Please enter a review first!")
    else:
        with st.spinner("Analyzing..."):
            #call your flask backend"
            response = requests.post(
                "https://amazon-reviews-4vp5.onrender.com/predict",# your render link
            json={"reviews":review}
            )
            result = response.json()
            #Display result
            sentiment = result['prediction']
            #confidence=result['confidence']
            if "pos" in sentiment or "neg" in sentiment:
                st.success(f"Sentiment :{sentiment}")
            else:
                st.error(f"Sentiment:{sentiment}")
                            