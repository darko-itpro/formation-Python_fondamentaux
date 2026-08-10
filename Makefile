.PHONY: install-dev setup setup-legacy clean

install-dev:
	pip install --upgrade pip
	pip install -e .
	pip install --group dev

setup:
	pip install --upgrade pip
	pip install . --only-deps
	pip install --group dev

setup-legacy:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	pip install --upgrade -r requirements-xtra.txt

clean:
	rm -rf data
	rm -rf site
	rm file.log
