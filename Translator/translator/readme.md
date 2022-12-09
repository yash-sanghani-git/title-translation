To successfully run the system one needs to do following stepls.

prerequisite: Your local system must have connected too the active database connection of postgresql

Replace your database connnections with the existing default connection from settings.py file.

1. Create virtual environment (python3 -m venv venv)
2. Install Requirements (pip install -r requirements.txt)
3. Connect to the database 
4. Create moigrations (python3 manage.py makemigrations)
5. Run Migrations (python3 manage.py migrate)
6. Create Superuser (python3 manage.py createsuperuser)
7. Move to the right directory (translator/translator)
8. Run Server (python3 manage.p runserver)

-- Server is ready to use on localhost:8000


##Notes: I created two APIS one which will be need user to enter the specific language in which he wants to translate the title and store in the JSON format database. Another API is the dynamic which will translate in all the available languages added by admin and store into the JSON format in the databse.