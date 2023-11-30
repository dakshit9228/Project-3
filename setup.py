from distutils.core import setup

setup(
    name='building_analysis',
    version='0.0.2',
    description='Classes for technical analysis of building dataset.',
    author='Dakshit',
    author_email='dgolakiy@mail.yu.edu',
    license='MIT',
    url='https://github.com/dakshit9228/Project-3',
    packages=find_packages(where="my_package"),
    package_dir={"": "my_package"},
    install_requires=[
        'matplotlib>=3.0.2',
        'numpy>=1.15.2',
        'pandas>=0.23.4',
        'pandas-datareader>=0.7.0',
        'seaborn>=0.11.0',
        'statsmodels>=0.11.1',
    ],
)