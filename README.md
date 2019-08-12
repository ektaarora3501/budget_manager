# budget_manager
Keep a track of your spent money

This is a simple web based port created to manage daily budgets .All you need is to add your regular expentidure. It will give you total amount spent. Further user can add daily bill reminders .Our site will notify user about last date of bill payment.An initiative for easy saving especially for students living away from home.
Work on additional features going  on :)


Languages/Tech used 
Django ,Python3 ,css,MYSQL

To install and configure site follow the steps :
1.Set up virtual env and Django on local machine using  https://docs.djangoproject.com/en/2.2/topics/install/

2.Set up MYSQL sever and configure it with application https://docs.oracle.com/javacomponents/advanced-management-console-2/install-guide/mysql-database-installation-and-configuration-advanced-management-console.htm#JSAMI116

3.Create a user and database and add the details in the database
4.Enter into directory /billing
5.Migrate the connected database using commands
    python3 manage.py makemigrations
    python3 manage.py migrate
5.Run the Django server using command python3 manage.py runserver

Have a bug free coding ;)
