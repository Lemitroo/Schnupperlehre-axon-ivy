#!/bin/bash

gerneratetnummber=$((RANDOM % 100))
guessednumber=0
Tries=0

echo guess the nummer
while [ $guessednumber != $gerneratetnummber ]; do 
    read guessednumber
    if [ "$gerneratetnummber" -gt "$guessednumber" ]; then 
        echo "The guessed number is not corect, the number has to be higher!"
    else 
        echo "The guessed number is not corect, the number has to be lower!"
    fi
    ((Tries++))
done
echo "Tries: $Tries"