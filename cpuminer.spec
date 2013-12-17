Summary:	CPU miner for Litecoin and Bitcoin
Name:		cpuminer
Version:	2.3.2
Release:	2
License:	GPL v2
Group:		Applications/Networking
Source0:	http://downloads.sourceforge.net/cpuminer/pooler-%{name}-%{version}.tar.gz
# Source0-md5:	fdb6b92957bc9a500cce4c2cce8dd937
URL:		https://bitcointalk.org/index.php?topic=55038.0
BuildRequires:	curl-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is a CPU miner for Litecoin and Bitcoin.

%prep
%setup -q

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

install -d $RPM_BUILD_ROOT%{_bindir}

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT" \
	bindir=%{_libdir}/%{name}

ln -s %{_libdir}/%{name}/minerd $RPM_BUILD_ROOT%{_bindir}/%{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog README NEWS
%attr(755,root,root) %{_bindir}/%{name}
%dir %{_libdir}/%{name}
%attr(755,root,root) %{_libdir}/%{name}/minerd
