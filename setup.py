from setuptools import setup, find_packages

setup(
    name="sentinel-act",
    version="0.1.0",
    description="Legal-poetic shield for indie creators",
    author="Sir Benjamin, Grok",
    license="CC-BY-NC-4.0 + Eternal Seal",
    packages=find_packages(),
    entry_points={
        'console_scripts': [
            'sentinel_act=sentinel_act:main',
        ],
    },
    install_requires=[],  # Zero deps
)
