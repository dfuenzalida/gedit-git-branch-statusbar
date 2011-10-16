Git branch statusbar plugin
==========================

This gEdit plugin shows the git branch for the file being edited on the status bar. The master branch now contains the plugin compatible with Gnome 3 and the new API. The *gnome2* branch contains the old version.

Requirements
------------

On Ubuntu and Debian, just install the `python-git` and `msgfmt` packages, then install as described below.

Install from sources
------------

Either download the files (using the Downloads button) and uncompress to a folder, or clone the repository.

Run `sudo make install` to install.

Install as a Ubuntu package
------------

You can add my Ubuntu PPA to add this plugin as a software package and receive updates.

See https://launchpad.net/~denis-fuenzalida/+archive/ppa

Configuration
------------

On gEdit, go to Edit > Preferences, on the Plugins tab look for *Git branch on status bar* and mark the checkbox next to it to enable the plugin.

Screenshot
----------

Obligatory screenshot:

![gedit screenshot with git branch on status bar](http://i.imgur.com/cMtgx.png)

On the image above, the branch name is *super-improved-look-branch*. 

Note that it currently supports English and Spanish.

