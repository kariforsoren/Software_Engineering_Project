# Young Explorer university Software Engineering project

## Description
This project is part of a project in the course TDT4140 - Software Engineering at NTNU. The project lasted for eight weeks, and we used agile methods throughout. We set up sprints in accordanse with Scrum wich lasted between 1-2 weeks, and the TA was the product owner while we had the role of both Scrum master and developement team. The team consisted of 7 students from different data and communications engineering programmes. If you would like more information on the backround of the project, please contact me.

This webpage allows young explorers and travelers to gain insight on, save qnd leave reviews on different locations around the world. 
When users are not logged in, they can only scroll along the page and see the front picture and name, as well as the rating of the different locations. 
They can filter and sort the locations based on tags, free text, price and rating. 

When users log in, they can see more informatuon like food, shelter, weather and pricing for the different locations.
The users can save the location and view it on their own profile, and they can review locations they have been to. 

There is support for admin-users.
Admin Users can add new places for other users to view by clicking "add new". The locations can be edited after the fact. 
      Using different APIs both the pictures for the locations and the weather in real time is displayed alongside the manually inputted infromation about food, culture and activities. 
      Admin users can add tags and so on using the django backend. 
      

## Installation
To view this project on your own computer you will have to follow these steps. 

The frontend uses react with Javascript, and youll need to set up "Node" for everything to work. 

1. The backend is hosted locally, so first you'll have to create a MySQL database called sample with password "root". If you already have a sample database or have done these steps before, you will need to _drop your database and do all these steps again each time you stop the server from running._ Sorry. 
2. Then you need to **delete** the already existing 0001_initial.py that is currently in gr18>user_api>migrations. I dont know why but it doesn't work unless you manually delete this. 
3. Then, after creating and connecting the database "sample", you have to first create the migration file "python manage.py makemigrations" (the new init.py file) and then migrate the changes "python manage.py migrate". This should make your sample-database have a bunch of different tables in it, _that are all empty._ (run commands from within the young_explorers folder.)
4. To fill the database with data so you dont have to manually input everything, run these files with these commands in this order inside the "young explorers"-folder:
   1. python .\basic-data.py      2. python .\specific-location-data.py
5. To create a admin-user for yourself to use in the frontend, use the command "python manage.py createsuperuser". The password must be 8 characters and the username must be an email. (run commands from within the young_explorers folder.)
6. To start the server run "python manage.py runserver". (run commands from within the young_explorers folder.)
7. To start the page run "npm start" in a different terminal while inside the folder "frontend".
8. Have fun adding places and leaving reviews!


## Contributing
I am not open to contributions directly, but contact me if you have suggestions for how to fix some of the issues. 

## Authors and acknowledgment
We are many pople who have contributed to this project throughout the course, but I will not name them here as I have not asked their permission. 


## Project status
There is a lot that should be done to make this project up to industry stanndard or at the very least better organized and easier to set up. This is something I will hopefulle get around to doing at some point. 
