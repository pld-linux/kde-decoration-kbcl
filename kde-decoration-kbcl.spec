%define		_decoration 	kbcl
Summary:	Kwin decoration - %{_decoration}
Summary(pl):	Dekoracja kwin - %{_decoration}
Name:		kde-decoration-%{_decoration}
Version:	1.0.7
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.geocities.jp/prefsx1/kbcl/%{_decoration}-%{version}.tar.gz
# Source0-md5:	9502827b16327b2cf89370d68a538aaf
URL:		http://www.kde-look.org/content/show.php?content=11219	
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	freetype-devel
BuildRequires:	qt-devel >= 3.0.5
Requires:	kdelibs
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define         _htmldir        /usr/share/doc/kde/HTML

%description
k3dnomore is one of more creative kwin decorations found on kde-look,
includes configuration module for kcontrol.

%description -l pl
k3dnomore to jedna z najbardziej kreatywnych dekoracji kwin, jakie
mo¿na znale¼æ na kde-look. Zawiera modu³ konfiguracyjny dla kcontrol.

%prep
%setup -q -n %{_decoration}-%{version}

%build
kde_htmldir="%{_htmldir}"; export kde_htmldir
kde_icondir="%{_pixmapsdir}"; export kde_icondir

%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_libdir}/kde3/*.la
%attr(755,root,root) %{_libdir}/kde3/*.so
%{_datadir}/apps/kwin/*
