#!/usr/bin/env bash

I=$(egrep "^Port\s+50022" /etc/ssh/sshd_config 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ];then
	echo 'Existe "Port 50022"'
	exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT -eq 1 ];then
	echo 'No existe "Port 50022"'
	exit $XCCDF_RESULT_FAIL
else
	echo "Error al ejecutar, revisar manualmente."
	echo "$I"
	exit $XCCDF_RESULT_ERROR
fi
