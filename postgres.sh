#!/bin/bash

if [ "$1" == "build" ]; then
  docker run -d --name hackathondb -p 127.0.0.1:5434:5432 -e POSTGRES_PASSWORD=hackathon timescale/timescaledb-ha:pg15-latest
elif [ "$1" == "configure" ]; then
    psql postgresql://postgres:hackathon@localhost:5434 -f initialize_tables.sql
elif [ "$1" == "start" ]; then
    docker start hackathondb
elif [ "$1" == "shell" ]; then
    psql postgresql://postgres:hackathon@localhost:5434
elif [ "$1" == "stop" ]; then
    docker stop hackathondb
elif [ "$1" == "drop" ]; then
  read -p "Are you sure you want to drop the postgres tables? (y/n) " answer
  if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
      psql postgresql://postgres:hackathon@localhost:5434 -f drop_tables.sql
      echo "Tables dropped."
  else
      echo "Table drop cancelled."
  fi
elif [ "$1" == "reset" ]; then
  read -p "Are you sure you want to delete all data from the postgres tables? (y/n) " answer
  if [[ "$answer" == "y" || "$answer" == "Y" ]]; then
      psql postgresql://postgres:hackathon@localhost:5434 -f reset_tables.sql
      echo "Data deleted."
  else
      echo "Data deletion cancelled."
  fi
else
  echo "Unknown command: $1"
  echo "Valid commands are 'build', 'configure', 'start', 'shell', 'stop', 'drop', and 'reset'."
fi
