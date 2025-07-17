# setup.py
from setuptools import setup, find_packages

setup(
    name='chat_insight',
    version='0.1.0',
    packages=find_packages(),
    install_requires=[
        'openai',
        'pandas'
    ],
    author='Jelius Heneriko',
    description='A package to analyze chat conversations for struggling customers using LLMs',
)
