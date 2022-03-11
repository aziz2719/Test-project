Installation Instructions

Make sure docker engine and docker-compose are installed on you dev machine,
Clone the repository
CD into the project code
copy or move .env.example into .env

Generate a secret key and assign the value to SECRET_KEY variable
Assign the relevant values to your database connections params and make sure you assgin the value of db to your DB_HOST variable.
Run docker-compose build

Run docker-compose up -d,
Run docker-compose exec polling python3 manage.py migrate,
Run docker-compose exec polling python3 manage.py createsuperuser