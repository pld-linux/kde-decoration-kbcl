%define		_decoration 	kbcl
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0.8
Release:	3
License:	GPL
Group:		Themes
Source0:	http://www.geocities.jp/prefsx1/kbcl/%{_decoration}-%{version}.tar.gz
# Source0-md5:	d6b2d3bef51a912aef495e105c09c4e9
URL:		http://www.kde-look.org/content/show.php?content=11219
BuildRequires:	autoconf
BuildRequires:	unsermake
BuildRequires:	automake
BuildRequires:	kdelibs-devel >= 9:3.2.0
BuildRequires:	kdebase-desktop-libs >= 9:3.2.0
Requires:	kdebase-desktop-libs >= 9:3.2.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
A mild-colored and convexed clone of Luna from Windows XP.

%description -l pl
Klon dekoracji Luna znanej z Windows XP z dodanym poczuciem wypukłości
i łagodniejszym doborem kolorów.

%prep
%setup -q -n %{_decoration}-%{version}

%build
cp -f %{_datadir}/automake/config.sub admin
export UNSERMAKE=%{_datadir}/unsermake/unsermake
%{__make} -f Makefile.cvs

%configure \
	--with-qt-libraries=%{_libdir}
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT \
	kde_htmldir="%{_kdedocdir}"


%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kwin/*
