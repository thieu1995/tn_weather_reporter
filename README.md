# My very first library python

1. Install requirements to build library
```code 
    pip3 install wheel
    pip3 install twine
```
2. Build your packages
```code 
    python3 setup.py sdist bdist wheel
```
   
3. Check the distribution
```code 
    twine check dist/*
    ===> If passes ==> Now we goonna published to website
```
3. TestPyPI: Test python package publishing before publishes on Python Package Index
```code 
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*
```
4. PyPI: Find, install and publish python packages with PPI
```code 
    twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
