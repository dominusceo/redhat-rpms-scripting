#!/usr/bin/env bash

O=$(mount | grep "[[:space:]]/tmp[[:space:]]" | grep noexec 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ];then
	echo "ConfiguraciOn correcta"
	echo "$O"
	exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT -eq 1 ];then
	echo "ConfiguraciOn incorrecta"
	exit $XCCDF_RESULT_FAIL
else
	echo "Error al ejecutar, revisar manualmente."
	echo "$O"
	exit $XCCDF_RESULT_ERROR
fi
