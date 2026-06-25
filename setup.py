from setuptools import find_packages,setup
from typing import List


def get_requirememts()->List[str]:

    """
    This function will return list of the requirements

    """
    requirements_list:List[str] = []

    try:
        #open and read the requirements.txt file
        with open('requirements.txt','r') as file:
            #read lines from the file
            lines = file.readlines()
            #process each line

            for line in lines:
                #strip the whitespacce and newline char

                requirement = line.strip()
                #ignore the empty lines and -e .

                if requirement and requirement != '-e .':
                    requirements_list.append(requirement)
    
    except FileNotFoundError:
        print('Requirement.txt file not found')

    return requirements_list

print(get_requirememts())

setup(
    name='Ai_trip_Planner',
    version='0.0.1',
    author='Nikhil G',
    author_email='nikhilgoral587@gmail.com',
    packages= find_packages(),
    install_requires=get_requirememts()
)