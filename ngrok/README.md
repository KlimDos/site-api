docker run -d -p 4040 --link site-api:http --net site-api_default --name site-api-ngrok wernight/ngrok

curl $(docker port site-api-ngrok 4040)/api/tunnels


docker run --rm -it --link site-api --net site-api_default shkoliar/ngrok ngrok http site-api:80

see compose file