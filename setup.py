from setuptools import setup, find_packages

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()

setup(
    name="fossdev-automation",
    version="0.1.2",
    author="waqque",
    author_email="waqqueta@gmail.com",
    description="Automation tools for Python development with Makefile",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/waqque/buzinaeva_tv_fossdev",
    project_urls={
        "Repository": "https://github.com/waqque/buzinaeva_tv_fossdev",
    },
    packages=find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.8",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
    install_requires=[
        "mypy>=1.0.0",
        "black>=23.0.0",
        "flake8>=6.0.0",
        "requests>=2.28.0",
    ],
    entry_points={
        "console_scripts": [
            "fossdev=fossdev_utils.cli:main",
        ],
    },
)
