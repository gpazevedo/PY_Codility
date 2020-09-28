# Python

## Starting a new project

$ pipenv shell                         # first time in this folder starts a fresh environment with a new Pipfile
$ pipenv install xxx                   # install xxx package and adds a related production dependency in Pipfile
$ pipenv uninstall xxx                 # uninstall xxx package and removes the related dependency in Pipfile
$ pipenv install xxx --dev             # install xxx package and adds a related dev dependency in Pipfile
$ pipenv install -r ./requirements.txt # install the packages in the requirements.txt file updating Pipfile
$ pipenv check                         # check for security vulnerabilities
$ pipenv graph                         # shows the dependency graph
$ pipenv lock                          # prepares for Pipfile.lock file for deployment
$ pipenv install --ignore-pipfile      # uses Pipfile.lock file (packages versions defined) for deployment

$ pipenv lock -r # show the dependencies