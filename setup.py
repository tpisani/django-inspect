from setuptools import setup, find_packages

setup(
    name="django-inspect",
    description="Provides information about django models",
    version="0.1",
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
    ],
)
