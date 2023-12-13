Name:           ndwaita-gnome
Version: 20231026
Release:        1
License:        CC-BY-SA-4.0
Summary:        NdWaita GNOME theme
Url:            https://empty.com/ndwaita-gnome
Group:          User Interface/Desktops
Source:         https://github.com/nordlex/%{name}/archive/%{version}.tar.gz
BuildRoot:      %{_tmppath}/%{name}-%{version}-build
BuildArch:      noarch
Requires:       glib2-devel, gnome-extensions-app, gnome-shell >= 44.0, gnome-shell << 45, gnome-shell-extension-user-theme, ImageMagick, make
BuildRequires:  make

%description
NdWaita Theme is a GNOME Shell theme inspired by material design. It is mostly flat using a colorful palette with some shadows, highlights, and gradients for some depth.

%prep
%setup -q

%install
%make_install

%build


%post
cd /usr/share/ndwaita-gnome
make
make install

%preun
if [ $1 == 0 ]
then
	cd /usr/share/ndwaita-gnome
	make uninstall
fi

%files
%doc LICENSE README.md
%{_datadir}/ndwaita-gnome

