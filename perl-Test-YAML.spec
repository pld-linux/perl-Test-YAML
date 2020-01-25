#
# Conditional build:
%bcond_without	tests		# do not perform "make test"
#
%define		pdir	Test
%define		pnam	YAML
Summary:	Test::YAML - Testing Module for YAML Implementations
Summary(pl.UTF-8):	Test::YAML - moduł testujący dla implementacji YAML-a
Name:		perl-Test-YAML
Version:	1.06
Release:	1
# same as perl
License:	GPL v1+ or Artistic
Group:		Development/Languages/Perl
Source0:	http://www.cpan.org/modules/by-module/Test/%{pdir}-%{pnam}-%{version}.tar.gz
# Source0-md5:	92e6ea57576428095fe3c9b8e00e6f29
URL:		http://search.cpan.org/dist/Test-YAML/
BuildRequires:	perl-devel >= 1:5.8.0
BuildRequires:	rpm-perlprov >= 4.1-13
%if %{with tests}
BuildRequires:	perl-Test-Base >= 0.86
%endif
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
Test::YAML is a subclass of Test::Base with YAML specific support.

%description -l pl.UTF-8
Test::YAML to podklasa Test::Base ze wsparciem specyficznym dla
YAML-a.

%prep
%setup -q -n %{pdir}-%{pnam}-%{version}

%build
%{__perl} Makefile.PL \
	INSTALLDIRS=vendor
%{__make}

%{?with_tests:%{__make} test}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} pure_install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{perl_vendorlib}/Test/YAML.pod
%{__rm} $RPM_BUILD_ROOT%{_bindir}/test-yaml

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc Changes README
%{perl_vendorlib}/Test/YAML.pm
%{_mandir}/man3/Test::YAML.3pm*
