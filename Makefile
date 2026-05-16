.PHONY: install dev api orchestrator edge seed test lint fmt docker-up docker-down zip

install:
	python -m venv .venv
	. .venv/bin/activate && pip install -U pip && pip install -e '.[dev,providers]'

dev: docker-up
	@echo "Cloud API: http://localhost:8080/docs"
	@echo "Run API with: make api"

api:
	uvicorn apps.api.main:app --host 0.0.0.0 --port 8080 --reload

orchestrator:
	python -m apps.orchestrator.main

edge:
	python -m apps.edge_agent.main

seed:
	python scripts/seed_agents.py

test:
	pytest -q

lint:
	ruff check .

fmt:
	ruff format .

docker-up:
	docker compose up -d postgres redis mosquitto minio

docker-down:
	docker compose down

zip:
	cd .. && zip -r agri-agent-mesh.zip agri-agent-mesh -x 'agri-agent-mesh/.venv/*' 'agri-agent-mesh/data/*'
