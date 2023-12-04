# build: test lint poetry-export
lint:
	cfn-lint template.yaml -a cfn_lint_serverless.rules

build: lint
	sam build --parallel --cached

deploy: build
	sam deploy

release: build
	sam deploy --config-env prod

# test:
# 	pytest tests/unit/

clean:
	find . \
		   -type f -name '*.py[co]'         -delete \
		-o -type f -name 'requirements.txt' -delete \
		-o -type d -name __pycache__        -delete
	rm -rf .pytest_cache/

purge: clean
	sam delete --no-prompts
	rm -rf .aws-sam/

dev-init:
	poetry install --no-root

dev-deps:
	poetry update
	poetry export -f requirements.txt --output requirements.txt
	cp requirements.txt purple_p_e2/
	cp requirements.txt purple_s_e1/
	cp requirements.txt purple_s_e3/
	rm ./requirements.txt
