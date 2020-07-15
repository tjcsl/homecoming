#!/bin/bash

docker run \
	--name hoco_psql \
       	-e POSTGRES_DB=homecoming \
       	-e POSTGRES_USER=homecoming \
       	-e POSTGRES_PASSWORD=pwd \
       	-v pgdata:/var/lib/postgresql/data \
       	-d -p 5432:5432 postgres:latest
