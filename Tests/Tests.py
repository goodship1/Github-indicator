import pytest
import GithubInformation
import mainwindow

Git = GithubInformation()

mainWindow = GithubInfobar()



def testing_Mainwindow_repositories():
    assert(type(mainWindow.repositories))==int


def testing_Mainwindow_stars():
    assert(type(mainWindow.stars))==int

def testing_Mainwindow_followers():
    assert(type(mainWindow.followers))==int

def  testing_Of_get_Star():
    assert(type(git.get_stars())==int


def testing_of_get_public_repositoru():
    assert(type(git.get_stars()))==int

def testing_Of_get_Followers():
    assert(type(get.get_followers())==int
