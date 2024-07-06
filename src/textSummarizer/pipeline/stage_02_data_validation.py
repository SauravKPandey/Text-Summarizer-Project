#pipeline
from textSummarizer.components.data_validation import DataValidation
from textSummarizer.config.configuration import ConfigurationManager
from textSummarizer.logging import logger

class DataValidationTrainingPipeline:
    def _init_(self):
        pass
    
    def main(self):

        try:
            config = ConfigurationManager()
            data_validation_config = config.get_data_validation_config()
            data_validation = DataValidation(config=data_validation_config)
            validation_status = data_validation.validate_all_files_exist()
            logger.info(f"Data validation completed successfully: {validation_status}")

        except Exception as e:
            logger.error(f"Error in data validation: {str(e)}")
            raise e
