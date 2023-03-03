# Run from this directory using "docker build -t default/stackdump ." to create image
# Run the container using "docker run -d -p 8080:8080 --name stackdump default/stackdump"
# Debug run container with "docker run -it --rm default/stackdump /bin/ash"
FROM ubuntu:latest

MAINTAINER Bloodvault "bloodvault@bloodvault.net"

EXPOSE 8080

RUN apt-get update -y && apt-get install -y python2 openjdk-8-jre

COPY . /stackdump

RUN chmod 777 -R stackdump

WORKDIR /stackdump

RUN ./docker_start.sh

#RUN sleep 45

#RUN ./manage.sh import_site ./networkengineering/ -u networkengineering -c "November 2020" -d "NetworkEngineering" -k "0" -n "Offline StackOverflow" -Y

ENTRYPOINT ./start_solr.sh; ./start_web.sh

