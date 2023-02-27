

__________________________________________________________________________________________________________________________________
**environment :
there is 3 environment file, each for a setting file by this name in automation_core/settings/ folder
 
 
__________________________________________________________________________________________________________________________________
**settings:

in setting folder we have 4 module:
include gloabal and common settings:

./automation_core/settings/settings.py

setting for production mode:

./automation_core/settings/prod.py

setting for development mode:

./automation_core/settings/dev.py

setting for production mode with debug=true:

./automation_core/settings/test.py


__________________________________________________________________________________________________________________________________
**running project:
    developement mode:
     
        installing dependencies:
            pip install -r requirement.txt  
            or 
            pipenv install

        running developement server:
            python manage.py runserver 

    production mode:
        1-install docker on target machine 
        2-run ./entrypoint.sh 


__________________________________________________________________________________________________________________________________
**creating user for admin panel:
    developement:
        python manage.py createsuperuser

    production:
        docker-compose exec backend python manage.py createsuperuser


__________________________________________________________________________________________________________________________________
**changing user  password for admin panel:
    developement:
        python manage.py changepassword <<username>>

    production:
        docker-compose exec backend python changepassword <<username>>
     