Name: ojuba-repo
Version: 38
Release: 2%{?dist}
Summary: Ojuba Software Repos
Summary(ar): مستودعات أعجوبة البرمجية
License: WAQFv2
URL: http://ojuba.org
BuildArch: noarch

%description
Ojuba software repos are including Software from many sources, mainly from Ojuba.

%description -l ar
تتضمّن مستودعات أعجوبة البرمجية برمجيات من مصادر متعددة، وبشكل رئيسي من أعجوبة.

%prep
%if 0%{?rhel}
echo '[ojuba]
name=Ojuba Software Repos
mirrorlist=http://ojuba.org/mirrors/ojuba.php?name=epel&ver=7&arch=$basearch
gpgcheck=1
gpgkey=http://ojuba.org/repos/pubkey.gpg
metadata_expire=7h
enabled=1
enabled_metadata=1' > ojuba.repo
%else
%if 0%{?mandriva}
echo '[ojuba]
name=Ojuba Software Repos
mirrorlist=http://ojuba.org/mirrors/ojuba.php?name=mageia&ver=$releasever&arch=$basearch
gpgcheck=1
gpgkey=http://ojuba.org/repos/pubkey.gpg
metadata_expire=7h
enabled=1
enabled_metadata=1' > ojuba.repo
%else
echo '[ojuba]
name=Ojuba Software Repos
mirrorlist=http://ojuba.org/mirrors/ojuba.php?name=fedora&ver=$releasever&arch=$basearch
gpgcheck=1
gpgkey=http://ojuba.org/repos/pubkey.gpg
metadata_expire=7h
enabled=1
enabled_metadata=1' > ojuba.repo
%endif
%endif

%build
#Nothing to build

%install
install -d -m 755 %{buildroot}/etc/yum.repos.d
install -m 644 ojuba.repo %{buildroot}/etc/yum.repos.d

%files
%config(noreplace) /etc/yum.repos.d/ojuba.repo

%changelog
* Sat Dec 17 2016 Mosaab Alzoubi <moceap@hotmail.com> - 38-2
- Enabling repos for Mageia

* Sat Dec 17 2016 Mosaab Alzoubi <moceap@hotmail.com> - 38-1
- Update to Ojuba 38
- Using Ojuba Software Repos Mirror Generator 2.0
- Add meta data time period
- Disabling rawhide

* Mon Jul 20 2015 Mosaab Alzoubi <moceap@hotmail.com> - 36-2
- Using Mirrorlist.

* Mon Jul 20 2015 Mosaab Alzoubi <moceap@hotmail.com> - 36-1
- First package for just ojuba.repo file getting from ojuba-release package.
