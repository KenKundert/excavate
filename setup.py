from setuptools import setup

with open('README.rst') as f:
    readme = f.read()

keywords = '''
    disk usage
'''
dependencies = 'docopt inform arrow quantiphy'

setup(
    name='excavate',
    version='1.0',
    description='understand disk usage over time',
    long_description=readme,
    author="Ken Kundert",
    author_email='excavate@nurdletech.com',
    license='GPLv3+',
    zip_safe=True,
    scripts='excavate'.split(),
    install_requires=dependencies.split(),
    keywords=keywords.split(),
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
        'Natural Language :: English',
        'Operating System :: POSIX :: Linux',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
        'Topic :: Utilities',
    ],
)
