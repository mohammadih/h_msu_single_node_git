#!/bin/bash

GENI_GET="/usr/bin/geni-get"
MYFILE=$1

if [ ! -f $MYFILE ]; then
    touch $MYFILE && \
	$GENI_GET slice_urn > $MYFILE || \
	    { echo "Failed to write to $MYFILE"; exit 1; }
fi

exit 0
