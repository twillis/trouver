import setuptools

install_requires = [
    'pyramid',
    'elasticsearch-dsl>=6.0.0',
    'tika'
]

setup_requires = [
    'setuptools_git',
    'pytest-runner'
]

tests_require = [
    'pytest',
    'pytest-cov',
    'webtest'
]

exclude_package_data = {
    '': ['.gitignore',
         '.dir-locals.el']
}

entry_points = {
    'console_scripts': [
        'trouver = trouver.command:main',
        'trouver-web = trouver.command:web_main',
        'trouver-scan = trouver.command:scanner_main'
    ]
}

setuptools.setup(
    name="trouver",
    version="0.1.0",
    url="",
    author="Tom Willis",
    author_email="Tom Willis",
    description="minmum full text search of files",
    long_description=open('README.rst').read(),
    packages=setuptools.find_packages(),
    install_requires=install_requires,
    setup_requires=setup_requires,
    tests_requires=tests_require,
    exclude_package_data=exclude_package_data,
    entry_points=entry_points,
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Programming Language :: Python',
        'Programming Language :: Python :: 3.6',
    ],
)
