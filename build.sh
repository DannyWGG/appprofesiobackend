#!/usr/bin/env bash
set -e

# Instalar dependencias usando wheels precompilados
pip install --only-binary :all: -r requirements.txt