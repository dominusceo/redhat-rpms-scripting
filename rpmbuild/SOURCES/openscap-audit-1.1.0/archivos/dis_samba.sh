#!/usr/bin/env bash

SERV="samba"
I=$(rpm -qa $SERV 2>&1)

if [ $I != "" ]
then
	echo "INCORRECTO, el paquete $SERV estA instalado en el equipo. Se debe desinstalar"
	echo "$I"
	exit $XCCDF_RESULT_FAIL
else
	echo "El paquete $SERV no estA instalado en el equipo"
	echo "$I"
	exit $XCCDF_RESULT_PASS
fi
