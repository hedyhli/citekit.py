# -*- coding: utf-8 -*-
from setuptools import setup

packages = \
['citekit']

package_data = \
{'': ['*']}

install_requires = \
['beautifulsoup4>=4.9.1,<5.0.0',
 'dateparser>=0.7.6,<0.8.0',
 'requests>=2.24.0,<3.0.0']

setup_kwargs = {
    'name': 'citekit',
    'version': '0.1.0',
    'description': 'Python library to cite websites, similar to citethisforme.com',
    'long_description': None,
    'author': 'Hedy Li',
    'author_email': 'hedyhyry@gmail.com',
    'maintainer': None,
    'maintainer_email': None,
    'url': None,
    'packages': packages,
    'package_data': package_data,
    'install_requires': install_requires,
    'python_requires': '>=3.8,<4.0',
}


setup(**setup_kwargs)
