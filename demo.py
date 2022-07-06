from housing.exception import HousingException
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration

def main():
    try:
        data_transformation_config = Configuration().get_data_transformation_config()
        print(data_transformation_config)
        #pipeline = Pipeline()
        #pipeline.run_pipeline()
    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()

