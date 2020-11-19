#!/bin/bash

# Bash script to pull inputs for pull aoc input data
# need to have activated python environment with advent-of-code-data installed

if [ $AOC_SESSION = '' ]
then
    read -sp 'Input AOC Session header: ' AOC_SESSION
fi

read -p 'Input short user name: ' USER
read -a years -p "Please give the list of years' data needed (e.g. 2015 2016): "
read -p "Please give the first day of data needed (e.g. 1 for December 1st): " DAY_START
read -p "Please give the last day of data needed (e.g. 25 for December 25th): " DAY_END

for year in "${years[@]}"; do

    if [ "$year" -lt 2015 ] || [ "$year" -gt 2020 ]
    then
        continue
    else

    for ((day=$DAY_START; day<=$DAY_END; day++)); do

        if [ "$day" -lt 1 ] || [ "$day" -gt 25 ]
        then
            continue
        else
            if [ ! -d "../$year/$day/inputs/" ]
            then
                mkdir ../$year/$day
                mkdir ../$year/$day/inputs
            fi
            aocd $day $year > ../$year/$day/inputs/$USER'-input.txt'
        fi
    done
    fi
done