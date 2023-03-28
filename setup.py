from setuptools import find_packages, setup

HYPEN_E_DOT="-e ."
def get_requirements(file):
    '''
    This fuction return list of libraries to be installed.
    '''
    requirements=[]
    with open(file) as requirements_file:
        requirements=requirements_file.readlines()
        requirements=[req.replace("\n","") for req in requirements]

        if HYPEN_E_DOT in requirements:
            requirements.remove(HYPEN_E_DOT)
setup(
    name="Shortly-Text Summarizer",
    version="0.0.1",
    author="Chintan Vekariya",
    author_email="vekariyachintan404@gmail.com",
    packages=find_packages(),
    install_requires=get_requirements('requirements.txt')
)