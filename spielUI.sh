#!/bin/bash


startgame () {
    generatetnumber=$((RANDOM % 100))
    guessednumber=0
    Tries=0
  while [ "$guessednumber" -ne "$generatetnumber" ]; do 
    guessednumber=$(dialog --inputbox "Guess the number: $generatetnumber" 10 30 2>&1 >/dev/tty)
    if [ "$generatetnumber" -gt "$guessednumber" ]; then 
        dialog --msgbox "The guessed number is not corect, the number has to be higher!" 10 30
    elif [ "$generatetnumber" -lt "$guessednumber" ]; then
        dialog --msgbox "The guessed number is not corect, the number has to be lower!" 10 30
    fi
    ((Tries++))
done

dialog --title "You won!" --msgbox "The corect number is: $generatetnumber \nTries: $Tries" 10 30

dialog --yesno "Do you wan't to play again?" 10 30 
restartgame=$?
case $restartgame in
    0) startgame;;
    1) clear
    exit 1;;
esac
}

startgame