# nonprofit-webapp-final
source env/bin/activate
cd nonprofit_webapp
python3 manage.py runserver

superuser
fatih/manager

users
testuser1
testuser2

password: test123+!A


# interactive shell
python manage.py shell
from volunteer_listing.models import Job
import os
os.system('clear')