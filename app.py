import uvicorn
from fastapi import FastAPI
from model import SentimentModel

app = FastAPI()
model = SentimentModel()

@app.post('/predict')
def predict(input_sentence):
    polarity, subjectivity, result = model.get_sentiment_analysis(input_sentence)
    return { 'Sentiment': result
    }

if __name__ == '__main__':
    uvicorn.run(app, host='0.0.0.0', port=8000)