from setuptools import setup

setup(
    name='iot_camera',
    version='0.1',
    packages=['iot_camera'],
    url='https://github.com/pawelkolodziej/iot_camera',
    license='MIT',
    author='PawelK',
    author_email='pakolodziej@gmail.com',
    description='Raspberry PI - if motion detect, make a preview and send as puhs notofication',
    install_requires=['picamera','flask']
)
