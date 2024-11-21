import setuptools
from setuptools import find_packages, setup
from typing import List
var = '-e .'
def get_requirements(file_path: str) -> List[str]:
    requirements= []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace("\n","")for req in requirements]
        if var in requirements:
            requirements.remove(var)
        return requirements
    
    
setup(
    name = "mlProject",
    version = '0.0.1',
    author = 'avish006',
    author_email = 'avishcoder@gmail.com',
    packages = find_packages(),
    install_requires=get_requirements('requirements.txt')

)