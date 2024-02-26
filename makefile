build:
	cd CraftyLlamaProto && make python && cp -r generated ../ && rm -rf generated
