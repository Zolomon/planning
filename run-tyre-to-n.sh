#!/bin/sh
COUNTER=1
END=$1
while [ $COUNTER -lt $END ]; do
	i=$COUNTER
	echo "I: $i"
	cd Tyreworld/
	GENERATOR_32bit/tyreworld -n $i > tyreworld-$i.pddl
	cd ..
	out=`FF-X/ff -p Tyreworld/ -f tyreworld-$i.pddl -o domain.pddl | grep "total"`
	echo $out
	COUNTER=$((COUNTER+1))
done

#GENERATOR_32bit/tyreworld -n $1 > tyreworld-$1.pddl

#cd .. 
#FF-X/ff -p Tyreworld/ -f tyreworld-$1.pddl -o domain.pddl

