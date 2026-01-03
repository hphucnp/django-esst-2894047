# Development commands for Django project with pip-tools

.PHONY: install install-dev update-deps sync help

# Install production dependencies
install:
	pip-sync requirements.txt

# Install development dependencies
install-dev:
	pip-sync dev-requirements.txt

# Update requirements files (recompile from .in files)
update-deps:
	pip-compile --upgrade requirements.in
	pip-compile --upgrade dev-requirements.in

# Sync environment with current requirements
sync:
	pip-sync dev-requirements.txt

# Install/upgrade pip-tools
install-pip-tools:
	pip install --upgrade pip-tools

# Show help
help:
	@echo "Available commands:"
	@echo "  install          - Install production dependencies"
	@echo "  install-dev      - Install development dependencies"  
	@echo "  update-deps      - Update requirements files from .in files"
	@echo "  sync             - Sync environment with requirements"
	@echo "  install-pip-tools - Install/upgrade pip-tools"
	@echo "  help             - Show this help message"