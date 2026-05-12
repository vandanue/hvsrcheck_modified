import setuptools

with open("README.md","r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="hvsrcheck_modified",
    version="0.2",
    author="Annora Vandanu Erlangga",
    author_email="annora.vandanu@ui.ac.id",
    description="Program to check reliable and clear peak of H/V curve. Edited program from khalqillah's repository",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/vandanue/hvsrcheck_modified",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires='>=3.7',
)
