from numpy import dtype
from housing.exception import HousingException
from housing.pipeline.pipeline import Pipeline
from housing.exception import HousingException
from housing.logger import logging
from housing.config.configuration import Configuration
from housing.component.data_transformation import DataTransformation

def main():
    try:
        #model_trainer_config = Configuration().get_model_trainer_config()
        #print(model_trainer_config)
        pipeline = Pipeline()
        pipeline.run_pipeline()
        #schema_file_path = r"D:\ML Projects\project_housing\config\schema.yaml"
        #file_path = r"D:\ML Projects\project_housing\housing\artifact\data_ingestion\2022-06-30-20-49-16\ingested_data\train\housing.csv"
        #df = DataTransformation.load_data(file_path=file_path,schema_file_path=schema_file_path)
        #print(df.columns)
        #print(df.dtypes)

    except Exception as e:
        logging.error(f"{e}")
        print(e)

if __name__ == "__main__":
    main()

