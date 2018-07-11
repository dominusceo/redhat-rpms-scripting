#!/usr/bin/env bash

FS_EXT=$(lsblk -o FSTYPE | egrep "ext4|xfs" 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]
then
	exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT -eq 1 ]
then
	echo "Sistema de archivos incorrecto."
	echo "############ /etc/fstab ###############"
	egrep -v '^#' /etc/fstab
	exit $XCCDF_RESULT_FAIL
else
	echo 'Error, revisar en sitio.'
	echo "$FS_EXT"
	exit $XCCDF_RESULT_ERROR
fi