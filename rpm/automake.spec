Name:       automake
Summary:    A GNU tool for automatically creating Makefiles
Version:    1.15
Release:    1
Group:      Development/Tools
License:    GPLv2+ and GFDL and MIT
BuildArch:  noarch
URL:        http://www.gnu.org/software/automake/
Source0:    http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz
Source1:    automake-rpmlintrc
Patch1:     0001-automake-hack-mer1218.diff
Requires:   autoconf >= 2.65
BuildRequires:  autoconf >= 2.65
BuildRequires:  bison
BuildRequires:  texinfo
BuildRequires:  xz

%description
Automake is a tool for automatically generating `Makefile.in'
files compliant with the GNU Coding Standards.

You should install Automake if you are developing software and would
like to use its ability to automatically generate GNU standard
Makefiles. If you install Automake, you will also need to install
GNU's Autoconf package.

%prep
%setup -q -n %{name}-%{version}/%{name}

# HACK! A temporarily hack. See MER#1218.
# The problem is that our RPM doesn't have macros directory for *-eabihf
# platform. So it can't find macros file at all that breaks build of some
# packages. The correct solution is to upgrade RPM version that is a bit
# complex task. Please remove this hack after RPM upgrade.
%patch1 -p1

%build
./bootstrap.sh
%configure --docdir=%{_docdir}/%{name}-%{version}

make %{?_smp_mflags}

mv -f NEWS NEWS_
iconv -f ISO_8859-15 -t UTF-8 NEWS_ -o NEWS

%install
rm -rf %{buildroot}
rm -rf ${RPM_BUILD_ROOT}

%make_install
install -m644 AUTHORS COPYING NEWS README THANKS %{buildroot}%{_docdir}/%{name}-%{version}

# create this dir empty so we can own it
mkdir -p ${RPM_BUILD_ROOT}%{_datadir}/aclocal
# info's dir file is not auto ignored on some systems
rm -f $RPM_BUILD_ROOT%{_infodir}/dir

%files
%defattr(-,root,root,-)
%doc %{_docdir}/%{name}-%{version}
%{_bindir}/*
%doc %{_infodir}/*.gz
%doc %{_mandir}/man1/*
%{_datadir}/aclocal*
%{_datadir}/automake-*
%dir %{_datadir}/aclocal
