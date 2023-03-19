from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'
def get_requirements(file_path:str)->List[str]:
    '''
    this function will return the list of requirements
    '''
    requirements=[]
    with open(file_path) as file_obj:
        requirements=file_obj.readlines()  #it helps to read the pakage name one by one from  requirments.txt
        requirements=[req.replace("\n","") for req in requirements]# it helpsto avoid the /n comes from readline function

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT) # it autometically conncts th requirments file
    
    return requirements

setup(
name='mlproject',
version='0.0.1',
author='Biswajit',
author_email='likulikuab@gmail.com',
packages=find_packages(),
install_requires=get_requirements('requirements.txt')

)