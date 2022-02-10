from setuptools import find_packages, setup

with open("Readme.md") as fh:
    long_description = fh.read()

setup(
    name='sp_algopyformance',
    packages=find_packages(include=['sp_algopyformancelib']),
    version='0.1.0',
    description="A package to aid students of ISCTE in testing their algorithms",
    long_description=long_description,
    long_description_content_type="text/markdown",
    url="https://github.com/stefanpostolache/algopyformance",
    author="Stefan Postolache",
    author_email="stefanogiovanochestii@gmail.com",
    license='MIT',
    install_requires=['Pillow', 'cycler', 'matplotlib', 'seaborn', 'pandas',
                      'numpy', 'typing', 'typing-extensions', 'fonttools',
                      'kiwisolver', 'packaging', 'pyparsing',
                      'python-dateutil', 'pytz', 'scipy', 'six'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests',
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)