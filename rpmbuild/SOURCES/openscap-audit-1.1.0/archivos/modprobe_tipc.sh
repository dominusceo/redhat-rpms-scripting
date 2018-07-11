#!/usr/bin/env bash

SERV="tipc"
I=$(modprobe -n -v $SERV 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]
then
	echo "INCORRECTO, el mOdulo $SERV estA habilitado. Se debe deshabilitar"
	echo "$I"
	exit $XCCDF_RESULT_FAIL
elif [ $CODE_EXIT -eq 1 ]; then
	echo "El mOdulo $SERV no se encuentra en el equipo"
	exit $XCCDF_RESULT_PASS
else
    echo "Error"
	echo "$I"
	echo $XCCDF_RESULT_ERROR
fi
