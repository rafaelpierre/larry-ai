rebuild:
	cd ui && yarn install && yarn build && cd .. && docker build -t larry .

python:
	rm -rf src/larry/www && \
	mkdir src/larry/www && \
	cd ui && yarn install && \
	yarn build && \
	cp -r build/* ../src/larry/www && \
	cd ../ && \
	python -m build ./src

install:
	pip install ./src/dist/larry-0.0.1-py3-none-any.whl --force-reinstall