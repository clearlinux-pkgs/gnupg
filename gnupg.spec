#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
# Using build pattern: configure
# autospec version: v26
# autospec commit: 99a7985
#
# Source0 file verified with key 0x528897B826403ADA
#
Name     : gnupg
Version  : 2.4.8
Release  : 103
URL      : https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.4.8.tar.bz2
Source0  : https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.4.8.tar.bz2
Source1  : https://gnupg.org/ftp/gcrypt/gnupg/gnupg-2.4.8.tar.bz2.sig
Source2  : 528897B826403ADA.pkey
Summary  : zlib compression library
Group    : Development/Tools
License  : BSD-3-Clause CC0-1.0 GPL-2.0 GPL-3.0 LGPL-2.1 LGPL-3.0 NCSA
Requires: gnupg-bin = %{version}-%{release}
Requires: gnupg-data = %{version}-%{release}
Requires: gnupg-info = %{version}-%{release}
Requires: gnupg-libexec = %{version}-%{release}
Requires: gnupg-license = %{version}-%{release}
Requires: gnupg-locales = %{version}-%{release}
Requires: gnupg-man = %{version}-%{release}
Requires: pcsc-lite
Requires: pinentry
BuildRequires : buildreq-configure
BuildRequires : bzip2-dev
BuildRequires : gnupg
BuildRequires : libassuan-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libgpg-error-extras
BuildRequires : libksba-dev
BuildRequires : libusb-dev
BuildRequires : npth-dev
BuildRequires : pkgconfig(gnutls)
BuildRequires : pkgconfig(sqlite3)
BuildRequires : pkgconfig(zlib)
# Suppress stripping binaries
%define __strip /bin/true
%define debug_package %{nil}
Patch1: 0001-Warn-on-use-of-insecure-3DES-algo.patch
Patch2: backport-b1857a2836c9a91ef4e359ef7ba949b54c77219d.patch

%description
The GNU Privacy Guard
=======================
Version 2.4
* INTRODUCTION
GnuPG is a complete and free implementation of the OpenPGP standard
as defined by RFC4880 (also known as PGP).  GnuPG enables encryption
and signing of data and communication, and features a versatile key
management system as well as access modules for public key
directories.

%package bin
Summary: bin components for the gnupg package.
Group: Binaries
Requires: gnupg-data = %{version}-%{release}
Requires: gnupg-libexec = %{version}-%{release}
Requires: gnupg-license = %{version}-%{release}

%description bin
bin components for the gnupg package.


%package data
Summary: data components for the gnupg package.
Group: Data

%description data
data components for the gnupg package.


%package doc
Summary: doc components for the gnupg package.
Group: Documentation
Requires: gnupg-man = %{version}-%{release}
Requires: gnupg-info = %{version}-%{release}

%description doc
doc components for the gnupg package.


%package info
Summary: info components for the gnupg package.
Group: Default

%description info
info components for the gnupg package.


%package libexec
Summary: libexec components for the gnupg package.
Group: Default
Requires: gnupg-license = %{version}-%{release}

%description libexec
libexec components for the gnupg package.


%package license
Summary: license components for the gnupg package.
Group: Default

%description license
license components for the gnupg package.


%package locales
Summary: locales components for the gnupg package.
Group: Default

%description locales
locales components for the gnupg package.


%package man
Summary: man components for the gnupg package.
Group: Default

%description man
man components for the gnupg package.


%prep
mkdir .gnupg
chmod 700 .gnupg
gpg --homedir .gnupg --import %{SOURCE2}
gpg --homedir .gnupg --status-fd 1 --verify %{SOURCE1} %{SOURCE0} > gpg.status
grep -E '^\[GNUPG:\] (GOODSIG|EXPKEYSIG) 528897B826403ADA' gpg.status
%setup -q -n gnupg-2.4.8
cd %{_builddir}/gnupg-2.4.8
%patch -P 1 -p1
%patch -P 2 -p1
pushd ..
cp -a gnupg-2.4.8 buildavx2
popd

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1747232217
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export GOAMD64=v2
%configure --disable-static --disable-rpath
make  %{?_smp_mflags}

unset PKG_CONFIG_PATH
pushd ../buildavx2/
GOAMD64=v3
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -march=x86-64-v3 -Wl,-z,x86-64-v3 "
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS -march=x86-64-v3 "
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS -march=x86-64-v3 "
%configure --disable-static --disable-rpath
make  %{?_smp_mflags}
popd
%check
export LANG=C.UTF-8
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
make check || :

%install
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
CLEAR_INTERMEDIATE_CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FCFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CLEAR_INTERMEDIATE_CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS -O3 -fdebug-types-section -femit-struct-debug-baseonly -ffat-lto-objects -flto=auto -fstack-protector-strong -fzero-call-used-regs=used -g1 -gno-column-info -gno-variable-location-views -gz=zstd "
CFLAGS="$CLEAR_INTERMEDIATE_CFLAGS"
CXXFLAGS="$CLEAR_INTERMEDIATE_CXXFLAGS"
FFLAGS="$CLEAR_INTERMEDIATE_FFLAGS"
FCFLAGS="$CLEAR_INTERMEDIATE_FCFLAGS"
ASFLAGS="$CLEAR_INTERMEDIATE_ASFLAGS"
LDFLAGS="$CLEAR_INTERMEDIATE_LDFLAGS"
export SOURCE_DATE_EPOCH=1747232217
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/gnupg
cp %{_builddir}/gnupg-%{version}/COPYING %{buildroot}/usr/share/package-licenses/gnupg/4bc05f7560e1e3ced08b71c93f10abe9e702c3ee || :
cp %{_builddir}/gnupg-%{version}/COPYING.CC0 %{buildroot}/usr/share/package-licenses/gnupg/754becb73f3b288d7d8a62d8927a334cd38ac10b || :
cp %{_builddir}/gnupg-%{version}/COPYING.GPL2 %{buildroot}/usr/share/package-licenses/gnupg/4cc77b90af91e615a64ae04893fdffa7939db84c || :
cp %{_builddir}/gnupg-%{version}/COPYING.LGPL21 %{buildroot}/usr/share/package-licenses/gnupg/ac1b58bbd5bc11cacb7205718d620156ffd57c7e || :
cp %{_builddir}/gnupg-%{version}/COPYING.LGPL3 %{buildroot}/usr/share/package-licenses/gnupg/bf58811df8e4261d540cc1872f42011872ca8f54 || :
cp %{_builddir}/gnupg-%{version}/COPYING.other %{buildroot}/usr/share/package-licenses/gnupg/366d4e13a65adbfd0f7972f4c8dc9891692e92e5 || :
cp %{_builddir}/gnupg-%{version}/tests/gpgscm/LICENSE.TinySCHEME %{buildroot}/usr/share/package-licenses/gnupg/ca474fc88304aab05401b27d158b3f9e0c1ffae6 || :
export GOAMD64=v2
GOAMD64=v3
pushd ../buildavx2/
%make_install_v3
popd
GOAMD64=v2
%make_install
%find_lang gnupg2
## install_append content
ln -s gpg %{buildroot}/usr/bin/gpg2
## install_append end
/usr/bin/elf-move.py avx2 %{buildroot}-v3 %{buildroot} %{buildroot}/usr/share/clear/filemap/filemap-%{name}

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/V3/usr/bin/dirmngr
/V3/usr/bin/dirmngr-client
/V3/usr/bin/gpg
/V3/usr/bin/gpg-agent
/V3/usr/bin/gpg-card
/V3/usr/bin/gpg-connect-agent
/V3/usr/bin/gpg-mail-tube
/V3/usr/bin/gpg-wks-client
/V3/usr/bin/gpg-wks-server
/V3/usr/bin/gpgconf
/V3/usr/bin/gpgparsemail
/V3/usr/bin/gpgscm
/V3/usr/bin/gpgsm
/V3/usr/bin/gpgsplit
/V3/usr/bin/gpgtar
/V3/usr/bin/gpgv
/V3/usr/bin/kbxutil
/V3/usr/bin/watchgnupg
/usr/bin/addgnupghome
/usr/bin/applygnupgdefaults
/usr/bin/dirmngr
/usr/bin/dirmngr-client
/usr/bin/gpg
/usr/bin/gpg-agent
/usr/bin/gpg-card
/usr/bin/gpg-connect-agent
/usr/bin/gpg-mail-tube
/usr/bin/gpg-wks-client
/usr/bin/gpg-wks-server
/usr/bin/gpg2
/usr/bin/gpgconf
/usr/bin/gpgparsemail
/usr/bin/gpgscm
/usr/bin/gpgsm
/usr/bin/gpgsplit
/usr/bin/gpgtar
/usr/bin/gpgv
/usr/bin/kbxutil
/usr/bin/watchgnupg

%files data
%defattr(-,root,root,-)
/usr/share/gnupg/distsigkey.gpg
/usr/share/gnupg/help.be.txt
/usr/share/gnupg/help.ca.txt
/usr/share/gnupg/help.cs.txt
/usr/share/gnupg/help.da.txt
/usr/share/gnupg/help.de.txt
/usr/share/gnupg/help.el.txt
/usr/share/gnupg/help.eo.txt
/usr/share/gnupg/help.es.txt
/usr/share/gnupg/help.et.txt
/usr/share/gnupg/help.fi.txt
/usr/share/gnupg/help.fr.txt
/usr/share/gnupg/help.gl.txt
/usr/share/gnupg/help.hu.txt
/usr/share/gnupg/help.id.txt
/usr/share/gnupg/help.it.txt
/usr/share/gnupg/help.ja.txt
/usr/share/gnupg/help.nb.txt
/usr/share/gnupg/help.pl.txt
/usr/share/gnupg/help.pt.txt
/usr/share/gnupg/help.pt_BR.txt
/usr/share/gnupg/help.ro.txt
/usr/share/gnupg/help.ru.txt
/usr/share/gnupg/help.sk.txt
/usr/share/gnupg/help.sv.txt
/usr/share/gnupg/help.tr.txt
/usr/share/gnupg/help.txt
/usr/share/gnupg/help.zh_CN.txt
/usr/share/gnupg/help.zh_TW.txt
/usr/share/gnupg/sks-keyservers.netCA.pem

%files doc
%defattr(0644,root,root,0755)
/usr/share/doc/gnupg/*

%files info
%defattr(0644,root,root,0755)
/usr/share/info/gnupg.info
/usr/share/info/gnupg.info-1
/usr/share/info/gnupg.info-2
/usr/share/info/gnupg.info-3

%files libexec
%defattr(-,root,root,-)
/V3/usr/libexec/gpg-auth
/V3/usr/libexec/gpg-check-pattern
/V3/usr/libexec/gpg-pair-tool
/V3/usr/libexec/gpg-preset-passphrase
/V3/usr/libexec/gpg-protect-tool
/V3/usr/libexec/keyboxd
/V3/usr/libexec/scdaemon
/usr/libexec/gpg-auth
/usr/libexec/gpg-check-pattern
/usr/libexec/gpg-pair-tool
/usr/libexec/gpg-preset-passphrase
/usr/libexec/gpg-protect-tool
/usr/libexec/gpg-wks-client
/usr/libexec/keyboxd
/usr/libexec/scdaemon

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/gnupg/366d4e13a65adbfd0f7972f4c8dc9891692e92e5
/usr/share/package-licenses/gnupg/4bc05f7560e1e3ced08b71c93f10abe9e702c3ee
/usr/share/package-licenses/gnupg/4cc77b90af91e615a64ae04893fdffa7939db84c
/usr/share/package-licenses/gnupg/754becb73f3b288d7d8a62d8927a334cd38ac10b
/usr/share/package-licenses/gnupg/ac1b58bbd5bc11cacb7205718d620156ffd57c7e
/usr/share/package-licenses/gnupg/bf58811df8e4261d540cc1872f42011872ca8f54
/usr/share/package-licenses/gnupg/ca474fc88304aab05401b27d158b3f9e0c1ffae6

%files man
%defattr(0644,root,root,0755)
/usr/share/man/man1/dirmngr-client.1
/usr/share/man/man1/gpg-agent.1
/usr/share/man/man1/gpg-card.1
/usr/share/man/man1/gpg-check-pattern.1
/usr/share/man/man1/gpg-connect-agent.1
/usr/share/man/man1/gpg-mail-tube.1
/usr/share/man/man1/gpg-preset-passphrase.1
/usr/share/man/man1/gpg-wks-client.1
/usr/share/man/man1/gpg-wks-server.1
/usr/share/man/man1/gpg.1
/usr/share/man/man1/gpgconf.1
/usr/share/man/man1/gpgparsemail.1
/usr/share/man/man1/gpgsm.1
/usr/share/man/man1/gpgtar.1
/usr/share/man/man1/gpgv.1
/usr/share/man/man1/scdaemon.1
/usr/share/man/man1/watchgnupg.1
/usr/share/man/man7/gnupg.7
/usr/share/man/man8/addgnupghome.8
/usr/share/man/man8/applygnupgdefaults.8
/usr/share/man/man8/dirmngr.8

%files locales -f gnupg2.lang
%defattr(-,root,root,-)

