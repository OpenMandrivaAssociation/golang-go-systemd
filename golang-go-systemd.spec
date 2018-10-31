%define debug_package   %{nil}
%define import_path     github.com/coreos/go-systemd
%define gosrc		%{go_dir}/src/pkg/%{import_path}

Name:           golang-go-systemd
Version:        2
Release:        6
Summary:        Go bindings to systemd socket activation, journal and D-BUS APIs
License:        ASL 2.0
URL:            http://%{import_path}
Source0:        https://%{import_path}/archive/v%{version}.tar.gz
Group:		Development/Other
BuildRequires:	golang
Requires:       golang
Provides:       golang(%{import_path}) = %{version}-%{release}
Provides:       golang(%{import_path}/activation) = %{version}-%{release}
Provides:       golang(%{import_path}/dbus) = %{version}-%{release}
Provides:       golang(%{import_path}/journal) = %{version}-%{release}
BuildArch:	noarch


%description
%{summary}

This package contains library source intended for building other packages
which use coreos/go-systemd.

%prep
%setup -n go-systemd-%{version}

%build

%install
install -d -p %{buildroot}/%{gosrc}/{activation,dbus,journal}
cp -av {activation,dbus,journal} %{buildroot}/%{gosrc}

%files
%doc LICENSE README.md
%dir %attr(755,root,root) %{gosrc}
%dir %attr(755,root,root) %{gosrc}/activation
%dir %attr(755,root,root) %{gosrc}/dbus
%dir %attr(755,root,root) %{gosrc}/journal
%{gosrc}/activation/*.go
%{gosrc}/dbus/*.go
%{gosrc}/journal/*.go
