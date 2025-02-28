from setuptools import setup, find_packages

setup(
    name="rpc-flask",
    version="0.1.0",
    packages=find_packages(),
    install_requires=[
        "flask",
    ],
    entry_points={
        "console_scripts": [
            "rpc=app.app:main",
        ],
    },
)