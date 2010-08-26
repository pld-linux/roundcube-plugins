%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Roundcube Plugins
Name:		roundcube-plugins
# DO NOT INCREASE VERSION, subpackages will suffer
Version:	0.1
Release:	1
License:	GPL v2
Group:		Applications/WWW
Source0:	http://roundcube-plugins.googlecode.com/files/jqueryui-1.8.2.1.tgz
# Source0-md5:	b997167d710915eac71e969fae7c033d
Source1:	http://roundcube-plugins.googlecode.com/files/keyboard_shortcuts-1.5.tgz
# Source1-md5:	7c3858cce34ead5b2a4c5a3d21e988e2
URL:		http://code.google.com/p/roundcube-plugins/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.268
BuildRequires:	sed >= 4.0
Requires:	roundcubemail
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

# want only php deps
%define		_noautopear	pear

%define		_webapps		/etc/webapps
%define		_webapp			roundcube
%define		_sysconfdir		%{_webapps}/%{_webapp}
%define		roundcubedir	%{_datadir}/%{_webapp}
%define		pluginsdir		%{roundcubedir}/plugins

# extract version from tarball
%define		ever()	%(basename %1 .tgz | sed -e 's,^.*-\\([0-9.]\\+\\)$,\\1,')

%description
RoundCube Webmail Plugins.

%package -n roundcube-plugin-jqueryui
Summary:	jquery-ui for roundcube
Version:	%{ever %{S:0}}
Group:		Applications/WWW
Requires:	php-common >= 4:%{php_min_version}
Requires:	roundcubemail

%description -n roundcube-plugin-jqueryui
jquery-ui for roundcube.

%package -n roundcube-plugin-keyboard_shortcuts
Summary:	jquery-ui for roundcube
Version:	%{ever %{S:1}}
Group:		Applications/WWW
Requires:	php-common >= 4:%{php_min_version}
Requires:	roundcube-plugin-jqueryui
Requires:	roundcubemail

%description -n roundcube-plugin-keyboard_shortcuts
keyboard shortcuts.

%prep
%setup -qcT %(seq -f -a%g 0 1 | xargs)

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{pluginsdir}
cp -a * $RPM_BUILD_ROOT%{pluginsdir}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n roundcube-plugin-jqueryui
%defattr(644,root,root,755)
%{pluginsdir}/jqueryui

%files -n roundcube-plugin-keyboard_shortcuts
%defattr(644,root,root,755)
%{pluginsdir}/keyboard_shortcuts
