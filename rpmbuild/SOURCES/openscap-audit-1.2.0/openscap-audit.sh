###############################################
##  
##
###############################################
/usr/bin/oscap xccdf eval --results /tmp/xccdf-results_$(hostname)_$(date +%d-%m-%Y).xml --report /tmp/xccdf-report_$(hostname)_$(date +%d-%m-%Y).html --profile xccdf.profile_rhel7 --oval-results /usr/share/benchmark/RHEL7/ssg-rhel7-xccdf-1.2.xml
