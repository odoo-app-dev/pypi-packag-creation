# pypi-packag-creation
file structure:
```
pypi-packag-creation/
      |- setup.py
      |- LICENSE
      |- README.md
      |- MANIFEST.in
      |+ test/
            |- __init__.py
            |- test.py
      |+ src/
            |- __init__.py
            |- package_name.py
```
1. Build your package

 `\pypi-packag-creation\python setup.py sdist bdist_wheel`
 
2. Install newly created packge localy to make sure it is working fine
 
 `\pypi-packag-creation\pip install -e .`
 
3. pytest
 
4. MANIFEST.in

5.  twine upload .\dist\my-first-package-0.0.1* --repository-url https://test.pypi.org/legacy/ 

6.  twine upload .\dist\my-first-package-0.0.1* 



Resources:

[Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo)