#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : perl-Class-Refresh
Version  : 0.07
Release  : 15
URL      : https://cpan.metacpan.org/authors/id/D/DO/DOY/Class-Refresh-0.07.tar.gz
Source0  : https://cpan.metacpan.org/authors/id/D/DO/DOY/Class-Refresh-0.07.tar.gz
Summary  : 'refresh your classes during runtime'
Group    : Development/Tools
License  : Artistic-1.0 Artistic-1.0-Perl GPL-1.0
Requires: perl-Class-Refresh-license = %{version}-%{release}
Requires: perl-Class-Refresh-perl = %{version}-%{release}
Requires: perl(Class::Inspector)
Requires: perl(Class::Load)
Requires: perl(Class::Load::XS)
Requires: perl(Class::Unload)
Requires: perl(Data::OptList)
Requires: perl(Devel::OverrideGlobalRequire)
Requires: perl(Module::Implementation)
Requires: perl(Package::Stash)
Requires: perl(Params::Util)
Requires: perl(Sub::Install)
BuildRequires : buildreq-cpan
BuildRequires : perl(Class::Inspector)
BuildRequires : perl(Class::Load)
BuildRequires : perl(Class::Load::XS)
BuildRequires : perl(Class::Unload)
BuildRequires : perl(Data::OptList)
BuildRequires : perl(Devel::OverrideGlobalRequire)
BuildRequires : perl(Module::Implementation)
BuildRequires : perl(Package::Stash)
BuildRequires : perl(Params::Util)
BuildRequires : perl(Sub::Install)
BuildRequires : perl(Test::Fatal)
BuildRequires : perl(Test::Requires)
BuildRequires : perl(Try::Tiny)

%description
This archive contains the distribution Class-Refresh,
version 0.07:
refresh your classes during runtime

%package dev
Summary: dev components for the perl-Class-Refresh package.
Group: Development
Provides: perl-Class-Refresh-devel = %{version}-%{release}
Requires: perl-Class-Refresh = %{version}-%{release}

%description dev
dev components for the perl-Class-Refresh package.


%package license
Summary: license components for the perl-Class-Refresh package.
Group: Default

%description license
license components for the perl-Class-Refresh package.


%package perl
Summary: perl components for the perl-Class-Refresh package.
Group: Default
Requires: perl-Class-Refresh = %{version}-%{release}

%description perl
perl components for the perl-Class-Refresh package.


%prep
%setup -q -n Class-Refresh-0.07
cd %{_builddir}/Class-Refresh-0.07

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
if test -f Makefile.PL; then
%{__perl} Makefile.PL
make  %{?_smp_mflags}
else
%{__perl} Build.PL
./Build
fi

%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make TEST_VERBOSE=1 test

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/perl-Class-Refresh
cp %{_builddir}/Class-Refresh-0.07/LICENSE %{buildroot}/usr/share/package-licenses/perl-Class-Refresh/d5c24f5cbba45be1414bb00664fc82eef47d14d1
if test -f Makefile.PL; then
make pure_install PERL_INSTALL_ROOT=%{buildroot} INSTALLDIRS=vendor
else
./Build install --installdirs=vendor --destdir=%{buildroot}
fi
find %{buildroot} -type f -name .packlist -exec rm -f {} ';'
find %{buildroot} -depth -type d -exec rmdir {} 2>/dev/null ';'
find %{buildroot} -type f -name '*.bs' -empty -exec rm -f {} ';'
%{_fixperms} %{buildroot}/*

%files
%defattr(-,root,root,-)

%files dev
%defattr(-,root,root,-)
/usr/share/man/man3/Class::Refresh.3

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/perl-Class-Refresh/d5c24f5cbba45be1414bb00664fc82eef47d14d1

%files perl
%defattr(-,root,root,-)
/usr/lib/perl5/*
