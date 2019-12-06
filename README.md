# My very first library python

0. Tutorial from
```code 
    https://www.youtube.com/watch?v=KTaLs494xgo&list=PLyb_C2HpOQSB3z_4WliKt56WyDgfXzzMz
    https://realpython.com/pypi-publish-python-package/
```

1. Install requirements to build library
```code 
    pip3 install wheel
    pip3 install twine
```
2. Build your packages
```code 
    python3 setup.py sdist bdist_wheel
```
   
3. Check the distribution
```code 
    twine check dist/*
    ===> If passed ==> Now we goonna published to website
```
3. TestPyPI: Test python package publishing before publishes on Python Package Index
```code 
    twine upload --repository-url https://test.pypi.org/legacy/ dist/*

- If you are using ubuntu, maybe you will get this error from commandline
....
    from keyring.util.escape import escape as escape_for_ini
ModuleNotFoundError: No module named 'keyring.util.escape'

    pip3 install --upgrade keyrings.alt 
```
4. PyPI: Find, install and publish python packages with PPI
```code 
    twine upload --repository-url https://upload.pypi.org/legacy/ dist/*
```
