import joblib
from pathlib import Path

class predictionPipeline:
    def __init__(self):
        self.model=joblib.load(Path('artifacts\model_trainer\model.joblib'))

    def prediction(self, data):
        pred=self.model.predict(data)

        return pred