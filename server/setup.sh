#!/bin/bash

if   ! type   "pip" > /dev/null || ! type "python3" > /dev/null ;     
then 
    echo "Make sure you have pip and python3 installed";
    exit 1;
fi


echo "installing virtualEnv and deps";
if   ! type   "virtualenv" > /dev/null;
then 
    pip install virtualenv;
fi

if ! ls env > /dev/null; 
then
    virtualenv env;
fi

echo "Run 'source ./env/bin/activate'"
echo "Run 'pip install setuptools==58'"
echo "Run 'pip install -r requirements.txt'"

