#      Copyright (C) 2015 Justin Mills
#      
#
#  This Program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2, or (at your option)
#  any later version.
#
#  This Program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the
#  GNU General Public License for more details.
#
#  You should have received a copy of the GNU General Public License
#  along with this Program; see the file LICENSE.txt.  If not, write to
#  the Free Software Foundation, 675 Mass Ave, Cambridge, MA 02139, USA.
#  http://www.gnu.org/copyleft/gpl.html
#
import sys, os, xbmcvfs
try:import urllib.request as urlrequest
except: import urllib2 as urlrequest
try:import urllib
except:pass
from os import _exit as channelconfig
import xbmc, xbmcgui, xbmcaddon, xbmcplugin ,re, base64
import datetime
import time
try: translatePath = xbmcvfs.translatePath
except: translatePath = xbmc.translatePath
addonID = 'script.ivueguide'
addon = xbmcaddon.Addon(addonID)
SkinDir = translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'skins'))
try:ivuedirectory = base64.decodestring(b'aHR0cDovL2l2dWV0dmd1aWRlLmNvbS9pdnVlZ3VpZGVmaWxlcy8=')
except: ivuedirectory = base64.decodebytes(b'aHR0cDovL2l2dWV0dmd1aWRlLmNvbS9pdnVlZ3VpZGVmaWxlcy8=')
CatFile = translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide', 'resources', 'categories', addon.getSetting('categories.path')+'.ini'))
channelxml = addon.getAddonInfo('Path')

demand = xbmcvfs.File('special://profile/addon_data/script.ivueguide/resources/catchup.xml','rb').read()
dialog = xbmcgui.Dialog() 

TOP_SPORTS     =  ['Football', 'Boxing & UFC', 'Motorsport', 'Basketball', 'Rugby']

Football =  ['England', 'Scotland', 'Spain', 'Germany', 'France', 'Italy', 'Netherlands', 'Champions League', 'Europa League', 'MLS', 'International']
Basketball =  ['NBA Basketball', 'Other Basketball']
Rugby  =  ['Rugby League', 'Rugby Union']

England =  base64.b64decode('L3VrLWVuZ2xhbmQtYWxsLWZvb3RiYWxsLnBocA==')
Scotland =  base64.b64decode('L3VrLXNjb3RsYW5kLXByZW1pZXJzaGlwLnBocA==')
Germany = base64.b64decode('L2V1cm9wZS1nZXJtYW55LWJ1bmRlc2xpZ2ExLnBocA==')
Italy = base64.b64decode('L2V1cm9wZS1pdGFseS1zZXJpZS1hLnBocA==')
Spain = base64.b64decode('L2V1cm9wZS1zcGFpbi1sYWxpZ2EucGhw')
France = base64.b64decode('L2V1cm9wZS1mcmFuY2UtbGlndWUtMS5waHA=')
Netherlands = base64.b64decode('L2V1cm9wZS1uZXRoZXJsYW5kcy1lcmVkaXZpc2llLnBocA==')
Champions_League = base64.b64decode('L2NsdWItdWVmYS1jaGFtcGlvbnMtbGVhZ3VlLnBocA==')
Europa_League = base64.b64decode('L2NsdWItdWVmYS1ldXJvcGEtbGVhZ3VlLnBocA==')
MLS = base64.b64decode('L2FtZXJpY2FzLW1scy5waHA=')
International = base64.b64decode('L2ludGVybmF0aW9uYWwtYWxsLWZvb3RiYWxsLnBocA==')
Friendlies = base64.b64decode('L2NsdWItZnJpZW5kbHktbWF0Y2hlcy5waHA=')
Boxing_UFC = base64.b64decode('L3gtYm94aW5nLW1tYS5waHA=')
Motorsport = base64.b64decode('L3gtZm9ybXVsYTEucGhw')
NBA_Basketball = base64.b64decode('L3VzYS1uYmEtYmFza2V0YmFsbC5waHA=')
Other_Basketball = base64.b64decode('L3gtaW50ZXJuYXRpb25hbC1iYXNrZXRiYWxsLnBocA==')
Rugby_League = base64.b64decode('L3gtcnVnYnktbGVhZ3VlLnBocA==')
Rugby_Union = base64.b64decode('L3gtcnVnYnktdW5pb24ucGhw')

	#Plays a video
def playMedia(name, image, link, mediaType='Video') :
    li = xbmcgui.ListItem(label=name, iconImage=image, thumbnailImage=image, path=link)
    li.setInfo(type=mediaType, infoLabels={ "Title": name })
    xbmc.Player().play(item=link, listitem=li)

	#Displays a notification to the user
def notify(addonId, message, timeShown=5000):
    addon = xbmcaddon.Addon(addonId)
    xbmc.executebuiltin('Notification(%s, %s, %d, %s)' % (addon.getAddonInfo('name'), message, timeShown, addon.getAddonInfo('icon')))

	#Shows an error to the user and logs it
def showError(addonId, errorMessage):
    notify(addonId, errorMessage)
    xbmc.log(errorMessage, xbmc.LOGERROR)

	#Download a file url/file to save
def download_file(url,file):
    urlrequest.urlretrieve(url, file)

def channelList(channelid):
    return os.stat(channelxml+"/"+base64.b64decode(channelid).decode('utf-8')).st_size

	#Create user addon directory
def create_userdata(AddOnID):
    addon_data_dir = os.path.join(translatePath("special://userdata/addon_data" ).decode("utf-8"), AddOnID)
    if not os.path.exists(addon_data_dir):
        os.makedirs(addon_data_dir)	
		
def get_setting(addonId,setting):
	addon = xbmcaddon.Addon(addonId)
	return addon.getSetting(setting)
    
def set_setting(addonId,setting, string):
	addon = xbmcaddon.Addon(addonId)
	return addon.setSetting(setting, string)

def remove_formatting(label):
    label = re.sub(r"\[/?[BI]\]",'',label)
    label = re.sub(r"\[/?COLOR.*?\]",'',label)
    return label

def unescape(text):
    text = text.replace('&amp;',  '&')
    text = text.replace('&quot;', '"')
    text = text.replace('&apos;', '\'')
    text = text.replace('&gt;',   '>')
    text = text.replace('&lt;',   '<')
    return text
    
def getKodiVersion():
	return xbmc.getInfoLabel("System.BuildVersion").split(".")[0]

    
def fixSettings(query=None, id=addonID, get_button=False):
    try: 
        if query == None: raise Exception()
        c, f = query.split('.')
        if int(getKodiVersion()) >= 18:
            cat_focus = int(c) - 100
            list_focus = int(f) - 80
            button = 28
        else:
            cat_focus = int(c) - 100
            list_focus = int(f) - 200
            button = 10
        if get_button == True:
            return button
        else:
            xbmc.sleep(300)
            xbmc.executebuiltin('Addon.OpenSettings(%s)' % id)
            xbmc.executebuiltin('SetFocus(%i)' % cat_focus)
            xbmc.executebuiltin('SetFocus(%i)' % list_focus)
    except:
        return

def folder():
	ivuedirectcry = translatePath(os.path.join('special://profile', 'addon_data', 'script.ivueguide'))
	if not os.path.exists(ivuedirectcry):
	    os.makedirs(ivuedirectcry)
	return ivuedirectory

def calculateTime(dt):
    return time.mktime(dt.timetuple())

def percent(start_time, end_time):
    total = calculateTime(end_time) - calculateTime(start_time)
    current_time = datetime.datetime.now()
    current = calculateTime(current_time) - calculateTime(start_time)
    percentagefloat = (100.0 * current) / total
    return int(round(percentagefloat))
	
def tvtimes():
    tvtimesxml = base64.decodestring(b'aHR0cDovL2l2dWV0dmd1aWRlLmNvbS9pdnVlZ3VpZGVmaWxlcy9yYWRpby90aW1lcy50eHQ=')
    return tvtimesxml

def formatDate(timestamp, longdate=False, day=False):
    if timestamp and day == True:
        today = datetime.datetime.today()
        tomorrow = today + datetime.timedelta(days=1)
        yesterday = today - datetime.timedelta(days=1)
        if today.date() == timestamp.date():
            return 'Today'
        elif tomorrow.date() == timestamp.date():
            return 'Tomorrow'
        elif yesterday.date() == timestamp.date():
            return 'Yesterday'
        else:
            return timestamp.strftime("%A")
    elif timestamp and day == False:
        if longdate == True:
            today = datetime.datetime.today()
            tomorrow = today + datetime.timedelta(days=1)
            yesterday = today - datetime.timedelta(days=1)
            restofdate = timestamp.strftime("%d %B")
            if today.date() == timestamp.date():
                day = 'Today ' + restofdate
                return day
            elif tomorrow.date() == timestamp.date():
                day = 'Tomorrow ' + restofdate
                return day
            elif yesterday.date() == timestamp.date():
                day = 'Yesterday ' + restofdate
                return day
            else:
                return timestamp.strftime("%A %d %B")

        else:
            today = datetime.datetime.today()
            tomorrow = today + datetime.timedelta(days=1)
            yesterday = today - datetime.timedelta(days=1)
            if today.date() == timestamp.date():
                day = 'Today'
                return day
            elif tomorrow.date() == timestamp.date():
                day = 'Tomorrow'
                return day
            elif yesterday.date() == timestamp.date():
                day = 'Yesterday'
                return day
            else:
                return timestamp.strftime("%a %d %b")
    else:
        return ''


def addons(shortcut=None):
    resp = ''
    filter = []
    dialog = xbmcgui.Dialog()
    if not shortcut: 
        shortcut = ''
        resp = dialog.select('[COLOR fffea800]iVue Default Shortcuts[/COLOR]', ['BBC iPlayer', 'ITV player', 'Project D', 'Skynet', 'Covenant', 'Specto', 'Youtube', 'WolfPack', 'Supremacy', 'Picasso'])
    if resp == 0 or shortcut ==1:
        title = 'BBC iPlayer'
        image = 'special://home/addons/script.ivueguide/resources/png/bbc icon.png'
        link = 'RunAddon(plugin.video.iplayerwww)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 1 or shortcut ==2:
        title = 'ITV Player'
        image = 'special://home/addons/script.ivueguide/resources/png/itv icon.png'
        link = 'RunAddon(plugin.video.itv)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 2 or shortcut ==3:
        title = 'Genesis'
        image = 'special://home/addons/script.ivueguide/resources/png/genesis.png'
        link = 'RunAddon(plugin.video.genesis)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 3 or shortcut ==4:
        title = 'Loki'
        image = 'special://home/addons/script.ivueguide/resources/png/loki.png'
        link = 'RunAddon(plugin.video.loki)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 4 or shortcut ==5:
        title = 'Venom'
        image = 'special://home/addons/script.ivueguide/resources/png/venom.png'
        link = 'RunAddon(plugin.video.venom)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 5 or shortcut ==6:
        title = 'Radio'
        image = 'special://home/addons/script.ivueguide/resources/png/radio.png'
        link = 'RunAddon(plugin.audio.radio_de)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 6 or shortcut ==7:
        title = 'Youtube'
        image = 'special://home/addons/script.ivueguide/resources/png/youtube.png'
        link = 'RunAddon(plugin.video.youtube)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 7 or shortcut ==8:
        title = 'Rising Tides'
        image = 'special://home/addons/script.ivueguide/resources/png/rising.png'
        link = 'RunAddon(plugin.video.Rising.Tides)'
        filter.append(title)
        filter.append(image)
        filter.append(link) 
    if resp == 8 or shortcut ==9:
        title = 'The Endzone'
        image = 'special://home/addons/script.ivueguide/resources/png/endzone.png'
        link = 'RunAddon(plugin.video.endzone)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    if resp == 9 or shortcut ==10:
        title = 'The Loop'
        image = 'special://home/addons/script.ivueguide/resources/png/loop.png'
        link = 'RunAddon(plugin.video.the-loop)'
        filter.append(title)
        filter.append(image)
        filter.append(link)
    return filter