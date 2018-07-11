#!/usr/bin/env bash

A=$(sysctl fs.suid_dumpable | grep 0 2>/dev/null)
CODE_EXIT=$?

if [ $CODE_EXIT -eq 0 ]; then
  echo "ConfiguraciOn correcta"
  exit $XCCDF_RESULT_PASS
elif [ $CODE_EXIT -eq 1 ]; then
  echo "ConfiguraciOn incorrecta"
  sysctl fs.suid_dumpable
  exit $XCCDF_RESULT_FAIL
else
  echo "Error, revisar en sitio"
  echo "$A"
  exit $XCCDF_RESULT_ERROR
fi
