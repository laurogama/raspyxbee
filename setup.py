from distutils.core import setup

setup(
    name='snakebed',
    version='0.1',
    packages=['commandHandler'],
    url='',
    license='MIT',
    author='laurogama',
    author_email='lauro.gama@fpf.br',
    description='Flask Api to comunicate with Xbee devices',
    install_requires=['Flask==0.10.1','Flask-RESTful==0.3.0','Flask-Bootstrap==3.3.0.1']
)
