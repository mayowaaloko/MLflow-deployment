import setuptools


with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


repo_name = "MLflow-deployment"
author_name = "Daniel"
src_dir = "mlproject"
author_email = "mayowaaloko@gmail.com"


setuptools.setup(
    name=repo_name,
    version="0.0.1",
    author=author_name,
    author_email=author_email,
    description="A machine learning project setup",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/mayowaaloko/mlflow-deployment",
    project_urls={
        "Bug Tracker": "https://github.com/mayowaaloko/mlflow-deployment/issues",
    },
    package_dir={"": src_dir},
    packages=setuptools.find_packages(where=src_dir),
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.6",
)
