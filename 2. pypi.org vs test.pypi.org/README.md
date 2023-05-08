# pypi.org vs test.pypi.org

In development phase of a new package, you need to make sure that the package would work properly.
For this reason, pypi preapared a test system on which you can upload your package first.
During the test period, you can ask your community to install it and give you feedback.

Install from the test website is similar to pypi installation. However, you need to use the --index-url or -i switch to give your test package address.

`python3 -m pip install --index-url https://test.pypi.org/simple/ your-package`

`pip install -i https://test.pypi.org/simple/ your-package`

[odoolv, odoo log viewer ](https://test.pypi.org/project/odoolv/)




Resources:

[Using TestPyPI](https://packaging.python.org/en/latest/guides/using-testpypi/)

