
import streamlit as st
import pandas as pd
import numpy as np
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import BernoulliNB
import ssl
ssl._create_default_https_context = ssl._create_unverified_context

# Load data
@st.cache_data()
def load_data():
    return pd.read_json("https://raw.githubusercontent.com/amankharwal/Website-data/master/Sarcasm.json", lines=True)

data = load_data()

# Preprocess data
data["is_sarcastic"] = data["is_sarcastic"].map({0: "Not Sarcasm", 1: "Sarcasm"})
data = data[["headline", "is_sarcastic"]]
x = np.array(data["headline"])
y = np.array(data["is_sarcastic"])

# Train-test split
cv = CountVectorizer()
X = cv.fit_transform(x) 
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.20, random_state=42)

# Train model
model = BernoulliNB()
model.fit(X_train, y_train)
print(model.score(X_test, y_test))

# Streamlit app
st.title('Sarcasm Detector')
user_input = st.text_input('Enter a Text:')
if user_input:
    data = cv.transform([user_input]).toarray()
    output = model.predict(data)
    st.write("Prediction:", output)
    print(output)
