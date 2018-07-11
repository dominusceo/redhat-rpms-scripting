#!/usr/bin/env bash

UPDATES=$(yum --security check-update 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 100 ]; then
	echo "Hay actualizaciones de seguridad disponibles."
	echo "###########################"
	echo "$UPDATES"
	exit $XCCDF_RESULT_FAIL
elif [ $CODE_EXIT -eq 0 ]; then 
	exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT -eq 1 ]; then 
	echo "Codigo de salida yum: $CODE_EXIT."
	echo 'Error al ejecutar "yum --security check-update", revisar en sitio'
	echo 'Se necesita instalar: "yum -y install yum-plugin-security".'
	echo "###########################"
	echo "$UPDATES"
	exit $XCCDF_RESULT_ERROR
else
	echo "Codigo de salida yum: $CODE_EXIT."
	echo 'Error al ejecutar "yum --security check-update", revisar en sitio.'
	echo "###########################"
	echo "$UPDATES"
	exit $XCCDF_RESULT_ERROR
fi