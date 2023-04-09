from setuptools import setup, find_packages

import os

if __name__ == '__main__':
    setup(
        name='dauth',
        version=os.getenv('PACKAGE_VERSION', '0.0.1'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'dauth*'
        ]),
        description='FastAPI ABAC authorization realization',
    )
