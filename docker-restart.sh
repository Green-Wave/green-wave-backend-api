sudo docker stop gw-api-server
sudo docker build -t green-wave-backend .
sudo docker run -d --rm --name gw-api-server -p 80:80 green-wave-backend

