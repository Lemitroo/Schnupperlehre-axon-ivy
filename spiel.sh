#!/bin/bash

generatetnumber=$((RANDOM % 100))
guessednumber=0
Tries=0

echo guess the number
while [ $guessednumber != $generatetnumber ]; do 
    read guessednumber
    if [ "$generatetnumber" -gt "$guessednumber" ]; then 
        echo "The guessed number is not corect, the number has to be higher!"
    else 
        echo "The guessed number is not corect, the number has to be lower!"
    fi
    ((Tries++))
done
echo "Tries: $Tries"