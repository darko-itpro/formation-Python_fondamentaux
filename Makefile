.PHONY: setup clean

setup:
	pip install --upgrade pip
	pip install --upgrade -r requirements.txt
	pip install --upgrade -r requirements-xtra.txt

clean:
	rm -rf data
	rm -rf site
