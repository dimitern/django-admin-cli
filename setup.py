from setuptools import setup, find_packages
import admin_cli

with open('README.rst') as f:
    readme = f.read()

setup(
    name='django-admin-cli',
    version=admin_cli.__version__,
    url=admin_cli.__url__,
    description=admin_cli.__doc__,
    long_description=readme,
    author='ZuluPro (Anthony MONTHE)',
    author_email='anthony.monthe@gmail.com',
    license=admin_cli.__license__,
    platforms='any',
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Environment :: Console',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'Intended Audience :: System Administrators',
        'Natural Language :: English',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Framework :: Django',
    ],
    packages=find_packages(exclude=['tests.runtests.main']),
    include_package_data=True,
    test_suite='tests.runtests.main',
    install_requires=[],
)
