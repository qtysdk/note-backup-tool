from setuptools import setup, find_packages

# Read the contents of your README file
with open('README.md', encoding='utf-8') as f:
    long_description = f.read()

setup(
    name='NoteBackupCLI',
    version='0.1',
    description='A simple command-line tool to back up notes, with HackMD integration.',
    long_description=long_description,
    long_description_content_type='text/markdown',
    author='Chan Ching Yi',
    author_email='chingyichan.tw@gmail.com',
    url='https://github.com/yourusername/NoteBackupCLI',
    packages=find_packages(),
    install_requires=[
        'requests>=2.30',
        'click>=8.0',
        'rich>=13.0',
        'mistune>=3.0'
    ],
    entry_points={
        'console_scripts': [
            'nbc = notebackupcli.main:main',
        ],
    },
    classifiers=[
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'License :: OSI Approved :: Apache Software License',
        'Operating System :: OS Independent',
    ],
    python_requires='>=3.10',
)
