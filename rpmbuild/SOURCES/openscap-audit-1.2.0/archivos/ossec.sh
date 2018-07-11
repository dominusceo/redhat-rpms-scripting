#!/usr/bin/env bash

SERV="ossec.service"
I=$(systemctl is-enabled $SERV 2>&1)
CODE_EXIT1=$?
J=$(ps aux | grep ossec | grep -v 'color\|bash\|grep' 2>&1)
CODE_EXIT2=$?

if [ $CODE_EXIT1 -eq 0 ] && [ $CODE_EXIT2 -eq 0 ]
then
	echo "ConfiguraciOn correcta, OSSEC-HIDS se encuentra ejecutandose y habilitado."
	echo "###################"
	echo "$I"
	echo "###################"
	echo "$J"
	exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT1 -eq 0 ] && [ $CODE_EXIT2 -ne 0 ]; then
	echo "OSSEC-HIDS se encuentra habilitado pero no se estA ejecutando"
        echo "Ejecutar: /var/ossec/bin/ossec-control start"
	echo "###################"
	echo "$I"
	echo "###################"
	echo "$J"
	exit $XCCDF_RESULT_FAIL
elif [ $CODE_EXIT1 -ne 0 ] && [ $CODE_EXIT2 -eq 0 ]; then
	echo "OSSEC-HIDS se encuentra deshabilitado pero se estA ejecutando"
        echo "Ejecutar: chkconfig ossec on"
	echo "###################"
	echo "$I"
	echo "###################"
	echo "$J"
	exit $XCCDF_RESULT_FAIL
else
        echo "OSSEC-HIDS se encuentra deshabilitado y sin ejecuciOn"
        echo "Favor de ponerse en cotacto con el DSe"
	exit $XCCDF_RESULT_FAIL
fi
