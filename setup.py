import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
     name='reachy_screen',  
     version='1.0',
     author="Elisa Bianchi",
     author_email="elisa.bianchi@epfl.ch",
     description="Reachy's touchscreen interaction package",
     long_description=long_description,
   long_description_content_type="text/markdown",
     url="https://github.com/cest-elisa",
     packages=setuptools.find_packages(),
     classifiers=[
         "Programming Language :: Python :: 3",
         "License :: OSI Approved :: MIT License",
         "Operating System :: OS Independent",
     ],
 )
