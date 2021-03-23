# File: run_pytest_noteconversion.sh
# Function: Start pytest for test_noteconversion.py
#           and usage of pyenv and pipenv.

# -k means: mbv de parameter k kan men alle tests laten uitvoeren
#           waarvan de naam ovreen komt met de <substring>
#           achter de parameter k.
#           Hiermee kan men een subset van een test suite uitvoeren
# -v means: increases the verbosity
pipenv run pytest -k getNote -v
