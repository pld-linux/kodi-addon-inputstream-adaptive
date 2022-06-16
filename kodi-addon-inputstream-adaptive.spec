%define		kodi_ver	19
%define		next_kodi_ver	%(echo $((%{kodi_ver}+1)))
%define		codename	Matrix
%define		addon		inputstream.adaptive

Summary:	Kodi InputStream addon for several manifest types
Name:		kodi-addon-inputstream-adaptive
Version:	%{kodi_ver}.0.6
Release:	1
License:	GPL v2+
Group:		Applications/Multimedia
Source0:	https://github.com/xbmc/inputstream.adaptive/archive/%{version}-%{codename}/%{version}-%{codename}.tar.gz
# Source0-md5:	9c3e8b31d778f5f87b2f3fab02f26ecb
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

%build
%cmake -B build \
	-DBUILD_TESTING:BOOL=OFF
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
%{_datadir}/kodi/addons/%{addon}/resources
