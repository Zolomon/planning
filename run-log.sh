#!/bin/sh


COUNTERA=1
COUNTERC=1
COUNTERS=1
COUNTERP=1

ENDA=$1
ENDC=$2
ENDS=$3
ENDP=$4
while [ $COUNTERA -le $ENDA ]; do
	ia=$COUNTERA

	COUNTERC=1

	while [ $COUNTERC -le $ENDC ]; do
		ic=$COUNTERC

		COUNTERS=1
		
		while [ $COUNTERS -le $ENDS ]; do
			is=$COUNTERS

			COUNTERP=1

			while [ $COUNTERP -le $ENDP ]; do
				ip=$COUNTERP
				
				echo "logistics-$ia-$ic-$is-$ip.pddl"

				cd Logistics/
				GENERATOR_32bit/logistics -a $ia -c $ic -s $is -p $ip > logistics-$ia-$ic-$is-$ip.pddl
				#echo "Running: GENERATOR_32bit/logistics -a $ia -c $ic -s -$is -p $ip > logistics-$ia-$ic-$is-$ip.pddl"

				cd ..

				#echo "Running: FF-X/ff -p Logistics/ -f logistics-$ia-$ic-$is-$ip.pddl -o domain.pddl"
				out=`FF-X/ff -p Logistics/ -f logistics-$ia-$ic-$is-$ip.pddl -o domain.pddl | grep "total"`
				echo $out

				rm Logistics/logistics-$ia-$ic-$is-$ip.pddl
				rm *TIME*

				COUNTERP=$((COUNTERP+1))
			done

			COUNTERS=$((COUNTERS+1))
		done

		COUNTERC=$((COUNTERC+1))
	done
	
	COUNTERA=$((COUNTERA+1))
done

# echo "I: $i"
# 	cd Tyreworld/
# 	GENERATOR_32bit/tyreworld -n $i > tyreworld-$i.pddl
# 	cd ..
# 	out=`FF-X/ff -p Tyreworld/ -f tyreworld-$i.pddl -o domain.pddl | grep "total"`
# 	echo $out
# 	COUNTERA=$((COUNTERA+1))

#GENERATOR_32bit/tyreworld -n $1 > tyreworld-$1.pddl

#cd .. 
#FF-X/ff -p Tyreworld/ -f tyreworld-$1.pddl -o domain.pddl

