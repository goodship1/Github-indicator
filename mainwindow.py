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
		
		
		def _github_Info(self):
			git = GithubInformation()
			repos = git.get_Public_repository
			stars = git.get_Stars()
			followers = git.get_Followers()
			return (repos,stars,followers)
		    
		
		
		
		@staticmethod
		def main():
			gtk.main()
	
	
		



Git = GithubInfobar()

