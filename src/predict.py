import joblib

model = joblib.load("model/model.pkl")
vectorizer = joblib.load("model/vectorizer.pkl")


def predict_news(title, description):
    text = title + " " + description

    from src.preprocessing import clean_text

    text = clean_text(text)

    text_tfidf = vectorizer.transform([text])

    prediction = model.predict(text_tfidf)[0]

    class_names = {
        1: "World",
        2: "Sports",
        3: "Business",
        4: "Sci/Tech"
    }

    return class_names[prediction]