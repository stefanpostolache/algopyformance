from setuptools import find_packages, setup

setup(
    name='sp_algopyformance',
    packages=find_packages(include=['sp_algopyformancelib']),
    version='0.1.0',
    description="A package to aid students of ISCTE in testing their algorithms",
    author="Stefan Postolache",
    license='MIT',
    install_requires=['Pillow', 'cycler', 'matplotlib', 'seaborn', 'pandas',
                      'numpy', 'typing', 'typing-extensions', 'fonttools',
                      'kiwisolver', 'packaging', 'pyparsing',
                      'python-dateutil', 'pytz', 'scipy', 'six'],
    setup_requires=['pytest-runner'],
    tests_require=['pytest==4.4.1'],
    test_suite='tests'
)