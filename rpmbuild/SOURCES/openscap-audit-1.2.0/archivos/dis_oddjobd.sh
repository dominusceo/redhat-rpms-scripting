#!/usr/bin/env bash

SERV="oddjobd.service"
I=$(systemctl is-enabled $SERV 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]
then
	echo "INCORRECTO, el servicio $SERV estA habilitado. Se debe deshabilitar"
	echo "$I"
	exit $XCCDF_RESULT_FAIL
else
	echo "El servicio $SERV se encuentra deshabilitado o no estA instalado en el equipo"
	echo "$I"
	exit $XCCDF_RESULT_PASS
fi
