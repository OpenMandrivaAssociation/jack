%define version 3.1.1
%define rel	 4
%define release %mkrel %{rel}

Summary:	Console frontend for CD rippers and audio encoders
Name:		jack
Version:	%{version}
Release:	%{release}
License:	GPL
Group:		Sound
URL:		http://www.home.unix-ag.org/arne/jack/

Source0:	%{name}-%{version}.tar.bz2

BuildRequires:	python-devel
BuildRequires:	python-ID3 
BuildRequires:	python-CDDB
BuildRequires:	pyid3lib
BuildRequires:	pyvorbis >= 1.0
BuildRequires:	ncurses-devel
Requires:	python-ID3
Requires:	python-CDDB
Requires:	vorbis-tools 
Requires:	pyid3lib
Requires:	pyvorbis >= 1.0
Requires:	cdparanoia

%description
Jack has been developed with one main goal: ripping CDs without having
to worry. There is nearly no way that an incomplete rip goes
unnoticed, e.g. jack compares WAV and MP3/Vorbis filesizes when continuing
from a previous run. Jack also checks your HD space before doing
anything (even keeps some MB free).

%prep
%setup -q

%build
python setup.py build
python -c "import jack_CDTime"
python -c "import jack_misc"
python -c "import jack_mp3"
python -c "import jack_TOCentry"
python -c "import jack_TOC"

%install
rm -rf %{buildroot}
python setup.py install --root %{buildroot}
install -D -m 755 jack %{buildroot}%{_bindir}/jack
install -D -m 644 jack.man %{buildroot}%{_mandir}/man1/jack.1
cp jack_* %{buildroot}%{_libdir}/python%{pyver}/site-packages/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc doc/* README
%{_bindir}/jack
%{_libdir}/python%{pyver}/site-packages/*
%{_mandir}/man?/*
