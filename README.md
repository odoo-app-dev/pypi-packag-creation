# PYPI Registration Process 

1. [Virtual Environment](#virtual-nvironment)
1. [Create simple file structure](#file-structure)
2. [Update package information](#update-package-information)
3. [Build the package](#build-the-package)
4. [Test your package locally](#test-your-package-locally)
5. [upload and test the package on test.pypi.org](#upload-and-test-the-package-on-testpypiorg)
6. [upload to the pypi.org](#upload-to-the-pypiorg)
7. [upload the source files to github.com](#upload-the-source-files-to-githubcom)

## Virtual Environment

```
python -m venv project_name
project_name\Scripts\activate
```

## File Structure


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

## Update package information
- LICENSE
- README.md
- setup.py
- setup.cfg
- MANIFEST.in


## Build the package

`\pypi-packag-creation\python setup.py sdist bdist_wheel`

## Test your package locally
- Install newly created packge localy to make sure it is working fine

`\pypi-packag-creation\pip install -e .`

- pytest

## Upload and test the package on test.pypi.org

`twine upload .\dist\my-first-package-0.0.1\* --repository-url https://test.pypi.org/legacy/`

## Upload to the pypi.org

`twine upload .\dist\my-first-package-0.0.1\*`

## Upload the source files to github.com




Resources:

[Publishing (Perfect) Python Packages on PyPi](https://www.youtube.com/watch?v=GIF3LaRqgXo)












