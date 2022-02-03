# Emotion Correction with Shap API
This repository contains an API that detects toxic emotions in text.

## How to run
```commandline
git clone https://github.com/knmlprz/ShapEmotionsCorrectionAPI.git
cd ShapEmotionsCorrectionAPI
uvicorn src.main:app --reload
```

## Documentation
First, start the server:
```commandline
uvicorn src.main:app 
```
Then go to: [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs). There 
you'll find all the available endpoints, their example requests and responses.