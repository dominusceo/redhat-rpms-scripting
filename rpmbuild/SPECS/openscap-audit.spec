# Authority: OpenInsecure(IT)-Tuxcursos.CoM
Name: 	openscap-audit
Version: 1.2.0
Release:        1%{?dist}
Summary: OpenScap audit files and execution script for RHEL 7
Group: Development/Tools
License: GNU General Public License Version 3
#Source: %{name}-%{version}.tar.gz
Source0: http://tuxcursos.com/webas/wp-content/uploads/2018/07/openscap-audit-1.2.0.tar.gz
Packager: Ricardo Carrillo <ricardo.carrillo@ine.mx> <dominus.ceo@gmail.com>
Vendor: OpenInsecure(IT) TuxCursos.CoM
URL: https://www.gnu.org/licenses/gpl-3.0.html
BuildRequires: bash
Requires: openscap,openscap-utils,openscap-engine-sce

%description
The openscap-audit package contains scripts to evaluate security in RHEL/CentOS 7 bare metal installations

With this script you can get security status from any RHEL/CentOS 7 host.
%prep
#%setup -n %{name}-%{version}
%setup -q -c %{name}-%{version}
%build
%install
mkdir -pv  %{buildroot}/usr/share/benchmark/RHEL7/archivos
#mkdir -pv %{buildroot}
# Putting all files into file system
pushd %{name}-%{version}
install -m 700 README.md %{buildroot}/usr/share/benchmark/RHEL7
install -m 700 openscap-audit.sh %{buildroot}/usr/share/benchmark/RHEL7
install -m 700 ssg-rhel7-oval.xml  %{buildroot}/usr/share/benchmark/RHEL7
install -m 700 ssg-rhel7-xccdf-1.2.xml %{buildroot}/usr/share/benchmark/RHEL7
pushd archivos
install -m 700 actualizaciones_seg.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_abrtd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_acpid.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_anacron.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_atd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_autofs.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_avahi.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_bluetooth.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_certmonger.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_cgconfig.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_cgred.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_core_dumps_suid.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_cpupower.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_cups.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_debug-shell.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_dhcpd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_kdump.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_mdmonitor.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_messagebus.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_named.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_netconsole.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_nfslock.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_nfs.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_ntpdate.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_oddjobd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_portreserve.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_qpidd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_quota_nld.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rdisc.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rexec.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rhnsd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rhsmcertd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rlogin.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rpcbind.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rpcgssd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rpcidmapd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rpcsvcgssd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_rsh.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_samba.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_saslauthd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_smartd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_smb.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_snmpd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_squid.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_sysstat.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_telnet.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_tftp.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_vsftpd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_xinetd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 dis_ypbind.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ena_auditd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ena_chronyd.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ena_crond.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ena_firewalld.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ena_irqbalance.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ena_psacct.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_cramfs.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_freevxfs.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_hfsplus.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_hfs.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_jffs2.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_rds.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_squashfs.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_tipc.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 modprobe_udf.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ntp_institucional.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 ossec.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 priv_servicios.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 puerto_ssh.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 sistema_archivos.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 sticky_bit.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 suscripciones.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 tcp_wrappers.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 tmp_noexec.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos
install -m 700 world-writable-files.sh %{buildroot}/usr/share/benchmark/RHEL7/archivos

popd
popd
%files
%doc
%dir %attr(0700,root,root) /usr/share/benchmark/RHEL7
%dir %attr(0700,root,root) /usr/share/benchmark/RHEL7/archivos
%dir %attr(-,root,root) /usr/share/benchmark/RHEL7
%defattr(-, root, root, 0700)
/usr/share/benchmark/RHEL7/README.md
/usr/share/benchmark/RHEL7/openscap-audit.sh
/usr/share/benchmark/RHEL7/ssg-rhel7-oval.xml
/usr/share/benchmark/RHEL7/ssg-rhel7-xccdf-1.2.xml
/usr/share/benchmark/RHEL7/archivos/actualizaciones_seg.sh
/usr/share/benchmark/RHEL7/archivos/dis_abrtd.sh
/usr/share/benchmark/RHEL7/archivos/dis_acpid.sh
/usr/share/benchmark/RHEL7/archivos/dis_anacron.sh
/usr/share/benchmark/RHEL7/archivos/dis_atd.sh
/usr/share/benchmark/RHEL7/archivos/dis_autofs.sh
/usr/share/benchmark/RHEL7/archivos/dis_avahi.sh
/usr/share/benchmark/RHEL7/archivos/dis_bluetooth.sh
/usr/share/benchmark/RHEL7/archivos/dis_certmonger.sh
/usr/share/benchmark/RHEL7/archivos/dis_cgconfig.sh
/usr/share/benchmark/RHEL7/archivos/dis_cgred.sh
/usr/share/benchmark/RHEL7/archivos/dis_core_dumps_suid.sh
/usr/share/benchmark/RHEL7/archivos/dis_cpupower.sh
/usr/share/benchmark/RHEL7/archivos/dis_cups.sh
/usr/share/benchmark/RHEL7/archivos/dis_debug-shell.sh
/usr/share/benchmark/RHEL7/archivos/dis_dhcpd.sh
/usr/share/benchmark/RHEL7/archivos/dis_kdump.sh
/usr/share/benchmark/RHEL7/archivos/dis_mdmonitor.sh
/usr/share/benchmark/RHEL7/archivos/dis_messagebus.sh
/usr/share/benchmark/RHEL7/archivos/dis_named.sh
/usr/share/benchmark/RHEL7/archivos/dis_netconsole.sh
/usr/share/benchmark/RHEL7/archivos/dis_nfslock.sh
/usr/share/benchmark/RHEL7/archivos/dis_nfs.sh
/usr/share/benchmark/RHEL7/archivos/dis_ntpdate.sh
/usr/share/benchmark/RHEL7/archivos/dis_oddjobd.sh
/usr/share/benchmark/RHEL7/archivos/dis_portreserve.sh
/usr/share/benchmark/RHEL7/archivos/dis_qpidd.sh
/usr/share/benchmark/RHEL7/archivos/dis_quota_nld.sh
/usr/share/benchmark/RHEL7/archivos/dis_rdisc.sh
/usr/share/benchmark/RHEL7/archivos/dis_rexec.sh
/usr/share/benchmark/RHEL7/archivos/dis_rhnsd.sh
/usr/share/benchmark/RHEL7/archivos/dis_rhsmcertd.sh
/usr/share/benchmark/RHEL7/archivos/dis_rlogin.sh
/usr/share/benchmark/RHEL7/archivos/dis_rpcbind.sh
/usr/share/benchmark/RHEL7/archivos/dis_rpcgssd.sh
/usr/share/benchmark/RHEL7/archivos/dis_rpcidmapd.sh
/usr/share/benchmark/RHEL7/archivos/dis_rpcsvcgssd.sh
/usr/share/benchmark/RHEL7/archivos/dis_rsh.sh
/usr/share/benchmark/RHEL7/archivos/dis_samba.sh
/usr/share/benchmark/RHEL7/archivos/dis_saslauthd.sh
/usr/share/benchmark/RHEL7/archivos/dis_smartd.sh
/usr/share/benchmark/RHEL7/archivos/dis_smb.sh
/usr/share/benchmark/RHEL7/archivos/dis_snmpd.sh
/usr/share/benchmark/RHEL7/archivos/dis_squid.sh
/usr/share/benchmark/RHEL7/archivos/dis_sysstat.sh
/usr/share/benchmark/RHEL7/archivos/dis_telnet.sh
/usr/share/benchmark/RHEL7/archivos/dis_tftp.sh
/usr/share/benchmark/RHEL7/archivos/dis_vsftpd.sh
/usr/share/benchmark/RHEL7/archivos/dis_xinetd.sh
/usr/share/benchmark/RHEL7/archivos/dis_ypbind.sh
/usr/share/benchmark/RHEL7/archivos/ena_auditd.sh
/usr/share/benchmark/RHEL7/archivos/ena_chronyd.sh
/usr/share/benchmark/RHEL7/archivos/ena_crond.sh
/usr/share/benchmark/RHEL7/archivos/ena_firewalld.sh
/usr/share/benchmark/RHEL7/archivos/ena_irqbalance.sh
/usr/share/benchmark/RHEL7/archivos/ena_psacct.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_cramfs.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_freevxfs.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_hfsplus.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_hfs.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_jffs2.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_rds.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_squashfs.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_tipc.sh
/usr/share/benchmark/RHEL7/archivos/modprobe_udf.sh
/usr/share/benchmark/RHEL7/archivos/ntp_institucional.sh
/usr/share/benchmark/RHEL7/archivos/ossec.sh
/usr/share/benchmark/RHEL7/archivos/priv_servicios.sh
/usr/share/benchmark/RHEL7/archivos/puerto_ssh.sh
/usr/share/benchmark/RHEL7/archivos/sistema_archivos.sh
/usr/share/benchmark/RHEL7/archivos/sticky_bit.sh
/usr/share/benchmark/RHEL7/archivos/suscripciones.sh
/usr/share/benchmark/RHEL7/archivos/tcp_wrappers.sh
/usr/share/benchmark/RHEL7/archivos/tmp_noexec.sh
/usr/share/benchmark/RHEL7/archivos/world-writable-files.sh


%changelog
* Tue Jul 10 2018 Ricardo Carrillo  <dominus.ceo@gmail.com> <dominus.ceo@tuxcursos.com>- 1.2.0
- Updating information into README.md file - Information about packagers and vendors
- Updating spec file list about README file changed for README.md
* Thu Feb  9 2018 Ricardo Carrillo  <ricardo.carrillo@ine.mx> <dominus.ceo@gmail.com> - 1.1.0
- Desarrollo inicial RPM de auditoria Open Scap.
