#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : gnupg
Version  : 2.0.27
Release  : 4
URL      : ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-2.0.27.tar.bz2
Source0  : ftp://ftp.gnupg.org/gcrypt/gnupg/gnupg-2.0.27.tar.bz2
Summary  : No detailed summary available
Group    : Development/Tools
License  : GPL-3.0 LGPL-3.0
Requires: gnupg-bin
Requires: gnupg-doc
Requires: gnupg-data
Requires: gnupg-locales
BuildRequires : bzip2-dev
BuildRequires : curl-dev
BuildRequires : libassuan-dev
BuildRequires : libgcrypt-dev
BuildRequires : libgpg-error-dev
BuildRequires : libksba-dev
BuildRequires : pkgconfig(zlib)
BuildRequires : pth-dev

%description
The GNU Privacy Guard
=======================
Version 2.0
INTRODUCTION
============

%package bin
Summary: bin components for the gnupg package.
Group: Binaries
Requires: gnupg-data

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

%description doc
doc components for the gnupg package.


%package locales
Summary: locales components for the gnupg package.
Group: Default

%description locales
locales components for the gnupg package.


%prep
%setup -q -n gnupg-2.0.27

%build
%configure --disable-static
make V=1 %{?_smp_mflags}

%check
make VERBOSE=1 V=1 %{?_smp_mflags} check

%install
rm -rf %{buildroot}
%make_install
%find_lang gnupg2
## make_install_append content
ln -s gpg2 %{buildroot}/usr/bin/gpg
## make_install_append end

%files
%defattr(-,root,root,-)

%files bin
%defattr(-,root,root,-)
/usr/bin/addgnupghome
/usr/bin/applygnupgdefaults
/usr/bin/gpg
/usr/bin/gpg-agent
/usr/bin/gpg-connect-agent
/usr/bin/gpg2
/usr/bin/gpgconf
/usr/bin/gpgkey2ssh
/usr/bin/gpgparsemail
/usr/bin/gpgsm
/usr/bin/gpgsm-gencert.sh
/usr/bin/gpgv2
/usr/bin/kbxutil
/usr/bin/watchgnupg
/usr/libexec/gnupg-pcsc-wrapper
/usr/libexec/gpg-check-pattern
/usr/libexec/gpg-preset-passphrase
/usr/libexec/gpg-protect-tool
/usr/libexec/gpg2keys_curl
/usr/libexec/gpg2keys_finger
/usr/libexec/gpg2keys_hkp
/usr/libexec/scdaemon

%files data
%defattr(-,root,root,-)
/usr/share/gnupg/com-certs.pem
/usr/share/gnupg/gpg-conf.skel
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
/usr/share/gnupg/qualified.txt

%files doc
%defattr(-,root,root,-)
%doc /usr/share/doc/gnupg/*
%doc /usr/share/info/*
%doc /usr/share/man/man1/*
%doc /usr/share/man/man8/*

%files locales -f gnupg2.lang 
%defattr(-,root,root,-)

