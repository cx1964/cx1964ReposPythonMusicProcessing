#!/bin/bash
# file:  install_python_project_env.sh
# functie: install python project environment obv pyenv
# opmerking: Voor dat men dut script draait, check:
#            - alle benodigde modules worden genoemd om te installeren in ### Begin aanpassen ###
#            - Of de laatste versie van python is ingesteld.
#              zo nee pas die eventueel aan  
#            - Of dat men in de project directory staat als men dit script draait
# documentatie: https://www.activestate.com/resources/quick-reads/how-to-manage-python-dependencies-with-virtual-environments/
#               mbt bash https://linuxconfig.org/bash-scripting-tutorial-for-beginners


### Begin aanpassen ###
# kies een python versie mbv
# pyenv install --list
# Nog onbekend hoe een versie te installeren hoger dan de system python versie op het OS
export PYTHON_VERSION="3.8.5" 
### Einde aanpassen ###


# Dit script gaat ervan uit dat pyenv al is geinstalleerd
# als pyenv is geinstalleerd moet de directory ~/.pyenv bestaan
# nog een conditie maken dat dit script alleen iets doet als de directory ~/.pyenv bestaat.
# anders een melding geven dat men pyenv moet installeren
# Zie dan https://www.activestate.com/resources/quick-reads/how-to-manage-python-dependencies-with-virtual-environments/
# en gebruik paragraaf How to Install Pyenv


# Waar sta ik?
pwd

read -p 'Sta je in de project Directory (j/n)?:' ;
echo "";

if [ ${REPLY} != "j" ]; then
  # Breek installatie af omdat men NIET in de project directory staat
  echo "Abort installatie"
  return 1
else
  # Do de installatie omdat men de project directory staat

  # update pipenv 
  pip install --upgrade pipenv

  # install python version
  pipenv --python $PYTHON_VERSION

  ### Begin aanpassen ###
  pipenv install music21
  pipenv install matplotlib
  pipenv install numpy
  pipenv install pytest
  ## Einde aanpassen ###

  # Toon geinstalleerde modules 
  ###pipenv run pip list
  return 0
fi

echo "start nu pipenv shell"
echo "voor het activeren van de virtual env van het project"