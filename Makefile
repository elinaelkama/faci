# Discord Bot (FACI) Makefile
# ================================

.PHONY: help install venv activate run test clean lint format docker-build docker-run dev

help:
	@echo "Available commands:"
	@echo "  help         - Show this help message"
	@echo "  venv         - Create virtual environment"
	@echo "  install      - Install dependencies"
	@echo "  run          - Run the Discord bot"
	@echo "  test         - Run tests"
	@echo "  lint         - Run linting checks"
	@echo "  format       - Format code with black"
	@echo "  clean        - Clean up cache files"
	@echo "  docker-build - Build Docker image"
	@echo "  docker-run   - Run Docker container"
	@echo "  dev          - Setup development environment"

venv:
	python -m venv venv
	@echo "Virtual environment created. Activate with: .\venv\Scripts\Activate.ps1"

install:
	pip install -r requirements.txt

install-dev:
	pip install -r requirements.txt
	pip install -r requirements.dev.txt

run:
	python main.py

test:
	python -m unittest discover test -v

test-coverage:
	python -m coverage run -m unittest discover test
	python -m coverage report -m

lint:
	python -m flake8 . --exclude=venv,__pycache__
	python -m mypy . --exclude=venv

format:
	python -m black . --exclude=venv

clean:
	@echo "Cleaning up cache files..."
	if exist "__pycache__" rmdir /s /q __pycache__
	if exist "commandHandlers\__pycache__" rmdir /s /q commandHandlers\__pycache__
	if exist "eventHandlers\__pycache__" rmdir /s /q eventHandlers\__pycache__
	if exist "helpers\__pycache__" rmdir /s /q helpers\__pycache__
	if exist "healthCheck\__pycache__" rmdir /s /q healthCheck\__pycache__
	if exist "test\__pycache__" rmdir /s /q test\__pycache__
	if exist ".coverage" del .coverage
	if exist ".mypy_cache" rmdir /s /q .mypy_cache
	if exist ".pytest_cache" rmdir /s /q .pytest_cache
	@echo "Cache files cleaned!"

docker-build:
	docker build -t faci-discord-bot .

docker-run:
	docker run --env-file .env faci-discord-bot

#docker save -o faci-bot-1.2.0.tar faci-bot:1.2.0

dev: venv install-dev
	@echo "Development environment setup complete!"
	@echo "Activate virtual environment with: .\venv\Scripts\Activate.ps1"

quick-start: install run

health:
	@echo "Checking bot status..."
	python -c "import requests; print('Health check endpoint:', requests.get('http://localhost:8080/health').status_code)" 2>nul || echo "Health check server not running"

info:
	@echo "Python version:"
	python --version
	@echo "Pip version:"
	pip --version
	@echo "Virtual environment:"
	where python

backup:
	@echo "Creating backup..."
	powershell Compress-Archive -Path *.py,*.txt,*.md,Dockerfile,Makefile,commandHandlers,eventHandlers,helpers,healthCheck,test -DestinationPath "faci-backup-$(Get-Date -Format 'yyyy-MM-dd-HHmm').zip"
	@echo "Backup created!"