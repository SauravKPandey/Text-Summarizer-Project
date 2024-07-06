#src/textSummarizer/components
import os
from textSummarizer.entity import DataValidationConfig
from textSummarizer.logging import logger

class DataValidation:
    def __init__(self, config: DataValidationConfig):
        self.config = config
        self.status_file =  self.config.STATUS_FILE
        self.all_required_files = self.config.ALL_REQUIRED_FILES
    
    def validate_all_files_exist(self)-> bool:
        try:
            validation_status = True
            all_files = os.listdir(os.path.join("artifacts", "data_ingestion", "samsum_dataset"))
            for file in all_files:
                if file not in self.all_required_files:
                    validation_status = False
                    logger.error(f"File {file} is missing")
                    with open(self.status_file, "w") as f:
                        f.write(f"Validatetion Stats: {validation_status}")
                else:
                    logger.info(f"File {file} is present")
                    validation_status = True
                    with open(self.status_file, "w") as f:
                        f.write(f"Validation Stats: {validation_status}")
            return validation_status
        except Exception as e:
            logger.error(f"An error occurred during file validation: {str(e)}")
            raise e
        

        
