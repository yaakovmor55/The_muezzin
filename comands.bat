docker-compose up -d

docker rmi producer_image
docker build -t producer_image .
docker run producer_image

docker rmi consumer_service
docker build -t consumer_service .
docker run consumer_service

docker rmi data_processor
docker build -t data_processor .
docker run data_processor


