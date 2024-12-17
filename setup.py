import setuptools
from setuptools import setup, find_packages

with open("README.md","r",encoding="utf-8") as f:
    long_description = f.read()
    
    
__version__="1.0.0"

repo_name="Text-Summarizer-Project",
author_user_name="arohi",
src_repo="text-summarizer",
author_email="arohi@gmail.com",



setuptools.setup(
    name="Text-Summarizer",
    version="1.0.0",
    author="arohi",
    author_email="arohi@gmail.",
    description="A Text Summarization Project",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url=f"https://github.com/{author_user_name}/{repo_name}",
    project_urls={
        "Bug Tracker": f"https://github.com/{author_user_name}/{repo_name}/issues",
    },
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
    