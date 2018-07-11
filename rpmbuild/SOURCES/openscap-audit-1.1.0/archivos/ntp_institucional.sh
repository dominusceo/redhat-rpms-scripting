#!/usr/bin/env bash

SERVER_NTP="10.0.1.3"
J=$(egrep -v "^#" /etc/chrony.conf | grep $SERVER_NTP 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]
then
	exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT -eq 1 ]
then
	echo "INCORRECTO, no se detecta configurado el ntp con el servidor $SERVER_NTP."
	exit $XCCDF_RESULT_FAIL
else
	echo "Error, revisar en sitio."
	echo "###########################"
	echo "$J"
	exit $XCCDF_RESULT_ERROR
fi