%define		php_min_version 5.0.0
%include	/usr/lib/rpm/macros.php
Summary:	Roundcube Plugins
Name:		roundcube-plugins
Version:	0.1
# DO NOT DECREASE RELEASE, subpackages will suffer
Release:	1.2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://roundcube-plugins.googlecode.com/files/jqueryui-1.8.2.1.tgz
# Source0-md5:	b997167d710915eac71e969fae7c033d
Source1:	http://roundcube-plugins.googlecode.com/files/keyboard_shortcuts-1.5.tgz
# Source1-md5:	7c3858cce34ead5b2a4c5a3d21e988e2
URL:		http://code.google.com/p/roundcube-plugins/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
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
%undos -f php,js,css

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{pluginsdir}
cp -a * $RPM_BUILD_ROOT%{pluginsdir}

rm $RPM_BUILD_ROOT%{pluginsdir}/keyboard_shortcuts/README

%clean
rm -rf $RPM_BUILD_ROOT

%files -n roundcube-plugin-jqueryui
%defattr(644,root,root,755)
%{pluginsdir}/jqueryui

%files -n roundcube-plugin-keyboard_shortcuts
%defattr(644,root,root,755)
%doc keyboard_shortcuts/README
%dir %{pluginsdir}/keyboard_shortcuts
%{pluginsdir}/keyboard_shortcuts/skins
%{pluginsdir}/keyboard_shortcuts/keyboard_shortcuts.*
%dir %{pluginsdir}/keyboard_shortcuts/localization
%lang(cs) %{pluginsdir}/keyboard_shortcuts/localization/cs_CZ.inc
%lang(de) %{pluginsdir}/keyboard_shortcuts/localization/de_DE.inc
%lang(en) %{pluginsdir}/keyboard_shortcuts/localization/en_US.inc
%lang(nl) %{pluginsdir}/keyboard_shortcuts/localization/nl_NL.inc
%lang(pl) %{pluginsdir}/keyboard_shortcuts/localization/pl_PL.inc
%lang(sv) %{pluginsdir}/keyboard_shortcuts/localization/sv_SE.inc
