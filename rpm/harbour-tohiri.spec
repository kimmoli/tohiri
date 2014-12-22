#
# TOHIRI spec File
# (C) kimmoli 2014
# 

Name:       harbour-tohiri

%{!?qtc_qmake:%define qtc_qmake %qmake}
%{!?qtc_qmake5:%define qtc_qmake5 %qmake5}
%{!?qtc_make:%define qtc_make make}
%{?qtc_builddir:%define _builddir %qtc_builddir}

Summary:    The OtherHalf Thermal Imager
Version:    0.4.devel
Release:    4
Group:      Qt/Qt
License:    LICENSE
URL:        https://github.com/kimmoli/tohiri-app
Source0:    %{name}-%{version}.tar.bz2

Requires:   sailfishsilica-qt5 >= 0.10.9
BuildRequires:  pkgconfig(sailfishapp) >= 0.0.10
BuildRequires:  pkgconfig(Qt5Core)
BuildRequires:  pkgconfig(Qt5Qml)
BuildRequires:  pkgconfig(Qt5Quick)
BuildRequires:  pkgconfig(Qt5Multimedia)
BuildRequires:  desktop-file-utils

%description
Thermal Imaging application to be used with TOHIRI OtherHalf


%prep
%setup -q -n %{name}-%{version}

%build
%qtc_qmake5 SPECVERSION=%{version}
%qtc_make %{?_smp_mflags}

%install
rm -rf %{buildroot}

%qmake5_install

desktop-file-install --delete-original       \
  --dir %{buildroot}%{_datadir}/applications             \
   %{buildroot}%{_datadir}/applications/*.desktop

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}
%{_datadir}/icons/hicolor/86x86/apps/
%{_datadir}/applications/
%{_datadir}/%{name}/
%{_datadir}/%{name}/qml

