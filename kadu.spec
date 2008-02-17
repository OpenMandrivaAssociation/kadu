%define		agent_ver			0.4.4
%define		amarok_ver			20071220
%define		advanced_userlist		20070101
%define		ao_sound_ver			20060424
%define		dcopexport_ver			0.11.3-20071129-0.6.0
%define		exec_notify_ver			20070111
%define		ext_info_ver			2.0beta12
%define		falf_ver			20071225
%define		filedesc_ver			20080104
%define		filtering_ver			20080204
%define		firewall_ver			0.7.5
%define		iwait4u_ver			1.3
%define		led_notify_ver			0.18
%define		mail_ver			0.3.2
%define		mediaplayer_ver			20080210
%define		miastoplusa_sms_ver		0.6-1.3.9
%define		mime_tex_ver			1.4.1
%define		osdhints_notify_ver		0.4.0.5
%define		pcspeaker_ver			0.6.0.3
%define		powerkadu_ver			20070506
%define		profiles_ver			0.3.1
%define		screenshot_ver			20080104
%define		spellchecker_ver		20071230
%define		tabs_ver			1.1.4
%define		water_notify_ver		0.1.1
%define		weather_ver			3.13
%define		xmms_ver			20080116
%define		xosd_notify_ver			20070111

%define prel rc3

Summary:	A Gadu-Gadu client for online messaging
Name:		kadu
Version:	0.6.0
Release:	%mkrel 0.%{prel}.1
License:	GPLv2+
Group:		Networking/Instant messaging
Source0:	http://kadu.net/download/stable/%{name}-%{version}-%{prel}.tar.bz2
Source1:	%{name}.desktop

#Modules sources
Source2: 	http://www.kadu.net/download/modules_extra/amarok_mediaplayer/amarok_mediaplayer-%{amarok_ver}.tar.bz2
Source3: 	http://www.kadu.net/~joi/ao_sound/packages/ao_sound-%{ao_sound_ver}.tar.bz2
Source4: 	http://alan.umcs.lublin.pl/~pinkworm/dcopexport/dcopexport-%{dcopexport_ver}.tar.bz2
Source5: 	http://www.kadu.net/~joi/exec_notify/packages/exec_notify-%{exec_notify_ver}.tar.bz2
Source6: 	http://www.kadu.net/~dzwiedziu/pub/ext_info-%{ext_info_ver}.tar.bz2
Source7: 	http://www.kadu.net/download/modules_extra/filedesc/filedesc-%{filedesc_ver}.tar.bz2
Source8: 	http://alan.umcs.lublin.pl/~pinkworm/filtering/filtering-%{filtering_ver}.tar.bz2
Source9:	http://www.kadu.net/~dorr/moduly/kadu-firewall-%{firewall_ver}.tar.bz2
Source10: 	http://www.kadu.net/~pan_wojtas/iwait4u/download/kadu-iwait4u-%{iwait4u_ver}.tar.gz
Source11: 	http://kadu.net/~blysk/led_notify-%{led_notify_ver}.tar.bz2
Source12: 	http://www.kadu.net/download/modules_mirror/mail-%{mail_ver}.tar.bz2
Source13: 	http://www.kadu.net/~patryk/miastoplusa_sms/miastoplusa_sms-%{miastoplusa_sms_ver}.tar.gz
Source14:	http://www.kadu.net/~dorr/moduly/kadu-osdhints_notify-%{osdhints_notify_ver}.tar.bz2
Source15:	http://www.kadu.net/~dorr/moduly/kadu-pcspeaker-%{pcspeaker_ver}.tar.bz2
Source16: 	http://www.kadu.net/~patryk/powerkadu/powerkadu-%{powerkadu_ver}.tar.gz
Source17: 	http://www.kadu.net/~dorr/moduly/kadu-profiles-%{profiles_ver}.tar.bz2
Source18: 	http://www.kadu.net/download/modules_extra/screenshot/screenshot-%{screenshot_ver}.tar.bz2
Source19: 	http://scripts.one.pl/spellchecker/devel/0.5.0/spellchecker-%{spellchecker_ver}.tar.bz2
Source20: 	http://kadu.net/~arvenil/tabs/download/%{version}/%{tabs_ver}/kadu-tabs-%{tabs_ver}.tar.bz2
Source21: 	http://www.kadu.net/~blysk/weather-%{weather_ver}.tar.bz2
Source22: 	http://www.kadu.net/download/modules_extra/xmms_mediaplayer/xmms_mediaplayer-%{xmms_ver}.tar.bz2
Source23: 	http://www.kadu.net/~joi/xosd_notify/packages/xosd_notify-%{xosd_notify_ver}.tar.bz2
Source30:	http://www.kadu.net/~joi/advanced_userlist/packages/advanced_userlist-%{advanced_userlist}.tar.bz2
Source31:	http://www.kadu.net/download/modules_extra/falf_mediaplayer/falf_mediaplayer-%{falf_ver}.tar.bz2
Source32:	http://misiek.jah.pl/assets/2007/12/27/agent-%{agent_ver}.tar.gz
Source33:	http://tuxwarriors.wz.cz/qf.tar.bz2
Source35:	http://www.kadu.net/download/modules_extra/mediaplayer/mediaplayer-%{mediaplayer_ver}.tar.bz2
Source36:	http://kadu.net/~patryk/mime_tex/mime_tex-%{mime_tex_ver}.tar.bz2
#Source37:	http://kadu.jarzebski.pl/water_notify-%{water_notify_ver}.tar.bz2

#Icons sources
Source24:	http://www.kadu.net/download/additions/kadu-theme-crystal-16.tar.bz2
Source25:	http://www.kadu.net/download/additions/kadu-theme-crystal-22.tar.bz2
Source26:	http://www.kadu.net/download/additions/kadu-0.6-theme-glass-16.tar.gz
Source27:	http://www.kadu.net/download/additions/kadu-0.6-theme-glass-22.tar.gz
Source28:	http://www.kadu.net/download/additions/kadu-theme-nuvola-16.tar.gz
Source29:	http://www.kadu.net/download/additions/kadu-theme-nuvola-22.tar.gz
Source34:	http://www.kadu.net/download/additions/kadu-0.6-theme-tango-16.tar.gz

Patch0:		%{name}-config-enable-modular-build.patch
Patch2: 	%{name}-makefile-disable-desktop-file.patch
Patch4: 	%{name}-use-alsa-by-default.patch
Patch5: 	%{name}-disbale-ext_sound-autoload.patch
Patch6:		%{name}-0.6.0-rc1-voice-gsm-fixes.patch
URL:		http://www.kadu.net
BuildRequires:	libalsa-devel		>= 1.0.13
BuildRequires:	gettext-devel		>= 0.14.6-5
BuildRequires:	libgadu-devel 		>= 1.7
BuildRequires:	libgsm-devel		>= 1.0.10-11
BuildRequires:	libsndfile-devel 	>= 1.0.17
BuildRequires:	X11-devel		>= 7.1.0
BuildRequires:	qt3-devel 		>= 3.3.6
BuildRequires:	libopenssl-devel	>= 0.9.8d-3
BuildRequires:	desktop-file-utils
Requires: 	qt3-common 		>= 3.3.7
BuildRoot:	%{_tmppath}/%{name}-%{version}-buildroot

%description
Kadu is a dynamically evolving instant messenger 
compatible with the Gadu-Gadu protocol. It can be run 
on all platforms supporting the Qt toolkit (except Windows).

Compiled as modular as possible.

Static modules are:
- docking
- notify
- sound

%package	devel
Summary:	Kadu development libary
Group:		Development/C

%description 	devel
The kadu-devel package contains the header files and some
documentation needed to develop application with kadu.

%files 		devel
%defattr(-,root,root)
%multiarch %{multiarch_bindir}/kadu-config
%{_bindir}/kadu-config
%dir %{_includedir}/kadu
%dir %{_includedir}/kadu/modules
%{_includedir}/kadu/*.h
%{_includedir}/kadu/modules/*.h

#----------Modules----------

#module_agent
%package 	module-agent
Summary:	Spy module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kadu-module-spy

%description 	module-agent
This module shows who from contact list is hiding against us.

%files 		module-agent
%defattr(-,root,root)
%{_datadir}/%{name}/modules/agent.desc
%{_libdir}/%{name}/modules/agent.so
%lang(pl) %{_datadir}/%{name}/modules/translations/agent_pl.qm

#module-arts_sound
%package 	module-arts_sound
Summary:	Arts module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	arts
BuildRequires:	libarts-devel

%description 	module-arts_sound
aRts sound server support.

%files		module-arts_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/arts_sound.desc
%{_libdir}/%{name}/modules/arts_sound.so
%dir %{_libdir}/%{name}/modules/bin/
%dir %{_libdir}/%{name}/modules/bin/arts_sound
%{_libdir}/%{name}/modules/bin/arts_sound/arts_connector

#module-ao_sound
%package 	module-ao_sound
Summary:	Module ao_sound for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires:  libao-devel

%description 	module-ao_sound
ao library sound module (ALSA, OSS, ESD, AIX, IRIX, NAS, Sun, NetBSD, OpenBSD).

%files 		module-ao_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/ao_sound.desc
%{_libdir}/%{name}/modules/ao_sound.so

#module_dcopexport
%package	module-dcopexport
Summary:	DCOP module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires:	kdelibs-devel

%description	module-dcopexport
Exports some functions via DCOP.

%files		module-dcopexport
%defattr(-,root,root)
%dir %{_libdir}/%{name}/modules/bin/dcopexport
%dir %{_datadir}/%{name}/modules/data/dcopexport
%{_datadir}/%{name}/modules/dcopexport.desc
%{_datadir}/%{name}/modules/data/dcopexport/dcopexport.png
%{_libdir}/%{name}/modules/bin/dcopexport/*
%{_libdir}/%{name}/modules/dcopexport.so
%lang(pl) %{_datadir}/%{name}/modules/translations/dcopexport_pl.qm

#module_desktop_docking
%package	module-desktop_docking
Summary:	Always on top window docking
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description	module-desktop_docking
Always on top window docking module.

%files		module-desktop_docking
%defattr(-,root,root)
%{_datadir}/%{name}/modules/desktop_docking.desc
%{_datadir}/%{name}/modules/configuration/desktop_docking.ui
%{_libdir}/%{name}/modules/desktop_docking.so
%lang(de) %{_datadir}/%{name}/modules/translations/desktop_docking_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/desktop_docking_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/desktop_docking_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/desktop_docking_pl.qm

#module_dsp_sound
%package	module-dsp_sound
Summary:	OSS sound module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description	module-dsp_sound
Direct /dev/dsp sound support (Open Sound System).

%files		module-dsp_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/dsp_sound.desc
%{_datadir}/%{name}/modules/configuration/dsp_sound.ui
%{_libdir}/%{name}/modules/dsp_sound.so
%lang(de) %{_datadir}/%{name}/modules/translations/dsp_sound_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/dsp_sound_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/dsp_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/dsp_sound_pl.qm

#module_esd_sound
%package 	module-esd_sound
Summary:	ESD sound module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	esound
BuildRequires:	libesound-devel

%description 	module-esd_sound
ESD sound server support.

%files 		module-esd_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/esd_sound.desc
%{_libdir}/%{name}/modules/esd_sound.so

#module_ext_sound
%package        module-ext_sound
Summary:        External application sound support
Group:          Networking/Instant messaging
Requires:       %{name} = %{version}-%{release}

%description    module-ext_sound
External application sound support module.

%files          module-ext_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/ext_sound.desc
%{_datadir}/%{name}/modules/configuration/ext_sound.ui
%{_libdir}/%{name}/modules/ext_sound.so
%lang(de) %{_datadir}/%{name}/modules/translations/ext_sound_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/ext_sound_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/ext_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/ext_sound_pl.qm

	    
#module_led_notif
%package 	module-led_notify
Summary:	Notification by LED
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description	module-led_notify
Notification by keyboard's LED.

%files		module-led_notify
%defattr(-,root,root)
%doc modules/led_notify/Changelog
%{_datadir}/%{name}/modules/led_notify.desc
%{_datadir}/%{name}/modules/configuration/led_notify.ui
%{_libdir}/%{name}/modules/led_notify.so

%package	module-mediaplayer
Summary:	Mediaplayer module for kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description	module-mediaplayer
Mediaplayer module for kadu.

%files		module-mediaplayer
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/mediaplayer
%{_libdir}/%{name}/modules/mediaplayer.so
%{_datadir}/%{name}/modules/mediaplayer.desc
%{_datadir}/%{name}/modules/configuration/mediaplayer.ui
%{_datadir}/%{name}/modules/data/mediaplayer/mediaplayer.png
%lang(pl) %{_datadir}/%{name}/modules/translations/mediaplayer_pl.qm

#module_amarok
%package 	module-mediaplayer_amarok
Summary:	Amarok module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Obsoletes:	%{name}-module-amarok
Requires:	amarok

%description 	module-mediaplayer_amarok
Module which allows showing in status description information about
the song currently played in Amarok.

%files 		module-mediaplayer_amarok
%defattr(-,root,root)
%{_datadir}/%{name}/modules/amarok_mediaplayer.desc
%{_libdir}/%{name}/modules/amarok_mediaplayer.so

#module_falfp
%package	module-mediaplayer_falf
Summary:	Falf player odule for Kadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Obsoletes:	%{name}-module-falfp
Requires:	falf >= 1.0

%description	module-mediaplayer_falf
Module which allows showing in status description information about
the song currently played in Falf player.

%files		module-mediaplayer_falf
%defattr(-,root,root)
%{_datadir}/%{name}/modules/falf_mediaplayer.desc
%{_libdir}/%{name}/modules/falf_mediaplayer.so

#module_xmms
%package 	module-mediaplayer_xmms
Summary:	XMMS module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Obsoletes:	%{name}-module-xmms
Requires:	xmms
BuildRequires:	libxmms-devel

%description 	module-mediaplayer_xmms
Module which allows showing in status description information about
the song currently played in XMMS.

%files 		module-mediaplayer_xmms
%defattr(-,root,root)
%{_datadir}/%{name}/modules/xmms_mediaplayer.desc
%{_libdir}/%{name}/modules/xmms_mediaplayer.so

#module_miastoplusa_sms
%package	module-miastoplusa_sms
Summary:	Miasto Plusa SMS Gateway
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires:	libcurl-devel
BuildRequires:	libopenssl-devel

%description	module-miastoplusa_sms
Miasto Plusa SMS Gateway support module.

%files		module-miastoplusa_sms
%defattr(-,root,root)
%doc modules/miastoplusa_sms/ChangeLog
%dir %{_datadir}/%{name}/modules/data/miastoplusa_sms
%{_datadir}/%{name}/modules/data/miastoplusa_sms/*
%{_datadir}/%{name}/modules/miastoplusa_sms.desc
%{_datadir}/%{name}/modules/configuration/miastoplusa_sms.ui
%{_libdir}/%{name}/modules/miastoplusa_sms.so
%lang(pl) %{_datadir}/%{name}/modules/translations/miastoplusa_sms_pl.qm

#module_nas_sound
%package 	module-nas_sound
Summary:	NAS sound module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	nas
BuildRequires:	libnas-devel

%description 	module-nas_sound
Network Audio System support.

%files		 module-nas_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/nas_sound.desc
%{_libdir}/%{name}/modules/nas_sound.so

#module_pcspeaker
%package 	module-pcspeaker
Summary:	PC-Speaker support
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description 	module-pcspeaker
PC-Speaker support module.

%files		module-pcspeaker
%defattr(-,root,root)
%doc modules/pcspeaker/Changelog
%{_datadir}/%{name}/modules/configuration/pcspeaker.ui
%{_datadir}/%{name}/modules/pcspeaker.desc
%{_libdir}/%{name}/modules/pcspeaker.so
%lang(de) %{_datadir}/%{name}/modules/translations/pcspeaker_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/pcspeaker_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/pcspeaker_pl.qm

#module_powerkadu
#%package	module-powerkadu
#Summary:	Powerkadu
#Group:		Networking/Instant messaging
#Requires:	%{name} = %{version}-%{release}

#%description	module-powerkadu
#Powerkadu extends capabilities of Kadu.

#%files		module-powerkadu
#%defattr(-,root,root)
#%dir %{_libdir}/%{name}/modules/bin/powerkadu
#%dir %{_datadir}/%{name}/modules/data/powerkadu
#%dir %{_datadir}/%{name}/modules/data/powerkadu/mime_tex_icons
#%{_datadir}/%{name}/modules/data/powerkadu/AU*
#%{_datadir}/%{name}/modules/data/powerkadu/Ch*
#%{_datadir}/%{name}/modules/data/powerkadu/*.conf
#%{_datadir}/%{name}/modules/data/powerkadu/*.png
#%{_datadir}/%{name}/modules/data/powerkadu/*.data
#%{_datadir}/%{name}/modules/data/powerkadu/mime_tex_icons/*.png
#%{_datadir}/%{name}/modules/powerkadu.desc
#%{_libdir}/%{name}/modules/powerkadu.so
#%{_libdir}/%{name}/modules/bin/powerkadu/mimetex
#%lang(pl) %{_datadir}/%{name}/modules/translations/powerkadu_pl.qm

#module_speech
%package 	module-speech
Summary:	Speech synthesis support
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	powiedz

%description	module-speech
Speech synthesis support ("powiedz")

%files 		module-speech
%defattr(-,root,root)
%{_datadir}/%{name}/modules/speech.desc
%{_datadir}/%{name}/modules/configuration/speech.ui
%{_libdir}/%{name}/modules/speech.so
%lang(de) %{_datadir}/%{name}/modules/translations/speech_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/speech_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/speech_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/speech_pl.qm

#module_spellchecker
%package 	module-spellchecker
Summary:	Aspell module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	aspell
BuildRequires:	libaspell-devel

%description 	module-spellchecker
Checker of spelling mistakes.

%files 		module-spellchecker
%defattr(-,root,root)
%doc modules/spellchecker/{README,TODO,ChangeLog}
%dir %{_datadir}/%{name}/modules/data/spellchecker
%{_datadir}/%{name}/modules/spellchecker.desc
%{_datadir}/%{name}/modules/configuration/spellchecker.ui
%{_libdir}/%{name}/modules/spellchecker.so
%lang(pl) %{_datadir}/%{name}/modules/translations/spellchecker_pl.qm
%{_datadir}/%{name}/modules/data/spellchecker/config.png

#module_weather
%package 	module-weather
Summary:	Weather module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description 	module-weather
This module shows current weather for you and your contacts.

%files		module-weather
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/weather
%dir %{_datadir}/%{name}/modules/data/weather/icons
%{_datadir}/%{name}/modules/data/weather/icons/*
%{_datadir}/%{name}/modules/data/weather/interia.ini
%{_datadir}/%{name}/modules/data/weather/onetweather.ini
%{_datadir}/%{name}/modules/data/weather/pfweather.ini
%{_datadir}/%{name}/modules/weather.desc
%{_datadir}/%{name}/modules/configuration/weather.ui
%{_libdir}/%{name}/modules/weather.so
%lang(pl) %{_datadir}/%{name}/modules/translations/weather_pl.qm

#module_wmaker_docking
%package	module-wmaker_docking
Summary: 	WindowMaker docking module
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires: 	WindowMaker

%description 	module-wmaker_docking
WindowMaker docking module.

%files		module-wmaker_docking
%defattr(-,root,root)
%{_datadir}/%{name}/modules/wmaker_docking.desc
%{_libdir}/%{name}/modules/wmaker_docking.so

%package	module-xosd_notify
Summary: 	Notification by XOSD
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires: 	libgtk+-devel
BuildRequires: 	libxosd-devel

%description module-xosd_notify
Notification by XOSD module.

%files		module-xosd_notify
%defattr(-,root,root)
%doc modules/xosd_notify/{README,ChangeLog}
%dir %{_libdir}/%{name}/modules/bin/xosd_notify
%{_datadir}/%{name}/modules/xosd_notify.desc
%{_datadir}/%{name}/modules/configuration/xosd_notify.ui
%{_libdir}/%{name}/modules/xosd_notify.so
%{_libdir}/%{name}/modules/bin/xosd_notify/gtkfontdialog

#module_xqf
#%package 	module-xqf
#Summary:	XQF module for Kadu
#Group:		Networking/Instant messaging
#Requires:	%{name} = %{version}-%{release}
#Requires:	xqf

#%description 	module-xqf
#Module which allows showing in status description information about
#the game and ip of a gameserver currently played.

#%files 		module-xqf
#%defattr(-,root,root)
#%{_datadir}/%{name}/modules/qf.desc
#%{_libdir}/%{name}/modules/qf.so

#----------Icons----------

#icons_crystal
%package	icons_crystal
Summary: 	Crystal icons for Kadu
Group:		Networking/Instant messaging
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}

%Description 	icons_crystal
Crystal icon theme for kadu created by arcisz.

#icons_crystal
%files		icons_crystal
%defattr(-,root,root)
%doc varia/themes/icons/crystal16/README
%dir %{_datadir}/%{name}/themes/icons/crystal16
%dir %{_datadir}/%{name}/themes/icons/crystal22
%{_datadir}/%{name}/themes/icons/crystal16/*
%{_datadir}/%{name}/themes/icons/crystal22/*

#icons_glass
%package	icons_glass
Summary: 	Glass icons for Kadu
Group:		Networking/Instant messaging
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%Description 	icons_glass
Glass icon theme for kadu created by Mariusz Waluga.

%files		icons_glass
%defattr(-,root,root)
%dir %{_datadir}/%{name}/themes/icons/glass16
%dir %{_datadir}/%{name}/themes/icons/glass22
%{_datadir}/%{name}/themes/icons/glass16/*
%{_datadir}/%{name}/themes/icons/glass22/*

#icons_nuvola
%package	icons_nuvola
Summary: 	Nuvola icons for Kadu
Group:		Networking/Instant messaging
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}

%Description 	icons_nuvola
Nuvola icon theme for kadu created by David Vignoni.

%files		icons_nuvola
%defattr(-,root,root)
%doc varia/themes/icons/nuvola16/Copyright
%dir %{_datadir}/%{name}/themes/icons/nuvola16
%dir %{_datadir}/%{name}/themes/icons/nuvola22
%{_datadir}/%{name}/themes/icons/nuvola16/*
%{_datadir}/%{name}/themes/icons/nuvola22/*

#--------------------------------------------------------------

%prep

%setup -qn %{name}
#amarok
tar xjf %{SOURCE2} -C modules
#ao_sound
tar xjf %{SOURCE3} -C modules
#dcopexport
tar xjf %{SOURCE4} -C modules
#exec_notify
#tar xjf %{SOURCE5} -C modules
#ext_info
#tar xjf %{SOURCE6} -C modules
#filedesc
tar xjf %{SOURCE7} -C modules
#filtering
tar xjf %{SOURCE8} -C modules
#firewall
tar xjf %{SOURCE9} -C modules
#iwait4u
#tar xzf %{SOURCE10} -C modules
#led_notify
tar xjf %{SOURCE11} -C modules
#mail
tar xjf %{SOURCE12} -C modules
#miastoplusa_sms
tar xzf %{SOURCE13} -C modules
#osd_hints_notify
tar xjf %{SOURCE14} -C modules
#pcspeaker
tar xjf %{SOURCE15} -C modules
#powerkadu
#tar xzf %{SOURCE16} -C modules
#profiles
tar xjf %{SOURCE17} -C modules
#screenshot
tar xjf %{SOURCE18} -C modules
#spellchecker
tar xjf %{SOURCE19} -C modules
#tabs
tar xjf %{SOURCE20} -C modules
#weather
tar xjf %{SOURCE21} -C modules
#xmms
tar xjf %{SOURCE22} -C modules
#xosd_hints
#tar xjf %{SOURCE23} -C modules
#adavanced_iserlist
#tar xjf %{SOURCE30} -C modules
#falf
tar xjf %{SOURCE31} -C modules
#agent
tar xzf %{SOURCE32} -C modules
#xqf
#tar xjf %{SOURCE33} -C modules
#mediaplayer
tar xjf %{SOURCE35} -C modules
#mime_tex
#tar xjf %{SOURCE36} -C modules

tar xjf %{SOURCE24} -C varia/themes/icons
tar xjf %{SOURCE25} -C varia/themes/icons
tar xzf %{SOURCE26} -C varia/themes/icons
tar xzf %{SOURCE27} -C varia/themes/icons
tar xzf %{SOURCE28} -C varia/themes/icons
tar xzf %{SOURCE29} -C varia/themes/icons

pushd varia/themes/icons
for file in kadu-theme*; do
mv $file `echo $file | sed -e s/kadu-theme-//g -e s/[_-]//g`
done
popd

%patch0 -p1 -b .%{name}-config-enable-modular-build.patch
#%patch2 -p1 -b .%{name}-makefile-disable-desktop-file.patch
#%patch4 -p1 -b .%{name}-use-alsa-by-default.patch
#%patch5 -p1 -b .%{name}-disbale-ext_sound-autoload.patch
%patch6 -p1 -b .voice

%build
export CXXFLAGS="%{optflags}"

%{__sed} -i 's,dataPath("kadu/modules/*,("%{_libdir}/kadu/modules/,g' kadu-core/modules.cpp

%configure2_5x \
	--enable-pheaders \
	--with-existing-libgadu \
	--disable-autodownload \
	--enable-final \
	--enable-voice \
	--disable-debug \
	--enable-dist-info=Mandriva

%make
	
%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%makeinstall_std

%multiarch_binaries %{buildroot}%{_bindir}/kadu-config

sed -i -e 's/^Icon=%{name}.png$/Icon=%{name}/g' %{buildroot}%{_datadir}/applnk/Internet/*

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications %{SOURCE1}

rm -rf `find %{buildroot} -name CVS`

%post
%{update_menus}
%if %mdkversion >= 200700
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%postun
%{clean_menus}
%if %mdkversion >= 200700
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean 
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY README TODO VERSION THANKS AUTHORS FAQ
%{_bindir}/kadu
%{_bindir}/kadu-mozilla
%{_datadir}/applications/%{name}.desktop

#default directories
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_libdir}/%{name}/modules/bin
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/modules/data
%dir %{_datadir}/%{name}/modules/translations
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/emoticons
%dir %{_datadir}/%{name}/themes/icons
%dir %{_datadir}/%{name}/themes/sounds
%{_datadir}/%{name}/syntax
%{_datadir}/pixmaps/*.png
%exclude %{_datadir}/%{name}/HISTORY
%exclude %{_datadir}/%{name}/README
%exclude %{_datadir}/%{name}/AUTHORS
%exclude %{_datadir}/%{name}/ChangeLog
%exclude %{_datadir}/%{name}/COPYING
%exclude %{_datadir}/%{name}/THANKS
%exclude %{_datadir}/applnk/Internet/kadu.desktop
%{_datadir}/%{name}/configuration/dialog-look-chat-advanced.ui
%{_datadir}/%{name}/configuration/dialog.ui

#module_account_management
%{_datadir}/%{name}/modules/account_management.desc
%{_libdir}/%{name}/modules/account_management.so
%lang(de) %{_datadir}/%{name}/modules/translations/account_management_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/account_management_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/account_management_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/account_management_pl.qm

#module_adavanced_userlist
%{_libdir}/%{name}/modules/advanced_userlist.so
%{_datadir}/%{name}/modules/advanced_userlist.desc
%{_datadir}/%{name}/modules/configuration/advanced_userlist.ui
%lang(de) %{_datadir}/%{name}/modules/translations/advanced_userlist_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/advanced_userlist_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/advanced_userlist_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/advanced_userlist_pl.qm

#module_alsa_sound
%{_datadir}/%{name}/modules/alsa_sound.desc
%{_datadir}/%{name}/modules/configuration/alsa_sound.ui
%{_libdir}/%{name}/modules/alsa_sound.so
%lang(de) %{_datadir}/%{name}/modules/translations/alsa_sound_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/alsa_sound_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/alsa_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/alsa_sound_pl.qm

#module_autoaway
%{_datadir}/%{name}/modules/autoaway.desc
%{_datadir}/%{name}/modules/configuration/autoaway.ui
%{_libdir}/%{name}/modules/autoaway.so
%lang(de) %{_datadir}/%{name}/modules/translations/autoaway_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/autoaway_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/autoaway_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/autoaway_pl.qm

#module_autoresponder
%{_datadir}/%{name}/modules/autoresponder.desc
%{_datadir}/%{name}/modules/configuration/autoresponder.ui
%{_libdir}/%{name}/modules/autoresponder.so
%lang(de) %{_datadir}/%{name}/modules/translations/autoresponder_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/autoresponder_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/autoresponder_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/autoresponder_pl.qm

#module_config_wizard
%dir %{_datadir}/%{name}/modules/data/config_wizard
%dir %{_datadir}/%{name}/modules/data/config_wizard/joi
%dir %{_datadir}/%{name}/modules/data/config_wizard/ronk2
%{_datadir}/%{name}/modules/data/config_wizard/joi/*
%{_datadir}/%{name}/modules/data/config_wizard/ronk2/*
%{_datadir}/%{name}/modules/config_wizard.desc
%{_libdir}/%{name}/modules/config_wizard.so
%lang(de) %{_datadir}/%{name}/modules/translations/config_wizard_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/config_wizard_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/config_wizard_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/config_wizard_pl.qm

#module_dcc
%{_datadir}/%{name}/modules/dcc.desc
%{_datadir}/%{name}/modules/configuration/dcc.ui
%{_libdir}/%{name}/modules/dcc.so
%lang(de) %{_datadir}/%{name}/modules/translations/dcc_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/dcc_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/dcc_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/dcc_pl.qm

#module_default_sms
%{_datadir}/%{name}/modules/default_sms.desc
%{_datadir}/%{name}/modules/configuration/default_sms.ui
%{_libdir}/%{name}/modules/default_sms.so
%lang(de) %{_datadir}/%{name}/modules/translations/default_sms_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/default_sms_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/default_sms_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/default_sms_pl.qm

#module_encryption
%{_datadir}/%{name}/modules/encryption.desc
%{_datadir}/%{name}/modules/configuration/encryption.ui
%{_libdir}/%{name}/modules/encryption.so
%lang(de) %{_datadir}/%{name}/modules/translations/encryption_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/encryption_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/encryption_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/encryption_pl.qm

#module_exec_notify
%{_datadir}/%{name}/modules/exec_notify.desc
%{_libdir}/%{name}/modules/exec_notify.so

#module_ext_info
#%dir %{_datadir}/%{name}/modules/data/ext_info
#%{_datadir}/%{name}/modules/data/ext_info/*
#%{_datadir}/%{name}/modules/ext_info.desc
#%{_libdir}/%{name}/modules/ext_info.so
#%lang(pl) %{_datadir}/%{name}/modules/translations/ext_info_pl.qm

#module_filedesc
%dir %{_datadir}/%{name}/modules/data/filedesc
%{_datadir}/%{name}/modules/data/filedesc/*
%{_datadir}/%{name}/modules/configuration/filedesc.ui
%{_datadir}/%{name}/modules/filedesc.desc
%{_libdir}/%{name}/modules/filedesc.so
%lang(pl) %{_datadir}/%{name}/modules/translations/filedesc_pl.qm

#module_filtering
%dir %{_datadir}/%{name}/modules/data/filtering
%{_datadir}/%{name}/modules/data/filtering/*.png
%{_datadir}/%{name}/modules/filtering.desc
%{_datadir}/%{name}/modules/configuration/filtering.ui
%{_libdir}/%{name}/modules/filtering.so
%lang(pl) %{_datadir}/%{name}/modules/translations/filtering_pl.qm

#module_firewall
#%dir %{_datadir}/%{name}/modules/data/firewall
#%{_datadir}/%{name}/modules/firewall.desc
#%{_datadir}/%{name}/modules/data/firewall/firewall.png
%{_datadir}/%{name}/modules/configuration/firewall.ui
%{_libdir}/%{name}/modules/firewall.so
%lang(pl) %{_datadir}/%{name}/modules/translations/firewall_pl.qm

#module_iwait4u
#%{_datadir}/%{name}/modules/iwait4u.desc
#%{_libdir}/%{name}/modules/iwait4u.so
#%lang(pl) %{_datadir}/%{name}/modules/translations/iwait4u_pl.qm

#module_hints
%{_datadir}/%{name}/modules/hints.desc
%{_datadir}/%{name}/modules/configuration/hints.ui
%{_libdir}/%{name}/modules/hints.so
%lang(de) %{_datadir}/%{name}/modules/translations/hints_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/hints_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/hints_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/hints_pl.qm

#module_mail
#%{_datadir}/%{name}/modules/mail.desc
#%{_libdir}/%{name}/modules/mail.so
#%lang(pl) %{_datadir}/%{name}/modules/translations/mail_pl.qm

#module_history
%{_datadir}/%{name}/modules/history.desc
%{_datadir}/%{name}/modules/configuration/history.ui
%{_libdir}/%{name}/modules/history.so
%lang(de) %{_datadir}/%{name}/modules/translations/history_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/history_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/history_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/history_pl.qm

#module_migration
%{_datadir}/%{name}/modules/migration.desc
%{_libdir}/%{name}/modules/migration.so
%lang(de) %{_datadir}/%{name}/modules/translations/migration_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/migration_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/migration_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/migration_pl.qm

#module_osdhints_notify
%dir %{_datadir}/%{name}/modules/data/osdhints_notify
%{_datadir}/%{name}/modules/configuration/osdhints_notify.ui
%{_datadir}/%{name}/modules/data/osdhints_notify/*.png
%{_datadir}/%{name}/modules/osdhints_notify.desc
%{_libdir}/%{name}/modules/osdhints_notify.so

#module_profiles
%{_datadir}/%{name}/modules/profiles.desc
%{_libdir}/%{name}/modules/profiles.so
#%lang(de) %{_datadir}/%{name}/modules/translations/profiles_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/profiles_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/profiles_pl.qm

#module_screenshot
%dir %{_datadir}/%{name}/modules/data/screenshot
%{_datadir}/%{name}/modules/screenshot.desc
%{_datadir}/%{name}/modules/configuration/screenshot.ui
%{_datadir}/%{name}/modules/data/screenshot/camera.png
%{_datadir}/%{name}/modules/data/screenshot/camera_small.png
%{_libdir}/%{name}/modules/screenshot.so
%lang(pl) %{_datadir}/%{name}/modules/translations/screenshot_pl.qm

#module_sms
%{_datadir}/%{name}/modules/sms.desc
%{_datadir}/%{name}/modules/configuration/sms.ui
%{_libdir}/%{name}/modules/sms.so
%lang(de) %{_datadir}/%{name}/modules/translations/sms_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/sms_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/sms_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/sms_pl.qm

#module_tabs
#%dir %{_datadir}/%{name}/modules/data/tabs
#%{_datadir}/%{name}/modules/data/tabs/*
%{_datadir}/%{name}/modules/tabs.desc
%{_datadir}/%{name}/modules/configuration/tabs.ui
%{_libdir}/%{name}/modules/tabs.so
%lang(pl) %{_datadir}/%{name}/modules/translations/tabs_pl.qm

#module_window_notify
%{_datadir}/%{name}/modules/window_notify.desc
%{_libdir}/%{name}/modules/window_notify.so
%lang(de) %{_datadir}/%{name}/modules/translations/*notify_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/*notify_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/*notify_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/*notify_pl.qm

#module_voice
%{_datadir}/%{name}/modules/voice.desc
%{_datadir}/%{name}/modules/configuration/voice.ui
%{_libdir}/%{name}/modules/voice.so
%lang(de) %{_datadir}/%{name}/modules/translations/voice_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/voice_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/voice_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/voice_pl.qm

#module_x11_docking
%{_datadir}/%{name}/modules/x11_docking.desc
%{_libdir}/%{name}/modules/x11_docking.so
%lang(de) %{_datadir}/%{name}/modules/translations/x11_docking_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/x11_docking_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/x11_docking_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/x11_docking_pl.qm

#icons_default
%dir %{_datadir}/%{name}/themes/icons/default
%{_datadir}/%{name}/themes/icons/default/*

#emoticons_penguins
%dir %{_datadir}/%{name}/themes/emoticons/penguins
%{_datadir}/%{name}/themes/emoticons/penguins/*

#sounds_default
%dir %{_datadir}/%{name}/themes/sounds/default
%{_datadir}/%{name}/themes/sounds/default/*
%lang(de) %{_datadir}/%{name}/modules/translations/sound_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/sound_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/sound_pl.qm

#----------Static modules----------

#module_docking
%{_datadir}/%{name}/modules/docking.desc
%{_datadir}/%{name}/modules/configuration/docking.ui
%lang(de) %{_datadir}/%{name}/modules/translations/docking_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/docking_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/docking_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/docking_pl.qm

#module_notify
%{_datadir}/%{name}/modules/notify.desc
%{_datadir}/%{name}/modules/configuration/notify.ui

#module_sound
%{_datadir}/%{name}/modules/sound.desc
%{_datadir}/%{name}/modules/configuration/sound.ui

#----------

#global translation:
%lang(de) %{_datadir}/%{name}/translations/kadu_de.qm
%lang(en) %{_datadir}/%{name}/translations/kadu_en.qm
%lang(fr) %{_datadir}/%{name}/translations/kadu_fr.qm
%lang(it) %{_datadir}/%{name}/translations/kadu_it.qm
%lang(pl) %{_datadir}/%{name}/translations/kadu_pl.qm
%lang(de) %{_datadir}/%{name}/translations/qt_de.qm
%lang(en) %{_datadir}/%{name}/translations/qt_en.qm
%lang(en) %{_datadir}/%{name}/translations/qt_fr.qm
%lang(it) %{_datadir}/%{name}/translations/qt_it.qm
%lang(pl) %{_datadir}/%{name}/translations/qt_pl.qm
