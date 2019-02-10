import gi
import os
from GithubInformation import GithubInformation
gi.require_version('Gtk', '3.0')
gi.require_version('AppIndicator3', '0.1')
from gi.repository import Gtk as gtk
from gi.repository import AppIndicator3 as appindicator
 


class GithubInfobar(object):
	
		
	    
		def __init__(self):
		    self.indicator = appindicator.Indicator.new("githubapplication" , os.path.dirname(os.path.realpath(__file__))+'/image/github.jpg',appindicator.IndicatorCategory.APPLICATION_STATUS)
		    self.indicator.set_status(appindicator.IndicatorStatus.ACTIVE)
		    self.indicator.set_menu(gtk.Menu())
		    
		    
		
		
		def menu(self):
			pass
		    
	
		def main(self):
			gtk.main()
	
	
		



Git = GithubInfobar()
Git.main()
