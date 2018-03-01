# -*- coding: utf-8 -*-
#
# This file is part of Zenodo.
# Copyright (C) 2015, 2016 CERN.
#
# Zenodo is free software; you can redistribute it
# and/or modify it under the terms of the GNU General Public License as
# published by the Free Software Foundation; either version 2 of the
# License, or (at your option) any later version.
#
# Zenodo is distributed in the hope that it will be
# useful, but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with Zenodo; if not, write to the
# Free Software Foundation, Inc., 59 Temple Place, Suite 330, Boston,
# MA 02111-1307, USA.
#
# In applying this license, CERN does not
# waive the privileges and immunities granted to it by virtue of its status
# as an Intergovernmental Organization or submit itself to any jurisdiction.

"""Zenodo - Research. Shared."""

import os

from setuptools import find_packages, setup

readme = open('README.rst').read()
history = open('CHANGES.rst').read()

tests_require = [
    'check-manifest>=0.35',
    'coverage>=4.4.1',
    'isort>=4.2.15',
    'pydocstyle>=2.0.0',
    'pytest-cache>=1.0',
    'pytest-cov>=2.5.1',
    'pytest-flask>=0.10.0',
    'pytest-mock>=1.6.0',
    'pytest-pep8>=1.0.6',
    'pytest-random-order>=0.5.4',
    'pytest>=3.3.1',
    'selenium>=3.5.0,<3.6.0',
    'six>=1.10.0',
]

db_version = '>=1.0.0b9'
search_version = '>=1.0.0b4'

extras_require = {
    'docs': [
        'Sphinx>=1.5,<1.6',
    ],
    # Database version
    'postgresql': [
        'invenio-db[postgresql,versioning]{}'.format(db_version),
    ],
    'mysql': [
        'invenio-db[mysql,versioning]{}'.format(db_version),
    ],
    'sqlite': [
        'invenio-db[versioning]{}'.format(db_version),
    ],
    # Elasticsearch version
    'elasticsearch2': [
        'invenio-search[elasticsearch2]{}'.format(search_version),
    ],
    # 'elasticsearch5': [
    #     'invenio-search[elasticsearch5]{}'.format(search_version),
    # ],
    # 'elasticsearch6': [
    #     'invenio-search[elasticsearch5]{}'.format(search_version),
    # ],
    'tests': tests_require,
}

extras_require['all'] = []
for name, reqs in extras_require.items():
    if name in ('postgresql', 'mysql', 'sqlite', 'elasticsearch2',
                'elasticsearch5', 'elasticsearch6'):
        continue
    extras_require['all'].extend(reqs)

# Do not include in all requirement
extras_require['xrootd'] = [
    'invenio-xrootd>=1.0.0a6',
    'xrootdpyfs>=0.1.5',
]

setup_requires = [
    'Babel>=2.4.0',
    'pytest-runner>=2.7.0',
]

install_requires = [
    'arrow>=0.10.0',
    'bleach>=2.0.0',
    'CairoSVG>=1.0.22,<2.0.0',
    'citeproc-py-styles>=0.1.0',
    'citeproc-py>=0.4.0',
    'datacite>=1.0.0',
    'dcxml>=0.1.0',
    'dojson>=1.3.2',
    'Flask>=0.12.2',
    'Flask-Admin>=1.5.0',
    'Flask-BabelEx>=0.9.3',
    'Flask-Caching>=1.3.2',
    'Flask-Debugtoolbar>=0.10.1',
    'ftfy>=4.4.3,<5',
    'idutils>=1.0.0',
    'invenio-access>=1.0.0b1',
    'invenio-accounts>=1.0.0b12',
    'invenio-admin>=1.0.0b4',
    'invenio-app>=1.0.0b2',
    'invenio-assets>=1.0.0b7',
    'invenio-base>=1.0.0b1',
    'invenio-cache>=1.0.0b1',
    'invenio-celery>=1.0.0b3',
    'invenio-communities>=1.0.0a19',
    'invenio-config>=1.0.0b3',
    'invenio-csl-rest>=1.0.0a1',
    'invenio-deposit>=1.0.0a9',
    'invenio-files-rest>=1.0.0a21',
    'invenio-formatter>=1.0.0b3',
    'invenio-github>=1.0.0a15',
    'invenio-i18n>=1.0.0b4',
    'invenio-indexer>=1.0.0b1',
    'invenio-jsonschemas>=1.0.0a7',
    'invenio-logging>=1.0.0b3',
    'invenio-mail>=1.0.0b1',
    'invenio-marc21>=1.0.0a6',
    'invenio-migrator>=1.0.0a9',
    'invenio-oaiserver>=1.0.0b2',
    'invenio-oauth2server>=1.0.0b3',
    'invenio-oauthclient[github]>=1.0.0b3',
    'invenio-openaire>=1.0.0a11',
    'invenio-opendefinition>=1.0.0a7',
    'invenio-pidrelations>=1.0.0a3',
    'invenio-pidstore>=1.0.0b2',
    'invenio-previewer>=1.0.0a11',
    'invenio-records>=1.0.0b4',
    'invenio-records-files>=1.0.0a9',
    'invenio-records-rest>=1.0.0b6',
    'invenio-records-ui>=1.0.0b2',
    'invenio-rest[cors]>=1.0.0b2',
    'invenio-search-ui>=1.0.0a9',
    'invenio-sipstore>=1.0.0a7',
    'invenio-theme>=1.0.0b4',
    'invenio-userprofiles>=1.0.0b2',
    'invenio-webhooks>=1.0.0a4',
    'jsonref>=0.1',
    'jsonresolver>=0.2.1',
    'mock>=2.0.0',
    'Pillow>=4.2.0',
    'pycountry>=17.5.14',
    'python-slugify>=1.2.4',
    'raven>=6.3.0',
    'sickle>=0.6.1',
    'uwsgi>=2.0.15',
    'uwsgitop>=0.10',
    'wsgi-statsd>=0.3.1',
    'zenodo-accessrequests>=1.0.0a2',
]

packages = find_packages()


# Get the version string. Cannot be done with import!
g = {}
with open(os.path.join('zenodo', 'version.py'), 'rt') as fp:
    exec(fp.read(), g)
    version = g['__version__']

setup(
    name='zenodo',
    version=version,
    description=__doc__,
    long_description=readme + '\n\n' + history,
    keywords='zenodo research data repository',
    license='GPLv2',
    author='CERN',
    author_email='info@zenodo.org',
    url='https://github.com/zenodo/zenodo',
    packages=packages,
    zip_safe=False,
    include_package_data=True,
    platforms='any',
    entry_points={
        'console_scripts': [
            'zenodo = invenio_app.cli:cli',
        ],
        'flask.commands': [
            'audit = zenodo.modules.auditor.cli:audit',
            'github = zenodo.modules.github.cli:github',
            'utils = zenodo.modules.utils.cli:utils',
        ],
        'invenio_base.apps': [
            'flask_debugtoolbar = flask_debugtoolbar:DebugToolbarExtension',
            'zenodo_auditor = zenodo.modules.auditor.ext:ZenodoAuditor',
            'zenodo_communities = '
            'zenodo.modules.communities.ext:ZenodoCommunities',
            'zenodo_fixtures = zenodo.modules.fixtures.ext:ZenodoFixtures',
            'zenodo_sitemap = zenodo.modules.sitemap.ext:ZenodoSitemap',
            'zenodo_support = zenodo.modules.support.ext:ZenodoSupport',
            'zenodo_records = zenodo.modules.records.ext:ZenodoRecords',
            'zenodo_deposit = zenodo.modules.deposit.ext:ZenodoDeposit',
            'zenodo_jsonschemas = '
            'zenodo.modules.jsonschemas.ext:ZenodoJSONSchemas',
            'zenodo_openaire = zenodo.modules.openaire.ext:ZenodoOpenAIRE',
        ],
        'invenio_base.api_apps': [
            'zenodo_communities = '
            'zenodo.modules.communities.ext:ZenodoCommunities',
            'zenodo_deposit = zenodo.modules.deposit.ext:ZenodoDeposit',
            'zenodo_openaire = zenodo.modules.openaire.ext:ZenodoOpenAIRE',
            'zenodo_records = zenodo.modules.records.ext:ZenodoRecords',
        ],
        'invenio_base.blueprints': [
            'zenodo_communities = zenodo.modules.communities.views:blueprint',
            'zenodo_deposit = zenodo.modules.deposit.views:blueprint',
            'zenodo_frontpage = zenodo.modules.frontpage.views:blueprint',
            'zenodo_openaire = zenodo.modules.openaire.views:blueprint',
            'zenodo_support = zenodo.modules.support.views:blueprint',
            'zenodo_redirector = zenodo.modules.redirector.views:blueprint',
            'zenodo_search_ui = zenodo.modules.search_ui.views:blueprint',
            'zenodo_theme = zenodo.modules.theme.views:blueprint',
            'zenodo_spam = zenodo.modules.spam.views:blueprint',
            'zenodo_sitemap = zenodo.modules.sitemap.views:blueprint',
        ],
        'invenio_base.api_blueprints': [
            'zenodo_rest = zenodo.modules.rest.views:blueprint',
            'zenodo_deposit = zenodo.modules.deposit.views_rest:blueprint',
        ],
        'invenio_base.api_converters': [
            'file_key = zenodo.modules.deposit.utils:FileKeyConverter',
        ],
        'invenio_i18n.translations': [
            'messages = zenodo',
        ],
        'invenio_celery.tasks': [
            'zenodo_auditor = zenodo.modules.auditor.tasks',
            'zenodo_records = zenodo.modules.records.tasks',
            'zenodo_utils = zenodo.modules.utils.tasks',
            'zenodo_sipstore = zenodo.modules.sipstore.tasks',
            'zenodo_sitemap = zenodo.modules.sitemap.tasks',
        ],
        'invenio_config.module': [
            'zenodo = zenodo.config',
        ],
        'invenio_pidstore.minters': [
            'zenodo_record_minter '
            '= zenodo.modules.records.minters:zenodo_record_minter',
            'zenodo_deposit_minter '
            '= zenodo.modules.deposit.minters:zenodo_deposit_minter',
        ],
        'invenio_pidstore.fetchers': [
            'zenodo_record_fetcher '
            '= zenodo.modules.records.fetchers:zenodo_record_fetcher',
            'zenodo_deposit_fetcher '
            '= zenodo.modules.deposit.fetchers:zenodo_deposit_fetcher',
            'zenodo_doi_fetcher '
            '= zenodo.modules.records.fetchers:zenodo_doi_fetcher',
        ],
        'invenio_assets.bundles': [
            'zenodo_deposit_js = zenodo.modules.deposit.bundles:js_deposit',
            'zenodo_theme_css = zenodo.modules.theme.bundles:css',
            'zenodo_theme_js = zenodo.modules.theme.bundles:js',
            'zenodo_search_js = zenodo.modules.theme.bundles:search_js',
        ],
        'invenio_jsonschemas.schemas': [
            'zenodo_records = zenodo.modules.records.jsonschemas',
            'zenodo_deposit = zenodo.modules.deposit.jsonschemas',
            'zenodo_sipstore = zenodo.modules.sipstore.jsonschemas',
        ],
        'invenio_search.mappings': [
            'records = zenodo.modules.records.mappings',
            'deposits = zenodo.modules.deposit.mappings',
        ],
        'dojson.contrib.to_marc21': [
            'zenodo = zenodo.modules.records.serializers.to_marc21.rules',
        ],
    },
    extras_require=extras_require,
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_require=tests_require,
    classifiers=[
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v2 (GPLv2)',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
        'Topic :: Software Development :: Libraries :: Python Modules',
        'Programming Language :: Python :: 2',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.5',
        'Development Status :: 3 - Alpha',
    ],
)
