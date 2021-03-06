#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : aspell-fr
Version  : 0.50.3
Release  : 4
URL      : https://mirrors.kernel.org/gnu/aspell/dict/fr/aspell-fr-0.50-3.tar.bz2
Source0  : https://mirrors.kernel.org/gnu/aspell/dict/fr/aspell-fr-0.50-3.tar.bz2
Summary  : French dictionary for aspell
Group    : Development/Tools
License  : GPL-2.0
Requires: aspell-fr-license = %{version}-%{release}
BuildRequires : aspell-dev
Patch1: 0001-configure-ignore-unknown-options.patch

%description
GNU Aspell French Word List Package

%package license
Summary: license components for the aspell-fr package.
Group: Default

%description license
license components for the aspell-fr package.


%prep
%setup -q -n aspell-fr-0.50-3
cd %{_builddir}/aspell-fr-0.50-3
%patch1 -p1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1602132577
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
%configure --disable-static
make  %{?_smp_mflags}

%install
export SOURCE_DATE_EPOCH=1602132577
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/aspell-fr
cp %{_builddir}/aspell-fr-0.50-3/COPYING %{buildroot}/usr/share/package-licenses/aspell-fr/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
%make_install

%files
%defattr(-,root,root,-)
/usr/lib64/aspell-0.60/fr-40-only.rws
/usr/lib64/aspell-0.60/fr-40.multi
/usr/lib64/aspell-0.60/fr-60-only.rws
/usr/lib64/aspell-0.60/fr-60.multi
/usr/lib64/aspell-0.60/fr-80-only.rws
/usr/lib64/aspell-0.60/fr-80.multi
/usr/lib64/aspell-0.60/fr-lrg.alias
/usr/lib64/aspell-0.60/fr-med.alias
/usr/lib64/aspell-0.60/fr-sml.alias
/usr/lib64/aspell-0.60/fr.dat
/usr/lib64/aspell-0.60/fr.multi
/usr/lib64/aspell-0.60/fr_CH-40.multi
/usr/lib64/aspell-0.60/fr_CH-60.multi
/usr/lib64/aspell-0.60/fr_CH-80.multi
/usr/lib64/aspell-0.60/fr_CH-lrg.alias
/usr/lib64/aspell-0.60/fr_CH-med.alias
/usr/lib64/aspell-0.60/fr_CH-only.rws
/usr/lib64/aspell-0.60/fr_CH-sml.alias
/usr/lib64/aspell-0.60/fr_CH.multi
/usr/lib64/aspell-0.60/fr_FR-40.multi
/usr/lib64/aspell-0.60/fr_FR-60.multi
/usr/lib64/aspell-0.60/fr_FR-80.multi
/usr/lib64/aspell-0.60/fr_FR-lrg.alias
/usr/lib64/aspell-0.60/fr_FR-med.alias
/usr/lib64/aspell-0.60/fr_FR-sml.alias
/usr/lib64/aspell-0.60/fr_FR.multi
/usr/lib64/aspell-0.60/fr_phonet.dat
/usr/lib64/aspell-0.60/francais-40.alias
/usr/lib64/aspell-0.60/francais-60.alias
/usr/lib64/aspell-0.60/francais-80.alias
/usr/lib64/aspell-0.60/francais-lrg.alias
/usr/lib64/aspell-0.60/francais-med.alias
/usr/lib64/aspell-0.60/francais-sml.alias
/usr/lib64/aspell-0.60/francais.alias
/usr/lib64/aspell-0.60/french-40.alias
/usr/lib64/aspell-0.60/french-60.alias
/usr/lib64/aspell-0.60/french-80.alias
/usr/lib64/aspell-0.60/french-lrg.alias
/usr/lib64/aspell-0.60/french-med.alias
/usr/lib64/aspell-0.60/french-sml.alias
/usr/lib64/aspell-0.60/french.alias
/usr/lib64/aspell-0.60/suisse-40.alias
/usr/lib64/aspell-0.60/suisse-60.alias
/usr/lib64/aspell-0.60/suisse-80.alias
/usr/lib64/aspell-0.60/suisse-lrg.alias
/usr/lib64/aspell-0.60/suisse-med.alias
/usr/lib64/aspell-0.60/suisse-sml.alias
/usr/lib64/aspell-0.60/suisse.alias

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/aspell-fr/0b184ad51ba2a79e85d2288d5fcf8a1ea0481ea4
