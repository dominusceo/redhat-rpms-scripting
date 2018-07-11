#!/usr/bin/env bash

J=$(egrep -v '^#' /etc/hosts.allow)
I=$(egrep "^ALL\s*:\s*ALL" /etc/hosts.deny)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ];then
	echo "Existe polItica restrictiva."
	if [ -z "$J" ]; then
		echo "Archivo /etc/hosts.allow comentado o sin contenido."
		exit $XCCDF_RESULT_FAIL
	else
		echo "Existe /etc/hosts.allow:"
		egrep -v '^#' /etc/hosts.allow
		exit $XCCDF_RESULT_PASS
	fi
elif [ $CODE_EXIT -eq 1 ];then
	echo 'No existe polItica restrictiva.'
	echo 'CorreciOn: echo  "ALL: ALL" >> /etc/hosts.deny.'
	echo "/etc/hosts.deny:"
	egrep -v '^#' /etc/hosts.deny
	echo ""
	if [ -z "$J" ]; then
		echo "Archivo /etc/hosts.allow comentado o sin contenido."
	else
		echo "Existe /etc/hosts.allow:"
		egrep -v '^#' /etc/hosts.allow
	fi
	exit $XCCDF_RESULT_FAIL
else
	echo "Error al ejecutar, revisar manualmente."
	echo "$I"
	echo "$J"
	exit $XCCDF_RESULT_ERROR
fi
