from setuptools import find_packages, setup
from typing import List


HYPHEN_E_DOT = '-e .'
def get_requirements(file_path:str)->List[str]:
    '''Returns the list of requirements'''

    requirements = []
    with open(file_path, 'r') as file_obj:
        requirements = file_obj.readlines()
        requirements = [req.replace('\n' , '') for req in requirements]

        if HYPHEN_E_DOT in requirements:
            requirements.remove(HYPHEN_E_DOT)
    
    return requirements

main_requirements = ['pandas', 'numpy', 'scikit-learn', 'matplotlib', 'seaborn', 'joblib', 'pyyaml']

setup(

name = 'Mlproject',
version='0.0.1',
author='Aditya',
author_email='adityaayush10mishra@gmail.com',
packages=find_packages(),
install_requires = main_requirements + get_requirements('requirements.txt')

)

