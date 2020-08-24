import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pycatwire", # Replace with your own username
    version="0.0.1",
    author="Johannes K Becker",
    author_email="jkbecker@bu.edu",
    description="Python implementation of catwire/catwire.",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/catwire/pycatwire",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    install_requires=[
        'kaitaistruct',
    ],
    python_requires='>=3.6',
)
