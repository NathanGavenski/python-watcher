from setuptools import find_packages, setup

with open("README.md", "r") as f:
    long_description = f.read()

setup(
    name="watcher-cli",
    version="0.0.1",
    description="A watcher for running python code when after every modification",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/NathanGavenski/python-watcher",
    author="NathanGavenski",
    author_email="nathangavenski@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3.10",
        "Operating System :: OS Independent",
    ],
    install_requires=["watchdog"],
    extras_require={
        "dev": ["pytest>=7.0", "twine>=4.0.2", "pylint>=2.17"],
    },
    python_requires=">=3.10",
    entry_points={
        'console_scripts': [
            'watcher=watcher:main'
        ]
    },
)
