%define		php_min_version 5.0.0
Summary:	Roundcube Plugins
Name:		roundcube-plugins
Version:	0.2
# DO NOT DECREASE RELEASE unless *all* subpackage versions are increased too
Release:	2
License:	GPL v2
Group:		Applications/WWW
Source0:	http://roundcube-plugins.googlecode.com/files/jqueryui-1.8.6.1.tgz
# Source0-md5:	0cd5fe2270c5e790174829b96a2acead
Source1:	http://roundcube-plugins.googlecode.com/files/keyboard_shortcuts-1.7.tgz
# Source1-md5:	05566987027f5d8ef21caaffbc3e47b7
URL:		http://code.google.com/p/roundcube-plugins/
BuildRequires:	rpm-php-pearprov >= 4.4.2-11
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
Requires:	roundcubemail >= 0.4
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
Summary:	jQuery-UI for Roundcube
Version:	%{ever %{S:0}}
Group:		Applications/WWW
Requires:	php(core) >= %{php_min_version}
Requires:	roundcubemail

%description -n roundcube-plugin-jqueryui
jQueryUI adds the complete jQuery-UI library including the smoothness
theme to Roundcube. This allows other plugins to use jQuery-UI without
having to load their own version. The benefit of using 1 central
jQuery-UI is that we won't run into problems of conflicting jQuery
libraries being loaded. All plugins that want to use jQuery-UI should
use this plugin as a requirement.

%package -n roundcube-plugin-keyboard_shortcuts
Summary:	jquery-ui for roundcube
Version:	%{ever %{S:1}}
Group:		Applications/WWW
Requires:	php(core) >= %{php_min_version}
Requires:	roundcube-plugin-jqueryui
Requires:	roundcubemail

%description -n roundcube-plugin-keyboard_shortcuts
keyboard shortcuts.

%prep
%setup -qcT %(seq -f -a%g 0 1 | xargs)
%undos -f php,js,css

mv jqueryui/config.inc.php{.dist,}

# all languages bundle?
%{__rm} jqueryui/js/i18n/jquery-ui-i18n.js

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{pluginsdir}
cp -a * $RPM_BUILD_ROOT%{pluginsdir}

%{__rm} $RPM_BUILD_ROOT%{pluginsdir}/jqueryui/{README,LICENSE}
%{__rm} $RPM_BUILD_ROOT%{pluginsdir}/jqueryui/config.inc.php

%{__rm} $RPM_BUILD_ROOT%{pluginsdir}/keyboard_shortcuts/{README,LICENSE}

%clean
rm -rf $RPM_BUILD_ROOT

%files -n roundcube-plugin-jqueryui
%defattr(644,root,root,755)
%doc jqueryui/README
%doc jqueryui/config.inc.php
%dir %{pluginsdir}/jqueryui
%{pluginsdir}/jqueryui/jqueryui.php
# TODO: use jquery-ui rpm pkg here instead
%{pluginsdir}/jqueryui/skins
%dir %{pluginsdir}/jqueryui/js
%{pluginsdir}/jqueryui/js/jquery-ui-*.custom.min.js
%dir %{pluginsdir}/jqueryui/js/i18n
# TODO %lang, or above todo
%{pluginsdir}/jqueryui/js/i18n/jquery.ui.datepicker-*.js

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
