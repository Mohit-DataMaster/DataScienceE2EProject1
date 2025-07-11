from src.datascience.components.model_evaluation import ModelEvaluation
from src.datascience.config.configuration import ConfigurationManager

class ModelEvaluationPipeline:
    def __init__(self):
        pass

    def initiate_model_evaluation(self):#

        try:
            config=ConfigurationManager()
            model_evaluation_config=config.get_model_evaluation_config()
            model_evaluation=ModelEvaluation(config=model_evaluation_config)
            model_evaluation.mlflow_logging()
        except Exception as e:
            raise e
