Name: ojuba-repo
Version: 36
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
mirrorlist=http://ojuba.org/mirrors/epel-7-$basearch
gpgcheck=1
gpgkey=http://ojuba.org/repos/pubkey.gpg
enabled=1
enabled_metadata=1' > ojuba.repo
%else
echo '[ojuba]
name=Ojuba Software Repos
mirrorlist=http://ojuba.org/mirrors/fedora-$releasever-$basearch
gpgcheck=1
gpgkey=http://ojuba.org/repos/pubkey.gpg
enabled=1
enabled_metadata=1

[ojuba-rawhide]
name=Ojuba Software Repos
mirrorlist=http://ojuba.org/mirrors/fedora-rawhide-$basearch
gpgcheck=1
gpgkey=http://ojuba.org/repos/pubkey.gpg
enabled=0
enabled_metadata=1' > ojuba.repo
%endif

%build
#Nothing to build

%install
install -d -m 755 %{buildroot}/etc/yum.repos.d
install -m 644 ojuba.repo %{buildroot}/etc/yum.repos.d

%files
%config(noreplace) /etc/yum.repos.d/ojuba.repo

%changelog
* Mon Jul 20 2015 Mosaab Alzoubi <moceap@hotmail.com> - 36-2
- Using Mirrorlist.

* Mon Jul 20 2015 Mosaab Alzoubi <moceap@hotmail.com> - 36-1
- First package for just ojuba.repo file getting from ojuba-release package.
