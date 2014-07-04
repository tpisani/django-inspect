from setuptools import setup, find_packages

setup(
    name="django-inspect",
    description="Provides information about django models by a series of conveniences",
    long_description=open("README.md").read(),
    version="0.3",
    packages=find_packages(),
    author="Thiago Pisani",
    author_email="pisani.thiago@gmail.com",
    url="https://github.com/tpisani/django-inspect",
    license="BSD",
    install_requires=["Django"],
    classifiers=[
        "Environment :: Web Environment",
        "Framework :: Django",
        "Intended Audience :: Developers",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 2.7",
    ],
)
