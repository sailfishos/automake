Name:       automake
Summary:    A GNU tool for automatically creating Makefiles
Version:    1.16.5
Release:    1
License:    GPLv2+ and GFDL and MIT
BuildArch:  noarch
URL:        http://www.gnu.org/software/automake/
Source0:    http://ftp.gnu.org/gnu/automake/automake-%{version}.tar.xz
Source1:    automake-rpmlintrc
Requires:   autoconf >= 2.65
Requires:   perl
Requires:   perl-threads
Requires:   perl-threads-shared
BuildRequires:  autoconf >= 2.65
BuildRequires:  bison
BuildRequires:  coreutils
BuildRequires:  gnu-gzip
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
%autosetup -p1 -n %{name}-%{version}/%{name}

%build
./bootstrap
%configure --docdir=%{_docdir}/%{name}-%{version}

%make_build

mv -f NEWS NEWS_
iconv -f ISO_8859-15 -t UTF-8 NEWS_ -o NEWS

%install

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
