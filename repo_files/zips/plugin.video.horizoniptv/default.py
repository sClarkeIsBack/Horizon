 #############Imports#############
import xbmc,xbmcaddon,xbmcgui,xbmcplugin,base64,os,re,unicodedata,requests,time,string,sys,urllib,urllib2,json,urlparse,datetime,zipfile,shutil
from resources.modules import client,control,tools,user,trailer
from datetime import date


icon         = xbmc.translatePath(os.path.join('special://home/addons/' + user.id, 'icon.png'))
fanart       = xbmc.translatePath(os.path.join('special://home/addons/' + user.id , 'fanart.jpg'))

KODIV        = float(xbmc.getInfoLabel("System.BuildVersion")[:4])

iconFolder   = xbmc.translatePath('special://home/addons/'+user.id+'/resources/images/Horizon')
	
def MAIN():
	tools.addDir('[B]Select Your Service[/B]','s',9999,icon,fanart,'')
	tools.addDir('[B][COLOR ffE5E4E2]PLATNIUM[/COLOR][/B]','server1',999,icon,fanart,'')
	tools.addDir('[B][COLOR gold]GOLD[/COLOR][/B]','server2',999,icon,fanart,'')
	

def start(url):
	if 'server1' in url:
		username = control.setting('server1user')
		password = control.setting('server1pass')
		host     = user.server1host
		port     = user.server1port
		if username == "":
			usern = userpopup()
			passw = passpopup()
			control.setSetting('server1user',usern)
			control.setSetting('server1pass',passw)
			xbmc.executebuiltin('Container.Refresh')
			auth = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(host,port,usern,passw)
			auth = tools.OPEN_URL(auth)
			if auth == "":
				line1 = "Incorrect Login Details"
				line2 = "Please Re-enter" 
				line3 = "" 
				xbmcgui.Dialog().ok('Attention', line1, line2, line3)
				MAIN()
			else:
				line1 = "Login Sucsessfull"
				line2 = "Welcome to "+user.name 
				line3 = ('[COLOR white]%s[/COLOR]'%usern)
				xbmcgui.Dialog().ok(user.name, line1, line2, line3)
				xbmc.executebuiltin('Container.Refresh')
				tools.addDir('Account Information','server1',6,xbmc.translatePath(os.path.join(iconFolder,'myacc.png')),fanart,'My Account Info - Containing Information Inlcuding Your Expiry Date & More')
				tools.addDir('Live TV','server1',1,xbmc.translatePath(os.path.join(iconFolder,'livetv.png')),fanart,'Live TV - Containing Our Selection of Live TV Channels')
				if xbmc.getCondVisibility('Pvr.HasTVChannels'):
					tools.addDir('TV Guide','server1',7,xbmc.translatePath(os.path.join(iconFolder,'tvguide.png')),fanart,'TV Guide - IPTV Simple Client PVR TV Guide')
				tools.addDir('Catchup TV','server1',9,xbmc.translatePath(os.path.join(iconFolder,'catchup.png')),fanart,'Catchup TV - Catchup On Your Favourite Shows From the Past 7 Days')
				tools.addDir('On Demand','VOD:server1',3,xbmc.translatePath(os.path.join(iconFolder,'vod.png')),fanart,'VOD - Containing A Wide Selection of Movies & TV Series')
				tools.addDir('Search','server1',5,xbmc.translatePath(os.path.join(iconFolder,'search.png')),fanart,'Search - Search Horizon IPTV For Your Favourite Channel or Movie')
				tools.addDir('Extras','server1',11,xbmc.translatePath(os.path.join(iconFolder,'extras.png')),fanart,'Extras - Horizon Extras')
				tools.addDir('Settings','AS',10,xbmc.translatePath(os.path.join(iconFolder,'settings.png')),fanart,'Settings - Open Addon Settings')
		else:
			auth = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(host,port,username,password)
			auth = tools.OPEN_URL(auth)
			if not auth=="":
				tools.addDir('Account Information','server1',6,xbmc.translatePath(os.path.join(iconFolder,'myacc.png')),fanart,'My Account Info - Containing Information Inlcuding Your Expiry Date & More')
				tools.addDir('Live TV','server1',1,xbmc.translatePath(os.path.join(iconFolder,'livetv.png')),fanart,'Live TV - Containing Our Selection of Live TV Channels')
				if xbmc.getCondVisibility('Pvr.HasTVChannels'):
					tools.addDir('TV Guide','server1',7,xbmc.translatePath(os.path.join(iconFolder,'tvguide.png')),fanart,'TV Guide - IPTV Simple Client PVR TV Guide')
				tools.addDir('Catchup TV','server1',9,xbmc.translatePath(os.path.join(iconFolder,'catchup.png')),fanart,'Catchup TV - Catchup On Your Favourite Shows From the Past 7 Days')
				tools.addDir('On Demand','VOD:server1',3,xbmc.translatePath(os.path.join(iconFolder,'vod.png')),fanart,'VOD - Containing A Wide Selection of Movies & TV Series')
				tools.addDir('Search','server1',5,xbmc.translatePath(os.path.join(iconFolder,'search.png')),fanart,'Search - Search Horizon IPTV For Your Favourite Channel or Movie')
				tools.addDir('Extras','server1',11,xbmc.translatePath(os.path.join(iconFolder,'extras.png')),fanart,'Extras - Horizon Extras')
				tools.addDir('Settings','AS',10,xbmc.translatePath(os.path.join(iconFolder,'settings.png')),fanart,'Settings - Open Addon Settings')
	elif 'server2' in url:
		username = control.setting('server2user')
		password = control.setting('server2pass')
		host     = user.server2host
		port     = user.server2port
		if username == "":
			usern = userpopup()
			passw = passpopup()
			control.setSetting('server2user',usern)
			control.setSetting('server2pass',passw)
			xbmc.executebuiltin('Container.Refresh')
			auth = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(host,port,usern,passw)
			auth = tools.OPEN_URL(auth)
			if auth == "":
				line1 = "Incorrect Login Details"
				line2 = "Please Re-enter" 
				line3 = "" 
				xbmcgui.Dialog().ok('Attention', line1, line2, line3)
				MAIN()
			else:
				line1 = "Login Sucsessfull"
				line2 = "Welcome to "+user.name 
				line3 = ('[COLOR white]%s[/COLOR]'%usern)
				xbmcgui.Dialog().ok(user.name, line1, line2, line3)
				xbmc.executebuiltin('Container.Refresh')
				tools.addDir('Account Information','server2',6,xbmc.translatePath(os.path.join(iconFolder,'myacc.png')),fanart,'My Account Info - Containing Information Inlcuding Your Expiry Date & More')
				tools.addDir('Live TV','server2',1,xbmc.translatePath(os.path.join(iconFolder,'livetv.png')),fanart,'Live TV - Containing Our Selection of Live TV Channels')
				if xbmc.getCondVisibility('Pvr.HasTVChannels'):
					tools.addDir('TV Guide','server2',7,xbmc.translatePath(os.path.join(iconFolder,'tvguide.png')),fanart,'TV Guide - IPTV Simple Client PVR TV Guide')
				tools.addDir('Catchup TV','server2',9,xbmc.translatePath(os.path.join(iconFolder,'catchup.png')),fanart,'Catchup TV - Catchup On Your Favourite Shows From the Past 7 Days')
				tools.addDir('On Demand','VOD:server2',3,xbmc.translatePath(os.path.join(iconFolder,'vod.png')),fanart,'VOD - Containing A Wide Selection of Movies & TV Series')
				tools.addDir('Search','server2',5,xbmc.translatePath(os.path.join(iconFolder,'search.png')),fanart,'Search - Search Horizon IPTV For Your Favourite Channel or Movie')
				tools.addDir('Extras','server2',11,xbmc.translatePath(os.path.join(iconFolder,'extras.png')),fanart,'Extras - Horizon Extras')
				tools.addDir('Settings','AS',10,xbmc.translatePath(os.path.join(iconFolder,'settings.png')),fanart,'Settings - Open Addon Settings')
		else:
			auth = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(host,port,username,password)
			auth = tools.OPEN_URL(auth)
			if not auth=="":
				tools.addDir('Account Information','server2',6,xbmc.translatePath(os.path.join(iconFolder,'myacc.png')),fanart,'My Account Info - Containing Information Inlcuding Your Expiry Date & More')
				tools.addDir('Live TV','server2',1,xbmc.translatePath(os.path.join(iconFolder,'livetv.png')),fanart,'Live TV - Containing Our Selection of Live TV Channels')
				if xbmc.getCondVisibility('Pvr.HasTVChannels'):
					tools.addDir('TV Guide','server2',7,xbmc.translatePath(os.path.join(iconFolder,'tvguide.png')),fanart,'TV Guide - IPTV Simple Client PVR TV Guide')
				tools.addDir('Catchup TV','server2',9,xbmc.translatePath(os.path.join(iconFolder,'catchup.png')),fanart,'Catchup TV - Catchup On Your Favourite Shows From the Past 7 Days')
				tools.addDir('On Demand','VOD:server2',3,xbmc.translatePath(os.path.join(iconFolder,'vod.png')),fanart,'VOD - Containing A Wide Selection of Movies & TV Series')
				tools.addDir('Search','server2',5,xbmc.translatePath(os.path.join(iconFolder,'search.png')),fanart,'Search - Search Horizon IPTV For Your Favourite Channel or Movie')
				tools.addDir('Extras','server2',11,xbmc.translatePath(os.path.join(iconFolder,'extras.png')),fanart,'Extras - Horizon Extras')
				tools.addDir('Settings','AS',10,xbmc.translatePath(os.path.join(iconFolder,'settings.png')),fanart,'Settings - Open Addon Settings')

		
def livecategory(url):
	if 'server1' in url:
		username = control.setting('server1user')
		password = control.setting('server1pass')
		host     = user.server1host
		port     = user.server1port
	elif 'server2' in url:
		username = control.setting('server2user')
		password = control.setting('server2pass')
		host     = user.server2host
		port     = user.server2port
		
	url = '%s:%s/enigma2.php?username=%s&password=%s&type=get_live_categories'%(host,port,username,password)
	open = tools.OPEN_URL(url)
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
		if not 'Install Videos' in name:
			if not 'TEST CHANNELS' in name:
					tools.addDir(name,url1,2,icon,fanart,'')
		
def Livelist(url):
	open = tools.OPEN_URL(url)
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		name = tools.regex_from_to(a,'<title>','</title>')
		name = base64.b64decode(name)
		xbmc.log(str(name))
		name = re.sub('\[.*?min ','-',name)
		thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
		url1  = tools.regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
		desc = tools.regex_from_to(a,'<description>','</description>')
		tools.addDir(name,url1,4,thumb,fanart,base64.b64decode(desc))
		
	
def vod(url):
	if 'VOD:' in url:
		a = url.replace('VOD:','')
		if 'server1' in a:
			username = control.setting('server1user')
			password = control.setting('server1pass')
			host     = user.server1host
			port     = user.server1port
			url = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(host,port,username,password)
		elif 'server2' in a:
			username = control.setting('server2user')
			password = control.setting('server2pass')
			host     = user.server2host
			port     = user.server2port
			url = '%s:%s/enigma2.php?username=%s&password=%s&type=get_vod_categories'%(host,port,username,password)
			
		open= tools.OPEN_URL(url)

	else:
		open = tools.OPEN_URL(url)
	all_cats = tools.regex_get_all(open,'<channel>','</channel>')
	for a in all_cats:
		if '<playlist_url>' in open:
			name = tools.regex_from_to(a,'<title>','</title>')
			url1  = tools.regex_from_to(a,'<playlist_url>','</playlist_url>').replace('<![CDATA[','').replace(']]>','')
			tools.addDir(str(base64.b64decode(name)).replace('?',''),url1,3,icon,fanart,'')
		else:
			name = tools.regex_from_to(a,'<title>','</title>')
			name = base64.b64decode(name)
			thumb= tools.regex_from_to(a,'<desc_image>','</desc_image>').replace('<![CDATA[','').replace(']]>','')
			url  = tools.regex_from_to(a,'<stream_url>','</stream_url>').replace('<![CDATA[','').replace(']]>','')
			desc = tools.regex_from_to(a,'<description>','</description>')
			tools.addDir(name,url,13,thumb,fanart,base64.b64decode(desc))
				
				
		
##############################################
#### RULE NO.1 - DONT WRITE CODE THAT IS  ####
#### ALREADY WRITTEN AND PROVEN TO WORK :)####
##############################################


def catchup():
    listcatchup()
		
def listcatchup(url):
	if 'server1' in url:
			username = control.setting('server1user')
			password = control.setting('server1pass')
			host     = user.server1host
			port     = user.server1port
			u = '%s:%s/panel_api.php?username=%s&password=%s'%(host,port,username,password)
	elif 'server2' in url:
			username = control.setting('server2user')
			password = control.setting('server2pass')
			host     = user.server2host
			port     = user.server2port
			u = '%s:%s/panel_api.php?username=%s&password=%s'%(host,port,username,password)
	open = tools.OPEN_URL(u)
	all  = tools.regex_get_all(open,'{"num','direct')
	for a in all:
		if '"tv_archive":1' in a:
			name = tools.regex_from_to(a,'"epg_channel_id":"','"').replace('\/','/')
			thumb= tools.regex_from_to(a,'"stream_icon":"','"').replace('\/','/')
			id   = tools.regex_from_to(a,'stream_id":"','"')
			if not name=="":
				tools.addDir(name,url,12,thumb,fanart,id)
			

def tvarchive(name,url,description):
		if 'server1' in url:
				username = control.setting('server1user')
				password = control.setting('server1pass')
				host     = user.server1host
				port     = user.server1port
				days = 7
		elif 'server2' in url:
				username = control.setting('server2user')
				password = control.setting('server2pass')
				host     = user.server2host
				port     = user.server2port
				days = 5
			
		now = str(datetime.datetime.now()).replace('-','').replace(':','').replace(' ','')
		date3 = datetime.datetime.now() - datetime.timedelta(days)
		date = str(date3)
		date = str(date).replace('-','').replace(':','').replace(' ','')
		APIv2 = base64.b64decode("JXM6JXMvcGxheWVyX2FwaS5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmYWN0aW9uPWdldF9zaW1wbGVfZGF0YV90YWJsZSZzdHJlYW1faWQ9JXM=")%(host,port,username,password,description)
		
		link=tools.OPEN_URL(APIv2)
		match = re.compile('"title":"(.+?)".+?"start":"(.+?)","end":"(.+?)","description":"(.+?)"').findall(link)
		for ShowTitle,start,end,DesC in match:
			ShowTitle = base64.b64decode(ShowTitle)
			DesC = base64.b64decode(DesC)
			format = '%Y-%m-%d %H:%M:%S'
			try:
				modend = dtdeep.strptime(end, format)
				modstart = dtdeep.strptime(start, format)
			except:
				modend = datetime.datetime(*(time.strptime(end, format)[0:6]))
				modstart = datetime.datetime(*(time.strptime(start, format)[0:6]))
			StreamDuration = modend - modstart
			modend_ts = time.mktime(modend.timetuple())
			modstart_ts = time.mktime(modstart.timetuple())
			FinalDuration = int(modend_ts-modstart_ts) / 60
			strstart = start
			Realstart = str(strstart).replace('-','').replace(':','').replace(' ','')
			start2 = start[:-3]
			editstart = start2
			start2 = str(start2).replace(' ',' - ')
			start = str(editstart).replace(' ',':')
			Editstart = start[:13] + '-' + start[13:]
			Finalstart = Editstart.replace('-:','-')
			if Realstart > date:
				if Realstart < now:
					catchupURL = base64.b64decode("JXM6JXMvc3RyZWFtaW5nL3RpbWVzaGlmdC5waHA/dXNlcm5hbWU9JXMmcGFzc3dvcmQ9JXMmc3RyZWFtPSVzJnN0YXJ0PQ==")%(host,port,username,password,description)
					ResultURL = catchupURL + str(Finalstart) + "&duration=%s"%(FinalDuration)
					kanalinimi = "[COLOR white]%s[/COLOR] - %s"%(start2,ShowTitle)
					tools.addDir(kanalinimi,ResultURL,4,icon,fanart,DesC)

	
					
def DownloaderClass(url, dest):
    dp = xbmcgui.DialogProgress()
    dp.create('Fetching latest Catch Up',"Fetching latest Catch Up...",' ', ' ')
    dp.update(0)
    start_time=time.time()
    urllib.urlretrieve(url, dest, lambda nb, bs, fs: _pbhook(nb, bs, fs, dp, start_time))

def _pbhook(numblocks, blocksize, filesize, dp, start_time):
        try: 
            percent = min(numblocks * blocksize * 100 / filesize, 100) 
            currently_downloaded = float(numblocks) * blocksize / (1024 * 1024) 
            kbps_speed = numblocks * blocksize / (time.time() - start_time) 
            if kbps_speed > 0: 
                eta = (filesize - numblocks * blocksize) / kbps_speed 
            else: 
                eta = 0 
            kbps_speed = kbps_speed / 1024 
            mbps_speed = kbps_speed / 1024 
            total = float(filesize) / (1024 * 1024) 
            mbs = '[COLOR white]%.02f MB of less than 5MB[/COLOR]' % (currently_downloaded)
            e = '[COLOR white]Speed:  %.02f Mb/s ' % mbps_speed  + '[/COLOR]'
            dp.update(percent, mbs, e)
        except: 
            percent = 100 
            dp.update(percent) 
        if dp.iscanceled():
            dialog = xbmcgui.Dialog()
            dialog.ok(user.name, 'The download was cancelled.')
				
            sys.exit()
            dp.close()
#####################################################################

def stream_video(url):
	liz = xbmcgui.ListItem('', iconImage='DefaultVideo.png', thumbnailImage=icon)
	liz.setInfo(type='Video', infoLabels={'Title': '', 'Plot': ''})
	liz.setProperty('IsPlayable','true')
	liz.setPath(str(url))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	
def stream_vod(url):
	liz = xbmcgui.ListItem('', iconImage='DefaultVideo.png', thumbnailImage=icon)
	liz.setInfo(type='Video', infoLabels={'Title': '', 'Plot': ''})
	liz.setProperty('IsPlayable','true')
	liz.setPath(str(url))
	xbmcplugin.setResolvedUrl(int(sys.argv[1]), True, liz)
	
def searchdialog():
	search = control.inputDialog(heading='Search '+user.name+':')
	if search=="":
		return
	else:
		return search

	
def search(url):
	if url=="" or mode==3:
		return False
	text = searchdialog()
	if not text:
		xbmc.executebuiltin("XBMC.Notification([COLOR white][B]Search is Empty[/B][/COLOR],Aborting search,4000,"+icon+")")
		return
		
	if 'server1' in url:
			username = control.setting('server1user')
			password = control.setting('server1pass')
			host     = user.server1host
			port     = user.server1port
			url = '%s:%s/panel_api.php?username=%s&password=%s'%(host,port,username,password)
	elif 'server2' in url:
			username = control.setting('server2user')
			password = control.setting('server2pass')
			host     = user.server2host
			port     = user.server2port
			url = '%s:%s/panel_api.php?username=%s&password=%s'%(host,port,username,password)
			
	open = tools.OPEN_URL(url)
	all_chans = tools.regex_get_all(open,'{"num":','epg')
	for a in all_chans:
		name = tools.regex_from_to(a,'name":"','"').replace('\/','/')
		url  = tools.regex_from_to(a,'"stream_id":"','"')
		thumb= tools.regex_from_to(a,'stream_icon":"','"').replace('\/','/')
		if text in name.lower():
			burl = '%s:%s/live/%s/%s/'%(host,port,username,password)
			tools.addDir(name,burl+url+'.ts',4,thumb,fanart,'')
		elif text not in name.lower() and text in name:
			burl = '%s:%s/live/%s/%s/'%(host,port,username,password)
			tools.addDir(name,burl+url+'.ts',4,thumb,fanart,'')
		
def userpopup():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Username')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		return text
	else:
		return False

		
def passpopup():
	kb =xbmc.Keyboard ('', 'heading', True)
	kb.setHeading('Enter Password')
	kb.setHiddenInput(False)
	kb.doModal()
	if (kb.isConfirmed()):
		text = kb.getText()
		return text
	else:
		return False
		
		
def accountinfo(url):
	if 'server1' in url:
			username = control.setting('server1user')
			password = control.setting('server1pass')
			host     = user.server1host
			port     = user.server1port
			url = '%s:%s/panel_api.php?username=%s&password=%s'%(host,port,username,password)
			sub = '[COLOR FFE5E4E2]Platnium[/COLOR]'
	elif 'server2' in url:
			username = control.setting('server2user')
			password = control.setting('server2pass')
			host     = user.server2host
			port     = user.server2port
			url = '%s:%s/panel_api.php?username=%s&password=%s'%(host,port,username,password)
			sub = '[COLOR gold]Gold[/COLOR]'
	try:
		open = tools.OPEN_URL(url)
		username   = tools.regex_from_to(open,'"username":"','"')
		password   = tools.regex_from_to(open,'"password":"','"')
		status     = tools.regex_from_to(open,'"status":"','"')
		connects   = tools.regex_from_to(open,'"max_connections":"','"')
		active     = tools.regex_from_to(open,'"active_cons":"','"')
		expiry     = tools.regex_from_to(open,'"exp_date":"','"')
		if expiry == "":
			expiry = 'Unlimited'
		else:
			expiry     = datetime.datetime.fromtimestamp(int(expiry)).strftime('%d/%m/%Y - %H:%M')
			expreg     = re.compile('^(.*?)/(.*?)/(.*?)$',re.DOTALL).findall(expiry)
			for day,month,year in expreg:
				month     = tools.MonthNumToName(month)
				year      = re.sub(' -.*?$','',year)
				expiry    = month+' '+day+' - '+year
		ip        = tools.getlocalip()
		extip     = tools.getexternalip()
		tools.addDir('[COLOR white]Service:[/COLOR] [COLOR red]'+sub+'[/COLOR]','','',icon,fanart,'')
		tools.addDir('[COLOR white]Username:[/COLOR] '+username,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Password:[/COLOR] '+password,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Expiry Date:[/COLOR] '+expiry,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Account Status :[/COLOR] %s'%status,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Current Connections:[/COLOR] '+ active,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Allowed Connections:[/COLOR] '+connects,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Local IP Address:[/COLOR] '+ip,'','',icon,fanart,'')
		tools.addDir('[COLOR white]External IP Address:[/COLOR] '+extip,'','',icon,fanart,'')
		tools.addDir('[COLOR white]Kodi Version:[/COLOR] '+str(KODIV),'','',icon,fanart,'')
	except:
		pass
		
	


def num2day(num):
	if num =="0":
		day = 'monday'
	elif num=="1":
		day = 'tuesday'
	elif num=="2":
		day = 'wednesday'
	elif num=="3":
		day = 'thursday'
	elif num=="4":
		day = 'friday'
	elif num=="5":
		day = 'saturday'
	elif num=="6":
		day = 'sunday'
	return day
	
	
def addonsettings(url):
	if   url =="CC":
		tools.clear_cache()
	elif url =="AS":
		xbmc.executebuiltin('Addon.OpenSettings(%s)'%user.id)
	elif url =="ADS":
		dialog = xbmcgui.Dialog().select('Edit Advanced Settings', ['Enable Fire TV Stick AS','Enable Fire TV AS','Enable 1GB Ram or Lower AS','Enable 2GB Ram or Higher AS','Enable Nvidia Shield AS','Disable AS'])
		if dialog==0:
			advancedsettings('stick')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==1:
			advancedsettings('firetv')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==2:
			advancedsettings('lessthan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==3:
			advancedsettings('morethan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==4:
			advancedsettings('shield')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==5:
			advancedsettings('remove')
			xbmcgui.Dialog().ok(user.name, 'Advanced Settings Removed')
	elif url =="ADS2":
		dialog = xbmcgui.Dialog().select('Select Your Device Or Closest To', ['Fire TV Stick ','Fire TV','1GB Ram or Lower','2GB Ram or Higher','Nvidia Shield'])
		if dialog==0:
			advancedsettings('stick')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==1:
			advancedsettings('firetv')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==2:
			advancedsettings('lessthan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==3:
			advancedsettings('morethan')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
		elif dialog==4:
			advancedsettings('shield')
			xbmcgui.Dialog().ok(user.name, 'Set Advanced Settings')
	elif "pvr:" in url:
		a = url.replace('pvr:','')
		correctPVR(a)
	elif url =="ST":
		xbmc.executebuiltin('Runscript("special://home/addons/'+user.id+'/resources/modules/speedtest.py")')
	elif "M3UG:" in url:
		a = url.replace('M3UG:','')
		m3uselector(a)
	elif url == 'KODILOG':
		from resources.modules import logviewer
		logviewer.do()
	
	
def extras(url):
			
	tools.addDir('M3U & EPG URL Generator','M3UG:'+url,10,icon,fanart,'Generates your unique details for use within 3rd Party Applications')
	tools.addDir('Edit Advanced Settings','ADS',10,icon,fanart,'Edit your Advanced Settings File')
	tools.addDir('Run a Speed Test','ST',10,icon,fanart,'Runs a speed test on your internet connection')
	tools.addDir('Setup PVR Guide','pvr:'+url,10,icon,fanart,'Setup PVR Client TV Guide')
	tools.addDir('Clear Cache','CC',10,icon,fanart,'Clear your Kodi Cache for Maintenance')
	tools.addDir('Log Viewer','KODILOG',10,icon,fanart,'View and Upload Your Kodi Log File')
	
def correctPVR(url):

	if 'server1' in url:
			username = control.setting('server1user')
			password = control.setting('server1pass')
			host     = user.server1host
			port     = user.server1port
	elif 'server2' in url:
			username = control.setting('server2user')
			password = control.setting('server2pass')
			host     = user.server2host
			port     = user.server2port

	addon = xbmcaddon.Addon(user.id)

	jsonSetPVR = '{"jsonrpc":"2.0", "method":"Settings.SetSettingValue", "params":{"setting":"pvrmanager.enabled", "value":true},"id":1}'
	IPTVon 	   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.iptvsimple","enabled":true},"id":1}'
	nulldemo   = '{"jsonrpc":"2.0","method":"Addons.SetAddonEnabled","params":{"addonid":"pvr.demo","enabled":false},"id":1}'
	loginurl   = host+':'+port+"/get.php?username=" + username + "&password=" + password + "&type=m3u_plus&output=ts"
	EPGurl     = host+':'+port+"/xmltv.php?username=" + username + "&password=" + password

	xbmc.executeJSONRPC(jsonSetPVR)
	xbmc.executeJSONRPC(IPTVon)
	xbmc.executeJSONRPC(nulldemo)
	
	moist = xbmcaddon.Addon('pvr.iptvsimple')
	moist.setSetting(id='m3uUrl', value=loginurl)
	moist.setSetting(id='epgUrl', value=EPGurl)
	moist.setSetting(id='m3uCache', value="false")
	moist.setSetting(id='epgCache', value="false")
	xbmc.executebuiltin("Container.Refresh")
	
	xbmcgui.Dialog().ok('Attention', 'PVR integration Complete','')
	
def advancedsettings(device):

	advanced_settings           =  xbmc.translatePath('special://home/addons/'+user.id+'/resources/advanced_settings')
	advanced_settings_target    =  xbmc.translatePath(os.path.join('special://home/userdata','advancedsettings.xml'))
	
	if device == 'stick':
		file = open(os.path.join(advanced_settings, 'stick.xml'))
	elif device == 'firetv':
		file = open(os.path.join(advanced_settings, 'firetv.xml'))
	elif device == 'lessthan':
		file = open(os.path.join(advanced_settings, 'lessthan1GB.xml'))
	elif device == 'morethan':
		file = open(os.path.join(advanced_settings, 'morethan1GB.xml'))
	elif device == 'shield':
		file = open(os.path.join(advanced_settings, 'shield.xml'))
	elif device == 'remove':
		os.remove(advanced_settings_target)
	
	try:
		read = file.read()
		f = open(advanced_settings_target, mode='w+')
		f.write(read)
		f.close()
	except:
		pass
	

def m3uselector(url):

	if 'server1' in url:
			username = control.setting('server1user')
			password = control.setting('server1pass')
			host     = user.server1host
			port     = user.server1port
	elif 'server2' in url:
			username = control.setting('server2user')
			password = control.setting('server2pass')
			host     = user.server2host
			port     = user.server2port
			
	dialog = xbmcgui.Dialog().select('Select a M3U Format', ['M3U Standard','M3U Plus (Has Channel Categorys)'])
	if dialog==0:
		type = 'm3u'
	elif dialog==1:
		type = 'm3u_plus'
	else:
		return
	
	dialog = xbmcgui.Dialog().select('Select a Stream Format', ['MPEGTS (Recommended)','HLS','RTMP'])
	if dialog==0:
		output = 'ts'
	elif dialog==1:
		output = 'm3u8'
	elif dialog==2:
		output = 'rtmp'
	else:
		return
		
	m3u = host + ':' + port + '/get.php?username=' + username + '&password=' + password + '&type=' + type + '&output=' + output
	epg = host + ':' + port + '/xmltv.php?username=' + username + '&password=' + password
	
	m3u = urllib.quote_plus(m3u)
	epg = urllib.quote_plus(epg)
	m3u,epg = tinyurlGet(m3u,epg)
	
	text = 'Here Is Your Shortened M3U & EPG URL[CR][CR]M3U URL: %s[CR][CR]EPG URL: %s'%(m3u,epg)
	popupd(text)

def tinyurlGet(m3u,epg):
		request  = 'https://tinyurl.com/create.php?source=indexpage&url='+m3u+'&submit=Make+TinyURL%21&alias='
		request2 = 'https://tinyurl.com/create.php?source=indexpage&url='+epg+'&submit=Make+TinyURL%21&alias='
		m3u = tools.OPEN_URL(request)
		epg = tools.OPEN_URL(request2)
		shortm3u = tools.regex_from_to(m3u,'<div class="indent"><b>','</b>')
		shortepg = tools.regex_from_to(epg,'<div class="indent"><b>','</b>')
		return shortm3u,shortepg
		
def popupd(announce):
	import time,xbmcgui
	class TextBox():
		WINDOW=10147
		CONTROL_LABEL=1
		CONTROL_TEXTBOX=5
		def __init__(self,*args,**kwargs):
			xbmc.executebuiltin("ActivateWindow(%d)" % (self.WINDOW, )) # activate the text viewer window
			self.win=xbmcgui.Window(self.WINDOW) # get window
			xbmc.sleep(500) # give window time to initialize
			self.setControls()
		def setControls(self):
			self.win.getControl(self.CONTROL_LABEL).setLabel('Kodi Log Viewer') # set heading
			try: f=open(announce); text=f.read()
			except: text=announce
			self.win.getControl(self.CONTROL_TEXTBOX).setText(str(text))
			return
	TextBox()
	while xbmc.getCondVisibility('Window.IsVisible(10147)'):
		time.sleep(.5)

params=tools.get_params()
url=None
name=None
mode=None
iconimage=None
description=None
query=None
type=None

try:
	url=urllib.unquote_plus(params["url"])
except:
	pass
try:
	name=urllib.unquote_plus(params["name"])
except:
	pass
try:
	iconimage=urllib.unquote_plus(params["iconimage"])
except:
	pass
try:
	mode=int(params["mode"])
except:
	pass
try:
	description=urllib.unquote_plus(params["description"])
except:
	pass
try:
	query=urllib.unquote_plus(params["query"])
except:
	pass
try:
	type=urllib.unquote_plus(params["type"])
except:
	pass

if mode==None or url==None or len(url)<1:
	MAIN()

elif mode==1:
	livecategory(url)
	
elif mode==2:
	Livelist(url)
	
elif mode==3:
	vod(url)
	
elif mode==4:
	stream_video(url)
	
elif mode==5:
	search(url)
	
elif mode==6:
	accountinfo(url)
	
elif mode==7:
	xbmc.executebuiltin('ActivateWindow(TVGuide)')
	
elif mode==8:
	xbmc.executebuiltin('ActivateWindow(busydialog)')
	tools.Trailer().play(url) 
	xbmc.executebuiltin('Dialog.Close(busydialog)')
	
elif mode==9:
	listcatchup(url)

elif mode==10:
	addonsettings(url)
	
elif mode==11:
	extras(url)
	
elif mode==12:
	tvarchive(name,url,description)
	
elif mode==13:
	stream_vod(url)
	
elif mode==999:
	start(url)
	
elif mode==9999:
	MAIN()

xbmcplugin.endOfDirectory(int(sys.argv[1]))