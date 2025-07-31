# This will help to make any folder into local package so that we can use it in different file 
from setuptools import find_packages, setup

setup(
    name= "Medical_chatbot",
    version="0.1.0",
    author="Ayaz Rabbani",
    author_email="ayazr425@gmail.com",
    packages=find_packages(),
    install_requires=[]
)