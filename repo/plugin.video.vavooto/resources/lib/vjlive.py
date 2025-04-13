# -*- coding: utf-8 -*-

# edit 2024-12-05 kasi

import sys, re, requests, time, xbmcgui, xbmc, json, os, random, time
from resources.lib import utils
from urllib.parse import urlsplit
try: 
	from infotagger.listitem import ListItemInfoTag
	tagger = True
except: tagger = False

allchannels = {}
timeout=int(utils.addon.getSetting("timeout"))

maclists = utils.get_cache("maclists")
if not maclists:
	maclists = requests.get("https://michaz1988.github.io/maclist.json").json()
	utils.set_cache("maclists", maclists, 75600)

def gettsSignature():
	vec = {"vec": "9frjpxPjxSNilxJPCJ0XGYs6scej3dW/h/VWlnKUiLSG8IP7mfyDU7NirOlld+VtCKGj03XjetfliDMhIev7wcARo+YTU8KPFuVQP9E2DVXzY2BFo1NhE6qEmPfNDnm74eyl/7iFJ0EETm6XbYyz8IKBkAqPN/Spp3PZ2ulKg3QBSDxcVN4R5zRn7OsgLJ2CNTuWkd/h451lDCp+TtTuvnAEhcQckdsydFhTZCK5IiWrrTIC/d4qDXEd+GtOP4hPdoIuCaNzYfX3lLCwFENC6RZoTBYLrcKVVgbqyQZ7DnLqfLqvf3z0FVUWx9H21liGFpByzdnoxyFkue3NzrFtkRL37xkx9ITucepSYKzUVEfyBh+/3mtzKY26VIRkJFkpf8KVcCRNrTRQn47Wuq4gC7sSwT7eHCAydKSACcUMMdpPSvbvfOmIqeBNA83osX8FPFYUMZsjvYNEE3arbFiGsQlggBKgg1V3oN+5ni3Vjc5InHg/xv476LHDFnNdAJx448ph3DoAiJjr2g4ZTNynfSxdzA68qSuJY8UjyzgDjG0RIMv2h7DlQNjkAXv4k1BrPpfOiOqH67yIarNmkPIwrIV+W9TTV/yRyE1LEgOr4DK8uW2AUtHOPA2gn6P5sgFyi68w55MZBPepddfYTQ+E1N6R/hWnMYPt/i0xSUeMPekX47iucfpFBEv9Uh9zdGiEB+0P3LVMP+q+pbBU4o1NkKyY1V8wH1Wilr0a+q87kEnQ1LWYMMBhaP9yFseGSbYwdeLsX9uR1uPaN+u4woO2g8sw9Y5ze5XMgOVpFCZaut02I5k0U4WPyN5adQjG8sAzxsI3KsV04DEVymj224iqg2Lzz53Xz9yEy+7/85ILQpJ6llCyqpHLFyHq/kJxYPhDUF755WaHJEaFRPxUqbparNX+mCE9Xzy7Q/KTgAPiRS41FHXXv+7XSPp4cy9jli0BVnYf13Xsp28OGs/D8Nl3NgEn3/eUcMN80JRdsOrV62fnBVMBNf36+LbISdvsFAFr0xyuPGmlIETcFyxJkrGZnhHAxwzsvZ+Uwf8lffBfZFPRrNv+tgeeLpatVcHLHZGeTgWWml6tIHwWUqv2TVJeMkAEL5PPS4Gtbscau5HM+FEjtGS+KClfX1CNKvgYJl7mLDEf5ZYQv5kHaoQ6RcPaR6vUNn02zpq5/X3EPIgUKF0r/0ctmoT84B2J1BKfCbctdFY9br7JSJ6DvUxyde68jB+Il6qNcQwTFj4cNErk4x719Y42NoAnnQYC2/qfL/gAhJl8TKMvBt3Bno+va8ve8E0z8yEuMLUqe8OXLce6nCa+L5LYK1aBdb60BYbMeWk1qmG6Nk9OnYLhzDyrd9iHDd7X95OM6X5wiMVZRn5ebw4askTTc50xmrg4eic2U1w1JpSEjdH/u/hXrWKSMWAxaj34uQnMuWxPZEXoVxzGyuUbroXRfkhzpqmqqqOcypjsWPdq5BOUGL/Riwjm6yMI0x9kbO8+VoQ6RYfjAbxNriZ1cQ+AW1fqEgnRWXmjt4Z1M0ygUBi8w71bDML1YG6UHeC2cJ2CCCxSrfycKQhpSdI1QIuwd2eyIpd4LgwrMiY3xNWreAF+qobNxvE7ypKTISNrz0iYIhU0aKNlcGwYd0FXIRfKVBzSBe4MRK2pGLDNO6ytoHxvJweZ8h1XG8RWc4aB5gTnB7Tjiqym4b64lRdj1DPHJnzD4aqRixpXhzYzWVDN2kONCR5i2quYbnVFN4sSfLiKeOwKX4JdmzpYixNZXjLkG14seS6KR0Wl8Itp5IMIWFpnNokjRH76RYRZAcx0jP0V5/GfNNTi5QsEU98en0SiXHQGXnROiHpRUDXTl8FmJORjwXc0AjrEMuQ2FDJDmAIlKUSLhjbIiKw3iaqp5TVyXuz0ZMYBhnqhcwqULqtFSuIKpaW8FgF8QJfP2frADf4kKZG1bQ99MrRrb2A="}
	url = 'https://www.vavoo.tv/api/box/ping2'
	req = requests.post(url, data=vec).json()
	return req['response'].get('signed')

def get_stalkerurl():
	utils.del_cache("stalker_groups")
	utils.del_cache("stalkchannels")
	a, b, c = [], [], []
	gruppen = utils.get_cache("maclists")
	for key, value in gruppen.items():
		a.append(key)
		b.append(value)
		c.append("%s, %s mac" % (urlsplit(key).hostname, len(value)))
	indicies = utils.selectDialog(c, "Stalkerurl auswählen")
	url = a[indicies]
	utils.log(url)
	utils.set_cache("stalker_url", url)
	utils.addon.setSetting("stalkerurl", url)
	utils.set_cache("maclist", b[indicies])
	return url

def get_headers():
	stalkerurl = utils.get_cache("stalker_url")
	if not stalkerurl: stalkerurl = get_stalkerurl()
	header = utils.get_cache("header")
	maclist = utils.get_cache("maclist")
	if not header:
		header = {'Accept-Encoding': 'identity',
		'Content-Type': 'application/x-www-form-urlencoded',
		'User-Agent': 'Mozilla/5.0 (QtEmbedded; U; Linux; C) AppleWebKit/533.3 (KHTML, like Gecko) MAG200 stbapp ver: 4 rev: 1812 Mobile Safari/533.3',
		'Referer': stalkerurl,
		'Accept': '*/*',
		'Connection': 'close',
		'X-User-Agent': 'Model: MAG254; Link: Ethernet'}
	post, token = True, ""
	for i in range(9):
		time.sleep(5)
		if not header.get("Authorization") or i >= 1:
			mac =random.choice(maclist)
			header["Cookie"] = "mac=%s; stb_lang=en; timezone=Europe/Berlin" % mac
			b="type=stb&action=handshake&JsHttpRequest=1-xml"
			try:
				if post:
					utils.log("versuch1")
					token = requests.post(stalkerurl, data = b, headers=header, timeout=timeout).json()["js"]["token"]
				else:
					utils.log("versuch2")
					token = requests.get(stalkerurl.replace("portal.php", "server/load.php")+"?type=stb&action=handshake", headers=header, timeout=timeout).json()["js"]["token"]
					stalkerurl = stalkerurl.replace("portal.php", "server/load.php")
					utils.set_cache("stalker_url", stalkerurl)
			except: 
				post = not post
				continue
			if not token:
				utils.log("Kein Token")
				return get_stalkerurl()
			header["Authorization"] = "Bearer "+ token
			params = {"type": "itv", "action": "get_all_channels"}
			try: 
				if post: data = requests.post(stalkerurl, params, headers=header, timeout=timeout).json()["js"]["data"]
				else: data = requests.get(stalkerurl.replace("portal.php", "server/load.php"), params, headers=header, timeout=timeout).json()["js"]["data"]
			except: data = ""
			if not data: 
				utils.log("No Data")
				continue
			cmd = data[3]
			if cmd["use_http_tmp_link"] == "0":
				streamurl = cmd['cmd'].split(" ")[-1]
			else:
				params = {"type": "itv", "action": "create_link", "cmd" : cmd['cmd'] , "forced_storage" : "undefined", "disable_ad" : "0", "JsHttpRequest" : "1-xml"}
				try:
					if post: streamurl = requests.post(stalkerurl, params=params, headers=header, timeout=timeout).json()["js"]["cmd"].split(" ")[-1]
					else: streamurl = requests.get(stalkerurl.replace("portal.php", "server/load.php"), params=params, headers=header, timeout=timeout).json()["js"]["cmd"].split(" ")[-1]
				except: streamurl = ""
			if "stream=&extension" in streamurl: streamurl = ""
			if not streamurl:
				utils.log("No Streamurl")
				continue
			else:
				utils.addon.setSetting("stalkerok", "true")
				utils.set_cache("header", header, timeout=3600)
				return header
		else:
			b="type=stb&action=handshake&JsHttpRequest=1-xml"
			try:
				if "post" in stalkerurl: token = requests.post(stalkerurl, data = b, headers=header, timeout=timeout).json()["js"]["token"]
				else: token = requests.get(stalkerurl+"?type=stb&action=handshake", headers=header, timeout=timeout).json()["js"]["token"]
			except: token = ""
			if not token:
				utils.log("Kein Token")
				continue
			header["Authorization"] = "Bearer "+ token
			utils.set_cache("header", header, timeout=3600)
			return header
	utils.addon.setSetting("stalker", "false")
	return

def get_genres():
	stalkerurl = utils.get_cache("stalker_url")
	if not stalkerurl: stalkerurl = get_stalkerurl()
	utils.del_cache("stalkchannels")
	params = {"type": "itv", "action": "get_genres"}
	if "portal" in stalkerurl:
		gruppen = requests.post(stalkerurl, params=params, headers=get_headers(),timeout=timeout).json()["js"]
	else: gruppen = requests.get(stalkerurl, params=params, headers=get_headers(),timeout=timeout).json()["js"]
	indicies =xbmcgui.Dialog().multiselect("Choose Groups", [i["title"] for i in gruppen])
	group = []
	for i in indicies: group.append(gruppen[i]["id"])
	utils.set_cache("stalker_groups", group, timeout=False)
	return group

def isNormal(myStr):
    return myStr.isascii()

def resolve_link(link):
	if not "vavoo" in link:
		stalkerurl = utils.get_cache("stalker_url")
		if not stalkerurl: stalkerurl = get_stalkerurl()
		headers = get_headers()
		params = {"type": "itv", "action": "create_link", "cmd" : link , "forced_storage" : "undefined", "disable_ad" : "0", "JsHttpRequest" : "1-xml"}
		if "post" in stalkerurl:
			streamurl = requests.post(stalkerurl, params=params, headers=headers, timeout=timeout).json()["js"]["cmd"].split(" ")[-1]
		else: streamurl = requests.get(stalkerurl, params=params, headers=headers, timeout=timeout).json()["js"]["cmd"].split(" ")[-1]
		res = requests.get(streamurl, headers=headers, stream=True)
		return res.url
	else:
		if utils.addon.getSetting("hls") == "true":
			_headers={"user-agent": "MediaHubMX/2", "accept": "application/json", "content-type": "application/json; charset=utf-8", "content-length": "115", "accept-encoding": "gzip", "mediahubmx-signature":utils.getAuthSignature()}
			_data={"language":"de","region":"AT","url":link,"clientVersion":"3.0.2"}
			url = "https://vavoo.to/vto-cluster/mediahubmx-resolve.json"
			return requests.post(url, json=_data, headers=_headers).json()[0]["url"]
		else:
			return "%s.ts?n=1&b=5&vavoo_auth=%s|User-Agent=VAVOO/2.6" % (link.replace("vavoo-iptv", "live2")[0:-12], gettsSignature())

def filterout(name):
	name = re.sub(r"\.\D", "", name).upper()
	name = re.sub(r"( (SD|HD|FHD|UHD|H265))?( \\(BACKUP\\))? \\(\\d+\\)$", "", name)
	name = re.sub(r"(DE\||DE : |DE: |CH: |DE:|DE \| |CH \| |4K \| |8K \| | \|\w| FHD| QHD| UHD| 2K| 4K| HD\+| HD| 1080| AUSTRIA| GERMANY| DEUTSCHLAND|HEVC|RAW| SD| YOU)", "", name).strip(".")
	if name.endswith(" DE"): name = name.strip(" DE")
	name = re.sub(r"\(.*\)", "", name)
	name = re.sub(r"\[.*\]", "", name)
	for r in(("EINS", "1"), ("ZWEI", "2"), ("DREI", "3"), ("SIEBEN", "7"), ("  ", " "), ("TNT", "WARNER"), ("III", "3"), ("II", "2"), ("BR TV", "BR"), ("ʜᴅ", "")): name = name.replace(*r).strip()
	if "ALLGAU" in name: name = "ALLGAU TV"
	if all(ele in name for ele in ["1", "2", "3"]): name = "1-2-3 TV"
	if "HR" in name and "FERNSEHEN" in name: name = "HR"
	elif "EURONEWS" in name: name = "EURONEWS"
	elif "NICKEL" in name: name = "NICKELODEON"
	elif "NICK" in name:
		if "TOONS" in name: name = "NICKTOONS"
		elif "J" in name: name = "NICK JUNIOR"
	elif "ORF" in name:
		if "SPORT" in name: name = "ORF SPORT"
		elif "3" in name: name = "ORF 3"
		elif "2" in name: name = "ORF 2"
		elif "1" in name: name = "ORF 1"
		elif "I" in name: name = "ORF 1"
	elif "BLACK" in name: name = "AXN BLACK"
	elif "AXN" in name or "WHITE" in name: name = "AXN WHITE"
	elif "SONY" in name: name = "AXN BLACK"
	elif "ANIXE" in name: name = "ANIXE"
	elif "HEIMA" in name: name = "HEIMATKANAL"
	elif "SIXX" in name: name = "SIXX"
	elif "SWR" in name: name = "SWR"
	elif "ALPHA" in name: name = "ARD-ALPHA"
	elif "ERSTE" in name and "DAS" in name: name = "ARD-ALPHA"
	elif "ARTE" in name: name = "ARTE"
	elif "MTV" in name: name = "MTV"
	elif "ARD" in name: name = "ARD"
	elif "PHOENIX" in name: name = "PHOENIX"
	elif "KIKA" in name: name = "KIKA"
	elif "CENTRAL" in name or "VIVA" in name: name = "COMEDY CENTRAL"
	elif "BR" in name and "FERNSEHEN" in name: name = "BR"
	elif "DMAX" in name: name = "DMAX"
	elif "DISNEY" in name: 
		if "CHANNEL" in name: name = "DISNEY CHANNEL"
		elif "J" in name: name = "DISNEY JUNIOR"
	elif "MDR" in name:	# edit kasi
		if "TH" in name: name = "MDR THUERINGEN"
		elif "ANHALT" in name: name = "MDR SACHSEN ANHALT"
		elif "SACHSEN" in name: name = "MDR SACHSEN"
		else: name = "MDR"
	elif "NDR" in name: name = "NDR"
	elif "RBB" in name: name = "RBB"
	elif "JUKEBOX" in name: name = "JUKEBOX"
	elif "SERVUS" in name: name = "SERVUS TV"
	elif "NITRO" in name: name = "RTL NITRO"
	elif "RTL" in name:
		if "SPORT" in name: name=name
		elif "CRIME" in name: name = "RTL CRIME"
		elif "SUPER" in name: name = "SUPER RTL"
		elif "UP" in name: name = "RTL UP"
		elif "+" in name or "PLUS" in name: name = "RTL UP"
		elif "PASSION" in name: name = "RTL PASSION"
		elif "LIVING" in name: name = "RTL LIVING"
		elif "2" in name: name = "RTL 2"
		else:name = "RTL"
	elif "UNIVERSAL" in name: name = "UNIVERSAL TV"
	elif "WDR" in name: name = "WDR"
	elif "ZDF" in name: 
		if "INFO" in name: name = "ZDF INFO"
		elif "NEO" in name: name = "ZDF NEO"
		else: name = "ZDF"
	elif "PLANET" in name:
		if "ANIMAL" in name: name = "ANIMAL PLANET"
		else: name = "PLANET"
	elif "SYFY" in name: name = "SYFY"
	elif "E!" in name: name = "E! ENTERTAINMENT"
	elif "ENTERTAINMENT" in name: name = "E! ENTERTAINMENT"
	elif "STREET" in name: name = "13TH STREET"
	elif "FOXI" in name: name = "FIX & FOXI"
	elif "TELE" in name and "5" in name: name = "TELE 5"
	elif "KABE" in name:
		if "CLA" in name: name = "KABEL 1 CLASSICS"
		elif "DO" in name: name = "KABEL 1 DOKU"
		else: name = "KABEL 1"
	elif "PRO" in name:
		if "FUN" in name: name = "PRO 7 FUN"
		elif "MAXX" in name: name = "PRO 7 MAXX"
		else: name = "PRO 7"
	elif "ZEE" in name: name = "ZEE ONE"
	elif "DELUX" in name: name = "DELUXE MUSIC"
	elif "DISCO" in name: name = "DISCOVERY"
	elif "TLC" in name: name = "TLC"
	elif "N-TV" in name or "NTV" in name: name = "NTV"
	elif "TAGESSCHAU" in name: name = "TAGESSCHAU 24"
	elif "EUROSPORT" in name:
		if "1" in name: name = "EUROSPORT 1"
		elif "2" in name: name = "EUROSPORT 2"
	elif "SPIEGEL" in name:
		if "GESCHICHTE" in name: name = "SPIEGEL GESCHICHTE"
		else: name = "SPIEGEL WISSEN"
	elif "HISTORY" in name: name = "HISTORY"
	elif "VISION" in name: name = "MOTORVISION"
	elif "INVESTIGATION" in name or "A&E" in name: name = "CRIME + INVESTIGATION"
	elif "AUTO" in name: name = "AUTO MOTOR SPORT"
	elif "WELT" in name:
		if "KINO" in name: name = "KINOWELT"
		elif "WUNDER" in name: name = "WELT DER WUNDER"
		else: name = "WELT"
	elif "NAT" in name and "GEO" in name: name = "NAT GEO WILD" if "WILD" in name else "NATIONAL GEOGRAPHIC"
	elif "3" in name and "SAT" in name: name = "3 SAT"
	elif "CURIOSITY" in name: name = "CURIOSITY CHANNEL"
	elif "ROMANCE" in name: name = "ROMANCE TV"
	elif "ATV" in name: 
		if "2" in name: name = "ATV 2"
		else: name = "ATV"
	elif "WARNER" in name:
		if "SERIE" in name: name = "WARNER TV SERIE"
		elif "FILM" in name: name = "WARNER TV FILM"
		elif "COMEDY" in name: name = "WARNER TV COMEDY"
	elif "VOX" in name:
		if "+" in name: name = "VOX UP"
		elif "UP" in name: name = "VOX UP"
		else: name = "VOX"
	elif "SAT" in name and "1" in name:
		if "GOLD" in name: name = "SAT 1 GOLD"
		elif "EMOT" in name: name = "SAT 1 EMOTIONS"
		else: name = "SAT 1"
	elif "SKY" in name:
		if "DO" in name: name = "SKY DOCUMENTARIES"
		elif "REPLAY" in name: name = "SKY REPLAY"
		elif "CASE" in name: name = "SKY SHOWCASE"
		elif "ATLANTIC" in name: name = "SKY ATLANTIC"
		elif "ACTION" in name: name = "SKY CINEMA ACTION"
		elif "HIGHLIGHT" in name: name = "SKY CINEMA HIGHLIGHT"
		elif "CINEMA" in name and "COMEDY" in name: name = "SKY CINEMA FUN"
		elif "COMEDY" in name: name = "SKY COMEDY"
		elif "FAMI" in name: name = "SKY CINEMA FAMILY"
		elif "SPECI" in name: name = "SKY CINEMA SPECIAL"
		elif "THRILLER" in name: name = "SKY CINEMA THRILLER"
		elif "FUN" in name: name = "SKY CINEMA FUN"
		elif "CLASS" in name: name = "SKY CINEMA CLASSICS"
		elif "NOSTALGIE" in name: name = "SKY CINEMA CLASSICS"
		elif "KRIM" in name: name = "SKY KRIMI"
		elif "CRIME" in name: name = "SKY CRIME"
		elif "NATURE" in name: name = "SKY NATURE"
		elif not any(ele in name for ele in ["BUNDES", "SPORT", "SELECT", "BOX"]):
			if "PREMIE" in name:
				name = "SKY CINEMA PREMIEREN +24" if "24" in name else "SKY CINEMA PREMIEREN"
			elif not "CINEMA" in name: 
				if "ONE" in name or "1" in name: name = "SKY ONE"
	elif "24" in name:
		if "PULS" in name: name = "PULS 24"
		elif "DO" in name: name = "N24 DOKU"
	elif "PULS" in name: name = "PULS 4"
	elif "FOX" in name: name = "SKY REPLAY"
	return name


def get_vavoo_channels():
	if utils.addon.getSetting("stalker")== "false" :
		global allchannels
		allchannels = {}
	try: groups = json.loads(utils.addon.getSetting("groups"))
	except: groups = choose()

	def _getchannels(group, filter, cursor=0):
		global allchannels
		filteron = True if utils.addon.getSetting("filter") == "true" else False
		_headers={"accept-encoding": "gzip", "user-agent":"MediaHubMX/2", "accept": "application/json", "content-type": "application/json; charset=utf-8", "mediahubmx-signature": utils.getAuthSignature()}
		_data={"language":"de","region":"AT","catalogId":"vto-iptv","id":"vto-iptv","adult":False,"search":"","sort":"name","filter":{"group":group},"cursor":cursor,"clientVersion":"3.0.2"}
		r = requests.post("https://vavoo.to/vto-cluster/mediahubmx-catalog.json", json=_data, headers=_headers).json()
		nextCursor = r.get("nextCursor")
		items = r.get("items")
		for item in items:
			if filter !=0 and "LUXEMBOURG" in item["name"]: continue
			if filter ==1:
				if any(ele in item["name"] for ele in ["DE :", " |D"]):
					name = filterout(item["name"])
					if name not in channels: channels[name] = []
					allchannels[name].append(item["url"])
			else:
				name = filterout(item["name"]) if (filter ==2 and filteron) else item["name"]
				if name not in allchannels: allchannels[name] = []
				allchannels[name].append({"url":item["url"], "tmp":"1"})
		if nextCursor: _getchannels(group, filter, nextCursor)
	if "Germany" in groups:
		_getchannels("Balkans", filter=1)
	for group in groups:
		if group == "Germany": _getchannels(group, filter=2)
		else: _getchannels(group, filter=0)

def get_stalker_channels():
	stalkerurl = utils.get_cache("stalker_url")
	if not stalkerurl: stalkerurl = get_stalkerurl()
	genres = utils.get_cache("stalker_groups")
	if not genres: genres = get_genres()
	global allchannels
	stalk_channels = utils.get_cache("stalkchannels")
	if stalk_channels: allchannels = stalk_channels
	else:
		stalk_channels = {}
		params = {"type": "itv", "action": "get_all_channels"}
		if "portal" in stalkerurl:
			data = requests.post(stalkerurl, params=params, headers=get_headers(), timeout=timeout).json()["js"]["data"]
		else: data = requests.get(stalkerurl, params=params, headers=get_headers(), timeout=timeout).json()["js"]["data"]
		for channel in data:
			if channel["tv_genre_id"] not in genres: continue
			name = filterout(channel["name"])
			if not isNormal(name): continue
			if ("====" in name) or ("###" in name) or ("*****" in name): continue
			if name not in stalk_channels: stalk_channels[name] = []
			stalk_channels[name].append({"url":channel['cmd'], "tmp":channel['use_http_tmp_link']})
		utils.set_cache("stalkchannels", stalk_channels, timeout=3600)
		allchannels = stalk_channels

def getchannels():
	if utils.addon.getSetting("stalker")== "true" :
		get_stalker_channels()
	if utils.addon.getSetting("vavoo")== "true" :
		get_vavoo_channels()
	return allchannels

def choose():
	groups=[]
	for c in requests.get("https://www2.vavoo.to/live2/index", params={"output": "json"}).json():
		if c["group"] not in groups: groups.append(c["group"])
	groups.sort()
	indicies = utils.selectDialog(groups, "Choose Groups", True)
	group = []
	if indicies:
		for i in indicies: group.append(groups[i])
		utils.addon.setSetting("groups", json.dumps(group))
		return group

def handle_wait(kanal):
	progress = xbmcgui.DialogProgress()
	create = progress.create("Abbrechen zur manuellen Auswahl", "STARTE  : %s" % kanal)
	time_to_wait = int(utils.addon.getSetting("count")) +1
	for secs in range(1, time_to_wait):
		secs_left = time_to_wait - secs
		if utils.PY2:progress.update(int(secs/time_to_wait*100),"STARTE  : %s" % kanal,"Starte Stream in  : %s" % secs_left)
		else:progress.update(int(secs/time_to_wait*100),"STARTE  : %s\nStarte Stream in  : %s" % (kanal, secs_left))
		xbmc.Monitor().waitForAbort(1)
		if (progress.iscanceled()):
			progress.close()
			return False
	progress.close()
	return True

def livePlay(name):
	m, i, title = getchannels()[name], 0, None
	if len(m) > 1:
		if utils.addon.getSetting("auto") == "0":
			# Autoplay - rotieren bei der Stream Auswahl
			# ist wichtig wenn z.B. der erste gelistete Stream nicht funzt
			if utils.addon.getSetting("idn") == name:
				i = int(utils.addon.getSetting("num")) + 1
				if i == len(m): i = 0
			utils.addon.setSetting("idn", name)
			utils.addon.setSetting("num", str(i))
			title = "%s (%s/%s)" % (name, i + 1, len(m))  # wird verwendet für infoLabels
		elif utils.addon.getSetting("auto") == "1":
			if not handle_wait(name):	# Dialog aufrufen
				cap = []
				for i, n in enumerate(m, 1):
					cap.append("STREAM %s" %i)
				i = utils.selectDialog(cap)
				if i < 0: return
			title = "%s (%s/%s)" %(name, i+1, len(m))  # wird verwendet für infoLabels
		else:
			cap=[]
			for i, n in enumerate(m, 1): cap.append("STREAM %s" %i)
			i = utils.selectDialog(cap)
			if i < 0: return
			title = "%s (%s/%s)" % (name, i + 1, len(m))  # wird verwendet für infoLabels
	n = m[i]
	o = xbmcgui.ListItem(name)
	playmode1 = True if "localhost" in n else False
	url = n["url"] if n["tmp"] == 0 else resolve_link(n["url"]) 
	utils.log("Spiele %s" % n)
	utils.log("Spiele %s" % url)
	o.setPath(url)
	if playmode1: 
		#headers = get_headers()
		if xbmc.getCondVisibility("System.HasAddon(inputstream.ffmpegdirect)"):
			#o.setMimeType("video/mp2t")
			o.setProperty("inputstream", "inputstream.ffmpegdirect")
			o.setProperty("inputstream.ffmpegdirect.is_realtime_stream", "true")
			o.setProperty("inputstream.ffmpegdirect.stream_mode", "timeshift")
			o.setProperty("inputstream.ffmpegdirect.open_mode", "curl")
			#o.setProperty('inputstream.ffmpegdirect.common_headers', headers)
			#o.setProperty('inputstream.ffmpegdirect.stream_headers', headers)
	elif utils.addon.getSetting("hls") == "true":
		o.setMimeType("application/vnd.apple.mpegurl")
		o.setProperty("inputstreamaddon" if utils.PY2 else "inputstream" , "inputstream.adaptive")
		o.setProperty("inputstream.adaptive.manifest_type", "hls")
	elif utils.addon.getSetting("ffmpeg") == "true" and xbmc.getCondVisibility("System.HasAddon(inputstream.ffmpegdirect)"):
		o.setMimeType("application/vnd.apple.mpegurl")
		o.setProperty("inputstream", "inputstream.ffmpegdirect")
		o.setProperty("inputstream.ffmpegdirect.is_realtime_stream", "true")
		o.setProperty("inputstream.ffmpegdirect.stream_mode", "timeshift")
		if utils.addon.getSetting("openmode") != "0":
			o.setProperty("inputstream.ffmpegdirect.open_mode", "ffmpeg" if  utils.addon.getSetting("openmode") == "1" else "curl")
		o.setProperty("inputstream.ffmpegdirect.manifest_type", "hls")
	o.setProperty("IsPlayable", "true")
	title = title if title else name
	infoLabels={"title": title, "plot": "[B]%s[/B] - Stream %s von %s" % (name, i+1, len(m))}
	if tagger:
		info_tag = ListItemInfoTag(o, 'video')
		info_tag.set_info(infoLabels)
	else: o.setInfo("Video", infoLabels) # so kann man die Stream Auswahl auch sehen (Info)
	utils.set_resolved(o)
	utils.end()
			
def makem3u():
	m3u = ["#EXTM3U\n"]
	for name in getchannels():
		m3u.append('#EXTINF:-1 group-title="Standart",%s\nplugin://plugin.video.vavooto/?name=%s\n' % (name.strip(), name.replace("&", "%26").replace("+", "%2b").strip()))
	m3uPath = os.path.join(utils.addonprofile, "vavoo.m3u")
	with open(m3uPath ,"w") as a:
		a.writelines(m3u)
	dialog = xbmcgui.Dialog()
	ok = dialog.ok('VAVOO.TO', 'm3u erstellt in %s' % m3uPath)
		
# edit kasi
def channels(items=None):
	try: lines = json.loads(utils.addon.getSetting("favs"))
	except: lines=[]
	if items: results = json.loads(items)
	else: results = getchannels()
	for name in results:
		name = name.strip()
		index = len(results[name])
		title = name if utils.addon.getSetting("stream_count") == "false" or index == 1 else "%s  (%s)" % (name, index)
		o = xbmcgui.ListItem(name)
		cm = []
		if not name in lines:
			cm.append(("zu TV Favoriten hinzufügen", "RunPlugin(%s?action=addTvFavorit&name=%s)" % (sys.argv[0], name.replace("&", "%26").replace("+", "%2b"))))
			plot = ""
		else:
			plot = "[COLOR gold]TV Favorit[/COLOR]" #% name
			cm.append(("von TV Favoriten entfernen", "RunPlugin(%s?action=delTvFavorit&name=%s)" % (sys.argv[0], name.replace("&", "%26").replace("+", "%2b"))))
		cm.append(("Einstellungen", "RunPlugin(%s?action=settings)" % sys.argv[0]))
		cm.append(("m3u erstellen", "RunPlugin(%s?action=makem3u)" % sys.argv[0]))
		o.addContextMenuItems(cm)
		o.setArt({'poster': 'DefaultTVShows.png', 'icon': 'DefaultTVShows.png'})
		infoLabels={"title": title, "plot": plot}
		if tagger:
			info_tag = ListItemInfoTag(o, 'video')
			info_tag.set_info(infoLabels)
		else: o.setInfo("Video", infoLabels)
		o.setProperty("IsPlayable", "true")
		utils.add({"name":name}, o)
	utils.sort_method()
	utils.end()

def favchannels():
	try: lines = json.loads(utils.addon.getSetting("favs"))
	except: return
	for name in getchannels():
		if not name in lines: continue
		o = xbmcgui.ListItem(name)
		cm = []
		cm.append(("von TV Favoriten entfernen", "RunPlugin(%s?action=delTvFavorit&name=%s)" % (sys.argv[0], name.replace("&", "%26").replace("+", "%2b"))))
		cm.append(("Einstellungen", "RunPlugin(%s?action=settings)" % sys.argv[0]))
		o.addContextMenuItems(cm)
		infoLabels={"title": name, "plot": "[COLOR gold]Liste der eigene Live Favoriten[/COLOR]"}
		if tagger:
			info_tag = ListItemInfoTag(o, 'video')
			info_tag.set_info(infoLabels)
		else: o.setInfo("Video", infoLabels)
		o.setProperty("IsPlayable", "true")
		utils.add({"name":name}, o)
	utils.sort_method()
	utils.end()

def change_favorit(name, delete=False):
	try: lines = json.loads(utils.addon.getSetting("favs"))
	except: lines= []
	if delete: lines.remove(name)
	else: lines.append(name)
	utils.addon.setSetting("favs", json.dumps(lines))
	if len(lines) == 0: xbmc.executebuiltin("Action(ParentDir)")
	else: xbmc.executebuiltin("Container.Refresh")

# edit by kasi
def live():
	from resources.lib.vjackson import addDir2
	try: lines = json.loads(utils.addon.getSetting("favs"))
	except:	lines = []
	if len(lines)>0: addDir2("Live - Favoriten", "DefaultAddonPVRClient", "favchannels")
	addDir2("Live - Alle", "DefaultAddonPVRClient", "channels")
	addDir2("Live - A bis Z", "DefaultAddonPVRClient", "a_z_tv")
	utils.end(cacheToDisc=False)

def a_z_tv():
	from resources.lib.vjackson import addDir2
	from collections import defaultdict
	from urllib.parse import quote_plus
	results = getchannels()
	res = defaultdict(dict)
	for key, val in results.items():
		prefix, number = key[:1].upper() if key[:1].isalpha() else "#", key
		res[prefix][number] = val
	res = dict(sorted(res.items()))
	for key, val in res.items():
		addDir2(key, "DefaultAddonPVRClient", "channels", items=json.dumps(val))
	utils.end()