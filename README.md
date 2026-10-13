# Amazon Reviews Sentiment Analysis

## Project Overview

This project uses Natural Language Processing (NLP) and Machine Learning to analyse Amazon product reviews and predict their sentiment.

The application provides a user interface built with Streamlit, allowing users to enter a review and obtain a sentiment prediction.

## Objectives

* Process and prepare review text for machine learning.
* Convert text into numerical features using a vectorizer.
* Use a trained machine learning model to predict sentiment.
* Provide an interactive interface for testing reviews.

## Technologies Used

* Python
* Natural Language Processing (NLP)
* Machine Learning
* Streamlit
* Scikit-learn
* Joblib

## Project Files

* `app.py` — Application logic.
* `preprocess.py` — Text preprocessing.
* `model.joblib` — Saved machine learning model.
* `vectorizer.joblib` — Saved text vectorizer.
* `streamlit_app.py` — Streamlit interface.
* `requirements.txt` — Project dependencies.

## How to Run the Project

1. Clone this repository.
2. Install the required dependencies.
3. Run the Streamlit application.

```bash
git clone https://github.com/mail2rajaponni-arch/AMAZON-REVIEWS.git
cd AMAZON-REVIEWS
pip install -r requirements.txt
streamlit run streamlit_app.py
```

## Learning Outcomes

This project demonstrates practical experience with text preprocessing, feature extraction, machine learning model usage, and deploying an interactive Python application.

## Future Improvements

* Add model evaluation metrics.
* Include a confusion matrix and classification report.
* Test the application with different review examples.
* Document the dataset and model performance.

## Author

GitHub: https://github.com/mail2rajaponni-arch
