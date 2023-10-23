from setuptools import setup

package_name = 'fleet_management'

setup(
    name=package_name,
    version='0.0.1',
    packages=[package_name],
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=[
        'setuptools',
    ],
    zip_safe=True,
    maintainer='Ali',
    maintainer_email='vahidovakbarali@gmail.com',
    description='ROS 2 package for fleet management',
    license='Apache License 2.0',
    tests_require=['pytest'],
    entry_points={
        'console_scripts': [
            'fleet_management_server_cli = fleet_management.fleet_management_server_cli:main',
            'fleet_management_client_cli = fleet_management.fleet_management_client_cli:main',
        ],
    },
)

