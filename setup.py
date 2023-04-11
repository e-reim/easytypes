import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name='easytypes',
    version='0.0.1',
    packages=setuptools.find_packages(),
    install_requires=["typeguard==3.0.2"],
    url='https://github.com/e-reim/easytypes',
    license='Apache Software License',
    author='Reim, Elijah',
    author_email='ellioh.72@gmail.com',
    description='Easily typed structures for Python with optional field presence checking and runtime type checking',
    long_description=long_description,
    long_description_content_type="text/markdown",
    python_requires='>=3.10',
    classifiers = [
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: Apache Software License",
        "Programming Language :: Python",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
    ]
)
