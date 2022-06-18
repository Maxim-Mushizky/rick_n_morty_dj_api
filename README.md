# amat_rick_and_morty_rest_api
Home assignment for AMAT

## How it works for development:
1. Create a virtual for python versions >= 3.8. Example for windows:
```cmd
python -m venv env 
```  
2. From virtual environment install the requirements.txt with the command:
```cmd
pip install -r requirements.txt
```
3. cd to amat_rick_and_morty/ folder and activate server with command:
```cmd
python manage.py runserver
```
The server default is to localhost port 8000 (http://127.0.0.1:8000)

## API endpoints 
To view the documentation run server and provide the url for the swagger ui: /swagger-ui
(or simply press this [link](http://127.0.0.1:8000/swagger-ui) if the server is running with the localhost default settings)

## Run docker
1. cd to location of the Dockerfile at amat_rick_and_morty_api/amat_rick_and_morty
2. Type in the commands:
```cmd
docker build --tag amat_rick_and_morty_rest_api .
```
This will create the image amat_rick_and_morty_rest_api
3. Open new termianl window and run a container for the image:
```cmd
docker run --publish 8000:8000 amat_rick_and_morty_rest_api
```

Now the server is available as specified previously (http://127.0.0.1:8000)