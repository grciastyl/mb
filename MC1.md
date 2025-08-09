# Mini Challenge!

Create the basic structure for a django project using the terminal

STR
1. create the folder to store the project (MB)  (mkdir mb)
2. move to mb (cd mb and you can use pwd to make sure your're on the right folder)
3. Install virtual environment and activate it (python3 -m venv venv , source venv/bin/activate)
4. install django (pip3 install django)
5. Save dependencices to txt file (pip3 freeze > requirements.txt)
6. Create a django project (django-admin startproject config .)
7. Create an app called pages and another one called post (python3 manage.py startapp pages) (python3 manage.py startapp post)
8. Create templates and static folder (mkdir static)(mkdir templates)
    8.1 Create templates/pages folder (mkdir templates/pages)
9. Create .gitingore file (touch .gitignore)
10. Create home and about html inside of pages (touch templates/pages/home.html,touch templates/pages/about.html, touch templates/pages/base.html, touch templates/pages/navbar.html)


Mini Challenge 2!!

Create the static views for home and about pages

STR:
1. Create a urls.py file inside of pages
2. Add the urls from pages to the urls.py inside of config
3. Create a class based view (using TemplateView) to render the HomePageView and AboutPageView (done in pages/views.py)
4. Fill the base.html adding the jinja tags and also adding bootstrap for the navbar
5. Fill the home.html and about.html
6. Add the paths inside of urls.py (pages)
7. Run server to display the home page