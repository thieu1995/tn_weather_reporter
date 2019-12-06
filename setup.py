from setuptools import setup

def readme():
    with open('README.md') as f:
        README = f.read()
    return README


setup(
    name="tn_weather_reporter",
    version="0.1.0",
    description="A Python package to get weather reports for any location.",
    long_description=readme(),
    long_description_content_type="text/markdown",
    url="https://github.com/thieunguyen5991/tn_weather_reporter",
    author="Thieu Nguyen",
    author_email="nguyenthieu2102@gmail.com",
    license="MIT",
    classifiers=[
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.7",
    ],
    packages=["weather_reporter"],
    include_package_data=True,
    install_requires=["requests"],
    entry_points={
        "console_scripts": [
            "tn_weather_reporter=weather_reporter.cli:main",
        ]
    },
)