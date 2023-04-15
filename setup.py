import os
from pathlib import Path
from setuptools import setup, find_packages

this_directory = Path(__file__).parent
long_description = (this_directory / "README.md").read_text()

print(long_description)

if __name__ == '__main__':
    setup(
        name='dauth',
        version=os.getenv('PACKAGE_VERSION', '0.1'),
        package_dir={'': 'src'},
        packages=find_packages('src', include=[
            'dauth*'
        ]),
        description='FastAPI ABAC authorization realization',
        long_description=long_description,
        long_description_content_type='text/markdown',
    )
