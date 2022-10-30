import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="pyledstrip-k0hax",
    version="0.0.7",
    author="Michael Englehorn",
    author_email="michael@englehorn.com",
    description="A bundle of utilities for ws281x based LED strips",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/k0hax/pyledstrip-k0hax",
    project_urls={
        "Bug Tracker": "https://github.com/k0hax/pyledstrip-k0hax/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "src"},
    packages=setuptools.find_packages(where="src"),
    python_requires=">=3.9",
    install_requires=[
        'rpi-ws281x>=4.3.3',
    ],
)

