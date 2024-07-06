from textSummarizer.logging import logger
from textSummarizer.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
from textSummarizer.pipeline.stage_02_data_validation import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    data_ingestion = DataIngestionTrainingPipeline()
    data_ingestion.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<< \n\n")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {str(e)}")
    raise e

STAGE_NAME ="Data Validation Stage"

try:
    logger.info(f">>>> {STAGE_NAME} started <<<<")
    data_validation = DataValidationTrainingPipeline()
    data_validation.main()
    logger.info(f">>>> {STAGE_NAME} completed <<<< \n\n")

except Exception as e:
    logger.error(f"Error in {STAGE_NAME}: {str(e)}")
    raise e
