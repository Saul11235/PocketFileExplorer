from setuptools  import find_packages
from setuptools  import setup

f=open("README.md","r")
readme_file=f.read()
f.close()


setup(

        name         = "pocketFileExplorer",
        version      = "0.0.0.1",
        description  = "share your files in an simple web app in a few code lines",
        author       = "Edwin Pareja",
        author_email = "edwinsaulpm@gmail.com",
        url          = "https://www.illarisoft.com/",
        long_description=readme_file,
        long_description_content_type="text/markdown",
        packages=find_packages(),

        )
