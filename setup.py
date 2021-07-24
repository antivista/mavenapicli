from setuptools import setup, find_packages


def read_requirements():
    with open('requirements.txt', 'r') as req:
        content = req.read()
        requirements = content.split('\n')

    return requirements


setup(
    name='mavenapicli',
    version='0.1.0',
    packages=find_packages(),
    include_package_date=True,
    install_requires=read_requirements(),
    # maven_api_cli will be the name of the command, that will look -> maven_api_cli package ->
    # -> cli.py -> having a func named cli.
    entry_points={'console_scripts': ['mavenapicli = mavenapicli.cli:cli']}
)
