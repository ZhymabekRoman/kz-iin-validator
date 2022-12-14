from setuptools import setup
from os import path


with open(path.join(path.abspath(path.dirname(__file__)), "README.md"), encoding="utf-8") as f:
    readme_description = f.read()


def read_requirements(filename):
    with open(filename, "r", encoding="utf-8") as fp:
        return fp.read().strip().splitlines()


setup(
    name="kz_iin_validator",
    version="0.2.0",
    author="Zhymabek Roman",
    author_email="robanokssamit@yandex.ru",
    long_description=readme_description,
    long_description_content_type="text/markdown",
    include_package_data=True,
    url="https://github.com/ZhymabekRoman/kz-iin-validator",
    license="LICENSE.txt",
    description="Kazakhstan IIN parser and validator",
    install_requires=read_requirements("requirements.txt")
)
