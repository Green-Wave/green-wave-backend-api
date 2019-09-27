# green-wave-backend-api
The backend API server which receives traffic light phase delays from the frontend and reports the remaining delay to the raspberries.

# Usage
* Build docker image: ```docker build -t green-wave-backend .```
* In docker image: ```docker run -d --name gw-api-server -p 80:80 green-wave-backend```
* Goto ```http://<server-adress>```
* Stop server: ```docker stop gw-api-server```

Alternative installation:
* Have Python >= 3.6 and pip installed
* Run ```./setup.sh```
* Run ```./startup-dev.sh```
