############### Define versions ####################
%define		agent_ver		0.5
%define		anonymous_check_ver	0.6.5.3-1
%define		cenzor_ver		0.3
%define		desc_history_ver	1.1
%define		dcopexport_ver		0.11.3-20071129-0.6.0
%define		ext_info_ver		2.0beta12
%define		globalhotkeys_ver	0.6.5-15
%define		iwait4u_ver		1.3
%define		led_notify_ver		0.21
%define		kde_notify_ver		0.3.4
%define		mail_ver		0.3.6
%define		mime_tex_ver		0.6.5.3
%define		osdhints_notify_ver	0.5pre
%define		panelkadu_ver		0.6.5-5
%define		powerkadu_ver		2.1.2
%define		plus_pl_sms_ver		0.6.5.3-3
%define		sent_history_ver	0.6.5-5
%define		split_messages_ver	0.3
%define		tabs_ver		1.2.7
%define		water_notify_ver	0.2.1
%define		weather_ver		3.15
%define		xmms_ver		20080116
%define		xosd_notify_ver		20070111

################ Enable modules #######################
%define		build_agent			1
%define		build_amarok			1
%define		build_adavanced_userlist	1
%define		build_anonymous_check		1
%define		build_antistring		1
%define		build_ao_sound			0
%define		build_arts_sound		0
%define		build_audacious			1
%define		build_auto_hide			1
%define		build_autostatus		1
%define		build_cenzor			1
%define		build_dcopexport		0
%define		build_desc_history		0
%define		build_desktop_docking		1
%define		build_esd_sound			0
%define		build_exec_notify		1
%define		build_ext_info			1
%define		build_falf			0
%define		build_filedesc			1
%define		build_filtering			1
%define		build_firewall			1
%define		build_globalhotkeys		1
%define		build_iwait4u			0
%define		build_kde_notify		1
%define		build_last_seen			1
%define		build_led_notify		1
%define		build_mail			0
%define		build_mediaplayer		1
%define		build_mediaplayer_mpris		1
%define		build_mime_tex			1
%define		build_nas_sound			0
%define		build_osdhints_notify		1
%define		build_panelkadu			1
%define		build_parser_extender		1
%define		build_pcspeaker			0
%define		build_plus_pl_sms		1
%define		build_powerkadu			1
%define		build_profiles			1
%define		build_screenshot		1
%define		build_sent_history		1
%define		build_speech			1
%define 	build_spellchecker		1
%define		build_split_messages		1
%define		build_tabs			1
%define		build_qt4_sound			1
%define		build_water_notify		1
%define		build_weather			1
%define		build_wmaker_docking		0
%define		build_word_fix			1
%define 	build_xmms			0
%define		build_xosd_notify		0
%define		build_xqf			0

# themes
%define		build_icons_crystal		1
%define		build_icons_glass		1
%define		build_icons_oxygen		1
%define		build_icons_nuvola		1
%define		build_icons_tango		1

####################################################

Summary:	A Gadu-Gadu client for online messaging
Name:		kadu
Version:	0.6.5.4
Release:	%mkrel 4
License:	GPLv2+
Group:		Networking/Instant messaging
URL:		http://www.kadu.net
Source0:	http://kadu.net/download/stable/%{name}-%{version}.tar.bz2
Source1:	%{name}.desktop

#Modules sources
Source4: 	http://alan.umcs.lublin.pl/~pinkworm/dcopexport/dcopexport-%{dcopexport_ver}.tar.bz2
Source6: 	http://www.kadu.net/~dzwiedziu/pub/ext_info-%{ext_info_ver}.tar.bz2
Source10: 	http://www.kadu.net/~pan_wojtas/iwait4u/download/kadu-iwait4u-%{iwait4u_ver}.tar.gz
Source11: 	http://kadu.net/~blysk/led_notify-%{led_notify_ver}.tar.bz2
Source12: 	http://www.kadu.net/download/modules_mirror/mail-%{mail_ver}.tar.bz2
Source13:	http://kadu.net/~patryk/plus_pl_sms/plus_pl_sms-%{plus_pl_sms_ver}.tar.bz2
Source14:	http://www.kadu.net/~dorr/moduly/kadu-osdhints_notify-%{osdhints_notify_ver}.tar.bz2
Source16: 	http://www.kadu.net/~dorr/moduly/kadu-powerkadu-%{powerkadu_ver}.tar.bz2
Source20: 	http://www.kadu.net/~weagle/tabs/kadu-tabs-%{tabs_ver}.tar.bz2
Source21: 	http://www.kadu.net/~blysk/weather-%{weather_ver}.tar.bz2
Source23: 	http://www.kadu.net/~joi/xosd_notify/packages/xosd_notify-%{xosd_notify_ver}.tar.bz2
Source32:	http://www.kadu.net/~dorr/moduly/kadu-agent-%{agent_ver}.tar.bz2
Source33:	http://tuxwarriors.wz.cz/qf.tar.bz2
Source36:	http://kadu.net/~patryk/mime_tex/mime_tex-%{mime_tex_ver}.tar.bz2
Source37:	http://kadu.jarzebski.pl/kadu-water_notify-%{water_notify_ver}.tar.bz2
Source38:	http://www.ultr.pl/kadu/panelkadu-%{panelkadu_ver}.tar.gz
Source41:	http://kadu.net/~patryk/anonymous_check/anonymous_check-%{anonymous_check_ver}.tar.bz2
Source45:	http://www.kadu.net/~dorr/moduly/kadu-split_messages-%{split_messages_ver}.tar.bz2
Source50:	http://www.ultr.pl/kadu/globalhotkeys-%{globalhotkeys_ver}.tar.gz
Source51:	http://myslenice.one.pl/~boogie/desc_history/desc_history-%{desc_history_ver}.tar.bz2
Source52:	http://www.ultr.pl/kadu/senthistory-%{sent_history_ver}.tar.gz
Source53:	http://www.kadu.net/~dorr/moduly/kde_notify-%{kde_notify_ver}.tar.gz

#Icons sources
Source24:	http://www.kadu.net/download/additions/kadu-theme-crystal-16.tar.bz2
Source25:	http://www.kadu.net/download/additions/kadu-theme-crystal-22.tar.bz2
Source26:	http://www.kadu.net/download/additions/kadu-0.6.5.4-theme-glass-16.tar.gz
Source27:	http://www.kadu.net/download/additions/kadu-0.6.5.4-theme-glass-22.tar.gz
Source28:	http://www.kadu.net/download/additions/kadu-theme-nuvola-16.tar.gz
Source29:	http://www.kadu.net/download/additions/kadu-theme-nuvola-22.tar.gz
Source34:	http://www.kadu.net/download/additions/kadu-0.6.5.4-theme-tango-16.tar.gz
Source48:	http://www.kadu.net/download/additions/kadu-0.6.5.4-theme-oxygen-16.tar.gz
#emoticons sources
Source49:	http://www.kadu.net/download/additions/kadu-0.6.5.4-emots-tango.tar.gz

Patch4: 	%{name}-use-alsa-by-default.patch
Patch5: 	%{name}-disbale-ext_sound-autoload.patch
Patch6:		%{name}-0.6.5-voice-gsm-fixes.patch
Patch7:		water_notify-libs.patch
Patch8:		kadu-stath.patch
BuildRequires:	libalsa-devel		>= 1.0.13
BuildRequires:	libgadu-devel 		>= 1.8
BuildRequires:	libgsm-devel		>= 1.0.10-11
BuildRequires:	libsndfile-devel 	>= 1.0.17
BuildRequires:	qt4-devel 		>= 4.2.0
Buildrequires:	libxscrnsaver-devel
BuildRequires:	libx11-devel
BuildRequires:	desktop-file-utils
BuildRequires:	cmake
BuildRequires:	qca2-devel
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

#%package devel
#Summary:	Kadu development libary
#Group:		Development/C

#%description devel
#The kadu-devel package contains the header files and some
#documentation needed to develop application with kadu.

#%files devel
#%defattr(-,root,root)
#multiarch %{multiarch_bindir}/kadu-config
#%{_bindir}/kadu-config
#%dir %{_includedir}/kadu
#%dir %{_includedir}/kadu/modules
#%{_includedir}/kadu/*.h
#%{_includedir}/kadu/modules/*.h

#----------Modules----------

%if %build_agent
%package module-agent
Summary:	Spy module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Obsoletes:	kadu-module-spy

%description module-agent
This module shows who from contact list is hiding against us.

%files module-agent
%defattr(-,root,root)
%{_datadir}/%{name}/modules/agent.desc
%{_libdir}/%{name}/modules/libagent.so
%lang(pl) %{_datadir}/%{name}/modules/translations/agent_pl.qm
%endif

%if %build_anonymous_check
%package module-anonymous_check
Summary:	Automatic lookup of an interlocutor in public directory
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-anonymous_check
Automatic lookup of an interlocutor in public directory.

%files module-anonymous_check
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libanonymous_check.so
%{_datadir}/%{name}/modules/anonymous_check.desc
%{_datadir}/%{name}/modules/configuration/anonymous_check.ui
%{_datadir}/%{name}/modules/translations/anonymous_check.qm
%endif

%if %build_antistring
%package module-antistring
Summary:	Antistring module for %{name}
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-antistring
Antistring module.

%files module-antistring
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/antistring
%{_libdir}/%{name}/modules/libantistring.so
%{_datadir}/%{name}/modules/antistring.desc
%{_datadir}/%{name}/modules/configuration/antistring.ui
%{_datadir}/%{name}/modules/data/antistring/*.conf
%lang(pl) %{_datadir}/%{name}/modules/translations/antistring_pl.qm
%endif

%if %build_ao_sound
%package module-ao_sound
Summary:	Module ao_sound for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires:  libao-devel

%description module-ao_sound
ao library sound module (ALSA, OSS, ESD, AIX, IRIX, NAS, Sun, NetBSD, OpenBSD).

%files module-ao_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/ao_sound.desc
#%{_libdir}/%{name}/modules/ao_sound.so
%endif

%if %build_arts_sound
%package module-arts_sound
Summary:	Arts module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	arts
BuildRequires:	libarts-devel

%description module-arts_sound
aRts sound server support.

%files module-arts_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/arts_sound.desc
%{_libdir}/%{name}/modules/arts_sound.so
%dir %{_libdir}/%{name}/modules/bin/
%dir %{_libdir}/%{name}/modules/bin/arts_sound
%{_libdir}/%{name}/modules/bin/arts_sound/arts_connector
%endif

%if %build_auto_hide
%package module-auto_hide
Summary:	Auto hide Kadu window
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-auto_hide
Auto hide Kadu window.

%files module-auto_hide
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libauto_hide.so
%{_datadir}/%{name}/modules/auto_hide.desc
%{_datadir}/%{name}/modules/configuration/auto_hide.ui
%lang(pl) %{_datadir}/%{name}/modules/translations/auto_hide_pl.qm
%endif

%if %build_autostatus
%package module-autostatus
Summary:	Automatic status change module for kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-autostatus
Automatic status change module for kadu.

%files module-autostatus
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libautostatus.so
%{_datadir}/%{name}/modules/autostatus.desc
%{_datadir}/%{name}/modules/configuration/autostatus.ui
%lang(pl) %{_datadir}/%{name}/modules/translations/autostatus_pl.qm
%endif

%if %build_cenzor
%package module-cenzor
Summary:	Censor module for %{name}
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-cenzor
Censor module for %{name}.

%files module-cenzor
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/cenzor
%{_libdir}/%{name}/modules/libcenzor.so
%{_datadir}/%{name}/modules/cenzor.desc
%{_datadir}/%{name}/modules/configuration/cenzor.ui
%{_datadir}/%{name}/modules/data/cenzor/*.conf
%lang(pl) %{_datadir}/%{name}/modules/translations/cenzor_pl.qm
%endif

%if %build_dcopexport
%package module-dcopexport
Summary:	DCOP module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires:	kdelibs-devel

%description module-dcopexport
Exports some functions via DCOP.

%files module-dcopexport
%defattr(-,root,root)
%dir %{_libdir}/%{name}/modules/bin/dcopexport
%dir %{_datadir}/%{name}/modules/data/dcopexport
%{_datadir}/%{name}/modules/dcopexport.desc
%{_datadir}/%{name}/modules/data/dcopexport/dcopexport.png
%{_libdir}/%{name}/modules/bin/dcopexport/*
%{_libdir}/%{name}/modules/dcopexport.so
%lang(pl) %{_datadir}/%{name}/modules/translations/dcopexport_pl.qm
%endif

%if %build_desc_history
%package module-desc_history
Summary:	History for status descriptions
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires:	sqlite3-devel

%description module-desc_history
History for status descriptions for kadu.

%files module-desc_history
%defattr(-,root,root)
#%{_datadir}/%{name}/modules/desc_history.desc
#%{_datadir}/%{name}/modules/configuration/desc_history.ui
#%{_libdir}/%{name}/modules/libdesc_history.so
#%lang(pl) %{_datadir}/%{name}/modules/translations/desc_history_pl.qm

%endif

%if %build_desktop_docking
%package module-desktop_docking
Summary:	Always on top window docking
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-desktop_docking
Always on top window docking module.

%files module-desktop_docking
%defattr(-,root,root)
%{_datadir}/%{name}/modules/desktop_docking.desc
%{_datadir}/%{name}/modules/configuration/desktop_docking.ui
%{_libdir}/%{name}/modules/libdesktop_docking.so
%lang(de) %{_datadir}/%{name}/modules/translations/desktop_docking_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/desktop_docking_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/desktop_docking_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/desktop_docking_pl.qm
%endif

#module_dsp_sound
%package module-dsp_sound
Summary:	OSS sound module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-dsp_sound
Direct /dev/dsp sound support (Open Sound System).

%files module-dsp_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/dsp_sound.desc
%{_datadir}/%{name}/modules/configuration/dsp_sound.ui
%{_libdir}/%{name}/modules/libdsp_sound.so
%lang(de) %{_datadir}/%{name}/modules/translations/dsp_sound_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/dsp_sound_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/dsp_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/dsp_sound_pl.qm

%if %build_esd_sound
%package module-esd_sound
Summary:	ESD sound module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	esound
BuildRequires:	libesound-devel

%description module-esd_sound
ESD sound server support.

%files module-esd_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/esd_sound.desc
#%{_libdir}/%{name}/modules/esd_sound.so
%endif

#module_ext_sound
#%package module-ext_sound
#Summary:        External application sound support
#Group:          Networking/Instant messaging
#Requires:       %{name} = %{version}-%{release}

#%description module-ext_sound
#External application sound support module.

#%files module-ext_sound
#%defattr(-,root,root)
#%{_datadir}/%{name}/modules/ext_sound.desc
#%{_datadir}/%{name}/modules/configuration/ext_sound.ui
#%{_libdir}/%{name}/modules/ext_sound.so
#%lang(de) %{_datadir}/%{name}/modules/translations/ext_sound_de.qm
#%lang(fr) %{_datadir}/%{name}/modules/translations/ext_sound_fr.qm
#%lang(it) %{_datadir}/%{name}/modules/translations/ext_sound_it.qm
#%lang(pl) %{_datadir}/%{name}/modules/translations/ext_sound_pl.qm

%if %build_globalhotkeys
%package module-globalhotkeys
Summary:	Hotkeys support for kadu
Group:          Networking/Instant messaging
Requires:       %{name} = %{version}-%{release}

%description module-globalhotkeys
Hotkeys support for kadu.

%files module-globalhotkeys
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libglobalhotkeys.so
%{_datadir}/%{name}/modules/configuration/globalhotkeys.ui
%{_datadir}/%{name}/modules/globalhotkeys.desc
%lang(pl) %{_datadir}/%{name}/modules/translations/globalhotkeys_pl.qm
%endif

%if %build_kde_notify
%package module-kde4-notify
Summary:	Notification for KDE4
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-kde4-notify
Notification for KDE4.

%files module-kde4-notify
%defattr(-,root,root)
%{_datadir}/%{name}/modules/kde_notify.desc
%{_datadir}/%{name}/modules/configuration/kde_notify.ui
%{_libdir}/%{name}/modules/libkde_notify.so
%endif

%if %build_last_seen
%package module-last_seen
Summary:	Last seen module for %{name}
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-last_seen
Last seen module for %{name}.

%files module-last_seen
%defattr(-,root,root)
%{_libdir}/%{name}/modules/liblast_seen.so
%{_datadir}/%{name}/modules/last_seen.desc
%lang(pl) %{_datadir}/%{name}/modules/translations/last_seen_pl.qm
%endif

%if %build_led_notify
%package module-led_notify
Summary:	Notification by LED
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-led_notify
Notification by keyboard's LED.

%files module-led_notify
%defattr(-,root,root)
%doc modules/led_notify/Changelog
%{_datadir}/%{name}/modules/led_notify.desc
%{_datadir}/%{name}/modules/configuration/led_notify.ui
%{_libdir}/%{name}/modules/libled_notify.so
%endif

%if %build_mediaplayer
%package module-mediaplayer
Summary:	Mediaplayer module for kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-mediaplayer
Mediaplayer module for kadu.

%files module-mediaplayer
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/mediaplayer
%{_libdir}/%{name}/modules/libmediaplayer.so
%{_datadir}/%{name}/modules/mediaplayer.desc
%{_datadir}/%{name}/modules/configuration/mediaplayer.ui
%{_datadir}/%{name}/modules/data/mediaplayer/mediaplayer.png
%lang(pl) %{_datadir}/%{name}/modules/translations/mediaplayer_pl.qm
%endif

%if %build_amarok
%package module-mediaplayer_amarok
Summary:	Amarok module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	%{name}-module-autostatus = %{version}-%{release}
Obsoletes:	%{name}-module-amarok
Requires:	amarok

%description module-mediaplayer_amarok
Module which allows showing in status description information about
the song currently played in Amarok.

%files module-mediaplayer_amarok
%defattr(-,root,root)
%{_datadir}/%{name}/modules/amarok2_mediaplayer.desc
%{_datadir}/%{name}/modules/amarok1_mediaplayer.desc
%{_libdir}/%{name}/modules/libamarok2_mediaplayer.so
%{_libdir}/%{name}/modules/libamarok1_mediaplayer.so
%endif

%if %build_audacious
%package module-mediaplayer_audacious
Summary:	Support audacious status
Group:		Networking/Instant messaging
BuildRequires:	audacious-devel
BuildRequires:	dbus-glib-devel
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	%{name}-module-autostatus = %{version}-%{release}
Requires:	audacious

%description module-mediaplayer_audacious
Module which allows showing in status description information about
the song currently played in audacious.

%files module-mediaplayer_audacious
%defattr(-,root,root)
%{_datadir}/%{name}/modules/audacious_mediaplayer.desc
%{_libdir}/%{name}/modules/libaudacious_mediaplayer.so
%endif

%if %build_falf
%package module-mediaplayer_falf
Summary:	Falf player odule for Kadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	%{name}-module-autostatus = %{version}-%{release}
Obsoletes:	%{name}-module-falfp
Requires:	falf >= 1.0

%description module-mediaplayer_falf
Module which allows showing in status description information about
the song currently played in Falf player.

%files module-mediaplayer_falf
%defattr(-,root,root)
%{_datadir}/%{name}/modules/falf_mediaplayer.desc
%{_libdir}/%{name}/modules/falf_mediaplayer.so
%endif

%if %build_xmms
%package module-mediaplayer_xmms
Summary:	XMMS module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-mediaplayer = %{version}-%{release}
Requires:	%{name}-module-autostatus = %{version}-%{release}
Obsoletes:	%{name}-module-xmms
Requires:	xmms
BuildRequires:	libxmms-devel

%description module-mediaplayer_xmms
Module which allows showing in status description information about
the song currently played in XMMS.

%files module-mediaplayer_xmms
%defattr(-,root,root)
%{_datadir}/%{name}/modules/xmms_mediaplayer.desc
%{_libdir}/%{name}/modules/xmms_mediaplayer.so
%endif

%if %build_mime_tex
%package module-mime_tex
Summary:	Mathematical TeX formulas for %{name}
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-mime_tex
Mathematical TeX formulas for %{name}.

%files module-mime_tex
%defattr(-,root,root)
%dir %{_libdir}/%{name}/modules/bin/mime_tex
%dir %{_datadir}/%{name}/modules/data/mime_tex
%dir %{_datadir}/%{name}/modules/data/mime_tex/editor_icons
%dir %{_datadir}/%{name}/modules/data/mime_tex/mime_tex_icons
%{_libdir}/%{name}/modules/bin/mime_tex/mimetex
%{_libdir}/%{name}/modules/libmime_tex.so
%{_datadir}/%{name}/modules/mime_tex.desc
%{_datadir}/%{name}/modules/configuration/mime_tex.ui
%{_datadir}/%{name}/modules/data/mime_tex/*.png
%{_datadir}/%{name}/modules/data/mime_tex/editor_icons/*.png
%{_datadir}/%{name}/modules/data/mime_tex/mime_tex_icons/*.png
%lang(pl) %{_datadir}/%{name}/modules/translations/mime_tex_pl.qm
%endif

%if %build_nas_sound
%package module-nas_sound
Summary:	NAS sound module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	nas
BuildRequires:	libnas-devel

%description module-nas_sound
Network Audio System support.

%files module-nas_sound
%defattr(-,root,root)
%{_datadir}/%{name}/modules/nas_sound.desc
%{_libdir}/%{name}/modules/nas_sound.so
%endif

%if %build_panelkadu
%package module-panelkadu
Summary:	Module which makes Kadu look and behave like a panel
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-panelkadu
Module which makes Kadu look and behave like a panel.

%files module-panelkadu
%defattr(-,root,root)
%{_datadir}/%{name}/modules/panelkadu.desc
%{_datadir}/%{name}/modules/configuration/panelkadu.ui
%{_libdir}/%{name}/modules/libpanelkadu.so
%lang(pl) %{_datadir}/%{name}/modules/translations/panelkadu_pl.qm
%endif

%if %build_parser_extender
%package module-parser_extender
Summary:	Module to extend Kadu Parser
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-parser_extender
Module to extend Kadu Parser.

%files module-parser_extender
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libparser_extender.so
%{_datadir}/%{name}/modules/parser_extender.desc
%{_datadir}/%{name}/modules/configuration/parser_extender.ui
%lang(pl) %{_datadir}/%{name}/modules/translations/parser_extender_pl.qm
%endif

%if %build_pcspeaker
%package module-pcspeaker
Summary:	PC-Speaker support
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-pcspeaker
PC-Speaker support module.

%files module-pcspeaker
%defattr(-,root,root)
%doc modules/pcspeaker/Changelog
%{_datadir}/%{name}/modules/configuration/pcspeaker.ui
%{_datadir}/%{name}/modules/pcspeaker.desc
%{_libdir}/%{name}/modules/pcspeaker.so
%lang(de) %{_datadir}/%{name}/modules/translations/pcspeaker_de.qm
%lang(it) %{_datadir}/%{name}/modules/translations/pcspeaker_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/pcspeaker_pl.qm
%endif

%if %build_plus_pl_sms
%package module-plus_pl_sms
Summary:	Miasto Plusa SMS Gateway
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Obsoletes:	%{name}-module-miastoplusa_sms < 0.6.5
Provides:	%{name}-module-miastoplusa_sms
BuildRequires:	libcurl-devel

%description module-plus_pl_sms
Miasto Plusa SMS Gateway support module.

%files module-plus_pl_sms
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/plus_pl_sms
%{_libdir}/%{name}/modules/libplus_pl_sms.so
%{_datadir}/%{name}/modules/configuration/plus_pl_sms.ui
%{_datadir}/%{name}/modules/data/plus_pl_sms/curl-ca-bundle.crt
%{_datadir}/%{name}/modules/plus_pl_sms.desc
%lang(pl) %{_datadir}/%{name}/modules/translations/plus_pl_sms_pl.qm
%endif

%if %build_powerkadu
%package module-powerkadu
Summary:	Powerkadu
Group:		Networking/Instant messaging
Requires:	%{name}-module-anonymous_check = %{version}-%{release}
Requires:	%{name}-module-antistring = %{version}-%{release}
Requires:	%{name}-module-auto_hide = %{version}-%{release}
Requires:	%{name}-module-cenzor = %{version}-%{release}
Requires:	%{name}-module-parser_extender = %{version}-%{release}
Requires:	%{name}-module-split_messages = %{version}-%{release}
Requires:	%{name}-module-word_fix = %{version}-%{release}

%description module-powerkadu
Powerkadu extends capabilities of Kadu.

%files module-powerkadu
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/powerkadu
%{_datadir}/%{name}/modules/data/powerkadu/AU*
%{_datadir}/%{name}/modules/data/powerkadu/Ch*
%{_datadir}/%{name}/modules/data/powerkadu/*.png
%{_datadir}/%{name}/modules/powerkadu.desc
%{_libdir}/%{name}/modules/libpowerkadu.so
%lang(pl) %{_datadir}/%{name}/modules/translations/powerkadu_pl.qm
%endif

%if %build_speech
%package module-speech
Summary:	Speech synthesis support
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
#Requires:	powiedz

%description	module-speech
Speech synthesis support.

%files module-speech
%defattr(-,root,root)
%{_datadir}/%{name}/modules/speech.desc
%{_datadir}/%{name}/modules/configuration/speech.ui
%{_libdir}/%{name}/modules/libspeech.so
%lang(de) %{_datadir}/%{name}/modules/translations/speech_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/speech_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/speech_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/speech_pl.qm
%endif

%if %build_spellchecker
%package module-spellchecker
Summary:	Aspell module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	aspell
BuildRequires:	libaspell-devel

%description module-spellchecker
Checker of spelling mistakes.

%files module-spellchecker
%defattr(-,root,root)
%doc modules/spellchecker/{README,ChangeLog}
%{_datadir}/%{name}/modules/spellchecker.desc
%{_datadir}/%{name}/modules/configuration/spellchecker.ui
%{_libdir}/%{name}/modules/libspellchecker.so
%lang(pl) %{_datadir}/%{name}/modules/translations/spellchecker_pl.qm
%endif

%if %build_split_messages
%package module-split_messages
Summary:	Automaticaly split too long messages in %{name}
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	aspell

%description module-split_messages
Automaticaly split too long messages in %{name}.

%files module-split_messages
%defattr(-,root,root)
%{_libdir}/%{name}/modules/libsplit_messages.so
%{_datadir}/%{name}/modules/split_messages.desc
%{_datadir}/%{name}/modules/configuration/split_messages.ui
%lang(pl) %{_datadir}/%{name}/modules/translations/split_messages_pl.qm
%endif

%if %build_water_notify
%package module-water-notify
Summary:	Notification by Water Plugin in Compiz
Group:		Networking/Instant messaging
BuildRequires:	dbus-devel
Requires:	%{name} = %{version}-%{release}
Requires:	compiz
Obsoletes:	%{name}-module-notify-water

%description module-water-notify
Notification by water plugin in Compiz.

%files module-water-notify
%defattr(-,root,root)
%{_datadir}/%{name}/modules/water_notify.desc
%{_datadir}/%{name}/modules/configuration/water_notify.ui
%{_libdir}/%{name}/modules/libwater_notify.so
%lang(pl) %{_datadir}/%{name}/modules/translations/water_notify_pl.qm
%endif

%if %build_weather
%package module-weather
Summary:	Weather module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-weather
This module shows current weather for you and your contacts.

%files module-weather
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/weather
%dir %{_datadir}/%{name}/modules/data/weather/icons
%{_datadir}/%{name}/modules/data/weather/icons/*
%{_datadir}/%{name}/modules/data/weather/interia.ini
%{_datadir}/%{name}/modules/data/weather/onetweather.ini
%{_datadir}/%{name}/modules/data/weather/pfweather.ini
%{_datadir}/%{name}/modules/weather.desc
%{_datadir}/%{name}/modules/configuration/weather.ui
%{_libdir}/%{name}/modules/libweather.so
%lang(pl) %{_datadir}/%{name}/modules/translations/weather_pl.qm
%endif

%if %build_wmaker_docking
%package module-wmaker_docking
Summary: 	WindowMaker docking module
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires: 	WindowMaker

%description module-wmaker_docking
WindowMaker docking module.

%files module-wmaker_docking
%defattr(-,root,root)
%{_datadir}/%{name}/modules/wmaker_docking.desc
#%{_libdir}/%{name}/modules/wmaker_docking.so
%endif

%if %build_word_fix
%package module-word_fix
Summary:	Automatic word replacement module for %{name}
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}

%description module-word_fix
Automatic word replacement module for %{name}.

%files		module-word_fix
%defattr(-,root,root)
%dir %{_datadir}/%{name}/modules/data/word_fix
%{_libdir}/%{name}/modules/libword_fix.so
%{_datadir}/%{name}/modules/word_fix.desc
%{_datadir}/%{name}/modules/configuration/word_fix.ui
%{_datadir}/%{name}/modules/data/word_fix/*.data
%lang(pl) %{_datadir}/%{name}/modules/translations/word_fix_pl.qm
%endif

%if %build_xosd_notify
%package module-xosd_notify
Summary: 	Notification by XOSD
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
BuildRequires: 	gtk2-devel
BuildRequires: 	libxosd-devel

%description module-xosd_notify
Notification by XOSD module.

%files module-xosd_notify
%defattr(-,root,root)
%doc modules/xosd_notify/{README,ChangeLog}
%dir %{_libdir}/%{name}/modules/bin/xosd_notify
%{_datadir}/%{name}/modules/xosd_notify.desc
%{_datadir}/%{name}/modules/configuration/xosd_notify.ui
#%{_libdir}/%{name}/modules/xosd_notify.so
%{_libdir}/%{name}/modules/bin/xosd_notify/gtkfontdialog
%endif

%if %build_xqf
%package module-xqf
Summary:	XQF module for Kadu
Group:		Networking/Instant messaging
Requires:	%{name} = %{version}-%{release}
Requires:	xqf

%description module-xqf
Module which allows showing in status description information about
the game and ip of a gameserver currently played.

%files module-xqf
%defattr(-,root,root)
%{_datadir}/%{name}/modules/qf.desc
%{_libdir}/%{name}/modules/qf.so
%endif

#----------Icons----------

%if %build_icons_crystal
%package icons_crystal
Summary: 	Crystal icons for Kadu
Group:		Networking/Instant messaging
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}

%description icons_crystal
Crystal icon theme for kadu created by arcisz.

#icons_crystal
%files icons_crystal
%defattr(-,root,root)
%doc varia/themes/icons/crystal16/README
%dir %{_datadir}/%{name}/themes/icons/crystal16
%dir %{_datadir}/%{name}/themes/icons/crystal22
%{_datadir}/%{name}/themes/icons/crystal16/*
%{_datadir}/%{name}/themes/icons/crystal22/*
%endif

%if %build_icons_glass
%package icons_glass
Summary: 	Glass icons for Kadu
Group:		Networking/Instant messaging
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%description icons_glass
Glass icon theme for kadu created by Mariusz Waluga.

%files icons_glass
%defattr(-,root,root)
%dir %{_datadir}/%{name}/themes/icons/glass16
%dir %{_datadir}/%{name}/themes/icons/glass22
%{_datadir}/%{name}/themes/icons/glass16/*
%{_datadir}/%{name}/themes/icons/glass22/*
%endif

%if %build_icons_nuvola
%package icons_nuvola
Summary: 	Nuvola icons for Kadu
Group:		Networking/Instant messaging
License:	LGPLv2+
Requires:	%{name} = %{version}-%{release}

%description icons_nuvola
Nuvola icon theme for kadu created by David Vignoni.

%files icons_nuvola
%defattr(-,root,root)
%doc varia/themes/icons/nuvola16/Copyright
%dir %{_datadir}/%{name}/themes/icons/nuvola16
%dir %{_datadir}/%{name}/themes/icons/nuvola22
%{_datadir}/%{name}/themes/icons/nuvola16/*
%{_datadir}/%{name}/themes/icons/nuvola22/*
%endif

%if %build_icons_oxygen
%package icons_oxygen
Summary: 	Oxygen icons for Kadu
Group:		Networking/Instant messaging
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%description icons_oxygen
Oxygen icon theme for kadu.

%files icons_oxygen
%defattr(-,root,root)
%dir %{_datadir}/%{name}/themes/icons/oxygen16
%{_datadir}/%{name}/themes/icons/oxygen16/*
%endif

%if %build_icons_tango
%package icons_tango
Summary: 	Tango icons for Kadu
Group:		Networking/Instant messaging
License:	GPLv2+
Requires:	%{name} = %{version}-%{release}

%description icons_tango
Tango icon theme for kadu.

%files icons_tango
%defattr(-,root,root)
%dir %{_datadir}/%{name}/themes/icons/tango16
%{_datadir}/%{name}/themes/icons/tango16/*
%endif


#--------------------------------------------------------------

%prep
%setup -qn %{name}
%if %build_amarok
%{__sed} -i 's/module_amarok2_mediaplayer=./module_amarok2_mediaplayer=m/' .config
%endif
%if %build_ao_sound
%{__sed} -i 's/module_ao_sound=./module_ao_sound=m/' .config
%endif
%if %build_arts_sound
%{__sed} -i 's/module_arts_sound=./module_arts_sound=m/' .config
%endif
%if %build_audacious
%{__sed} -i 's/module_audacious_mediaplayer=./module_audacious_mediaplayer=m/' .config
%endif
%if %build_autostatus
%{__sed} -i 's/module_autostatus=./module_autostatus=m/' .config
%endif
%if %build_dcopexport
tar xf %{SOURCE4} -C modules
%{__sed} -i 's/module_dcopexport=./module_dcopexport=m/' .config
%endif
%if %build_desc_history
tar xf %{SOURCE51} -C modules
%{__sed} -i 's/module_desc_history=./module_desc_history=m/' .config
%endif
%if %build_desktop_docking
%{__sed} -i 's/module_desktop_docking=./module_desktop_docking=m/' .config
%endif
%if %build_esd_sound
%{__sed} -i 's/module_esd_sound=./module_esd_sound=m/' .config
%endif
%if %build_exec_notify
%{__sed} -i 's/module_exec_notify=./module_exec_notify=m/' .config
%endif
%if %build_ext_info
tar xf %{SOURCE6} -C modules
%endif
%if %build_filedesc
%{__sed} -i 's/module_filedesc=./module_filedesc=m/' .config
%endif
%if %build_filtering
%{__sed} -i 's/module_filtering=./module_filtering=m/' .config
%endif
%if %build_firewall
%{__sed} -i 's/module_firewall=./module_firewall=m/' .config
%endif
%if %build_globalhotkeys
tar xf %{SOURCE50} -C modules
%{__sed} -i 's/module_globalhotkeys=./module_globalhotkeys=m/' .config
%endif
%if %build_iwait4u
tar xf %{SOURCE10} -C modules
%{__sed} -i 's/module_iwait4u=./module_iwait4u=m/' .config
%endif
%if %build_kde_notify
tar xf %{SOURCE53} -C modules
%{__sed} -i 's/module_kde_notify=n/module_kde_notify=m/' .config
%endif
%if %build_led_notify
tar xf %{SOURCE11} -C modules
%{__sed} -i 's/module_led_notify=./module_led_notify=m/' .config
%endif
%if %build_mail
tar xf %{SOURCE12} -C modules
%{__sed} -i 's/module_mail=./module_mail=m/' .config
%endif
%if %build_plus_pl_sms
tar xf %{SOURCE13} -C modules
%{__sed} -i 's/module_plus_pl_sms=./module_plus_pl_sms=m/' .config
%endif
%if %build_nas_sound
%{__sed} -i 's/module_nas_sound=./module_nas_sound=m/' .config
%endif
%if %build_osdhints_notify
tar xf %{SOURCE14} -C modules
%{__sed} -i 's/module_osdhints_notify=./module_osdhints_notify=m/' .config
%endif
%if %build_pcspeaker
%{__sed} -i 's/module_pcspeaker=./module_pcspeaker=m/' .config
%endif
%if %build_powerkadu
tar xf %{SOURCE16} -C modules
%{__sed} -i 's/module_powerkadu=./module_powerkadu=m/' .config
%endif
%if %build_profiles
%{__sed} -i 's/module_profiles=./module_profiles=m/' .config
%endif
%if %build_screenshot
%{__sed} -i 's/module_screenshot=./module_screenshot=m/' .config
%endif
%if %build_speech
%{__sed} -i 's/module_speech=./module_speech=m/' .config
%endif
%if %build_spellchecker
%{__sed} -i 's/module_spellchecker=./module_spellchecker=m/' .config
%endif
%if %build_tabs
tar xf %{SOURCE20} -C modules
%{__sed} -i 's/module_tabs=./module_tabs=m/' .config
%endif
%if %build_qt4_sound
%{__sed} -i 's/module_qt4_sound=./module_qt4_sound=m/' .config
%endif
%if %build_weather
tar xf %{SOURCE21} -C modules
%{__sed} -i 's/module_weather=./module_weather=m/' .config
%endif
%if %build_wmaker_docking
%{__sed} -i 's/module_wmaker_docking=./module_wmaker_docking=m/' .config
%endif
%if %build_xmms
%{__sed} -i 's/module_xmms_mediaplayer=./module_xmms_mediaplayer=m/' .config
%endif
%if %build_xosd_notify
tar xf %{SOURCE23} -C modules
%{__sed} -i 's/module_xosd_notify=./module_xosd_notify=m/' .config
%endif
%if %build_adavanced_userlist
%{__sed} -i 's/module_advanced_userlist=./module_advanced_userlist=m/' .config
%endif
%if %build_falf
%{__sed} -i 's/module_falf_mediaplayer=./module_falf_mediaplayer=m/' .config
%endif
%if %build_agent
tar xf %{SOURCE32} -C modules
%{__sed} -i 's/module_agent=./module_agent=m/' .config
%endif
%if %build_xqf
tar xf %{SOURCE33} -C modules
%endif
%if %build_mediaplayer
%{__sed} -i 's/module_mediaplayer=./module_mediaplayer=m/' .config
%endif
%if %build_mediaplayer_mpris
%{__sed} -i 's/module_mpris_mediaplayer=n/module_mpris_mediaplayer=m/' .config
%endif

%if %build_mime_tex
tar xf %{SOURCE36} -C modules
%{__sed} -i 's/module_mime_tex=./module_mime_tex=m/' .config
%endif
%if %build_water_notify
tar xf %{SOURCE37} -C modules
%{__sed} -i 's/module_water_notify=./module_water_notify=m/' .config
%endif
%if %build_panelkadu
tar xf %{SOURCE38} -C modules
%{__sed} -i 's/module_panelkadu=./module_panelkadu=m/' .config
%endif
%if %build_antistring
%{__sed} -i 's/module_antistring=./module_antistring=m/' .config
%endif
%if %build_anonymous_check
tar xf %{SOURCE41} -C modules
%{__sed} -i 's/module_anonymous_check=./module_anonymous_check=m/' .config
%endif
%if %build_auto_hide
%{__sed} -i 's/module_auto_hide=./module_auto_hide=m/' .config
%endif
%if %build_cenzor
%{__sed} -i 's/module_cenzor=./module_cenzor=m/' .config
%endif
%if %build_parser_extender
%{__sed} -i 's/module_parser_extender=./module_parser_extender=m/' .config
%endif
%if %build_sent_history
tar xf %{SOURCE52} -C modules
%{__sed} -i 's/module_sent_history=./module_sent_history=m/' .config
%endif
%if %build_split_messages
tar xf %{SOURCE45} -C modules
%{__sed} -i 's/module_split_messages=./module_split_messages=m/' .config
%endif
%if %build_word_fix
%{__sed} -i 's/module_word_fix=./module_word_fix=m/' .config
%endif
%if %build_last_seen
%{__sed} -i 's/module_last_seen=./module_last_seen=m/' .config
%endif

%if %build_icons_crystal
tar xf %{SOURCE24} -C varia/themes/icons
tar xf %{SOURCE25} -C varia/themes/icons
%endif
%if %build_icons_glass
tar xf %{SOURCE26} -C varia/themes/icons
tar xf %{SOURCE27} -C varia/themes/icons
%{__sed} -i 's/icons_glass16=n/icons_glass16=y/' .config
%{__sed} -i 's/icons_glass22=n/icons_glass22=y/' .config
%endif
%if %build_icons_nuvola
tar xf %{SOURCE28} -C varia/themes/icons
tar xf %{SOURCE29} -C varia/themes/icons
%endif
%if %build_icons_oxygen
tar xf %{SOURCE48} -C varia/themes/icons
%{__sed} -i 's/icons_oxygen16=n/icons_oxygen16=y/' .config
%endif
%if %build_icons_tango
tar xf %{SOURCE34} -C varia/themes/icons
%{__sed} -i 's/icons_tango16=n/icons_tango16=y/' .config
%endif


#emoticons
tar xf %{SOURCE49} -C varia/themes/emoticons
%{__sed} -i 's/emoticons_tango=n/emoticons_tango=y/' .config


pushd varia/themes/icons
for file in kadu-theme*; do
mv $file `echo $file | sed -e s/kadu-theme-//g -e s/[_-]//g`
done
popd

#%patch4 -p1 -b .alsa
#%patch5 -p1 -b .ext_sound
%patch6 -p1 -b .voice
#%patch7 -p1 -b .water
%patch8 -p0

%build
#(tpg) disable notifications about upstream updates
pushd kadu-core
sed -i -e "/CheckUpdates/s#true#false#" kadu.cpp
popd

# force the right lib path and set DETAILED_VERSION
sed -i -e 's#set (LIBDIR ${CMAKE_INSTALL_PREFIX}/lib)#set (LIBDIR %{_libdir})#' CMakeLists.txt
sed -i -e 's@#define DETAILED.*@#define DETAILED_VERSION "%{name}-%{version}-%{release}"@' kadu-config.h.cmake

# change sounds path
#sed -i -e 's#share/kadu/themes/sound#share/kadu/themes/sounds#g' varia/themes/sounds/CMakeLists.txt

%define _disable_ld_no_undefined 1
%define Werror_cflags %nil

%cmake \
    -DCMAKE_USE_PTHREADS:BOOL=ON \
    -DBUILD_DESCRIPTION="%vendor" \
    -DENABLE_AUTDOWNLOAD:BOOL=OFF \
%if "%{_lib}" == "lib64"
    -DLIB_SUFFIX_64:BOOL=ON \
%endif
    -DCMAKE_USE_PTHREADS:BOOL=ON

%make

%install
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

pushd build
%makeinstall_std
popd

desktop-file-install \
	--dir %{buildroot}%{_datadir}/applications %{SOURCE1}

rm -rf `find %{buildroot} -name CVS`
pushd %{buildroot}%{_datadir}/%{name}
rm -f AUTHORS COPYING ChangeLog HISTORY README THANKS modules/data/osdhints_notify/License
popd

#(tpg) cmake stuff is weird...
if [ "x%{_lib}" != "xlib" ]; then
    cp -af %{buildroot}%{_prefix}/lib/kadu %{buildroot}%{_libdir}
    sleep 1
    rm -rf %{buildroot}%{_prefix}/lib/kadu
fi


%if %mdkversion < 200900
%post
%{update_menus}
%{update_desktop_database}
%update_icon_cache hicolor
%endif

%if %mdkversion < 200900
%postun
%{clean_menus}
%{clean_desktop_database}
%clean_icon_cache hicolor
%endif

%clean
[ "%{buildroot}" != "/" ] && rm -rf %{buildroot}

%files
%defattr(-,root,root)
%doc HISTORY README TODO VERSION THANKS AUTHORS FAQ
%{_bindir}/kadu
%{_datadir}/applications/%{name}.desktop

#default directories
%dir %{_libdir}/%{name}
%dir %{_libdir}/%{name}/modules
%dir %{_datadir}/%{name}
%dir %{_datadir}/%{name}/configuration
%dir %{_datadir}/%{name}/translations
%dir %{_datadir}/%{name}/modules
%dir %{_datadir}/%{name}/modules/configuration
%dir %{_datadir}/%{name}/modules/data
%dir %{_datadir}/%{name}/modules/translations
%dir %{_datadir}/%{name}/themes
%dir %{_datadir}/%{name}/themes/emoticons
%dir %{_datadir}/%{name}/themes/icons
%{_datadir}/%{name}/syntax
%{_iconsdir}/hicolor/*/apps/*.png
%{_datadir}/%{name}/configuration/dialog-look-chat-advanced.ui
%{_datadir}/%{name}/configuration/dialog.ui

#module_account_management
%{_datadir}/%{name}/modules/account_management.desc
%{_libdir}/%{name}/modules/libaccount_management.so
%lang(de) %{_datadir}/%{name}/modules/translations/account_management_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/account_management_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/account_management_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/account_management_pl.qm

#module_adavanced_userlist
%{_libdir}/%{name}/modules/libadvanced_userlist.so
%{_datadir}/%{name}/modules/advanced_userlist.desc
%{_datadir}/%{name}/modules/configuration/advanced_userlist.ui
%lang(de) %{_datadir}/%{name}/modules/translations/advanced_userlist_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/advanced_userlist_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/advanced_userlist_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/advanced_userlist_pl.qm

#module_alsa_sound
%{_datadir}/%{name}/modules/alsa_sound.desc
%{_datadir}/%{name}/modules/configuration/alsa_sound.ui
%{_libdir}/%{name}/modules/libalsa_sound.so
%lang(de) %{_datadir}/%{name}/modules/translations/alsa_sound_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/alsa_sound_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/alsa_sound_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/alsa_sound_pl.qm

#module_autoaway
%{_datadir}/%{name}/modules/autoaway.desc
%{_datadir}/%{name}/modules/configuration/autoaway.ui
%{_libdir}/%{name}/modules/libautoaway.so
%lang(de) %{_datadir}/%{name}/modules/translations/autoaway_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/autoaway_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/autoaway_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/autoaway_pl.qm

#module_autoresponder
%{_datadir}/%{name}/modules/autoresponder.desc
%{_datadir}/%{name}/modules/configuration/autoresponder.ui
%{_libdir}/%{name}/modules/libautoresponder.so
%lang(de) %{_datadir}/%{name}/modules/translations/autoresponder_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/autoresponder_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/autoresponder_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/autoresponder_pl.qm

#module_config_wizard
%dir %{_datadir}/%{name}/modules/data/config_wizard
%{_datadir}/%{name}/modules/config_wizard.desc
%{_libdir}/%{name}/modules/libconfig_wizard.so
%{_datadir}/%{name}/modules/data/config_wizard/*
%lang(de) %{_datadir}/%{name}/modules/translations/config_wizard_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/config_wizard_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/config_wizard_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/config_wizard_pl.qm

#module_dbus
%{_datadir}/%{name}/modules/dbus.desc
%{_libdir}/%{name}/modules/libdbus.so

#module_dcc
%{_datadir}/%{name}/modules/dcc.desc
%{_datadir}/%{name}/modules/configuration/dcc.ui
%{_libdir}/%{name}/modules/libdcc.so
%lang(de) %{_datadir}/%{name}/modules/translations/dcc_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/dcc_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/dcc_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/dcc_pl.qm

#module_default_sms
%{_datadir}/%{name}/modules/default_sms.desc
%{_datadir}/%{name}/modules/configuration/default_sms.ui
%{_libdir}/%{name}/modules/libdefault_sms.so
%lang(de) %{_datadir}/%{name}/modules/translations/default_sms_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/default_sms_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/default_sms_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/default_sms_pl.qm

#module_encryption
%{_datadir}/%{name}/modules/encryption.desc
%{_datadir}/%{name}/modules/configuration/encryption.ui
%{_libdir}/%{name}/modules/libencryption.so
%lang(de) %{_datadir}/%{name}/modules/translations/encryption_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/encryption_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/encryption_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/encryption_pl.qm

#module_exec_notify
%{_datadir}/%{name}/modules/exec_notify.desc
%{_libdir}/%{name}/modules/libexec_notify.so

#module_ext_info
#%dir %{_datadir}/%{name}/modules/data/ext_info
#%{_datadir}/%{name}/modules/data/ext_info/*
#%{_datadir}/%{name}/modules/ext_info.desc
#%{_libdir}/%{name}/modules/ext_info.so
#%lang(pl) %{_datadir}/%{name}/modules/translations/ext_info_pl.qm

#module_filedesc
%{_datadir}/%{name}/modules/configuration/filedesc.ui
%{_datadir}/%{name}/modules/filedesc.desc
%{_libdir}/%{name}/modules/libfiledesc.so
%lang(pl) %{_datadir}/%{name}/modules/translations/filedesc_pl.qm

#module_filtering
%dir %{_datadir}/%{name}/modules/data/filtering
%{_datadir}/%{name}/modules/data/filtering/*.png
%{_datadir}/%{name}/modules/filtering.desc
%{_datadir}/%{name}/modules/configuration/filtering.ui
%{_libdir}/%{name}/modules/libfiltering.so
%lang(pl) %{_datadir}/%{name}/modules/translations/filtering_pl.qm

#module_firewall
%{_datadir}/%{name}/modules/firewall.desc
%{_datadir}/%{name}/modules/configuration/firewall.ui
%{_libdir}/%{name}/modules/libfirewall.so
%lang(pl) %{_datadir}/%{name}/modules/translations/firewall_pl.qm

#module_iwait4u
#%{_datadir}/%{name}/modules/iwait4u.desc
#%{_libdir}/%{name}/modules/iwait4u.so
#%lang(pl) %{_datadir}/%{name}/modules/translations/iwait4u_pl.qm

#module_idle
%{_datadir}/%{name}/modules/idle.desc
%{_libdir}/%{name}/modules/libidle.so

#module_hints
%{_datadir}/%{name}/modules/hints.desc
%{_datadir}/%{name}/modules/configuration/hints.ui
%{_libdir}/%{name}/modules/libhints.so
%lang(de) %{_datadir}/%{name}/modules/translations/hints_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/hints_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/hints_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/hints_pl.qm

#module_mail
%if %build_mail
%{_datadir}/%{name}/modules/mail.desc
%{_libdir}/%{name}/modules/libmail.so
%{_datadir}/%{name}/modules/configuration/mail.ui
%lang(pl) %{_datadir}/%{name}/modules/translations/mail_pl.qm
%endif

#module_history
%{_datadir}/%{name}/modules/history.desc
%{_datadir}/%{name}/modules/configuration/history.ui
%{_libdir}/%{name}/modules/libhistory.so
%lang(de) %{_datadir}/%{name}/modules/translations/history_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/history_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/history_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/history_pl.qm

%if %build_mediaplayer_mpris
#module_mpris
%{_datadir}/%{name}/modules/mpris_mediaplayer.desc
%{_datadir}/%{name}/modules/configuration/mpris_mediaplayer.ui
%{_libdir}/%{name}/modules/libmpris_mediaplayer.so
%lang(pl) %{_datadir}/%{name}/modules/translations/mpris_mediaplayer_pl.qm
%endif

#module_migration
#%{_datadir}/%{name}/modules/migration.desc
#%{_libdir}/%{name}/modules/migration.so
#%lang(de) %{_datadir}/%{name}/modules/translations/migration_de.qm
#%lang(fr) %{_datadir}/%{name}/modules/translations/migration_fr.qm
#%lang(it) %{_datadir}/%{name}/modules/translations/migration_it.qm
#%lang(pl) %{_datadir}/%{name}/modules/translations/migration_pl.qm

#module_osdhints_notify
%dir %{_datadir}/%{name}/modules/data/osdhints_notify
%{_datadir}/%{name}/modules/configuration/osdhints_notify.ui
%{_datadir}/%{name}/modules/data/osdhints_notify/*.png
%{_datadir}/%{name}/modules/osdhints_notify.desc
%{_libdir}/%{name}/modules/libosdhints_notify.so

#module_profiles
%if %build_profiles
%{_datadir}/%{name}/modules/profiles.desc
%{_libdir}/%{name}/modules/libprofiles.so
%lang(pl) %{_datadir}/%{name}/modules/translations/profiles_pl.qm
%endif

#module_screenshot
%{_datadir}/%{name}/modules/screenshot.desc
%{_datadir}/%{name}/modules/configuration/screenshot.ui
%{_libdir}/%{name}/modules/libscreenshot.so
%lang(pl) %{_datadir}/%{name}/modules/translations/screenshot_pl.qm

#module_sms
%{_datadir}/%{name}/modules/sms.desc
%{_datadir}/%{name}/modules/configuration/sms.ui
%{_libdir}/%{name}/modules/libsms.so
%lang(de) %{_datadir}/%{name}/modules/translations/sms_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/sms_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/sms_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/sms_pl.qm

#module_tabs
%{_datadir}/%{name}/modules/tabs.desc
%{_datadir}/%{name}/modules/configuration/tabs.ui
%{_libdir}/%{name}/modules/libtabs.so
%lang(pl) %{_datadir}/%{name}/modules/translations/tabs_pl.qm

#module_window_notify
%{_datadir}/%{name}/modules/window_notify.desc
%{_libdir}/%{name}/modules/libwindow_notify.so
%lang(de) %{_datadir}/%{name}/modules/translations/*notify_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/*notify_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/*notify_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/*notify_pl.qm
%exclude %{_datadir}/%{name}/modules/translations/water_notify_pl.qm

#module_voice
%{_datadir}/%{name}/modules/voice.desc
%{_datadir}/%{name}/modules/configuration/voice.ui
%{_libdir}/%{name}/modules/libvoice.so
%lang(de) %{_datadir}/%{name}/modules/translations/voice_de.qm
%lang(fr) %{_datadir}/%{name}/modules/translations/voice_fr.qm
%lang(it) %{_datadir}/%{name}/modules/translations/voice_it.qm
%lang(pl) %{_datadir}/%{name}/modules/translations/voice_pl.qm

#module_x11_docking
%{_datadir}/%{name}/modules/qt4_docking.desc
#%{_datadir}/%{name}/modules/x11_docking.desc
#%{_libdir}/%{name}/modules/x11_docking.so
#%lang(de) %{_datadir}/%{name}/modules/translations/x11_docking_de.qm
#%lang(fr) %{_datadir}/%{name}/modules/translations/x11_docking_fr.qm
#%lang(it) %{_datadir}/%{name}/modules/translations/x11_docking_it.qm
#%lang(pl) %{_datadir}/%{name}/modules/translations/x11_docking_pl.qm

%if %build_qt4_sound
%{_libdir}/%{name}/modules/libqt4_sound.so
%{_datadir}/%{name}/modules/qt4_sound.desc
%endif

#icons_default
%dir %{_datadir}/%{name}/themes/icons/default
%{_datadir}/%{name}/themes/icons/default/*

#emoticons_penguins
%dir %{_datadir}/%{name}/themes/emoticons/penguins
%{_datadir}/%{name}/themes/emoticons/penguins/*

#emoticons tango
%dir %{_datadir}/%{name}/themes/emoticons/tango
%{_datadir}/%{name}/themes/emoticons/tango/*

#sounds_default
%dir %{_datadir}/%{name}/themes/sounds
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
%{_libdir}/%{name}/modules/libnotify.so
%{_datadir}/%{name}/modules/configuration/notify.ui

#module_sound
%{_datadir}/%{name}/modules/sound.desc
%{_libdir}/%{name}/modules/libsound.so
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
