# pypi-packag-creation
file structure:
```
base_dir
      \ setup.py
      \ LICENSE
      \ README.md
      \ src_dir
             \ __init__.py
             \ package_name.py
```
1. Build your package
 
 `\base_dir\python setup.py sdist bdist_wheel`
 
2. Install newly created packge localy to make sure it is working fine
 
 `\base_dir\python install -e .`
 
 3.  

