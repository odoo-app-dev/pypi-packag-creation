# PYPI Registration Process 

1. [Create simple file structure](#1.file-structure)
2. Update package information
3. Build the package
4. test your package locally
5. upload and test the package on test.pypi.org
6. upload to the pypi.org
7. upload the source files to github.com

# 1.file structure


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