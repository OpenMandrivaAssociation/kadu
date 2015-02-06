%define _disable_ld_no_undefined 1

Summary:	A Gadu-Gadu client for online messaging
Name:		kadu
Version:	0.11.3
Release:	2
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.kadu.net
Source0:	http://download.kadu.im/stable/kadu-%{version}.tar.bz2
BuildRequires:	cmake
BuildRequires:	qt4-devel >= 4.7.0
BuildRequires:	aspell-devel
BuildRequires:	libgadu-devel >= 1.11.1
BuildRequires:	idn-devel
BuildRequires:	qca2-devel
BuildRequires:	pkgconfig(phonon)
BuildRequires:	pkgconfig(sndfile)
BuildRequires:	libxscrnsaver-devel
BuildRequires:	libmpdclient-devel

Obsoletes:	kadu-module-mediaplayer_falf < 0.10.1
Obsoletes:	kadu-emoticons_gg6_compatible < 0.10.1
Obsoletes:	kadu-emoticons_penguins < 0.10.1
Obsoletes:	kadu-emoticons_tango < 0.10.1
Obsoletes:	kadu-icons_glass < 0.10.1
Obsoletes:	kadu-icons_oxygen < 0.10.1
Obsoletes:	kadu-module-alsa_sound < 0.10.1
Obsoletes:	kadu-module-anonymous_check < 0.10.1
Obsoletes:	kadu-module-antistring < 0.10.1
Obsoletes:	kadu-module-ao_sound < 0.10.1
Obsoletes:	kadu-module-autoaway < 0.10.1
Obsoletes:	kadu-module-auto_hide < 0.10.1
Obsoletes:	kadu-module-auto_responder < 0.10.1
Obsoletes:	kadu-module-autostatus < 0.10.1
Obsoletes:	kadu-module-bmpx_mediaplayer < 0.10.1
Obsoletes:	kadu-module-cenzor < 0.10.1
Obsoletes:	kadu-module-config_wizard < 0.10.1
Obsoletes:	kadu-module-desktop_docking < 0.10.1
Obsoletes:	kadu-module-encryption_ng < 0.10.1
Obsoletes:	kadu-module-encryption_ng_simlite < 0.10.1
Obsoletes:	kadu-module-exec_notify < 0.10.1
Obsoletes:	kadu-module-ext_sound < 0.10.1
Obsoletes:	kadu-module-filedesc < 0.10.1
Obsoletes:	kadu-module-firewall < 0.10.1
Obsoletes:	kadu-module-gadu_protocol < 0.10.1
Obsoletes:	kadu-module-globalhotkeys < 0.10.1
Obsoletes:	kadu-module-hints < 0.10.1
Obsoletes:	kadu-module-history < 0.10.1
Obsoletes:	kadu-module-history_migration < 0.10.1
Obsoletes:	kadu-module-idle < 0.10.1
Obsoletes:	kadu-module-imagelink < 0.10.1
Obsoletes:	kadu-module-importhistory < 0.10.1
Obsoletes:	kadu-module-jabber_protocol < 0.10.1
Obsoletes:	kadu-module-kde-notify < 0.10.1
Obsoletes:	kadu-module-last_seen < 0.10.1
Obsoletes:	kadu-module-led_notify < 0.10.1
Obsoletes:	kadu-module-mediaplayer < 0.10.1
Obsoletes:	kadu-module-mediaplayer_amarok2 < 0.10.1
Obsoletes:	kadu-module-mediaplayer_audacious < 0.10.1
Obsoletes:	kadu-module-mediaplayer_dragon < 0.10.1
Obsoletes:	kadu-module-mediaplayer_mpris < 0.10.1
Obsoletes:	kadu-module-mediaplayer_vlc < 0.10.1
Obsoletes:	kadu-module-mime_tex < 0.10.1
Obsoletes:	kadu-module-nextinfo < 0.10.1
Obsoletes:	kadu-module-panelkadu < 0.10.1
Obsoletes:	kadu-module-parser_extender < 0.10.1
Obsoletes:	kadu-module-pcspeaker < 0.10.1
Obsoletes:	kadu-module-phonon_sound < 0.10.1
Obsoletes:	kadu-module-profiles_import < 0.10.1
Obsoletes:	kadu-module-qt4_docking < 0.10.1
Obsoletes:	kadu-module-qt4_docking_notify < 0.10.1
Obsoletes:	kadu-module-qt4_sound < 0.10.1
Obsoletes:	kadu-module-screenshot < 0.10.1
Obsoletes:	kadu-module-sent_history < 0.10.1
Obsoletes:	kadu-module-server_monitor < 0.10.1
Obsoletes:	kadu-module-simpleview < 0.10.1
Obsoletes:	kadu-module-single_window < 0.10.1
Obsoletes:	kadu-module-sms < 0.10.1
Obsoletes:	kadu-module-speech < 0.10.1
Obsoletes:	kadu-module-spellchecker < 0.10.1
Obsoletes:	kadu-module-sql_history < 0.10.1
Obsoletes:	kadu-module-tabs < 0.10.1
Obsoletes:	kadu-module-word_fix < 0.10.1
Obsoletes:	kadu-sound_bns < 0.10.1
Obsoletes:	kadu-sound_default < 0.10.1
Obsoletes:	kadu-sound_drums < 0.10.1
Obsoletes:	kadu-sound_florkus < 0.10.1
Obsoletes:	kadu-sound_michalsrodek < 0.10.1
Obsoletes:	kadu-sound_percussion < 0.10.1
Obsoletes:	kadu-sound_ultr < 0.10.1

%description
Kadu is a dynamically evolving instant messenger 
compatible with the Gadu-Gadu protocol. It can be run 
on all platforms supporting the Qt toolkit (except Windows).

Compiled as modular as possible.

Static modules are:
- docking
- sound

%prep
%setup -q

%build
%cmake -DENABLE_AUTODOWNLOAD:BOOL=OFF
%make

%install
%makeinstall_std -C build

rm -fr %{buildroot}%{_includedir} %{buildroot}%{_datadir}/cmake

%files
%{_bindir}/*
%{_libdir}/kadu
%{_datadir}/%{name}
%{_datadir}/applications/*.desktop
%{_iconsdir}/hicolor/*/apps/*



%changelog
* Mon May 28 2012 Andrey Bondrov <abondrov@mandriva.org> 0.11.3-1
+ Revision: 800981
- Update BuildRequires
- Update BuildRequires
- New version 0.11.3

  + Alexander Khrukin <akhrukin@mandriva.org>
    - version update 0.11.0

* Mon Nov 07 2011 Andrey Bondrov <abondrov@mandriva.org> 0.10.1-1
+ Revision: 725908
- Add libmpdclient-devel to BuildRequires
- New version 0.10.1, major spec update based on Funda Wang's work in Mageia

* Thu Feb 03 2011 Funda Wang <fwang@mandriva.org> 0.6.5.4-4
+ Revision: 635620
- remove unpacked files
- add fedora patch to make it build
- tighten BR

  + Oden Eriksson <oeriksson@mandriva.com>
    - the mass rebuild of 2010.1 packages

* Sat May 15 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.4-2mdv2010.1
+ Revision: 544854
- drop requires on powiedz

* Sun Mar 07 2010 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.4-1mdv2010.1
+ Revision: 515520
- update to new version 0.6.5.4
- update modules globalhotkeys, kde_notify and tabs
- update themes
- add tango theme
- enable modules qt4-sound, speech dbus, mpris
- disable modules mail

* Sat Nov 14 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.3-4mdv2010.1
+ Revision: 466055
- fix file list
- enable mediaplayer modules

* Sat Oct 10 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.3-3mdv2010.0
+ Revision: 456532
- rebuild for new libgadu

* Thu Oct 08 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.3-2mdv2010.0
+ Revision: 455871
- rebuild for new curl SSL backend

* Sun Sep 20 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.3-1mdv2010.0
+ Revision: 445732
- fix instalation on x86_64
- update to new version 0.6.5.3
- drop patch 8, fixed upstream
- new module kde4-notify
- update modules:
  o anonymous_check
  o globalhotkeys
  o mail
  o mime_tex
  o plus_pl_sms
  o panelkadu
  o powerkadu
  o sent_history
  o water notify
  o weather
  o tabs

* Sat Jun 06 2009 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5.2-1mdv2010.0
+ Revision: 383347
- update to new version 0.5.6.2
- disable profiles module for now
- Patch8: fix compiling against gcc-4.4.0
- add missing buildrequires on qca-devel
- new module - idle
- fix file list

* Sat Dec 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5-2mdv2009.1
+ Revision: 316458
- module miastoplusa_sms is obsoleted by plus_pl_sms module
- fix sound theme install directory
- use %%define Werror_cflags

* Sat Dec 13 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.5-1mdv2009.1
+ Revision: 313865
- fix building on x86_64 (cmake stuff doesn't obey lib64 ?)
- update modules anonymous_check and mime_tex
- disable module weather
- kill devel subpackage
- fix file list
- few external modules was adopted by upstream, which means these are now in tarball
  o exec_notify, filedesc, filterning, firewall, pcspeaker, profiles, screenshot, spellchecker, antistring, auto_hide, cenzor, parser_extender,word_fix, last_seen and autostatus
- do not check for upstream new releases
- fix libdir
- set up proper DETAILED_VERSION
- use %%define _disable_ld_no_undefined 1
- fix file list (that was a real mess :)
- Patch6: rediff
- still work in progress
- disable autodownload moudules/themes etc.
- update to version 0.6.5
  o work in progress
  o kadu uses now Qt4 toolkit
- add buildrequires on cmake and libpng-devel
- disable all patches

* Fri Jul 18 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0.2-3mdv2009.0
+ Revision: 238060
- fix missing kadu entry in KDE menu (#42101)

* Sat Jul 12 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0.2-2mdv2009.0
+ Revision: 234090
- do not change dataPath, as it is working fine(hard to tell why i've modified this :| )
- remove not working configure options

* Fri Jul 11 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0.2-1mdv2009.0
+ Revision: 233661
- add buildrequires on sqlite3-devel
- new module desc_history
- tar is quite smart, it can figure out what kind of archive it is dealing with ;)
- update to new version 0.6.0.2

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Wed May 28 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0.1-1mdv2009.0
+ Revision: 212734
- update to new version 0.6.0.1
- new modules
  o autostatus
  o globalhotkeys
- update modules
  o firewall
  o last_seen
  o mime_tex
  o panelkadu
  o powerkadu
  o tabs
- disable arts module
- spec file clean

* Sat Mar 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-1mdv2008.1
+ Revision: 182160
- drop patch 0, use sed instead
- add new icons themes:
  o tango
  o oxygen
- new modules:
  o anonymous
  o antistring
  o auto_hide
  o cenzor
  o last_seen
  o mime_tex
  o parser_extender
  o split_messages
  o word_fix
- obsolete module-xqf
- update to the stable version 0.6.0
- use conditionals for building modules
- rediff patches 4 and 5
- drop patch 2
- tune up desktop file
- new release candidate
- new module: panelkadu
- update osdhints_notify module

* Sun Feb 17 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-0.rc3.1mdv2008.1
+ Revision: 170057
- add water_notify plugin, which enables notifications by water effet in compiz
- add patch 7, which enables building of water_plugin on x86_64
- export -DDBUS_API_SUBJECT_TO_CHANGE
- update modules
  o agent
  o filtering
  o firewall
  o mediaplayer
  o osdhints_notify
  o tabs
- update to latest release candidate

* Fri Feb 08 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-0.rc2.1mdv2008.1
+ Revision: 164208
- update to the latest release candidate rc2
- update modules
- enable modules
  o osdhints_notify
  o pcspeaker
- update modules
  o filtering
  o led_notify
  o mediaplayer
  o pcspeaker
  o weather

* Sun Jan 20 2008 Tomasz Pawel Gajc <tpg@mandriva.org> 0.6.0-0.rc1.1mdv2008.1
+ Revision: 155420
- add falf mediaplayer module
- fix linking against libgsm with patch 6
- exclude net needed files
- let's submit this ;)
- fix file list
- module-amarok became module-mediaplayer-amarok
- module-xmms became module-mediaplayer-xmms
- fix modules data path
- remove hardcoded icon extension in desktop file
- use desktop-file-install
- update firewall module
- update modules
  o amarok
  o dcopexport
  o falf
  o filedesc
  o miastoplusa
  o osd_hints
  o powerkadu
  o profiles
  o screenshot
  o spellchecker
  o xmms
- new modules
  o mediaplayer
  o agent
- configure script can now disable autodownloading feature, so patch 3 is not needed anymore
- update kadu modules to the latest release
  o xosd_notify
  o screenshot
  o weather
  o tabs
  o xmms
  o led_notify
  o ext_info
- update glass icon theme
- add new tango icon theme
- rediff patch 0
- somehow sources didn't get synced, a bad sign ?
- new release candidate
- this is a work-in-progress, because not all modules will be working(with 0.6.0+) and probably lot of them will be droped, as just upstream did
- let's begin ;)

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Dec 14 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-9mdv2008.1
+ Revision: 119606
- new license policy

* Wed Jun 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-9mdv2008.0
+ Revision: 38616
- rebuild against libgadu
- use default files attributes
- set requires on falf for a module-falfpl

* Tue May 22 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-7mdv2008.0
+ Revision: 29625
- correct configure options

* Sun Apr 29 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-6mdv2008.0
+ Revision: 19139
- rebuild against libgadu 1.7
- some spec file cleans


* Tue Feb 27 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-5mdv2007.0
+ Revision: 126628
- drop not needed requires/provides

* Tue Feb 13 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-4mdv2007.1
+ Revision: 120304
- move icons to more appropriate directory
- remove twice listed directory

* Fri Feb 09 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-3mdv2007.1
+ Revision: 118397
- rebuild
- add better provides for devel package
- fix typo
- drop patch 1
- own missing directories
- some minor cleans in spec file

* Wed Jan 03 2007 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-1mdv2007.1
+ Revision: 103878
- final release 0.5.0
- updated modules advanced_userlist, dcopexport, exec_notify
- disable kadu_cumulative-20061230 patch
- module encryption now is in main package

* Sun Dec 31 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.20061231.1mdv2007.1
+ Revision: 103003
- forgot to add falfpl and qf modules :(
- spec file clean
- weather in now standalone module
- new snapshot
- new module xqf
- updated falf, tabs and xmms modules
- drop patches 8, 9
- add kadu_cumulative-20061230 patch

* Sat Dec 23 2006 Tomasz Pawel Gajc <tpg@mandriva.org> 0.5.0-0.20061223.1mdv2007.1
+ Revision: 101946
-new snapshot
- updated modules ext_info, filtering and firewall
- added new modules spy and falfp
- spec file clean
- added %%multiarch for kadu-config (thanks goes to Anssi and misc)
- updated docs for few modules

* Mon Nov 27 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-0.20061127.1mdv2007.1
+ Revision: 87388
- new snapshot
- update the screenshot, powerkadu and dcopexport modules

* Wed Nov 08 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-0.20061108.1mdv2007.0
+ Revision: 78161
- add new
- add new version
- new snapshot
- update amarok, screenshot, xmms and snapshot
- add advanced userlist
- drop patches 6,7,9
- spec fixes
- move desktop entry to the right dir

* Wed Nov 01 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-0.20061101.2mdv2007.1
+ Revision: 75046
- fix buildrequires
- new version
- new snapshot
- update ext_info and powerkadu
- spec fixes
- patch all modules that use an old API
- new snapshot
- add devel package
- spec cleanup

* Thu Oct 26 2006 Götz Waschk <waschk@mandriva.org> 0.5.0-0.20061023.1mdv2007.1
+ Revision: 72614
- Import kadu

* Thu Oct 26 2006 G�tz Waschk <waschk@mandriva.org> 0.5.0-0.20061023.1mdv2007.1
- fix desktop entry
- spec file cleanup

* Wed Oct 25 2006 Tomasz Paweł Gajc <phenomenal at wp dot pl> 0.5.0-0.20061023.1mdv2007.1
- New snapshot
- Alsa is now default sound subsystem

* Mon Oct 23 2006 Tomasz Paweł Gajc <phenomenal at wp dot pl> 0.5.0-0.20061022.1mdv2007.1
- initial package for mdv
- patches 0,1,2,3

