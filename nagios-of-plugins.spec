Summary: Additional Nagios plugins by Open Fusion
Name: nagios-of-plugins
Version: %{version}
Release: 2.of
License: GPL
Group: Applications/System
Source: http://www.openfusion.com.au/labs/dist/%{name}-%{version}.tar.gz
URL: http://www.openfusion.com.au/labs/nagios/
Packager: Gavin Carr <gavin@openfusion.com.au>
Vendor: Open Fusion, http://www.openfusion.com.au
Buildroot: %_tmppath/%{name}-%{version}
Requires: bash
Requires: perl
Requires: nagios-plugins
AutoReq: no
# This is a noarch package
ExcludeArch: i386, i686, x86_64

%description
This package contains additional plugins for the Nagios monitoring system,
written by Gavin Carr of Open Fusion. It requires Nagios::Plugin from CPAN.

- check_daemontools_service
- check_db_query_rowcount
- check_file
- check_grep
- check_inodes
- check_ipmi_sdr
- check_kernel_version
- check_linux_raid
- check_memory
- check_qmailq
- check_tcp_range
- check_up2date
- check_yum

See the relevant plugin's -h output for usage details.

%prep
%setup

%build

%install
test "$RPM_BUILD_ROOT" != "/" && rm -rf $RPM_BUILD_ROOT
mkdir -p $RPM_BUILD_ROOT/usr/lib/nagios/plugins/Nagios
cp check* notify* $RPM_BUILD_ROOT/usr/lib/nagios/plugins
#cp Nagios/* $RPM_BUILD_ROOT/usr/lib/nagios/plugins/Nagios

%files
%defattr(-,root,root)
/usr/lib/nagios/plugins/*
%doc README

%changelog

* Wed May 02 2007 Gavin Carr <gavin@openfusion.com.au> 0.9.2
- Add glob support to check_daemontools_service.

* Fri Mar 16 2007 Gavin Carr <gavin@openfusion.com.au> 0.9
- Add initial check_memory plugin.
- Add initial check_ipmi_sdr plugin.

* Fri Dec 15 2006 Gavin Carr <gavin@openfusion.com.au> 0.8.2
- Add -C cmd support to check_grep plugin, for use with check_by_ssh.

* Thu Dec 14 2006 Gavin Carr <gavin@openfusion.com.au> 0.8.1
- Add initial check_grep plugin.

* Fri Mar 17 2006 Gavin Carr <gavin@openfusion.com.au> 0.8rc1
- Remove Nagios::Plugin (now on CPAN).

* Fri Mar 17 2006 Gavin Carr <gavin@openfusion.com.au> 0.7.1
- Change $Nagios::Plugins::CONFIG to load_config(), to workaround ePN problems.
- Add a hack to $Nagios::Plugins::PLUGIN derivation, to get to (hopefully) work under ePN.
- Update check_db_query_rowcount to take --auth argument and use new load_config.

* Thu Mar 16 2006 Gavin Carr <gavin@openfusion.com.au> 0.7
- Change Nagios::Plugins::exit to nagios_exit, to workaround ePN problems.

* Wed Feb 22 2006 Gavin Carr <gavin@openfusion.com.au> 0.6.4
- Revert 0.5.3 change - always use /usr/lib/nagios/plugins directory, even on 64-bit.

* Wed Feb 22 2006 Gavin Carr <gavin@openfusion.com.au> 0.6.3
- Add check_daemontools_service plugin, for checking a daemontools service.
- Add check_tcp_range plugin, for checking a range of tcp ports for a host.

* Thu Feb 16 2006 Gavin Carr <gavin@openfusion.com.au> 0.6.2
- Fix problems with check_yum package counts with yum 2.4.

* Fri Sep 02 2005 Gavin Carr <gavin@openfusion.com.au> 0.6.1
- Fix stupid typos in check_file.

* Mon Jul 18 2005 Gavin Carr <gavin@openfusion.com.au> 0.6
- Add check_db_query_rowcount plugin.
- Add plugins.cfg loading and $CONFIG export to Nagios::Plugin.
- Change Nagios::Plugin $plugin, $timeout, and $version variables to uppercase versions.

* Fri Jul 15 2005 Gavin Carr <gavin@openfusion.com.au> 0.5.3
- Update path names to use %_libdir instead of hardcoded /usr/lib, for AMD64.

* Wed Jun 08 2005 Gavin Carr <gavin@openfusion.com.au> 0.5.2
- Fix version comparison corner cases in check_kernel_version.

* Tue Jun 07 2005 Gavin Carr <gavin@openfusion.com.au> 0.5.1
- Fix bug with check_kernel_version not handling numeric comparisons properly.

* Mon Jun 06 2005 Gavin Carr <gavin@openfusion.com.au> 0.5
- Add check_file plugin, checking mtime, size, and file contents of a given file.
- Parameterise notify_by_jabber utility.

* Thu May 31 2005 Gavin Carr <gavin@openfusion.com.au> 0.4
- Add an improved check_qmailq plugin, derived from the contrib/check_qmailq.pl.
- Update existing plugins to use Nagios::Plugin.
- Add Nagios::Plugin, encapsulating lots of repeated code into a module.

* Thu May 26 2005 Gavin Carr <gavin@openfusion.com.au> 0.3
- Add an improved check_linux_raid plugin, derived from the 
  contrib/check_linux_raid.pl.

* Wed Mar 30 2005 Gavin Carr <gavin@openfusion.com.au> 0.2.2
- Add -u,--report_usage option to check_inodes to report inode usage
  rather than free inodes, like check_disk.

* Thu Mar 17 2005 Gavin Carr <gavin@openfusion.com.au> 0.2.1
- Update check_inodes to handle split df lines with long filesystem paths.

* Tue Mar 15 2005 Gavin Carr <gavin@openfusion.com.au> 0.2
- Add notify_by_jabber perl script.
- Add initial check_inodes plugin.

* Thu Feb 21 2005 Gavin Carr <gavin@openfusion.com.au> 0.1
- Initial release, initial check_yum/check_up2date plugin.


# arch-tag: 56c36703-99d8-409e-97dc-1b81e565b29a