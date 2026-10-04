# News Classification System

## Project Overview

This project is an NLP-based News Classification System that automatically classifies news articles into four categories using the article title and description.

The four categories are:

1. World
2. Sports
3. Business
4. Sci/Tech

The project uses text preprocessing, TF-IDF feature extraction, and Logistic Regression for classification. A FastAPI application is used to provide predictions through an API.

## Dataset

The dataset contains news articles with the following columns:

- Class Index
- Title
- Description

### Dataset Size

- Training data: 120,000 articles
- Testing data: 7,600 articles

The classes are balanced, with 30,000 training articles in each category.

## Classes

| Class Index | Category |
|---|---|
| 1 | World |
| 2 | Sports |
| 3 | Business |
| 4 | Sci/Tech |

## Data Preprocessing

The title and description are combined into a single text field.

The following preprocessing steps are performed:

- Convert text to lowercase
- Remove punctuation and numbers
- Remove unnecessary characters
- Remove extra spaces

## Feature Extraction

TF-IDF (Term Frequency-Inverse Document Frequency) is used to convert the cleaned text into numerical features.

The vectorizer uses:

- Maximum 50,000 features
- Unigrams and bigrams
- Minimum document frequency of 2

## Machine Learning Model

## Logistic Regression

Logistic Regression is used as the classification model because it performs well for text classification problems with high-dimensional TF-IDF features.

The model is trained on the training dataset and evaluated on the test dataset.

## Model Evaluation

The model is evaluated using:

- Accuracy
- Precision
- Recall
- F1-score
- Confusion Matrix

These metrics help measure how well the model classifies news articles into the four categories.

## Project Structure

```text
News_Classification_NLP/
│
├── data/
│   ├── train.csv
│   └── test.csv
│
├── model/
│   ├── model.pkl
│   └── vectorizer.pkl
│
├── notebooks/
│   └── news_classification.ipynb
│
├── src/
│   ├── preprocessing.py
│   ├── train.py
│   └── predict.py
│
├── app.py
├── requirements.txt
├── README.md
└── .gitignore

## How to Run Locally

### 1. Clone the repository
git clone https://github.com/shrishtiig/News_Classification_NLP.git

### 2. Open the project folder
cd News_Classification_NLP

### 3. Create a virtual environment
python3 -m venv venv

### 4. Activate the virtual environment
source venv/bin/activate

### 5. Install the required libraries
pip install -r requirements.txt

### 6. Start the FastAPI application
uvicorn app:app --reload

The API will be available at:
http://127.0.0.1:8000

Swagger API documentation:  
http://127.0.0.1:8000/docs


## API Usage

The project provides a FastAPI endpoint for predicting the category of a news article.

### Prediction Endpoint

**POST** `/predict`

The API accepts the title and description of a news article and returns its predicted category.

## Input Format

```json
{
  "title": "Football team reaches the championship final",
  "description": "The team defeated its opponent in a thrilling semifinal match and advanced to the final."
}

##Output Format
{
  "prediction": "Sports"
}


## Deployment

The FastAPI application has been deployed using Render.

Live API:
https://news-classification-nlp.onrender.com/

API Documentation:
https://news-classification-nlp.onrender.com/docs



## Limitations

- The model is trained to classify news articles into only four categories: World, Sports, Business, and Sci/Tech.
- The system does not contain an "Other" category. Therefore, an article that does not belong to these four categories may still be assigned to the closest available category.
- The model uses TF-IDF features and Logistic Regression, so its performance depends on the patterns learned from the training dataset.
- The system mainly uses the title and description of the news article for classification.

## Future Improvements

- Add more news categories
- Experiment with other NLP models
- Improve classification accuracy
- Add a web-based user interface


## Conclusion

This project implements an NLP-based News Classification System that automatically classifies news articles into four categories: World, Sports, Business, and Sci/Tech.

The system combines text preprocessing, TF-IDF feature extraction, and Logistic Regression to perform news classification. A FastAPI application was developed to provide predictions through an API, and the application was deployed using Render.

This project demonstrates the complete workflow of an NLP machine learning project, from data preprocessing and model training to evaluation and deployment.