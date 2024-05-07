#!/bin/bash

echo "The script is starting!"
echo "The current user is $(whoami)"
files=$AIRFLOW_HOME/include/scripts/*
#files=/usr/local/airflow/include/scripts/*

for file in $files; do
    echo "The include folder contains $(basename $file)"
done

echo "The script has run. Have an amazing day!"
