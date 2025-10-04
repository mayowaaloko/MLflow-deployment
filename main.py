from src.mlproject import logger
from src.mlproject.pipeline.stage01_data_ingestion import DataIngestionExceptionPipeline

STAGE_NAME = "Data Ingestion stage"


try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionExceptionPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e
