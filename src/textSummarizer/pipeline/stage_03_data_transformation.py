from textSummarizer.components.data_transformation import DataTransformation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class DataTransformationTrainingPipeline():
    def _init_(self):
        pass

    def main(self):

        try:
            config= ConfigurationManager()
            data_transformation_config = config.get_data_transformation_config()
            data_transformation = DataTransformation(data_transformation_config)
            data_transformation.convert()

        except Exception as e:
            logger.error(f"Error in data transformation: {str(e)}")
            raise e
