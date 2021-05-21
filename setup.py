import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()


setuptools.setup(
    name='docker-esopmoc',
    version='0.1',
    scripts=['docker-esopmoc'],
    author="Ali marefati",
    author_email="marefati110@gmail.com",
    description="generate docker compose file from running containers",
    long_description=long_description,
    long_description_content_type="text/markdown",
    download_url='https://github.com/marefati110/mysql-pydump/archive/0.1.1.tar.gz',
    url="https://github.com/javatechy/dokr",
    packages=setuptools.find_packages(),
    classifiers=[
        "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
    ],
)
