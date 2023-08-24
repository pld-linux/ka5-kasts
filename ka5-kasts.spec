#
# Conditional build:
%bcond_with	tests		# build with tests
%define		kdeappsver	23.08.0
%define		kframever	5.94.0
%define		qtver		5.15.2
%define		kaname		kasts
Summary:	kasts
Name:		ka5-%{kaname}
Version:	23.08.0
Release:	1
License:	BSD 2 Clause/BSD 3 Clause/GPL v2+/GPL v3+/LGPL v2.0+
Group:		X11/Applications
Source0:	https://download.kde.org/stable/release-service/%{kdeappsver}/src/%{kaname}-%{version}.tar.xz
# Source0-md5:	2f36e0b2a07ce0a918d9060037b93ad1
URL:		http://www.kde.org/
BuildRequires:	Qt5Core-devel
BuildRequires:	Qt5DBus-devel
BuildRequires:	Qt5Gui-devel
BuildRequires:	Qt5Keychain-devel
BuildRequires:	Qt5Multimedia-devel
BuildRequires:	Qt5Network-devel >= 5.15.10
BuildRequires:	Qt5Qml-devel >= 5.15.10
BuildRequires:	Qt5Quick-controls2-devel
BuildRequires:	Qt5Quick-devel
BuildRequires:	Qt5Sql-devel
BuildRequires:	Qt5Svg-devel
BuildRequires:	Qt5Test-devel
BuildRequires:	Qt5Widgets-devel
BuildRequires:	Qt5Xml-devel >= 5.15.2
BuildRequires:	gettext-devel
BuildRequires:	kf5-extra-cmake-modules >= 5.102.0
BuildRequires:	kf5-kconfig-devel >= 5.102.0
BuildRequires:	kf5-kcoreaddons-devel >= 5.102.0
BuildRequires:	kf5-ki18n-devel >= 5.102.0
BuildRequires:	kf5-kirigami2-devel >= 5.102.0
BuildRequires:	kf5-syndication-devel >= 5.102.0
BuildRequires:	kf5-threadweaver-devel >= 5.102.0
BuildRequires:	kirigami-addons-devel >= 0.7
BuildRequires:	ninja
BuildRequires:	pkgconfig
BuildRequires:	qt5-build >= %{qtver}
BuildRequires:	rpmbuild(macros) >= 1.164
BuildRequires:	shared-mime-info
BuildRequires:	taglib-devel
BuildRequires:	tar >= 1:1.22
BuildRequires:	vlc-devel
BuildRequires:	xz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kasts is a convergent podcast application.

%prep
%setup -q -n %{kaname}-%{version}

%build
%cmake \
	-B build \
	-G Ninja \
	%{!?with_tests:-DBUILD_TESTING=OFF} \
	-DHTML_INSTALL_DIR=%{_kdedocdir} \
	-DKDE_INSTALL_USE_QT_SYS_PATHS=ON
%ninja_build -C build

%if %{with tests}
ctest --test-dir build
%endif


%install
rm -rf $RPM_BUILD_ROOT
%ninja_install -C build

%find_lang %{kaname} --all-name --with-kde

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{kaname}.lang
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/kasts
%attr(755,root,root) %{_libdir}/libKMediaSession.so
%attr(755,root,root) %{_libdir}/libKastsSolidExtras.so
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kasts/solidextras/libkasts-solidextrasqmlplugin.so
%{_libdir}/qt5/qml/org/kde/kasts/solidextras/qmldir
%attr(755,root,root) %{_libdir}/qt5/qml/org/kde/kmediasession/libkmediasession-qmlplugin.so
%{_libdir}/qt5/qml/org/kde/kmediasession/qmldir
%{_desktopdir}/org.kde.kasts.desktop
%{_iconsdir}/hicolor/scalable/actions/media-playback-cloud.svg
%{_iconsdir}/hicolor/scalable/apps/kasts-tray-dark.svg
%{_iconsdir}/hicolor/scalable/apps/kasts-tray-light.svg
%{_iconsdir}/hicolor/scalable/apps/kasts.svg
%{_datadir}/metainfo/org.kde.kasts.appdata.xml
