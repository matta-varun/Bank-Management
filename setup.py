from setuptools import setup
setup(
    name = 'BANK-MANAGEMENT',
    version = '0.1.0',
    packages = ['bankmanagement'],
    entry_points = {
        'console_scripts': [
            'bankmanagement = bankmanagement.__main__:main'
        ]
    })