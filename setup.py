from setuptools import setup, Extension

setup(
    name='BostaSDK',
    version='1.0.0',
    author='bosta',
    author_email='sdk@bosta.com',
    scripts=[],
    keywords=["bosta", "client-sdk", "api", "api-integration"],
    url= 'https://pypi.org/project/BostaSDK/',
    license='LICENSE',
    description='Bosta Python SDK',
    long_description=open('README.md', 'r').read(),
    long_description_content_type='text/markdown',
    install_requires=[
        'requests'
    ],
)
