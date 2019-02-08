import gi
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
import signal 

class GithubInfobar(object):
	
	  APPINDICATOR_ID = "GithubInformation"
	  
	  def __init__(self):
		  self.indicator = appindicator.Indicator.new(APPINDICATOR_ID)
		  
	
	
	
