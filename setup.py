from setuptools import setup,find_packages
from typing import List

## declearing variables for the setup function

PROJECT_NAME = "housing_predictor"
VERSION = "0.0.1"
AUTHOR = "Sumit Bhagat"
DESCRIPTION = "This is the project to predict house price in bangalore"
#PACKAGES = ['housing']
REQUIREMENT_FILE_NAME='requirements.txt'

"""
Description - This function is going to return list of requirements mention in requirements.txt file.

return: this function is going to return a list which contains the list of libraries
mentioned in requiremnts.txt file.
"""
def get_requirements_list()->List[str]:
    with open(REQUIREMENT_FILE_NAME) as requirement_file:
        return requirement_file.readlines().remove("-e .")

setup(

name = PROJECT_NAME,
version=VERSION,
author=AUTHOR,
description=DESCRIPTION,
packages=find_packages(), # PACKAGES
install_requires=get_requirements_list()

)
