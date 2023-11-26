from src.Machine_learning_with_mlflow import logger
from Machine_learning_with_mlflow.pipelines.stage_01_data_ingestion import DataIngestionTrainingPipeline

logger.info("Welcome to our custom Logging")

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e