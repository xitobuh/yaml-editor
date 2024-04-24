from setuptools import setup, find_packages

setup(
    name='yaml_editor',
    version='0.1',
    author='Your Name',
    author_email='youremail@example.com',
    maintainer='Your Name',
    maintainer_email='maintainer@example.com',
    description='A YAML Editor built with PySide6',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/yourusername/yaml_editor',
    license='MIT',
    classifiers=[
        'Development Status :: 3 - Alpha',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Programming Language :: Python :: 3',
        'Programming Language :: Python :: 3.9',
        'Programming Language :: Python :: 3.10',
        'Programming Language :: Python :: 3.11',
        'Programming Language :: Python :: 3.12',
        'Operating System :: OS Independent',
    ],
    keywords='yaml editor pyside6',
    packages=find_packages(),
    include_package_data=True,
    install_requires=[
        'PySide6',
        'PyYAML'
    ],
    entry_points={
        'console_scripts': [
            'yaml-editor = src.main:main'
        ]
    },
    platforms=['Windows', 'Linux'],
    python_requires='>=3.9',
)
