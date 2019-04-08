from setuptools import find_packages
from setuptools import setup

package_name = 'pyueye_manager'

setup(
    name=package_name,
    version='0.6.2',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    author='skconan',
    author_email='supakit.kr@gmail.com',
    maintainer='skconan',
    maintainer_email='supakit.kr@gmail.com',
    keywords=['ROS'],
    classifiers=[
        'Intended Audience :: Developers',
        'License :: OSI Approved :: Apache Software License',
        'Programming Language :: Python',
        'Topic :: Software Development',
    ],
    description='Package containing GUI of ueye manager',
    license='Apache License, Version 2.0',
    test_suite='test',
    entry_points={
        'console_scripts': [
            'main = pyueye_manager.pyueye_manager:main'
        ],
    },
    
    
)