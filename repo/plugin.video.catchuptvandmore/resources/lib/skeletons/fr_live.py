# -*- coding: utf-8 -*-
# Copyright: (c) 2016, SylvainCecchetto
# GNU General Public License v2.0+ (see LICENSE.txt or https://www.gnu.org/licenses/gpl-2.0.txt)

# This file is part of Catch-up TV & More

from __future__ import unicode_literals

# The following dictionaries describe
# the addon's tree architecture.
# * Key: item id
# * Value: item infos
#     - route (folder)/resolver (playable URL): Callback function to run once this item is selected
#     - thumb: Item thumb path relative to "media" folder
#     - fanart: Item fanart path relative to "media" folder

root = 'live_tv'

menu = {
    'tf1': {
        'resolver': '/resources/lib/channels/fr/tf1plus:get_live_url',
        'label': 'TF1',
        'thumb': 'channels/fr/tf1.png',
        'fanart': 'channels/fr/tf1_fanart.jpg',
        'xmltv_id': 'C192.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 1,
        'enabled': True,
        'order': 1
    },
    'france-2': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'France 2',
        'thumb': 'channels/fr/france2.png',
        'fanart': 'channels/fr/france2_fanart.jpg',
        'xmltv_id': 'C4.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 2,
        'enabled': True,
        'order': 2
    },
    'france-3': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'France 3',
        'thumb': 'channels/fr/france3.png',
        'fanart': 'channels/fr/france3_fanart.jpg',
        'xmltv_id': 'C80.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 3,
        'enabled': True,
        'order': 3
    },
    'canalplus': {
        'resolver': '/resources/lib/channels/fr/mycanal:get_live_url',
        'label': 'Canal +',
        'thumb': 'channels/fr/canalplus.png',
        'fanart': 'channels/fr/canalplus_fanart.jpg',
        'xmltv_id': 'C34.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 4,
        'enabled': True,
        'order': 4
    },
    'france-5': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'France 5',
        'thumb': 'channels/fr/france5.png',
        'fanart': 'channels/fr/france5_fanart.jpg',
        'xmltv_id': 'C47.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 5,
        'enabled': True,
        'order': 5
    },
    'm6': {
        'resolver': '/resources/lib/channels/fr/6play:get_live_url',
        'label': 'M6',
        'thumb': 'channels/fr/m6.png',
        'fanart': 'channels/fr/m6_fanart.jpg',
        'xmltv_id': 'C118.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 6,
        'enabled': True,
        'order': 6
    },
    'c8': {
        'resolver': '/resources/lib/channels/fr/mycanal:get_live_url',
        'label': 'C8',
        'thumb': 'channels/fr/c8.png',
        'fanart': 'channels/fr/c8_fanart.jpg',
        'xmltv_id': 'C445.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 8,
        'enabled': True,
        'order': 7
    },
    'w9': {
        'resolver': '/resources/lib/channels/fr/6play:get_live_url',
        'label': 'W9',
        'thumb': 'channels/fr/w9.png',
        'fanart': 'channels/fr/w9_fanart.jpg',
        'xmltv_id': 'C119.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 9,
        'enabled': True,
        'order': 8
    },
    'tmc': {
        'resolver': '/resources/lib/channels/fr/tf1plus:get_live_url',
        'label': 'TMC',
        'thumb': 'channels/fr/tmc.png',
        'fanart': 'channels/fr/tmc_fanart.jpg',
        'xmltv_id': 'C195.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 10,
        'enabled': True,
        'order': 9
    },
    'tfx': {
        'resolver': '/resources/lib/channels/fr/tf1plus:get_live_url',
        'label': 'TFX',
        'thumb': 'channels/fr/tfx.png',
        'fanart': 'channels/fr/tfx_fanart.jpg',
        'xmltv_id': 'C446.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 11,
        'enabled': True,
        'order': 10
    },
    'nrj12': {
        'resolver': '/resources/lib/channels/fr/nrj:get_live_url',
        'label': 'NRJ 12',
        'thumb': 'channels/fr/nrj12.png',
        'fanart': 'channels/fr/nrj12_fanart.jpg',
        'xmltv_id': 'C444.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 12,
        'enabled': True,
        'order': 11
    },
    'lcp': {
        'resolver': '/resources/lib/channels/fr/lcp:get_live_url',
        'label': 'LCP Assemblée Nationale',
        'thumb': 'channels/fr/lcp.png',
        'fanart': 'channels/fr/lcp_fanart.jpg',
        'xmltv_id': 'C234.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 13,
        'enabled': True,
        'order': 12
    },
    'france-4': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'France 4',
        'thumb': 'channels/fr/france4.png',
        'fanart': 'channels/fr/france4_fanart.jpg',
        'xmltv_id': 'C78.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 14,
        'enabled': True,
        'order': 13
    },
    'BFM TV': {
        'resolver': '/resources/lib/channels/fr/bfmtv:get_live_url',
        'label': 'BFM TV',
        'thumb': 'channels/fr/bfmtv.png',
        'fanart': 'channels/fr/bfmtv_fanart.jpg',
        'xmltv_id': 'C481.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 15,
        'enabled': True,
        'order': 14
    },
    'cnews': {
        'resolver': '/resources/lib/channels/fr/cnews:get_live_url',
        'label': 'CNews',
        'thumb': 'channels/fr/cnews.png',
        'fanart': 'channels/fr/cnews_fanart.jpg',
        'xmltv_id': 'C226.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 16,
        'enabled': True,
        'order': 15
    },
    'cstar': {
        'resolver': '/resources/lib/channels/fr/mycanal:get_live_url',
        'label': 'CStar',
        'thumb': 'channels/fr/cstar.png',
        'fanart': 'channels/fr/cstar_fanart.jpg',
        'xmltv_id': 'C458.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 17,
        'enabled': True,
        'order': 16
    },
    'gulli': {
        'resolver': '/resources/lib/channels/fr/6play:get_live_url',
        'label': 'Gulli',
        'thumb': 'channels/fr/gulli.png',
        'fanart': 'channels/fr/gulli_fanart.jpg',
        'xmltv_id': 'C482.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 18,
        'enabled': True,
        'order': 17
    },
    'tf1-series-films': {
        'resolver': '/resources/lib/channels/fr/tf1plus:get_live_url',
        'label': 'TF1 Séries Films',
        'thumb': 'channels/fr/tf1seriesfilms.png',
        'fanart': 'channels/fr/tf1seriesfilms_fanart.jpg',
        'xmltv_id': 'C1404.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 18,
        'enabled': True,
        'order': 18
    },
    'lequipe': {
        'resolver': '/resources/lib/channels/fr/lequipe:get_live_url',
        'label': 'L\'Équipe',
        'thumb': 'channels/fr/lequipe.png',
        'fanart': 'channels/fr/lequipe_fanart.jpg',
        'xmltv_id': 'C1401.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 19,
        'enabled': True,
        'order': 19
    },
    '6ter': {
        'resolver': '/resources/lib/channels/fr/6play:get_live_url',
        'label': '6ter',
        'thumb': 'channels/fr/6ter.png',
        'fanart': 'channels/fr/6ter_fanart.jpg',
        'xmltv_id': 'C1403.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 20,
        'enabled': True,
        'order': 20
    },
    'RMC STORY': {
        'resolver': '/resources/lib/channels/fr/rmcbfmplay:get_live_url',
        'label': 'RMC Story',
        'thumb': 'channels/fr/rmcstory.png',
        'fanart': 'channels/fr/rmcstory_fanart.jpg',
        'xmltv_id': 'C1402.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 21,
        'enabled': True,
        'order': 21
    },
    'RMC Découverte': {
        'resolver': '/resources/lib/channels/fr/rmcbfmplay:get_live_url',
        'label': 'RMC Découverte',
        'thumb': 'channels/fr/rmcdecouverte.png',
        'fanart': 'channels/fr/rmcdecouverte_fanart.jpg',
        'xmltv_id': 'C1400.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 22,
        'enabled': True,
        'order': 22
    },
    'cherie25': {
        'resolver': '/resources/lib/channels/fr/nrj:get_live_url',
        'label': 'Chérie 25',
        'thumb': 'channels/fr/cherie25.png',
        'fanart': 'channels/fr/cherie25_fanart.jpg',
        'xmltv_id': 'C1399.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 23,
        'enabled': True,
        'order': 23
    },
    'lci': {
        'resolver': '/resources/lib/channels/fr/lci:get_live_url',
        'label': 'LCI',
        'thumb': 'channels/fr/lci.png',
        'fanart': 'channels/fr/lci_fanart.jpg',
        'xmltv_id': 'C112.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 24,
        'enabled': True,
        'order': 24
    },
    'franceinfo': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'France Info',
        'thumb': 'channels/fr/franceinfo.png',
        'fanart': 'channels/fr/franceinfo_fanart.jpg',
        'xmltv_id': 'C2111.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 25,
        'enabled': True,
        'order': 25
    },
    'publicsenat': {
        'resolver': '/resources/lib/channels/fr/publicsenat:get_live_url',
        'label': 'Public Sénat',
        'thumb': 'channels/fr/publicsenat.png',
        'fanart': 'channels/fr/publicsenat_fanart.jpg',
        'xmltv_id': 'C234.api.telerama.fr',
        'm3u_group': 'TNT',
        'm3u_order': 26,
        'enabled': True,
        'order': 26
    },
    'spectacles-et-culture': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'Culturebox',
        'thumb': 'channels/fr/culturebox.png',
        'fanart': 'channels/fr/culturebox_fanart.jpg',
        'xmltv_id': 'C3163.api.telerama.fr',
        'enabled': True,
        'order': 27
    },
    'francetvsport': {
        'route': '/resources/lib/channels/fr/francetvsport:list_lives',
        'label': 'France TV Sport (francetv)',
        'thumb': 'channels/fr/francetvsport.png',
        'fanart': 'channels/fr/francetvsport_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 28
    },
    'france3regions': {
        'resolver': '/resources/lib/channels/fr/france3regions:get_live_url',
        'label': 'France 3 Régions',
        'thumb': 'channels/fr/france3regions.png',
        'fanart': 'channels/fr/france3regions_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 29
    },
    'la_1ere': {
        'resolver': '/resources/lib/channels/fr/la_1ere:get_live_url',
        'label': 'La 1ère',
        'thumb':
        'channels/fr/la1ere.png',
        'fanart':
        'channels/fr/la1ere_fanart.jpg',
        'm3u_group':
        'Région',
        'available_languages': {
            "Guadeloupe": {
                'xmltv_id': 'C329.api.telerama.fr'
            },
            "Guyane": {
                'xmltv_id': 'C260.api.telerama.fr'
            },
            "Martinique": {
                'xmltv_id': 'C328.api.telerama.fr'
            },
            "Mayotte": {},
            "Nouvelle Calédonie": {
                'xmltv_id': 'C240.api.telerama.fr'
            },
            "Polynésie": {
                'xmltv_id': 'C459.api.telerama.fr'
            },
            "Réunion": {
                'xmltv_id': 'C245.api.telerama.fr'
            },
            "St-Pierre et Miquelon": {},
            "Wallis et Futuna": {}
        },
        'enabled': True,
        'order': 30
    },
    'antennereunion': {
        'resolver': '/resources/lib/channels/fr/antennereunion:get_live_url',
        'label': 'Antenne Réunion',
        'thumb': 'channels/fr/antennereunion.png',
        'fanart': 'channels/fr/antennereunion_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 31
    },
    'canal10': {
        'resolver': '/resources/lib/channels/fr/canal10:get_live_url',
        'label': 'Canal 10',
        'thumb': 'channels/fr/canal10.png',
        'fanart': 'channels/fr/canal10_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': False,
        'order': 32
    },
    'tntv': {
        'resolver': '/resources/lib/channels/fr/tntv:get_live_url',
        'label': 'Tahiti Nui Télévision',
        'thumb': 'channels/fr/tntv.png',
        'fanart': 'channels/fr/tntv_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 33
    },
    'viaatv': {
        'resolver': '/resources/lib/channels/fr/via:get_live_url',
        'label': 'viàATV',
        'thumb': 'channels/fr/viaatv.png',
        'fanart': 'channels/fr/viaatv_fanart.jpg',
        'xmltv_id': 'C295.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 34
    },
    'matele': {
        'resolver': '/resources/lib/channels/fr/via_matele:get_live_url',
        'label': 'viàMaTélé',
        'thumb': 'channels/fr/viamatele.png',
        'fanart': 'channels/fr/viamatele_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 35
    },
    'viaoccitanie': {
        'resolver': '/resources/lib/channels/fr/via_occitanie:get_live_url',
        'label': 'viàOccitanie',
        'thumb': 'channels/fr/viaoccitanie.png',
        'fanart': 'channels/fr/viaoccitanie_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 36
    },
    'viatelepaese': {
        'resolver': '/resources/lib/channels/fr/via:get_live_url',
        'label': 'viàTéléPaese',
        'thumb': 'channels/fr/viatelepaese.png',
        'fanart': 'channels/fr/viatelepaese_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 37
    },
    'viavosges': {
        'resolver': '/resources/lib/channels/fr/via:get_live_url',
        'label': 'viàVosges',
        'thumb': 'channels/fr/viavosges.png',
        'fanart': 'channels/fr/viavosges_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 38
    },
    'BFM_regions': {
        'resolver': '/resources/lib/channels/fr/rmcbfmplay:get_live_url',
        'label': 'BFM Régions',
        'thumb': 'channels/fr/bfmregions.png',
        'fanart': 'channels/fr/bfmregions_fanart.jpeg',
        'm3u_group': 'Région',
        'available_languages': {
            "BFM ALSACE": {},
            "BFM DICI HAUTE-PROVENCE": {},
            "BFM Grand Lille": {},
            "BFM Grand Littoral": {},
            "BFM Lyon": {},
            "BFM MARSEILLE PROVENCE": {},
            "BFM NICE COTE D'AZUR": {},
            "BFM NORMANDIE": {},
            "BFM PARIS ILE-DE-FRANCE": {},
            "BFM TOULON VAR": {},
        },
        'enabled': True,
        'order': 39
    },
    'albitv': {
        'resolver': '/resources/lib/channels/fr/albitv:get_live_url',
        'label': 'Albi TV',
        'thumb': 'channels/fr/albitv.png',
        'fanart': 'channels/fr/albitv_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 40
    },
    'biptv': {
        'resolver': '/resources/lib/channels/fr/biptv:get_live_url',
        'label': 'BIP TV',
        'thumb': 'channels/fr/biptv.png',
        'fanart': 'channels/fr/biptv_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 41
    },
    'dicitv': {
        'resolver': '/resources/lib/channels/fr/dicitv:get_live_url',
        'label': 'DiCi TV',
        'thumb': 'channels/fr/dicitv.png',
        'fanart': 'channels/fr/dicitv_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 42
    },
    'figarotv': {
        'resolver': '/resources/lib/channels/fr/figarotv:get_live_url',
        'label': 'Figaro TV Île-de-France',
        'thumb': 'channels/fr/figarotv_ile_de_france.png',
        'fanart': 'channels/fr/figarotv_ile_de_france_fanart.png',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 43
    },
    '20minutes': {
        'resolver': '/resources/lib/channels/fr/20minutes:get_live_url',
        'label': '20 Minutes Île de France',
        'thumb': 'channels/fr/20minutes.png',
        'fanart': 'channels/fr/20minutes_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 44
    },
    'lmtv': {
        'resolver': '/resources/lib/channels/fr/lmtv:get_live_url',
        'label': 'LMTV Sarthe',
        'thumb': 'channels/fr/LMTV_Sarthe.png',
        'fanart': 'channels/fr/LMTV_Sarthe_fanart.png',
        'xmltv_id': 'C535.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 45
    },
    'mblivetv': {
        'resolver': '/resources/lib/channels/fr/mblivetv:get_live_url',
        'label': 'Mont Blanc Live TV',
        'thumb': 'channels/fr/mblivetv.png',
        'fanart': 'channels/fr/mblivetv_fanart.jpg',
        'xmltv_id': 'C421.api.telerama.fr',
        'm3u_group': 'Satellite/FAI',
        'enabled': False,
        'order': 46
    },
    'moselletv': {
        'resolver': '/resources/lib/channels/fr/moselletv:get_live_url',
        'label': 'Moselle TV',
        'thumb': 'channels/fr/moselletv.png',
        'fanart': 'channels/fr/moselletv_fanart.jpg',
        'xmltv_id': 'C1045.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 47
    },
    'tebeo': {
        'resolver': '/resources/lib/channels/fr/tebeo:get_live_url',
        'label': 'Tébéo',
        'thumb': 'channels/fr/tebeo.png',
        'fanart': 'channels/fr/tebeo_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 48
    },
    'tebesud': {
        'resolver': '/resources/lib/channels/fr/tebeo:get_live_url',
        'label': 'TébéSud',
        'thumb': 'channels/fr/tebesud.png',
        'fanart': 'channels/fr/tebesud_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 49
    },
    'telegrenoble': {
        'resolver': '/resources/lib/channels/fr/telegrenoble:get_live_url',
        'label': 'TéléGrenoble',
        'thumb': 'channels/fr/telegrenoble.png',
        'fanart': 'channels/fr/telegrenoble_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 50
    },
    'telenantes': {
        'resolver': '/resources/lib/channels/fr/telenantes:get_live_url',
        'label': 'TéléNantes',
        'thumb': 'channels/fr/telenantes.png',
        'fanart': 'channels/fr/telenantes_fanart.jpg',
        'xmltv_id': 'C491.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 51
    },
    'tl7': {
        'resolver': '/resources/lib/channels/fr/tl7:get_live_url',
        'label': 'Télévision Loire 7',
        'thumb': 'channels/fr/tl7.png',
        'fanart': 'channels/fr/tl7_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 52
    },
    'tlc': {
        'resolver': '/resources/lib/channels/fr/tlc:get_live_url',
        'label': 'TLC',
        'thumb': 'channels/fr/tlc.png',
        'fanart': 'channels/fr/tlc_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 53
    },
    'tv7bordeaux': {
        'resolver': '/resources/lib/channels/fr/tv7bordeaux:get_live_url',
        'label': 'TV7 Bordeaux',
        'thumb': 'channels/fr/tv7bordeaux.png',
        'fanart': 'channels/fr/tv7bordeaux_fanart.jpg',
        'xmltv_id': 'C273.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 54
    },
    'tv7colmar': {
        'resolver': '/resources/lib/channels/fr/tv7colmar:get_live_url',
        'label': 'TV7 Colmar',
        'thumb': 'channels/fr/tv7colmar.png',
        'fanart': 'channels/fr/tv7colmar_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 55
    },
    'tv8montblanc': {
        'resolver': '/resources/lib/channels/fr/tv8montblanc:get_live_url',
        'label': '8 Mont-Blanc',
        'thumb': 'channels/fr/tv8montblanc.png',
        'fanart': 'channels/fr/tv8montblanc_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 56
    },
    'tvpifr': {
        'resolver': '/resources/lib/channels/fr/tvpifr:get_live_url',
        'label': 'TVPI télévision d\'ici',
        'thumb': 'channels/fr/tvpifr.png',
        'fanart': 'channels/fr/tvpifr_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 57
    },
    'tvr': {
        'resolver': '/resources/lib/channels/fr/tvr:get_live_url',
        'label': 'TVR',
        'thumb': 'channels/fr/tvr.png',
        'fanart': 'channels/fr/tvr_fanart.jpg',
        'xmltv_id': 'C539.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 58
    },
    'tvt': {
        'resolver': '/resources/lib/channels/fr/tvt:get_live_url',
        'label': 'TVT Val de Loire',
        'thumb': 'channels/fr/tvt.png',
        'fanart': 'channels/fr/tvt_fanart.jpg',
        'xmltv_id': 'C540.api.telerama.fr',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 59
    },
    'tvvendee': {
        'resolver': '/resources/lib/channels/fr/tvvendee:get_live_url',
        'label': 'TV Vendée',
        'thumb': 'channels/fr/tvvendee.png',
        'fanart': 'channels/fr/tvvendee_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 60
    },
    'tvv78': {
        'resolver': '/resources/lib/channels/fr/tv78:get_live_url',
        'label': 'TV78',
        'thumb': 'channels/fr/tv78.png',
        'fanart': 'channels/fr/tv78_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 61
    },
    'weo': {
        'resolver': '/resources/lib/channels/fr/weo:get_live_url',
        'label': 'Wéo TV',
        'thumb': 'channels/fr/weo.png',
        'fanart': 'channels/fr/weo_fanart.jpg',
        'm3u_group': 'Région',
        'enabled': True,
        'order': 62
    },
    'luckyjack': {
        'resolver': '/resources/lib/channels/fr/abweb:get_live_url',
        'label': 'Lucky Jack',
        'thumb': 'channels/fr/luckyjack.png',
        'fanart': 'channels/fr/luckyjack_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': False,
        'order': 63
    },
    'mb': {
        'resolver': '/resources/lib/channels/fr/6play:get_live_url',
        'label': 'M6 Boutique',
        'thumb': 'channels/fr/mb.png',
        'fanart': 'channels/fr/mb_fanart.jpg',
        'xmltv_id': 'C184.api.telerama.fr',
        'm3u_group': 'Satellite/FAI',
        'enabled': False,
        'order': 64
    },
    'BFM Business': {
        'resolver': '/resources/lib/channels/fr/bfmtv:get_live_url',
        'label': 'BFM Business',
        'thumb': 'channels/fr/bfmbusiness.png',
        'fanart': 'channels/fr/bfmbusiness_fanart.jpg',
        'xmltv_id': 'C1073.api.telerama.fr',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 65
    },
    'BFM2': {
        'resolver': '/resources/lib/channels/fr/bfmtv:get_live_url',
        'label': 'BFM2',
        'thumb': 'channels/fr/bfm2.png',
        'fanart': 'channels/fr/bfm2_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 66
    },
    'bsmart': {
        'resolver': '/resources/lib/channels/fr/bsmart:get_live_url',
        'label': 'B Smart',
        'thumb': 'channels/fr/bsmart.png',
        'fanart': 'channels/fr/bsmart_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 67
    },
    'TECH & CO': {
        'resolver': '/resources/lib/channels/fr/rmcbfmplay:get_live_url',
        'label': 'TECH & CO',
        'thumb': 'channels/fr/01net.png',
        'fanart': 'channels/fr/01net_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 68
    },
    'kto': {
        'resolver': '/resources/lib/channels/fr/kto:get_live_url',
        'label': 'KTO',
        'thumb': 'channels/fr/kto.png',
        'fanart': 'channels/fr/kto_fanart.jpg',
        'xmltv_id': 'C110.api.telerama.fr',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 69
    },
    'europe1': {
        'resolver': '/resources/lib/channels/fr/europe1:get_live_url',
        'label': 'Europe 1',
        'thumb': 'channels/fr/europe1.png',
        'fanart': 'channels/fr/europe1_fanart.jpg',
        'm3u_group': 'Radio',
        'enabled': True,
        'order': 70
    },
    'franceinter': {
        'resolver': '/resources/lib/channels/fr/franceinter:get_live_url',
        'label': 'France Inter',
        'thumb': 'channels/fr/franceinter.png',
        'fanart': 'channels/fr/franceinter_fanart.jpg',
        'm3u_group': 'Radio',
        'enabled': True,
        'order': 71
    },
    'funradio': {
        'resolver': '/resources/lib/channels/fr/rtl:get_live_url',
        'label': 'Fun Radio',
        'thumb': 'channels/fr/funradio.png',
        'fanart': 'channels/fr/funradio_fanart.jpg',
        'm3u_group': 'Radio',
        'enabled': True,
        'order': 72
    },
    'rtl': {
        'resolver': '/resources/lib/channels/fr/rtl:get_live_url',
        'label': 'RTL',
        'thumb': 'channels/fr/rtl.png',
        'fanart': 'channels/fr/rtl_fanart.jpg',
        'm3u_group': 'Radio',
        'enabled': True,
        'order': 73
    },
    'rtl2': {
        'resolver': '/resources/lib/channels/fr/rtl:get_live_url',
        'label': 'RTL 2',
        'thumb': 'channels/fr/rtl2.png',
        'fanart': 'channels/fr/rtl2_fanart.jpg',
        'm3u_group': 'Radio',
        'enabled': True,
        'order': 74
    },
    'sudradio': {
        'resolver': '/resources/lib/channels/fr/sudradio:get_live_url',
        'label': 'Sud Radio',
        'thumb': 'channels/fr/sudradio.png',
        'fanart': 'channels/fr/sudradio_fanart.jpg',
        'm3u_group': 'Radio',
        'enabled': True,
        'order': 75
    },
    'sportenfrance': {
        'resolver': '/resources/lib/channels/fr/sportenfrance:get_live_url',
        'label': 'Sport en France',
        'thumb': 'channels/fr/sportenfrance.png',
        'fanart': 'channels/fr/sportenfrance_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 76
    },
    'lequipelive': {
        'route': '/resources/lib/channels/fr/lequipe:get_multi_live_url',
        'label': 'L\'Equipe Live',
        'thumb': 'channels/fr/lequipelive.png',
        'fanart': 'channels/fr/lequipelive_fanart.png',
        'm3u_group': 'TNT',
        'enabled': True,
        'order': 77
    },
    'equidia-live2': {
        'resolver': '/resources/lib/channels/fr/equidia:get_live_url',
        'label': 'Equidia',
        'thumb': 'channels/fr/equidia.png',
        'fanart': 'channels/fr/equidia_fanart.jpg',
        'xmltv_id': 'C64.api.telerama.fr',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 78
    },
    'equidia-racingtrot': {
        'resolver': '/resources/lib/channels/fr/equidia:get_live_url',
        'label': 'Equidia Racing Trot',
        'thumb': 'channels/fr/equidiaracingtrot.png',
        'fanart': 'channels/fr/equidiaracingtrot_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 79
    },
    'equidia-racingmag': {
        'resolver': '/resources/lib/channels/fr/equidia:get_live_url',
        'label': 'Equidia Racing Mag',
        'thumb': 'channels/fr/equidiaracingmag.png',
        'fanart': 'channels/fr/equidiaracingmag_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 80
    },
    'equidia-racinggalop': {
        'resolver': '/resources/lib/channels/fr/equidia:get_live_url',
        'label': 'Equidia Racing Galop',
        'thumb': 'channels/fr/equidiaracinggalop.png',
        'fanart': 'channels/fr/equidiaracinggalop_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'enabled': True,
        'order': 81
    },
    'equidia-racing': {
        'resolver': '/resources/lib/channels/fr/equidia:get_live_url',
        'label': 'Equidia Racing',
        'thumb': 'channels/fr/equidiar.png',
        'fanart': 'channels/fr/equidiar_fanart.jpg',
        'm3u_group': 'Satellite/FAI',
        'available_languages': {
            "1": {},
            "2": {},
            "3": {},
            "4": {},
            "5": {},
            "6": {},
            "7": {},
            "8": {},
        },
        'enabled': True,
        'order': 82
    },
    'paris-h24': {
        'resolver': '/resources/lib/channels/fr/francetv:get_live_url',
        'label': 'France TV Paris 2024',
        'thumb': 'channels/fr/paris_h24.png',
        'fanart': 'channels/fr/paris_h24_fanart.jpg',
        'enabled': True,
        'order': 83
    }
}
