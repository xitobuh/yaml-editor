package:
	python3 setup.py sdist

install:
	pip install dist/yaml_editor-0.1.tar.gz

requirements:
	pip install -r requirements.txt