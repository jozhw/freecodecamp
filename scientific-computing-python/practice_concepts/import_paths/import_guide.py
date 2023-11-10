# for complete guide follow the link below
url = "https://chrisyeh96.github.io/2017/08/08/definitive-guide-python-imports.html"


"""
A simple work around when the directory stucture is like this:
/project
    /src
        __init__.py
        -main.py
        /module1
            ___init__.py
            -module1.py
    /test
        -test_main.py

if main.py imports from module1 then there will be an issue when using relative imports
when running main.py. The following is a solution I found online:

# if __package__ is None or __package__ == "":
#   from module1 import module1
# else:
#   from .module1 import module

"""

"""
The messy way of doing things is the following:
sys.path.append(os.path.dirname(os.path.dirname(os.path.realpath(__file__))))

"""
