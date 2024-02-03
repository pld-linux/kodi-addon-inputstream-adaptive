# TODO:
# - package Bento4 and use system one

%define		kodi_ver	20
%define		next_kodi_ver	%(echo $((%{kodi_ver}+1)))
%define		codename	Nexus
%define		addon		inputstream.adaptive

%define		bento4_ver	1.6.0-639-7-Omega

Summary:	Kodi InputStream addon for several manifest types
Name:		kodi-addon-inputstream-adaptive
Version:	%{kodi_ver}.3.17
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/xbmc/inputstream.adaptive/archive/%{version}-%{codename}/%{version}-%{codename}.tar.gz
# Source0-md5:	f40756c66374bd2c9958de8aacd6d740
Source1:	https://github.com/xbmc/Bento4/archive/%{bento4_ver}/Bento4-%{bento4_ver}.tar.gz
# Source1-md5:	5532a65b8da2e051b70de761ee84141d
Patch0:		bento4-hash.patch
URL:		https://github.com/xbmc/inputstream.adaptive
BuildRequires:	cmake >= 3.10
BuildRequires:	expat-devel
BuildRequires:	kodi-devel >= %{kodi_ver}
BuildRequires:	kodi-devel < %{next_kodi_ver}
BuildRequires:	libstdc++-devel >= 6:7
BuildRequires:	rpmbuild(macros) >= 1.605
Requires:	kodi >= %{kodi_ver}
Requires:	kodi < %{next_kodi_ver}
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Kodi InputStream addon for several manifest types

%prep
%setup -q -n %{addon}-%{version}-%{codename}
%patch0 -p1

install -d build/download
cp -p %{SOURCE1} build/download/%{bento4_ver}.tar.gz

%build
%cmake -B build \
	-DBUILD_TESTING:BOOL=OFF \
	-DENABLE_INTERNAL_BENTO4:BOOL=ON
%{__make} -C build

%install
rm -rf $RPM_BUILD_ROOT
%{__make} -C build install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%dir %{_libdir}/kodi/addons/%{addon}
%attr(755,root,root) %{_libdir}/kodi/addons/%{addon}/%{addon}.so.%{version}
%attr(755,root,root) %{_libdir}/kodi/addons/%{addon}/libssd_wv.so
%dir %{_datadir}/kodi/addons/%{addon}
%{_datadir}/kodi/addons/%{addon}/addon.xml
%{_datadir}/kodi/addons/%{addon}/changelog.txt
%{_datadir}/kodi/addons/%{addon}/fanart.jpg
%{_datadir}/kodi/addons/%{addon}/icon.png
%{_datadir}/kodi/addons/%{addon}/resources
