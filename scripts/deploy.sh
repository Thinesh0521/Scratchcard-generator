#!/bin/sh
ssh manager1 -o StrictHostKeyChecking=no << EOF
sudo docker pull thinesh55/Service1:latest
sudo docker pull thinesh55/Service2:latest
sudo docker pull thinesh55/Service3:latest
sudo docker pull thinesh55/Service4:latest
sudo docker pull nginx:alpine
git clone https://github.com/Thinesh0521/Scratchcard-generator.git
cd Scratchcard-generator
sudo docker stack deploy --compose-file docker-compose.yaml randprize
EOF