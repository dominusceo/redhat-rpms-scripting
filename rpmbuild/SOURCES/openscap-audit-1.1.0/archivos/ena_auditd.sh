#!/usr/bin/env bash

SERV="auditd.service"
I=$(systemctl is-enabled $SERV 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]
then
	echo "ConfiguraciOn correcta, el servicio $SERV se encuentra activo."
	echo "$I"
	exit $XCCDF_RESULT_PASS
else
	echo "El servicio $SERV se encuentra deshabilitado o no estA instalado en el equipo"
	echo "$I"
	exit $XCCDF_RESULT_FAIL
fi
