"""
Setup script for Business Analytics project.
"""
from setuptools import setup, find_packages

setup(
    name="business-analytics",
    version="0.1.0",
    description="Business Analytics Data Science Project",
    author="Your Name",
    packages=find_packages(),
    install_requires=[
        "pandas>=2.0.0",
        "numpy>=1.24.0",
        "matplotlib>=3.7.0",
        "seaborn>=0.12.0",
        "plotly>=5.14.0",
        "scipy>=1.10.0",
        "statsmodels>=0.14.0",
        "scikit-learn>=1.3.0",
        "jupyter>=1.0.0",
        "ipykernel>=6.25.0",
        "notebook>=7.0.0",
        "openpyxl>=3.1.0",
        "xlrd>=2.0.0",
        "python-dotenv>=1.0.0",
        "tqdm>=4.65.0",
    ],
    python_requires=">=3.8",
)

