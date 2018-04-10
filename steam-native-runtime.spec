%global ver 0.1

Name:	steam-native-runtime
Version:	1
Release:	%{ver}
Summary:	A metapackage to enable steam-native-runtime

License:	GPLv3
URL:		https://github.com/AxelSilverdew
Source0:	https://raw.githubusercontent.com/AxelSilverdew/fedora-packages/master/steam-native-runtime-files/steam-native
Source1:	https://raw.githubusercontent.com/AxelSilverdew/fedora-packages/master/steam-native-runtime-files/steam-native.desktop

Requires:	dbus-glib(x86-32)
Requires:	NetworkManager-glib(x86-32)
Requires:	libva(x86-32)

%description
This is a metapackage to install the necessary libs for Steam Native Runtime.

%install
ln -s -f /usr/lib/libudev.so.1.6.6 /usr/lib/libudev.so.0
ln -s -f /usr/lib/libbz2.so.1 /usr/lib/libbz2.so.1.0
install -pm 755 %{SOURCE0} %{buildroot}/%{_bindir}
install -pm 644 %{SOURCE1} %{buildroot}/%{_datadir}/applications/

%files
/usr/lib/libudev.so.0
/usr/lib/libbz2.so.1.0
%{_bindir}/steam-native
%{_datadir}/applications/*.desktop

%changelog
* Tue Apr 10 2018 AxelSilverdew <axeld@fedoraproject.org>
- Initial Spec
