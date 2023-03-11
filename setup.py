from setuptools import find_packages,setup
from typing import List

HYPEN_E_DOT='-e .'

def get_requirements(file_path:str)->List[str]:
    """
    this function will return the list of requirements
    """
    requiremnts=[]
    with open(file_path) as file_obj:
        requiremnts=file_obj.readlines()
        requiremnts=[req.replace("\n","") for req in requiremnts]

        if HYPEN_E_DOT in requiremnts:
            requiremnts.remove(HYPEN_E_DOT)

    return requiremnts

setup(
    name = 'mlproject',
    author = 'Sonali PATEKAR',
    author_email= 'mp.sonali29@gmail.com',
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')


)