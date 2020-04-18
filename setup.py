from setuptools import setup, find_packages

setup(
    name="gameoflife",
    version="0.0.0",
    description="A python and curses implementaiton of Conway's Game of Life",
    url="https://github.com/nsprenkle/game-of-life",
    author="Nathan Sprenkle",
    author_email="nathan.sprenkle@gmail.com",
    license="gpl-3.0",
    packages=find_packages(),
    zip_safe=False,
)
