#!/bin/bash

#docker run -it --rm -p --name embedding embedding
volume=$PWD/model
#faissvol=$PWD/faiss_indexes

if [ -x "$(command -v docker)" ]; then
EXEC=docker
IMGAGE_PREFIX=
else
EXEC=podman
IMAGE_PREFIX=localhost/
fi
DATA=$PWD/data
APP=$PWD/src

if [ ! -z $WINDIR ]; then
  volume=c:\\git\\a\\com-areal-imagery\\model
  #faissvol=c:\\git\\a\\com-agentic-rag\\faiss_indexes
  CACHE=c:\\Users\\${USERNAME}\\.cache\\huggingface\\hub
  DOCKER="winpty podman"
  DATA=c:\\git\\a\\com-areal-imagery\\data
  NOTEBOOKS=c:\\git\\a\\com-areal-imagery\\notebooks
  APP=c:\\git\\a\\com-agentic-rag\\src
fi
echo $IMAGE_PREFIX
#echo $EXEC run --rm  -v $PWD/data:/data -v $PWD/src:/app -v $PWD/tiktoken:/tiktoken --network="host" localhost/trieder83/com-agentic-rag:0.1
#$EXEC run --rm -v $PWD/data:/data -v $PWD/src:/app -v $PWD/tiktoken:/tiktoken --network="host" localhost/trieder83/com-agentic-rag:0.1

#$EXEC run --rm --name notebook -v $DATA:/data -v $APP:/app -env-file=.env -network="host" ${IMAGE_PREFIX}trieder83/com-agentic-rag:0.2
#$EXEC run --rm --name arealnotebook -v $DATA:/app/data -v $NOTEBOOKS:/app/notebooks -v $APP:/app -env-file=.env --net ainet -p 8888:8888 ${IMAGE_PREFIX}trieder83/com-areal-imagery:0.1

$EXEC run --rm --name arealnotebook -v $DATA:/app/data -v $NOTEBOOKS:/app/notebooks -v $APP:/app -env-file=.env --net ainet -p 8888:8888 ${IMAGE_PREFIX}trieder83/com-areal-imagery:0.1 uv run --with jupiter jupiter notebook --ip=0.0.0.0 --no-browser --allow-root --NotebookApp.default_url=/app/notebooks/default.ipynb

# podman network create ainet
# podman run -d --gpus=all -v ollama:/c/temp/ollama -p 11434:11434 --name ollama ollama/ollama
