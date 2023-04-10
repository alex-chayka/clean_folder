from setuptools import setup

setup(name='clean_folder',
      version='1.0.0',
      description='Script to clean folders',
      entry_points={'console_scripts': ['clean-folder = clean_folder.clean:main']})
