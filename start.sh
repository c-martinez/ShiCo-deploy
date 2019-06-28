#!/usr/bin/env bash
docker run -d --rm --name shico_backend -p 8000:8000 -v $PWD/gensim/:/home/shico/word2vec/ -v $PWD/backend/:/tmp/config/ "cmartinez/shico"
docker run -d --rm --name shico_front -p 3000:3000 -v $PWD/frontend/:/tmp/config/ "cmartinez/shico-frontend"
