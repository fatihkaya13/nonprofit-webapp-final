# Non Profit Web Application for Volunteering Jobs

Application is developed with Django framework.

## Features

- apply a job
- withdraw job application
- view job application status
- make donations
- user authentication
- profile management


## Installation
create a virtual environment

```sh
python3 -m venv env
source env/bin/activate
```
install dependencies
```sh
pip install requirements.txt
```

run unit tests
```sh
cd nonprofit_webapp
python3 manage.py test
```

start server
```sh
cd nonprofit_webapp
python3 manage.py runserver
```


| Super User / Admin    | Password |
| --------              | ------- |
| fatih                 | manager    |


| Users      | Password |
| --------   | ------- |
| testuser1  | test123+!A   |
| testuser2  | test123+!A    |


## interactive shell for working with models
```sh
python3 manage.py shell
from volunteer_listing.models import Job
import os
os.system('clear')
```


