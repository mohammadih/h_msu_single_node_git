#!/bin/bash

MYFILE=/var/tmp/$1

if [ ! -f $MYFILE ]; then
    touch $MYFILE && \
	echo "Hello World!" > $MYFILE || \
	    { echo "Failed to write to $MYFILE"; exit 1 }
fi

exit 0
