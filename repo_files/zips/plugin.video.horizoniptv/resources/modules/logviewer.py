
import os,xbmc,xbmcgui,xbmcaddon

from urllib import FancyURLopener,urlencode

def do():
	d = xbmcgui.Dialog().select('Select a Option',['View Kodi Log','Upload Kodi Log'])
	
	if d == 0:
		show()
	elif d == 1:
		upload()
		

def log_location(old=False):
    version_number = int(xbmc.getInfoLabel("System.BuildVersion")[0:2])
    if version_number < 12:
        if xbmc.getCondVisibility("system.platform.osx"):
            if xbmc.getCondVisibility("system.platform.atv2"):
                log_path = "/var/mobile/Library/Preferences"
            else:
                log_path = os.path.join(os.path.expanduser("~"), "Library/Logs")
        elif xbmc.getCondVisibility("system.platform.ios"):
            log_path = "/var/mobile/Library/Preferences"
        elif xbmc.getCondVisibility("system.platform.windows"):
            log_path = xbmc.translatePath("special://home")
        elif xbmc.getCondVisibility("system.platform.linux"):
            log_path = xbmc.translatePath("special://home/temp")
        else:
            log_path = xbmc.translatePath("special://logpath")
    else:
        log_path = xbmc.translatePath("special://logpath")

    if version_number < 14:
        filename = "xbmc.log"
        filename_old = "xbmc.old.log"
    else:
        filename = "kodi.log"
        filename_old = "kodi.old.log"

    if not os.path.exists(os.path.join(log_path, filename)):
        if os.path.exists(os.path.join(log_path, "spmc.log")):
            filename = "spmc.log"
            filename_old = "spmc.old.log"
        else:
            return False

    if old:
        log_path = os.path.join(log_path, filename_old)
    else:
        log_path = os.path.join(log_path, filename)

    return log_path.decode("utf-8")
	
	
def show():
	import time,xbmcgui
	announce = log_location()
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
		



class pasteURLopener(FancyURLopener):
    version = '%s: %s' % (xbmcaddon.Addon().getAddonInfo('id'), xbmcaddon.Addon().getAddonInfo('version'))

def upload():

	t      = log_location()
	text   = open(t,'r')
	text   = text.read()
	
	url     = 'https://paste.ubuntu.com/'
	
	params = {}
	params['poster'] = 'kodi'
	params['content'] = text
	params['syntax'] = 'text'
	params = urlencode(params)
			
	url_opener = pasteURLopener()

	try:
		page = url_opener.open(url, params)
	except:
		log('failed to connect to the server')
		return False

	try:
		page_url = page.url.strip()
	except:
		log('failed to get log URL')
				
	xbmcgui.Dialog().ok('Your Kodi Log File URL',page_url)