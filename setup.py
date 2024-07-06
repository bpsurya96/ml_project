from setuptools import find_packages, setup
from typing import List

HYPEN_E_DOT = "-e ."
def get_requirements(file_name:str)-> List[str]:
    lib_installed = []
    with open(file_name) as temp_obj:
        lib_installed = temp_obj.readlines()
        lib_installed = [i.strip() for i in lib_installed]

        if HYPEN_E_DOT in lib_installed:
            lib_installed.remove(HYPEN_E_DOT)

    return lib_installed


setup(
    name = "ml_project",
    version = "0.0.1",
    author = "Surya",
    author_email = "bpsurya96@gmail.com",
    packages = find_packages(),
    install_requires = get_requirements("requirements.txt")
)