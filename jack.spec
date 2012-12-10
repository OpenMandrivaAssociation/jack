Summary:		Console frontend for CD rippers and audio encoders
Name:		jack
Version:		3.1.1
Release:		9
License:		GPL
Group:		Sound
URL:		http://www.home.unix-ag.org/arne/jack/
Source0:		%{name}-%{version}.tar.bz2
BuildRequires:	python-devel
BuildRequires:	python-id3 
BuildRequires:	python-CDDB
BuildRequires:	pyid3lib
BuildRequires:	pyvorbis >= 1.0
BuildRequires:	ncurses-devel
Requires:	python-id3
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
python setup.py install --root %{buildroot}
install -D -m 755 jack %{buildroot}%{_bindir}/jack
install -D -m 644 jack.man %{buildroot}%{_mandir}/man1/jack.1
mkdir -p %{buildroot}%{_libdir}/python%{py_ver}/site-packages/
cp jack_* %{buildroot}%{_libdir}/python%{py_ver}/site-packages/


%files
%doc doc/* README
%{_bindir}/jack
%{_libdir}/python%{py_ver}/site-packages/*
%{_mandir}/man?/*


%changelog
* Wed Oct 31 2012 Giovanni Mariani <mc2374@mclink.it> 3.1.1-9
- Dropped BuildRoot, %%mkrel, %%defattr, %%clean section
- Adjusted BReq (there is no python-ID3 package)
- Use %%{py_ver} macro instead of %%{pyver}

* Wed Nov 16 2011 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.1-8mdv2012.0
+ Revision: 731089
- rebuild
- rebuild

* Fri Nov 12 2010 Bogdano Arendartchuk <bogdano@mandriva.com> 3.1.1-6mdv2011.0
+ Revision: 597011
- rebuild for python 2.7

* Fri Sep 11 2009 Thierry Vignaud <tv@mandriva.org> 3.1.1-5mdv2011.0
+ Revision: 438015
- rebuild

* Thu Feb 14 2008 Thierry Vignaud <tv@mandriva.org> 3.1.1-4mdv2009.0
+ Revision: 167925
- fix no-buildroot-tag
- kill re-definition of %%buildroot on Pixel's request

* Wed Aug 01 2007 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.1-4mdv2008.0
+ Revision: 57392
- Import jack



* Mon Jul 31 2006 GÃ¶tz Waschk <waschk@mandriva.org> 3.1.1-1mdv2007.0
- Rebuild

* Wed Oct 26 2005 Lenny Cartier <lenny@mandriva.com> 3.1.1-3mdk
- rebuild for allegro

* Thu Jul 28 2005 Eskild Hustvedt <eskild@mandriva.org> 3.1.1-2mdk
- %%mkrel
- Add require for cdparanoia
- Minor changes to the description

* Fri Apr 15 2005 Götz Waschk <waschk@linux-mandrake.com> 3.1.1-1mdk
- fix installation
- New release 3.1.1

* Sun Dec 05 2004 Michael Scherer <misc@mandrake.org> 3.0.0-3mdk
- Rebuild for new python

* Fri Dec  3 2004 Götz Waschk <waschk@linux-mandrake.com> 3.0.0-2mdk
- use pyver macro

* Tue Nov 25 2003 Abel Cheung <deaddog@deaddog.org> 3.0.0-1mdk
- 3.0.0

* Sat Aug  9 2003 Götz Waschk <waschk@linux-mandrake.com> 2.99.9-4mdk
- drop prefix
- new python

* Tue Mar 11 2003 Götz Waschk <waschk@linux-mandrake.com> 2.99.9-3mdk
- fix buildrequires

* Fri Dec 27 2002 Götz Waschk <waschk@linux-mandrake.com> 2.99.9-2mdk
- rebuild

* Wed Oct 23 2002 Götz Waschk <waschk@linux-mandrake.com> 2.99.9-1mdk
- require vorbis wrapper version 1.0
- 2.99.9

* Mon Jul  1 2002 Götz Waschk <waschk@linux-mandrake.com> 2.99.8-4mdk
- require pyvorbis for tagging of ogg files
- require oggenc to work out of the box

* Fri Jun 28 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.99.8-3mdk
- plf => mdk (sorry Goetz)
- add desc it support ogg.

* Fri Jun 28 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.99.8-1plf
- mdk => plf

* Wed Jun 12 2002 Olivier Thauvin <thauvin@aerov.jussieu.fr> 2.99.8-2mdk
- Fix buildrequires on python (<= not =)

* Tue Apr 16 2002 Götz Waschk <waschk@linux-mandrake.com> 2.99.8-1mdk
- 2.99.8
- remove patch

* Thu Feb  7 2002 Götz Waschk <waschk@linux-mandrake.com> 2.99.7-3mdk
- add a fix from cvs for a bug affecting oggenc

* Sun Jan  6 2002 Götz Waschk <waschk@linux-mandrake.com> 2.99.7-2mdk
- python 2.2
- updated BuildRequires

* Mon Nov 26 2001 Götz Waschk <waschk@linux-mandrake.com> 2.99.7-1mdk
- initial package
