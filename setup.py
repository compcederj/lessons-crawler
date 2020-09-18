# -*- coding: utf-8 -*-

# DO NOT EDIT THIS FILE!
# This file has been autogenerated by dephell <3
# https://github.com/dephell/dephell

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

readme = ''

setup(
    long_description=readme,
    name='lessons-crawler',
    version='0.2.0',
    python_requires='==3.*,>=3.8.0',
    author='Thiago da Cunha Borges',
    author_email='thiagoborges@id.uff.br',
    entry_points={
        "console_scripts": ["lessons-crawler = lessons_crawler.cli:cli"]
    },
    packages=[
        'lessons_crawler', 'lessons_crawler.app', 'lessons_crawler.cli',
        'lessons_crawler.dao', 'lessons_crawler.helpers',
        'lessons_crawler.models'
    ],
    package_dir={"": "."},
    package_data={},
    install_requires=[
        'beautifulsoup4==4.*,>=4.9.1', 'click==7.*,>=7.1.2',
        'lxml==4.*,>=4.5.2', 'psycopg2-binary==2.*,>=2.8.6',
        'python-dotenv==0.*,>=0.14.0', 'requests==2.*,>=2.24.0',
        'sqlalchemy==1.*,>=1.3.19', 'xmltodict==0.*,>=0.12.0'
    ],
    extras_require={
        "dev": [
            "black==20.*,>=20.8.0.b1", "ipython==7.*,>=7.18.1",
            "isort==5.*,>=5.5.2", "pytest==5.*,>=5.2.0"
        ]
    },
)
