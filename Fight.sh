#!/bin/bash

healtP1=100
healtP2=100

echo "The enimie has $healtP1 HP do you wan't to attack (1) ore protect yourself (2)?"

read option

if [ $option -eq 1 ]; then 
    ((healtP1-=20))
    echo "Your enimie got hit and now has $healtP1 HP"
if [ $option -eq 2 ]; then
    