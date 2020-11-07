from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

keywords = '''
    disk usage
'''
dependencies = 'docopt inform>=1.9 arrow quantiphy>=2.0'

setup(
    name = 'excavate',
    version = '1.0',
    description = 'understand disk usage over time',
    long_description = readme,
    author = "Ken Kundert",
    author_email = 'excavate@nurdletech.com',
    url = 'https://github.com/kenkundert/excavate',
    download_url = 'https://github.com/kenkundert/excavate/tarball/master',
    license = 'GPLv3+',
    zip_safe = False,
    scripts = 'excavate'.split(),
    install_requires = dependencies.split(),
    keywords = keywords.split(),
    classifiers = [
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.6',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
        'Programming Language :: Python :: 3.9',
        'Topic :: Utilities',
    ],
)
