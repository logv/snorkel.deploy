## snorkel.deploy

this repository is an example deployment of
[snorkel.lite](https://github.com/logv/snorkel/tree/slite) that can be cloned
and used to run a snorkel instance with custom configuration.

### installation

```
# make a virtualenv called 'dev'
virtualenv -p python2 dev
source dev/bin/activate
# install snorkel-lite
pip install snorkel-lite
# run the web server
PORT=2333 ENV=local.py python2 app.py
```


### flask commands

```
# add a regular user
flask add-user <name>

# setup superuser
flask add-superuser <name>

# get auth token
flask get-user-token <name>
```

### setting up local config

```
# edit config/local.py
# edit app.py
```

