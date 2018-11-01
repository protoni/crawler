#!/bin/bash

# Get page source


if [ $# -gt 0 ]; then
	url=$1

	content=$(wget ${url} -q -O -)

	# Echo all rows between 50 and 70 in character length
	#echo $content | grep -o -w '\w\{50,70\}'

	# Check if is WIF key
	for i in $(echo $content | grep -o -w '\w\{50,52\}'); do
		if [[ ${i:0:1} -eq 5 ]] ; then echo $i; fi
	done
else
	echo 0
fi
