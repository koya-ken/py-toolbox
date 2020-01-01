from setuptools import setup, find_packages

install_requires = ['tqdm>=4.10.0']

setup(name="py_toolbox",
      version="0.1",
      description="python script utility",
      url="https://github.com/koya-ken/py-toolbox",
      install_requires=install_requires,
      packages=find_packages(),
      )
