from setuptools import setup, find_packages

setup(
    name="aroontest",
    version="0.1.0",
    description="A Python package to pull the latest stock data and calculate the Aroon indicator.",
    author="Your Name",
    author_email="your.email@example.com",
    url="https://github.com/samueloskinner/aroontest",
    license="MIT",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "requests",
        "pandas",
        "numpy",
        "yfinance",
        "matplotlib",
    ],
    extras_require={
        "testing": [
            "pytest",
            "pytest-cov",
        ],
    },
    python_requires=">=3.6",
)