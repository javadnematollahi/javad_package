from setuptools import setup


def pre_install():
    f = open("readme.md", "r")
    text = f.read()
    return text

setup(
    name= "javad_cow",
    version= "1.0.0",
    author="javad",
    description="A test package for pydeploy",
    long_description=pre_install(),
    requires=[],
    author_email="torang7189@gmail.com",
    packages=["javad_cow"]
)