# HOW TO RUN THE APP
*NOTE*: This guildlines are for a linux environment

After cloning cloning the app:
1. Make sure you have python3 and pip3 installed in your machine
2. Create a virtual environment `python -m venv appvenv`. There are many ways of doing this [python virtual environments](https://docs.python.org/3/tutorial/venv.html)
3. In the terminal, navigate into the app directory. Make sure the virtual environment is activated. Run `pip install -r requirements.txt`
4. Make sure you have installed and postgresql server is running. You can use any database you want. Just remember to change the settings.
5. Run `python manage.py makemigrations`
6. Run `python manage.py migrate`
7. Add an admin by running `python manage.py createsuperuser`. Visit the admin site and add some dummy data.
7. Assuming everything is okay, run `python manage.py runserver` and you should see a link to the app.