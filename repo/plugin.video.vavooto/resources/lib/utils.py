# -*- coding: utf-8 -*-
import xbmcgui, xbmcaddon, sys, xbmc, os, time, json, xbmcplugin
PY2 = sys.version_info[0] == 2
if PY2:
	from urlparse import urlparse, parse_qsl, quote_plus
	from urllib import urlencode
	translatePath = xbmc.translatePath
else:
	from urllib.parse import urlencode, urlparse, parse_qsl, quote_plus
	import xbmcvfs
	translatePath = xbmcvfs.translatePath

def py2dec(msg):
	if PY2:
		return msg.decode("utf-8")
	return msg

addon = xbmcaddon.Addon()
addonInfo = addon.getAddonInfo
addonID = addonInfo('id')
addonprofile = py2dec(translatePath(addonInfo('profile')))
addonpath = py2dec(translatePath(addonInfo('path')))
cachepath = os.path.join(addonprofile, "cache")
if not os.path.exists(cachepath):
	os.makedirs(cachepath)

def selectDialog(list, heading=None, multiselect = False):
	if heading == 'default' or heading is None: heading = addonInfo('name')
	if multiselect:
		return xbmcgui.Dialog().multiselect(str(heading), list)
	return xbmcgui.Dialog().select(str(heading), list)

home = xbmcgui.Window(10000)

def set_cache(key, value, timeout=300):
	data={"sigValidUntil": int(time.time()) +timeout,"value": value}
	home.setProperty(key, json.dumps(data))
	file = os.path.join(cachepath, key)
	with open(file+".json", "w") as k:
		json.dump(data, k, indent=4)
	
def get_cache(key):
	keyfile = home.getProperty(key)
	if keyfile:
		r = json.loads(keyfile)
		if r.get('sigValidUntil', 0) > int(time.time()):
			return r.get('value')
		home.clearProperty(key)
	try:
		file = os.path.join(cachepath, key)
		with open(file+".json") as k:
			r = json.load(k)
		sigValidUntil = r.get('sigValidUntil', 0) 
		if sigValidUntil > int(time.time()):
			value = r.get('value')
			data={"sigValidUntil": sigValidUntil,"value": value}
			home.setProperty(key, json.dumps(data))
			return value
		os.remove(file)
	except:
		return

def getAuthSignature():
	signfile = get_cache('signfile')
	if signfile: return signfile
	vec = {"vec": "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"}
	url = 'https://www.vavoo.tv/api/box/ping2'
	import requests
	req = requests.post(url, data=vec).json()
	if req.get('signed'):
		signed = req['signed']
	elif req.get('data', {}).get('signed'):
		signed = req['data']['signed']
	else:
		signed = ""
	set_cache('signfile', signed)
	return signed

def getWatchedSig():
	watchedsignfile = get_cache('watchedsignfile')
	if watchedsignfile: return watchedsignfile
	import requests
	_data={"x":"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"}
	_headers={"user-agent": "Rokkr/1.8.3 (android)", "accept": "application/json", "content-type": "application/json; charset=utf-8", "content-length": "2408", "accept-encoding": "gzip", "cookie": "lng=en"}
	r = requests.post('https://www.rokkr.net/api/box/ping', json=_data, headers=_headers).json()['response']
	signed = r['signed']
	set_cache('watchedsignfile', signed)
	return signed

def log(*args):
	msg=""
	for arg in args:
		msg += repr(arg)
	xbmc.log(msg, xbmc.LOGINFO)

def yesno(heading, line1, line2='', line3='', nolabel='', yeslabel=''):
	if PY2: return xbmcgui.Dialog().yesno(heading, line1,line2,line3, nolabel, yeslabel)
	else: return xbmcgui.Dialog().yesno(heading, line1+"\n"+line2+"\n"+line3, nolabel, yeslabel)
	
def ok(heading, line1, line2='', line3=''):
	if PY2: return xbmcgui.Dialog().ok(heading, line1,line2,line3)
	else: return xbmcgui.Dialog().ok(heading, line1+"\n"+line2+"\n"+line3)

def getIcon(name):
	if os.path.exists("%s/resources/art/%s.png" % (addonpath ,name)):return "%s/resources/art/%s.png" % (addonpath ,name)
	else: return  name

def end(succeeded=True, cacheToDisc=True):
	return xbmcplugin.endOfDirectory(int(sys.argv[1]), succeeded=succeeded, cacheToDisc=cacheToDisc)
	
def add(params, o, isFolder=False):
	return xbmcplugin.addDirectoryItem(int(sys.argv[1]), url_for(params), o, isFolder)

def set_category(cat):
	xbmcplugin.setPluginCategory(int(sys.argv[1]), cat)


def set_content(cont):
	xbmcplugin.setContent(int(sys.argv[1]), cont)
	
def set_resolved(item):
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, item)

def sort_method():
	xbmcplugin.addSortMethod(int(sys.argv[1]), xbmcplugin.SORT_METHOD_VIDEO_TITLE)

def url_for(params):
	return "%s?%s" % (sys.argv[0], urlencode(params))
	