react:
	cd ui && yarn install && yarn build

python:
	rm -rf ./src/build && rm -rf ./src/dist && \
	pip install 'build<0.10.0' && python -m build ./src/ --wheel --outdir dist/

install:
	pip install ./dist/larry_ai-0.0.1-py3-none-any.whl --force-reinstall