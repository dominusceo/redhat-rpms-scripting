#!/usr/bin/env bash

I=$(df --local -P | awk {'if (NR!=1) print $6'} | xargs -I '{}' find '{}' -xdev -type d \( -perm -0002 -a ! -perm -1000 \) 2>/dev/null)
if [ -z "$I" ]; then
  echo "ConfiguraciOn correcta"
  exit $XCCDF_RESULT_PASS
else
  echo "Existen directorios con permisos de escritura global sin sticky bit:"
  echo "$I"
  exit $XCCDF_RESULT_FAIL
fi
