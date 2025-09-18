#!/bin/sh
set -euo pipefail

export PYTHONPATH="$(pwd)"

pytest -v --tb=short --html=reports/report.html --self-contained-html

