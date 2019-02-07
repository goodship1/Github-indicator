from github import Github

class GithubInformation(object):
      
    
	 access_Token = "b951b9eca1875daa9c3d2d18521d0fb363cbe70e"
	 git = Github(access_Token)
	 user = git.get_user("goodship1")
	 
	 @classmethod
	 def get_Repos(cls):
		 '''Only gets public repos of user'''
		 repo_Counter = 0
		 repo = sum([repo_Counter+1 for repos in cls.user.get_repos()])
		 return repo
     
	 
	 @classmethod
	 def get_Stars(cls):
		 pass
	 
	 @classmethod
	 def get_Followers(cls):
		 pass
    
   

