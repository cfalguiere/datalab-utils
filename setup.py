from setuptools import setup

def readme():
    with open('README.rst') as f:
        return f.read()

setup(name='easydatalab',
      version='0.1',
      description='The funniest datalab tool in the world',
      url='https://github.com/cfalguiere/easydatalab',
      author='Claude Falguiere',
      author_email='',
      license='MIT',
      packages=['easydatalab'],
      include_package_data=True
      zip_safe=False,

      test_suite='nose.collector',
      tests_require=['nose'])
