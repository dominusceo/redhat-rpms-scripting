#!/usr/bin/env bash

I=$(subscription-manager status 2>&1)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]; then
	exit $XCCDF_RESULT_PASS
else
	echo "Codigo de salida subscription-manager status: $CODE_EXIT."
	echo "###########################"
	echo "$I"
	exit $XCCDF_RESULT_FAIL
fi
