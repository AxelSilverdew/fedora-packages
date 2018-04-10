%global ver 0.1

Name:	steam-native-runtime
Version:	1
Release:	%{ver}
Summary:	A metapackage to enable steam-native-runtime

License:	GPLv3
URL:		https://github.com/AxelSilverdew
Source0:	

Requires:	dbus-glib(x86-32)
Requires:	NetworkManager-glib(x86-32)
Requires:	libva(x86-32)

%description
This is a metapackage to install the necessary libs for Steam Native Runtime.

%install
ln -s -f /usr/lib/libudev.so.1.6.6 /usr/lib/libudev.so.0
ln -s -f /usr/lib/libbz2.so.1 /usr/lib/libbz2.so.1.0

%files
/usr/lib/libudev.so.0
/usr/lib/libbz2.so.1.0

%changelog
* Tue Apr 10 2018 AxelSilverdew <axeld@fedoraproject.org>
- Initial Spec
