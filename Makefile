.PHONY: tests shell docs clean

BASE_SERVICE=base

TESTS_SERVICE=tests

DOCS_SERVICE=docs

shell:
	docker-compose run --rm ${TESTS_SERVICE} sh -c '/bin/sh'

tests:
	docker-compose run --rm ${TESTS_SERVICE} sh -c 'mamba tests -f documentation'

docs:
	docker-compose run --rm ${DOCS_SERVICE} sh -c 'cd docs; sphinx-build -b html . build'

clean:
	docker-compose stop; docker-compose rm --all -f
