from setuptools import setup, find_packages

setup(
    # Application name:
    name="svgtools",

    # Version number (initial):
    version="0.0.1",

    # Application author details:
    author="Vanessa Sochat",
    author_email="vsochat@stanford.edu",

    # Packages
    packages=find_packages(),

    # Data
    package_data = {'svgtools.templates':['html/*.html','*.zip','js/*.js','css/*.css','img/*'],
                    'svgtools.testing':['data/*.tsv','data/*.csv']},

    # Details
    url="http://www.github.com/vsoch/svgtools",

    license="LICENSE.txt",
    description="components from images and data for interactive visualizations",

    install_requires = ['Cython','networkx','numpy','scipy','scikit-learn','pandas','matplotlib','scikit-image']
)
