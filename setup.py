from setuptools import setup, find_packages
from os import path


with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme_description = f.read()


def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read().strip().splitlines()


setup(
    name="kz_iin_validator",
    version="0.6.0",
    python_requires='>=3.7',
    author="Zhymabek Roman",
    author_email="robanokssamit@yandex.ru",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    packages=find_packages(exclude=["tests", "images"]),
    url="https://github.com/ZhymabekRoman/kz-iin-validator",
    license="MIT",
    description="Kazakhstan IIN parser and validator",
    install_requires=read_requirements("requirements.txt"),
)
