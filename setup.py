from setuptools import setup, find_packages

setup(
    name='IriusRisk',
    version='1.0',
    long_description=__doc__,
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=['Flask', 'flask-api', 'sumy', 'numpy', 'nltk']
)