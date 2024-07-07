
from textSummarizer.logging import logger
from textSummarizer.components.model_trainer import ModelTrainer
from textSummarizer.config.configuration import ConfigurationManager


class ModelTrainerTrainingPipeline:
    def __init__(self):
        pass
    
    def main(self):
        try:
            config= ConfigurationManager()
            model_trainer_config=config.get_model_training_config()
            model_trainer=ModelTrainer(config=model_trainer_config)
            model_trainer.train()

        except Exception as e:
            logger.error(f"Error in model training: {str(e)}")
            raise e
