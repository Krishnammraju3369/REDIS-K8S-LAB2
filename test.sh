#!/bin/bash

read -p "Enter the key: " key
read -p "Enter the value: " value

curl "http://localhost:8000/api/set?key=$key&value=$value"
curl "http://localhost:8000/api/get?key=$key"

