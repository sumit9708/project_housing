import yaml
from housing.exception import HousingException
import os,sys

### This file we have created to write all the helper function to use in pipepline component file

def read_yaml_file(file_path:str)->dict:
    """
    This is the function to read config.yaml file and return file content as dictionary
    file_path:str
    """
    try:

        with open(file_path,'rb') as yaml_file:
            return yaml.safe_load(yaml_file)
    except Exception as e:
        raise HousingException(e,sys) from e
