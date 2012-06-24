%define		_decoration 	kbcl
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0.8
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.geocities.jp/prefsx1/kbcl/%{_decoration}-%{version}.tar.gz
# Source0-md5:	d6b2d3bef51a912aef495e105c09c4e9
URL:		http://www.kde-look.org/content/show.php?content=11219	
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	qt-devel >= 3.0.5
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
KBCL kwin decoration: Keramik Based Crystal Luna.

%description -l pl
Dekoracja kwin KBCL - Keramik Based Crystal Luna (oparta na Keramiku).

%prep
%setup -q -n %{_decoration}-%{version}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kwin/*
