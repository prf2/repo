# Module: default
# Author: Rayflix, noway
# Created on: 19.01.2022
import xbmcplugin
from urllib.parse import quote_plus, unquote_plus, parse_qsl
import xbmc
import xbmcvfs
import xbmcaddon
import xbmcgui
import xbmcplugin
from io import BytesIO
from urllib.request import urlopen
from zipfile import ZipFile
import os
import shutil
import requests
import random
import re

artworkPath = xbmcvfs.translatePath('special://home/addons/plugin.program.skinrayflix/resources/media/')
fanart = artworkPath + "fanart.jpg"

def notice(content):
    log(content, xbmc.LOGINFO)

def log(msg, level=xbmc.LOGINFO):
    addon = xbmcaddon.Addon()
    addonID = addon.getAddonInfo('id')
    xbmc.log('%s: %s' % (addonID, msg), level)

def showErrorNotification(message):
    xbmcgui.Dialog().notification("UptoRay", message,
                                  xbmcgui.NOTIFICATION_ERROR, 5000)
def showInfoNotification(message):
    xbmcgui.Dialog().notification("UptoRay", message, xbmcgui.NOTIFICATION_INFO, 15000)

def add_dir(name, mode, thumb):
    u = sys.argv[0] + "?" + "action=" + str(mode)
    liz = xbmcgui.ListItem(name)
    liz.setArt({'icon': thumb})
    liz.setProperty("fanart_image", fanart)
    ok = xbmcplugin.addDirectoryItem(handle=int(sys.argv[1]), url=u, listitem=liz, isFolder=True)
    return ok

##############################################

# MENU PRINCIPAL
def main_menu():
    xbmcplugin.setPluginCategory(__handle__, "Choix UptoRay")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("1 Modifier option addons en un clic", 'alloptions', artworkPath + 'icone.png')
    add_dir("2 [COLOR red]vstream[/COLOR] SKIN LIGHT [COLOR deepskyblue](le + leger)[/COLOR]", 'hk2lite', artworkPath + 'icone.png')
    add_dir("Installation - Modifier les options", 'modif_option', artworkPath + 'icone.png')
    add_dir("Mettre a jour les icones", 'au_maj', artworkPath + 'icone.png')   
    add_dir("Sauvegarde et restauration", 'save_restor', artworkPath + 'icone.png')
    add_dir("Mise a Jour Database HK2", 'menumajhk2', artworkPath + 'icone.png')
    add_dir("[COLOR red]NETTOYER KODI[/COLOR]", 'nettoye', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)

##############################################

# METTRE A JOUR LES ICONES
def au_maj():
    # mise a jour icone aura
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/au_maj.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('special://home/temp/temp/'))
    # copie des fichiers extraie
    source_dir = xbmcvfs.translatePath('special://home/temp/temp/addon_data')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data')
    source_dir2 = xbmcvfs.translatePath('special://home/temp/temp/addons')
    destination_dir2 = xbmcvfs.translatePath('special://home/addons')
    source_dir3 = xbmcvfs.translatePath('special://home/temp/temp/keymaps')
    destination_dir3 = xbmcvfs.translatePath('special://masterprofile/keymaps')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir2, destination_dir2, dirs_exist_ok=True)
    shutil.copytree(source_dir3, destination_dir3, dirs_exist_ok=True)
    xbmc.executebuiltin("Notification(EXTRACTION OK,Mise à jour effectuée !)")
    xbmc.sleep(2000)

##############################################

# MODIFIER LES OPTIONS
def modif_option():
    #Menu
    xbmcplugin.setPluginCategory(__handle__, "Modifier les options")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("Telecharger Kodi", 'dl_kodi', artworkPath + 'icone.png') 
    add_dir("Mettre a jour les icones", 'au_maj', artworkPath + 'icone.png')   
    add_dir("Modifier option addons en un clic", 'alloptions', artworkPath + 'icone.png')
    add_dir("Ajouter Compte CatchupTv", 'ajout_cpt_ctv', artworkPath + 'icone.png')
    add_dir("Choisir le skin vstream", 'hk2lite', artworkPath + 'icone.png')
    add_dir("Nettoyer Kodi", 'vider_cache', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)

def dl_kodi():
    #Telecharger Kodi
    xbmcplugin.setPluginCategory(__handle__, "Telecharger Kodi")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("Kodi 20.2 v7 pour Firestick", 'kodi_fire', artworkPath + 'icone.png') 
    add_dir("Kodi 20.2 v8 pour Shield et Autre box", 'kodi_box', artworkPath + 'icone.png') 
    add_dir("Kodi 20.2 v7 pour Autre box", 'kodi_box2', artworkPath + 'icone.png') 
    add_dir("[COLOR deepskyblue]Bonus[/COLOR] Telecharger application pour Firestick", 'apk_atv', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]Bonus[/COLOR] Telecharger application pour Autre box", 'apk_aut', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)

def kodi_fire():
    # kodi 20.2 pour firestick
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/kodi-20.2-Nexus-armeabi-v7a.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def kodi_box():
    # kodi 20.2 pour autre box
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/kodi-20.2-Nexus-arm64-v8a.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Download'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def kodi_box2():
    # kodi 20.2 pour autre box
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/kodi-20.2-Nexus-arm64-v7a2.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Download'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_atv():
    #menu telecharger application
    xbmcplugin.setPluginCategory(__handle__, "Bonus Telecharger application pour Firestick")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("Smartube Next (youtube MOD)", 'apk_smartube', artworkPath + 'icone.png')
    add_dir("Spotify version MOD", 'apk_spotify_atv', artworkPath + 'icone.png')
    add_dir("Deezer version MOD", 'apk_deezer_atv', artworkPath + 'icone.png')
    add_dir("Launcher Manager", 'apk_launcher_manager', artworkPath + 'icone.png')
    add_dir("Wolf Launcher", 'apk_wolf_launcher', artworkPath + 'icone.png')
    add_dir("Launch on Boot", 'apk_launchonboot', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)

def apk_smartube():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/apk_smartube.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_spotify_atv():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/apk_spotify_atv.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_deezer_atv():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/apk_deezer_atv.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_launcher_manager():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/apk_launcher_manager.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_wolf_launcher():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/apk_wolf_launcher.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_launchonboot():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/apk_launchonboot.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Android/data/io.github.visnkmr.wirelessexplorer'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def apk_aut():
    #menu telecharger application
    xbmcplugin.setPluginCategory(__handle__, "Bonus Telecharger application pour Autre box")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("Smartube Next (youtube MOD)", 'aut_smartube', artworkPath + 'icone.png')
    add_dir("Spotify version MOD", 'aut_spotify', artworkPath + 'icone.png')
    add_dir("Deezer version MOD", 'aut_deezer', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)

def aut_smartube():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/aut_smartube.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Download'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def aut_spotify():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/aut_spotify.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Download'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def aut_deezer():
    # telechargement et extraction du zip
    zipurl = 'https://github.com/prf2/repo/raw/main/aut_deezer.zip'
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('/storage/emulated/0/Download'))
    xbmc.executebuiltin("Notification(EXTRACTION OK,vous pouvez installer !)")
    xbmc.sleep(2000)

def alloptions():
    addon = xbmcaddon.Addon("plugin.video.sendtokodiU2P")
    ochk1 = "false"
    addon.setSetting(id="ochk1", value=ochk1)
    nb_items = "50"
    addon.setSetting(id="nb_items", value=nb_items)
    thumbnails = "2500"
    addon.setSetting(id="thumbnails", value=thumbnails)
    images_sizes = "Basse"
    addon.setSetting(id="images_sizes", value=images_sizes)
    actifnewpaste = "false"
    addon.setSetting(id="actifnewpaste", value=actifnewpaste)
    iptv = "true"
    addon.setSetting(id="iptv", value=iptv)

    showInfoNotification("Toutes les options activé")

# AJOUTER COMPTES CATCHUP TV
def ajout_cpt_ctv():
    addon = xbmcaddon.Addon("plugin.video.catchuptvandmore")
    mail = "rayflix@gmx.fr"
    mot2passe = "Mot2passe"
    addon.setSetting(id="nrj.login", value=mail)
    addon.setSetting(id="mytf1.login", value=mail)
    addon.setSetting(id="6play.login", value=mail)
    addon.setSetting(id="rmcbfmplay.login", value=mail)
    addon.setSetting(id="nrj.password", value=mot2passe)
    addon.setSetting(id="mytf1.password", value=mot2passe)
    addon.setSetting(id="6play.password", value=mot2passe)
    addon.setSetting(id="rmcbfmplay.password", value=mot2passe)

    showInfoNotification("Config Comptes ok")

##############################################

# IMPORT CHOIX SKIN
def importSkin(zipurl):
    # suppression dossier temporaire
    xbmc.executebuiltin("Notification(DOSSIER TEMP,Effacement en cours...)")
    dirPath = xbmcvfs.translatePath('special://home/temp/temp/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    # telechargement et extraction du zip
    with urlopen(zipurl) as zipresp:
        with ZipFile(BytesIO(zipresp.read())) as zfile:
            zfile.extractall(xbmcvfs.translatePath('special://home/temp/temp/'))
    # copie des fichiers extraie
    source_dir = xbmcvfs.translatePath('special://home/temp/temp/addon_data')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data')
    source_dir2 = xbmcvfs.translatePath('special://home/temp/temp/addons/skin.project.aura')
    destination_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir2, destination_dir2, dirs_exist_ok=True)
    xbmc.executebuiltin("Notification(COPIE SKIN OK,Faites retour et profitez !)")
    xbmc.sleep(2000)

##############################################

# MENU SAUVEGARDE RESTAURATION
def save_restor():
    #menu sauvegarde restauration
    xbmcplugin.setPluginCategory(__handle__, "Sauvegarde et restauration")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("[COLOR deepskyblue]1 CREER UNE SAUVEGARDE : [/COLOR]", 'skin_save1', artworkPath + 'icone.png')
    add_dir("Emplacement 1", 'skin_save1', artworkPath + 'icone.png')
    add_dir("Emplacement 2", 'skin_save2', artworkPath + 'icone.png')
    add_dir("Emplacement 3", 'skin_save3', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]2 RESTAURER UNE SAUVEGARDE : [/COLOR]", 'skin_restor1', artworkPath + 'icone.png')
    add_dir("Emplacement 1", 'skin_restor1', artworkPath + 'icone.png')
    add_dir("Emplacement 2", 'skin_restor2', artworkPath + 'icone.png')
    add_dir("Emplacement 3", 'skin_restor3', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)  

##############################################

# SAUVEGARDE
def skin_save1():
    xbmc.executebuiltin("Notification(PREPARATION DES FICHIERS,Copie en cours...)")
    # COPIE DES DOSSIERS ET FICHIERS DU SKIN
    source_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/skin.project.aura')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/1/addon_data/skin.project.aura')
    source_dir1 = xbmcvfs.translatePath('special://masterprofile/addon_data/script.skinshortcuts')
    destination_dir1 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/1/addon_data/script.skinshortcuts')
    source_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura/1080i/script-skinshortcuts-includes.xml')
    destination_dir2 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/1/addons/skin.project.aura/1080i/script-skinshortcuts-includes.xml')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir1, destination_dir1, dirs_exist_ok=True)
    shutil.copy(source_dir2, destination_dir2)
    # CREATION ARCHIVE ZIP
    shutil.make_archive((xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/Skin_save1')),'zip',(xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/1')))
    xbmc.executebuiltin("Notification(SKIN SAUVEGARDE, Archive ZIP créée !)")
    sys.exit()

def skin_save2():
    xbmc.executebuiltin("Notification(PREPARATION DES FICHIERS,Copie en cours...)")
    # COPIE DES DOSSIERS ET FICHIERS DU SKIN
    source_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/skin.project.aura')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/2/addon_data/skin.project.aura')
    source_dir1 = xbmcvfs.translatePath('special://masterprofile/addon_data/script.skinshortcuts')
    destination_dir1 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/2/addon_data/script.skinshortcuts')
    source_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura/1080i/script-skinshortcuts-includes.xml')
    destination_dir2 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/2/addons/skin.project.aura/1080i/script-skinshortcuts-includes.xml')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir1, destination_dir1, dirs_exist_ok=True)
    shutil.copy(source_dir2, destination_dir2)
    # CREATION ARCHIVE ZIP
    shutil.make_archive((xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/Skin_save1')),'zip',(xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/2')))
    xbmc.executebuiltin("Notification(SKIN SAUVEGARDE, Archive ZIP créée !)")
    sys.exit()

def skin_save3():
    xbmc.executebuiltin("Notification(PREPARATION DES FICHIERS,Copie en cours...)")
    # COPIE DES DOSSIERS ET FICHIERS DU SKIN
    source_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/skin.project.aura')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/3/addon_data/skin.project.aura')
    source_dir1 = xbmcvfs.translatePath('special://masterprofile/addon_data/script.skinshortcuts')
    destination_dir1 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/3/addon_data/script.skinshortcuts')
    source_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura/1080i/script-skinshortcuts-includes.xml')
    destination_dir2 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/3/addons/skin.project.aura/1080i/script-skinshortcuts-includes.xml')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir1, destination_dir1, dirs_exist_ok=True)
    shutil.copy(source_dir2, destination_dir2)
    # CREATION ARCHIVE ZIP
    shutil.make_archive((xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/Skin_save1')),'zip',(xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/3')))
    xbmc.executebuiltin("Notification(SKIN SAUVEGARDE, Archive ZIP créée !)")
    sys.exit()

##############################################

# RESTAURATION
def skin_restor1():
    # copie des fichiers sauvegarde
    source_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/1/addon_data')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data')
    source_dir2 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/1/addons/skin.project.aura')
    destination_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir2, destination_dir2, dirs_exist_ok=True)
    xbmc.executebuiltin("Notification(COPIE OK,Mise à jour effectuée !)")
    xbmc.sleep(5000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(ACTUALISATION DU SKIN, Skin Save 1...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')
    sys.exit()

def skin_restor2():
    # copie des fichiers sauvegarde
    source_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/2/addon_data')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data')
    source_dir2 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/2/addons/skin.project.aura')
    destination_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir2, destination_dir2, dirs_exist_ok=True)
    xbmc.executebuiltin("Notification(COPIE OK,Mise à jour effectuée !)")
    xbmc.sleep(5000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(ACTUALISATION DU SKIN, Skin Save 2...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')
    sys.exit()

def skin_restor3():
    # copie des fichiers sauvegarde
    source_dir = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/3/addon_data')
    destination_dir = xbmcvfs.translatePath('special://masterprofile/addon_data')
    source_dir2 = xbmcvfs.translatePath('special://masterprofile/addon_data/Scripts/Skin_save/3/addons/skin.project.aura')
    destination_dir2 = xbmcvfs.translatePath('special://home/addons/skin.project.aura')
    shutil.copytree(source_dir, destination_dir, dirs_exist_ok=True)
    shutil.copytree(source_dir2, destination_dir2, dirs_exist_ok=True)
    xbmc.executebuiltin("Notification(COPIE OK,Mise à jour effectuée !)")
    xbmc.sleep(5000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(ACTUALISATION DU SKIN, Skin Save 3...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')
    sys.exit()

##############################################

# MENU MAJ DATABASE
def menumajhk2():
    # menu maj
    xbmcplugin.setPluginCategory(__handle__, "Mise a Jour Database HK2")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("Modifier les options", 'modif_option', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]Actualiser Skin[/COLOR]", 'actuskin', artworkPath + 'icone.png')
    add_dir("--- [COLOR green]Clic ci dessous pour changer de skin[/COLOR] ---", 'hk2lite', artworkPath + 'icone.png')
    add_dir("SKIN Catchup TV [COLOR deepskyblue](new)[/COLOR]", 'ct_full', artworkPath + 'icone.png')
    add_dir("SKIN Vstream LIGHT [COLOR deepskyblue](le + leger)[/COLOR]", 'hk2lite', artworkPath + 'icone.png')
    add_dir("[COLOR red]NETTOYER KODI[/COLOR]", 'nettoye', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)  

def actuskin():
    # actualiser 
    xbmc.executebuiltin("Notification(actualisation OK,Faites retour !)")
    xbmc.sleep(1000)
    xbmc.executebuiltin('ReloadSkin')

##############################################

# MENU NETTOYAGE
def nettoye():
    #menu nettoyage
    xbmcplugin.setPluginCategory(__handle__, "NETTOYER KODI")
    xbmcplugin.setContent(__handle__, 'files')
    add_dir("[COLOR red]NETTOYER TOUT D'UN COUP : [/COLOR]clic ici", 'vider_cache', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]Vider Cache uniquement[/COLOR]", 'cache_seul', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]Vider Tmp uniquement[/COLOR]", 'tmp_seul', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]Vider Packages uniquement[/COLOR]", 'package_seul', artworkPath + 'icone.png')
    add_dir("[COLOR deepskyblue]Vider Thumbnails uniquement[/COLOR]", 'thumb_seul', artworkPath + 'icone.png')
    xbmcplugin.endOfDirectory(handle=__handle__, succeeded=True)  

##############################################

# NETTOYER TOUT D UN COUP
def vider_cache():
    #nettoyer tout
    xbmc.executebuiltin("Notification(FICHIER TEMP,Effacement en cours...)")
    # suppression dossier temporaire
    dirPath = xbmcvfs.translatePath('special://home/temp/temp/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    xbmc.executebuiltin("Notification(DOSSIER PACKAGES,Effacement en cours...)")
    # suppression dossier packages
    dirPath = xbmcvfs.translatePath('special://home/addons/packages/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    xbmc.executebuiltin("Notification(DOSSIER THUMBNAILS,Effacement en cours...)")
    # suppression dossier thumbnails
    dirPath = xbmcvfs.translatePath('special://masterprofile/Thumbnails/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    xbmc.executebuiltin("Notification(CACHE TEMP,Effacement en cours...)")
    # suppression dossier cache
    dirPath = xbmcvfs.translatePath('special://cache/temp/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(ATTENTION KODI VA SE FERMER , Relancez le...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')
    xbmc.sleep(2000)
    xbmc.executebuiltin('Quit')

##############################################

# VIDER CACHE
def cache_seul():
    #nettoyaer cache uniquement
    xbmc.executebuiltin("Notification(CACHE TEMP,Effacement en cours...)")
    # suppression dossier cache
    dirPath = xbmcvfs.translatePath('special://cache/temp/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(TERMINE , ...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')

##############################################

# VIDER TMP
def tmp_seul():
    #nettoyaer tmp uniquement
    xbmc.executebuiltin("Notification(FICHIER TEMP,Effacement en cours...)")
    # suppression dossier temporaire
    dirPath = xbmcvfs.translatePath('special://home/temp/temp/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    xbmc.executebuiltin("Notification(TERMINE , ...)")
    # actualisation du skin
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')

##############################################

# VIDER PACKAGES    
def package_seul():
    #nettoyaer packages uniquement
    xbmc.executebuiltin("Notification(DOSSIER PACKAGES,Effacement en cours...)")
    # suppression dossier packages
    dirPath = xbmcvfs.translatePath('special://home/addons/packages/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(TERMINE , ...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')

##############################################

# VIDER THUMBNAILS
def thumb_seul():
    #nettoyaer thumbnails uniquement
    xbmc.executebuiltin("Notification(DOSSIER THUMBNAILS,Effacement en cours...)")
    # suppression dossier thumbnails
    dirPath = xbmcvfs.translatePath('special://masterprofile/Thumbnails/')
    try:
       shutil.rmtree(dirPath)
    except:
       print('Error while deleting directory')
    xbmc.sleep(1000)
    # actualisation du skin
    xbmc.executebuiltin("Notification(ATTENTION KODI VA SE FERMER , Relancez le...)")
    xbmc.sleep(2000)
    xbmc.executebuiltin('ReloadSkin')
    xbmc.sleep(2000)
    xbmc.executebuiltin('Quit')

##############################################

def router(paramstring):
    params = dict(parse_qsl(paramstring))    
    dictActions = {
        #menu option
        'modif_option':(modif_option, ""),
        'alloptions':(alloptions, ""),
        'ajout_cpt_ctv': (ajout_cpt_ctv, ""),
        #telecharger kodi
        'dl_kodi':(dl_kodi, ""),
        'kodi_fire':(kodi_fire, ""),
        'kodi_box':(kodi_box, ""),
        'kodi_box2':(kodi_box2, ""),
        #bonus telecharger apk
        'apk_atv': (apk_atv, ""),
        'apk_smartube': (apk_smartube, ""),
        'apk_spotify_atv': (apk_spotify_atv, ""),
        'apk_deezer_atv': (apk_deezer_atv, ""),
        'apk_launcher_manager': (apk_launcher_manager, ""),
        'apk_wolf_launcher': (apk_wolf_launcher, ""),
        'apk_launchonboot': (apk_launchonboot, ""),
		'apk_aut': (apk_aut, ""),
        'aut_smartube': (aut_smartube, ""),
        'aut_spotify': (aut_spotify, ""),
        'aut_deezer': (aut_deezer, ""),
        #skin
        'hk2lite': (importSkin, 'http://kodi.prf2.ovh/pack/hk2_light.zip'),
        'hk2full': (importSkin, 'http://kodi.prf2.ovh/pack/hk2_full.zip'),
        'hk2kids': (importSkin, 'http://kodi.prf2.ovh/pack/hk2_kids.zip'),
        'hk2retro': (importSkin, 'http://kodi.prf2.ovh/pack/hk2_retro.zip'),
        'ct_full': (importSkin, 'http://kodi.prf2.ovh/pack/ct_full.zip'),    
        #maj hk2
        "menumajhk2": (menumajhk2, ""),
        "actuskin": (actuskin, ""),
        #nettoyage
        'vider_cache': (vider_cache, ""),
        'cache_seul': (cache_seul, ""),
        'tmp_seul': (tmp_seul, ""),
        'package_seul': (package_seul, ""),
        'thumb_seul': (thumb_seul, ""),
        'nettoye': (nettoye, ""),
        #sauvegarde restauration
        'save_restor': (save_restor, ""),
        'skin_save1': (skin_save1, ""), 
        'skin_save2': (skin_save2, ""), 
        'skin_save3': (skin_save3, ""), 
        'skin_restor1': (skin_restor1, ""), 
        'skin_restor2': (skin_restor2, ""), 
        'skin_restor3': (skin_restor3, ""), 
        #autres
        'au_maj': (au_maj, ""),
                }
        
    if params:
        fn = params['action']
        if fn in dictActions.keys():
            argv = dictActions[fn][1]
            if argv:
                dictActions[fn][0](argv)
            else:
                dictActions[fn][0]()
        else:
            raise ValueError('Invalid paramstring: {0}!'.format(paramstring))
    else:
         main_menu()

if __name__ == '__main__':
    __addon__ = xbmcaddon.Addon("plugin.program.skinrayflix")
    __handle__ = int(sys.argv[1])
    router(sys.argv[2][1:])