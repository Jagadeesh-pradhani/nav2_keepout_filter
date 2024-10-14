from setuptools import find_packages, setup
import os
from glob import glob

package_name = 'nav2_keepout_filter'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
        (os.path.join('share', package_name, 'launch'), glob('launch/*.*')),
        (os.path.join('share', package_name, 'params'), glob('params/*.*')),
        (os.path.join('share', package_name, 'map'), glob('map/*.*')),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='intel',
    maintainer_email='intel@todo.todo',
    description='TODO: Package description',
    license='TODO: License declaration',
    # tests_require=['pytest'],
    extras_require={'test':['pytest'],},
    entry_points={
        'console_scripts': [
        ],
    },
)
