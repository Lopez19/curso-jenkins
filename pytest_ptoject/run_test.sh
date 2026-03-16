#!/bin/bash
echo "Install the dependencies from pyproject.toml"
pip install -e .[dev]

echo "Run the tests"
pytest tests/ --junit-xml=reports/test-results.xml --html=reports/test-report.html --self-contained-html

echo "Pruebas finalizadas resultados en reports/"