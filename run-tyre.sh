#!/bin/sh

cd Tyreworld
GENERATOR_32bit/tyreworld -n $1 > tyreworld-$1.pddl

cd .. 

FF-X/ff -p Tyreworld/ -f tyreworld-$1.pddl -o domain.pddl

