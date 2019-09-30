## budget_manager
Keep a track of your spent money

This is a simple web based port created to manage daily budgets .All you need is to add your regular expentidure. It will give you total amount spent. Further user can add daily bill reminders .Our site will notify user about last date of bill payment.An initiative for easy saving especially for students living away from home.
Work on additional features going  on :)

# Techs used
The complete site is based on python3 framework Django,Plotly.js,Css,HTML and lots of code ;) 

## Installation
 
 To install Django on your local machines use the below link
1.[Django Installation](https://www.digitalocean.com/community/tutorials/how-to-install-django-and-set-up-a-development-environment-on-ubuntu-16-04)

2. Install MYSQL
 Since the entire database is based on mysql format ,create a mysql server on your machine . To install mysql use the below link:
 [mysql](https://www.digitalocean.com/community/tutorials/how-to-create-a-django-app-and-connect-it-to-a-database)
 
PLEASE NOTE ..
After creating database as the above step follow the below commands
 
 3.Creating the database
 Login into your mysql user account using command $mysql -u 'user name' -p
 In mysql shell create a database using command 
 
 ```bash
 mysql> CREATE DATABASAE 'db name';
 ```
 4.Configure database for adding tables
 In the terminal shell write the command 
 ```bash


 $sudo nano /etc/mysql/.my.cnf
 ```
 [client]
 database='db_name'    
 user='user name'
 password='password'
 default-character-set=utf8
 ```
 !Note: write all the credentials without ' '
 
 5.Restart your mysql server:
 Enter the following commands to restart the server
 ```bash
 $ systemctl daemon-reload
 $ systemctl restart mysql
 ```
 if everything is configured well , your database will be configured with the app
 
 6.To add migrations to django app
 In interact directory write the following commands
 ```bash
 ~/billing$ python3 manage.py makemigrations
 ~/billing$ python3 manage.py migrate
 ```
 7.Finally running your machine:
 ```bash
 ~/billing$ python3 manage.py runserver
 ```
 Your server will start at http://127.0.0.1:8000/billing/
 
 ## Congrates you just started budget_manager on your local server
 Keep contributing . Hav a bug free code :)
 

