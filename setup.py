from setuptools import setup, find_packages

setup(
    name="compressor",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "click",
    ],
    entry_points={
        "console_scripts": [
            "compressor=main:compressor",  # command_name = file:function
        ],
    },
)
