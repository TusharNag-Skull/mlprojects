# this is file we created so that we can import the package in other files
# our wholem l model will be a package in itself and can be used in 
# various other places

from setuptools import setup,find_packages
from typing import List

HYPEHEN_E_DOT = "-e ."
def get_requirements(file_path)-> List[str]:
    """this function will return the list of requirements"""
    requirements = []
    with open(file_path) as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","") for req in requirements]
        
        if HYPEHEN_E_DOT in requirements:
            requirements.remove(HYPEHEN_E_DOT)
    
    return requirements

    

setup(
name=  "mlproject",
version= "0.0.1",
author= "Tushar",
author_email= "toshynag04@gmail.com",
packages= find_packages(),
install_requires= get_requirements("requirements.txt")

)