# swappi
Steps to run:

1. docker build --tag <docker tag> .
2. docker run -p <port>:<port> <docker-image-id>

To run the film list (using curL): 

curl http://<docker ip>:<port>/filmlist -d None -H 'Content-Type: application/json'

To run the character list:

curl http://<docker ip>:<port>/filmchar -d '{"filmID": 0}' -H 'Content-Type: application/json'
