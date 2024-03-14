#!/usr/bin/env bash

if [ "$1" = "windows" ]
then
   CURRENT_DIR=`python3 getcwd-windows.py`
else
   CURRENT_DIR=$PWD
fi

docker run -d --rm --name shico_backend -p 8000:8000 -v $CURRENT_DIR/gensim/:/home/shico/word2vec/ -v $CURRENT_DIR/backend/:/tmp/config/ "cmartinez/shico"
docker run -d --rm --name shico_front -p 3000:3000 -v $CURRENT_DIR/frontend/:/tmp/config/ "cmartinez/shico-frontend"
