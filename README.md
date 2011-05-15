Git branch statusbar plugin
==========================

This gedit plugin shows the git branch for the file being edited on the status bar.

Requirements
------------

On Ubuntu and Debian, just install the `python-git` package, then install as described below.

Easy install
------------

Copy the files `git-branch-statusbar-plugin.gedit-plugin` and `git-branch-statusbar-plugin.py` to your `~/.gnome2/gedit/plugins` folder, then restart gEdit.

On gEdit, go to Edit > Preferences, on the Plugins tab look for *Git branch on status bar* and mark the checkbox next to it to enable the plugin.

Recommended Install
-------------------

Clone the repo in a folder of your choice (here I put it on `~/bin/gedit-git-branch-statusbar`)

```
$ mkdir -p ~/bin
$ cd ~/bin
$ git clone git@github.com:dfuenzalida/gedit-git-branch-statusbar.git
```

Create a symlink from your user's plugins folder to your copy of the repo:

```
$ cd ~/.gnome2/gedit/plugins
$ ln -s ~/bin/gedit-git-branch-statusbar/git-branch-statusbar-plugin.gedit-plugin git-branch-statusbar-plugin.gedit-plugin
$ ln -s ~/bin/gedit-git-branch-statusbar/git-branch-statusbar-plugin.py git-branch-statusbar-plugin.py
```

To update to the latest version of the plug-in, just update the repo and restart gEdit:

```
$ cd ~/bin/gedit-git-branch-statusbar
$ git pull
```

Screenshot
----------

Obligatory screenshot:

![gedit screenshot with git branch on status bar](http://i.imgur.com/TY4YD.png)

On the image above, the branch name is *super-improved-look-branch*
