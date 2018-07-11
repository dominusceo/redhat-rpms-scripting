#!/usr/bin/env bash

I=$(df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type f -perm -0002 2>/dev/null)
if [ -z "$I" ]; then
  echo "ConfiguraciOn correcta"
  exit $XCCDF_RESULT_PASS
else
  echo "Existen archivos en el sistema con permisos de escritura global:"
  echo "$I"
  exit $XCCDF_RESULT_FAIL
fi
