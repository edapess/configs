#!/bin/zsh

variant1=$(setxkbmap -query | grep layout)

varUs="layout:     us"
varAm="layout:     am"
if [ "$variant1" == "$varUs" ]

then

setxkbmap am phonetic-alt
 
elif [ "$variant1" == "$varAm" ]

then

setxkbmap ru

else

setxkbmap us

fi
