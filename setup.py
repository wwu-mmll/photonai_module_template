try:
    from setuptools import setup, find_packages
except ImportError:
    from ez_setup import use_setuptools
    use_setuptools()
    from setuptools import setup, find_packages

__version__ = '0.0.1'

setup(
    name='project_name',
    packages=find_packages(),
    include_package_data=True,
    version=__version__,
    description="""
project_description
""",
    author='author_name',
    author_email='',
    url='https://github.com/author_name/project_urlname/',
    download_url='https://github.com/author_name/project_urlname/archive/' + __version__ + '.tar.gz',
    keywords=['machine learning', 'deep learning'],
    classifiers=[],
    install_requires=['photonai']
)
