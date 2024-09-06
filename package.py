name = "studiolibrary"

version = "2.16.0"

authors = [
    "krathjen",
    "Jeremy Andriambolisoa",
]

description = \
    """
    Manage poses, animation and digital assets in Autodesk Maya.
    """

requires = [
    "python-3+",
    "maya-2025+"
]

uuid = "krathjen.studiolibrary"

build_command = 'python {root}/build.py {install}'

def commands():
    env.PYTHONPATH.append("{root}/python/studiolibrary")