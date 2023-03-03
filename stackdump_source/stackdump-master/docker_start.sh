#!/bin/bash
echo "Adding command variables to local paths for stackdump"
echo "/bin/python2" > PYTHON_CMD
echo "/bin/java" > JAVA_CMD
echo "Starting solr java indexer"
./start_solr.sh
echo "solr starting, waiting 30 seconds"
sleep 30
echo "Starting stack data import"
./manage.sh import_site ./stackexchange/ -u stackoverflow -c "November 2021" -d "StackOverflow" -k "so" -n "Offline StackOverflow" -Y

