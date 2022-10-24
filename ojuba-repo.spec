Name: ojuba-repo
Version: 44
Release: 1%{?dist}
Summary: Ojuba Software Repos
Summary(ar): مستودعات أعجوبة البرمجية
License: WAQFv2
URL: https://ojuba.org
BuildArch: noarch

%description
Ojuba software repos are including Software from many sources, mainly from Ojuba.

%description -l ar
تتضمّن مستودعات أعجوبة البرمجية برمجيات من مصادر متعددة، وبشكل رئيسي من أعجوبة.

%prep
%if 0%{?rhel}
echo '[ojuba]
name=Ojuba Software Repos
baseurl=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/epel-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
metadata_expire=7h' > ojuba.repo
%else
%if 0%{?mandriva}
echo '[ojuba]
name=Ojuba Software Repos
baseurl=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/mageia-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
metadata_expire=7h' > ojuba.repo
%else
echo '[ojuba]
name=Ojuba Software Repos
baseurl=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/fedora-$releasever-$basearch/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/pubkey.gpg
repo_gpgcheck=0
enabled=1
enabled_metadata=1
metadata_expire=7h

[ojuba:ml]
name=Ojuba Software Repos - Multilib
baseurl=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/fedora-$releasever-i386/
type=rpm-md
skip_if_unavailable=True
gpgcheck=1
gpgkey=https://download.copr.fedorainfracloud.org/results/moceap/Ojuba/pubkey.gpg
repo_gpgcheck=0
cost=1100
enabled=1
enabled_metadata=1
metadata_expire=7h' > ojuba.repo
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
* Tue Oct 25 2022 Mosaab Alzoubi <moceap[AT]fedoraproject[DOT]org> - 44-1
- New generation

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
