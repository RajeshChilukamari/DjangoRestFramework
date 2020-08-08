# DjangoRestFramework

It's a simple Django Rest Framework project, we can directly download and deploy this project in any cloud PaaS model and use the functionalities using REST APIs (Currently only GET method is implemented)


Prerequisites:
- 
-> PostgresSQL :- also known as Postgres, is a free and open-source relational database management system emphasizing extensibility and SQL compliance. It's an ORM (Object Relational Mapping) database. After installation, create a database as project name.

-> FactoryBoy, Faker :- Factory Boy allows you to create templates for producing valid objects and Faker generates fake data. When you install Factory Boy, "pip install factory_boy", you also get Faker. These two used to populate the Django database.

-> Django REST framework :- Django REST framework is a powerful and flexible toolkit for building Web APIs.

(Links for the additional info provided in References)


ORM Models
-
This Project has two models that are User and ActivityPeriod
  i) User (id - autoincrement, private key, real_name - character, tz - selection field of timezones default -UTC)
      contains the user details
      
  ii) ActivityPeriod (eid - Foreign key of User(id), start_time - datetime, end_time - datetime)
      contains the start time and end time for the user


Functionalities:
-
i) Supports for populating the dummy data
    python3 manage.py seed --activities 1   (default -5)
    -
    The above command will insert the dummy data into User and ActivityPeriod models using Factory_boy and Faker
    
    
ii) This project supports only GET request
      cmd# curl -X GET http://127.0.0.1:8000/api
 -
    The above command will serves the data in JSON format as below

{
	
	"members": [{
			"id": "1",
			"real_name": "Tony Stark",
			"tz": "America/Los_Angeles",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		},
		{
			"id": "2",
			"real_name": "Bruce Banner",
			"tz": "Asia/Kolkata",
			"activity_periods": [{
					"start_time": "Feb 1 2020  1:33PM",
					"end_time": "Feb 1 2020 1:54PM"
				},
				{
					"start_time": "Mar 1 2020  11:11AM",
					"end_time": "Mar 1 2020 2:00PM"
				},
				{
					"start_time": "Mar 16 2020  5:33PM",
					"end_time": "Mar 16 2020 8:02PM"
				}
			]
		}
	]
}


Download
-
Source: https://github.com/RajeshChilukamari/DjangoRestFramework

$ git clone git://github.com/RajeshChilukamari/DjangoRestFramework



References:
-
PostgresSQL for Django - https://docs.djangoproject.com/en/3.0/ref/contrib/postgres/

Faker - https://github.com/joke2k/faker

FactoryBoy - https://factoryboy.readthedocs.io/en/latest/
             https://medium.com/analytics-vidhya/factoryboy-usage-cd0398fd11d2
             
Django Rest Framework - https://www.django-rest-framework.org/api-guide/relations/
