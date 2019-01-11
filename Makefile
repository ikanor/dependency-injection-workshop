.PHONY: tests shell docs clean

BASE_SERVICE=base

TESTS_SERVICE=tests

DOCS_SERVICE=docs

shell:
	docker-compose run --rm ${TESTS_SERVICE} sh -c '/bin/sh'

test:
	docker-compose run --rm ${TESTS_SERVICE} sh -c 'mamba tests -f documentation'

clean:
	docker-compose stop; docker-compose rm --all -f
