from setuptools import setup

setup(
    name='fouriest_transform',
    version='1.0.4',
    packages=['fouriest_transform'],
    entry_points={
        'console_scripts': [
            'fouriest_transform = fouriest_transform.fouriest_transform:main',
        ],
    },
)
