from setuptools import setup, find_packages

setup(
    name="django-inspect",
    version="0.3.2",
    description="Provides inspection conveniences for django models",
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
