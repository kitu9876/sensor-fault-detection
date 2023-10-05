from setuptools import setup, find_packages
from typing import List

PROJECT_NAME="sensor-fault-detection"
VERSION="0.0.1"
AUTHOR="Kiran Bagade"
AUTHOR_EMAIL="kitu9876.kb@gmail.com"
REQUIREMENT_FILE_NAME="requirements.txt"
HYPHEN_E_DOT="-e ."


def get_requirements() ->List[str]:
    with open ("requirements.txt") as file:
        file_content=file.readlines()
        requirement_list=[line.replace("/n","") for line in file_content]
        if HYPHEN_E_DOT in requirement_list:
            requirement_list.remove(HYPHEN_E_DOT)
        return requirement_list

setup(
    name='PROJECT_NAME',
    version=VERSION,
    author=AUTHOR,
    author_email=AUTHOR_EMAIL,
    packages=find_packages(),
    install_requires=REQUIREMENT_FILE_NAME
    )
