Pet is a project based on the Django REST framework.

This is a small messenger with the following functions:

• sending and receiving messages;

• creating, editing and deleting group chats and correspondence in them (Chats are managed via the REST API, and correspondence is the same as in regular chats, but using the “rooms” ideology on the server);

• editing the user's personal information (name and avatar);

• viewing a list of other users and switching to sending them messages.

What to do to make it work (the database is clean):

1) You need to install dependencies (pip install -r requirements.txt)
   
2) Run the command python manage.py runserver
   
3) Follow the link http://127.0.0.1:8000/
   
4) Chat rooms can be created through the admin panel
