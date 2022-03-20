import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setuptools.setup(
    name="autopack",
    version="1.0.0",
    author="jiayou.liu",
    author_email="1229738142@qq.com",
    description="A mqtt protocol sub & pub secondary packaging",
    long_description=long_description,
    long_description_content_type="text/markdown",
    install_requires=["paho-mqtt"],
    url="https://github.com/Grapeskin/python-learn",
    project_urls={
        "Bug Tracker": "https://github.com/Grapeskin/python-learn/issues",
    },
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    package_dir={"": "."},
    packages=setuptools.find_packages(include=("autopack_mqtt",)),
    python_requires=">=3.8",
)
