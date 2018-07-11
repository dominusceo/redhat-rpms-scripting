#! /bin/bash
#
#
comprobarPermisos() {
	proc=$1
	usuario=`ps -aux | egrep -m 1 $proc | egrep -v "(egrep|python)" | cut -d ' ' -f 1`
	grupId=`cat /etc/passwd | grep $usuario | cut -d ':' -f 4`
	shell=`cat /etc/passwd | grep $usuario | cut -d ':' -f 7`
	if [ "$grupiId" = "0" ]
	then
		return 50
	elif [ "$shell" = "/bin/bash" ]
	then
		return 55
	else
		return 60
	fi	
}
#
#
control=0

for proceso in postgresql tomcat cups bind java
do
	resultadoPs=`ps -aux | egrep -m 1 "$proceso" | egrep -v "(egrep|python)"`
	if [ "$resultadoPs" != "" ]
	then
		comprobarPermisos "$proceso"
		resultadoFun=$?
		if [ $resultadoFun -eq 50 ]
		then
			echo "El proceso $proceso se ejecuta con privilegios de root"
			control=1
		elif [ $resultadoFun -eq 55 ]
		then
			echo "El proceso $proceso se ejecuta con un usuario con shell habilitada"
			control=1
		elif [ $resultadoFun -eq 60 ]
		then
			echo "El proceso $proceso se ejecuta de la forma esperada"
			control=0
		else
			echo "Ocurrio un error inesperado"
			control=1
		fi
	else
		echo "El proceso $proceso no se esta ejecutando"
	fi
done
#
if [ $control -eq 1 ]
then
	echo "INCORRECTO, existen servicios corriendo con privilegios"
	exit $XCCDF_RESULT_FAIL
elif [ $control -eq 0 ]
then
	echo "CORRECTO, ningun servicio se ejecuta con privilegios"
	exit $XCCDF_RESULT_PASS
fi