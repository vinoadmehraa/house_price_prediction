from setuptools import setup, find_packages

setup(
    name='housing_price_prediction',
    version='0.1',
    packages=find_packages(where='src'),
    package_dir={'': 'src'},
    install_requires=[
        'numpy',
        'pandas',
        'scikit-learn',
        'matplotlib',
        'seaborn',
        'jupyter'
    ],
    author='VINOAD MEHRAA',
    description='An end-to-end machine learning project for housing price prediction',
)
