from setuptools import find_packages, setup

package_name = 'panda_vision'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='Kanak Goyal',
    maintainer_email='kanakgoyal13@gmail.com',
    description='Color detection package for red, green, and blue object tracking',
    license='MIT',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
        'console_scripts': [
            'color_detector = panda_vision.color_detector:main',
        ],
    },
)
