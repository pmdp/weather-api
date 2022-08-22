#!/usr/bin/env bash

set -x

isort --recursive --check-only app
flake8
