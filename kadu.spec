Summary:	A Gadu-Gadu client for online messaging
Name:		kadu
Version:	0.11.3
Release:	1
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
%cmake
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

