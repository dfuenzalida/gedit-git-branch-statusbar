# -*- coding: utf-8 -*-
#    Gedit Git Branch On Statusbar Plugin
#    Copyright (C) 2010-2019 Denis Fuenzalida <denis.fuenzalida@gmail.com>
#
#    This program is free software; you can redistribute it and/or modify
#    it under the terms of the GNU General Public License as published by
#    the Free Software Foundation; either version 2 of the License, or
#    (at your option) any later version.
#
#    This program is distributed in the hope that it will be useful,
#    but WITHOUT ANY WARRANTY; without even the implied warranty of
#    MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#    GNU General Public License for more details.
#
#    You should have received a copy of the GNU General Public License
#    along with this program; if not, write to the Free Software
#    Foundation, Inc., 51 Franklin St, Fifth Floor, Boston, MA  02110-1301  USA

from gettext import gettext as _

from gi.repository import GObject, Gtk, Gedit

# Plug-in specific imports
import git

# gettext support
import gettext
import os

# Load localization messages
gettext.bindtextdomain('gedit-git-branch-statusbar')
gettext.textdomain('gedit-git-branch-statusbar')

# Shows the Git branch of the current file on the status bar
class GitBranchPlugin(GObject.Object, Gedit.WindowActivatable):
    __gtype_name__ = "GitBranchPlugin"

    window = GObject.property(type=Gedit.Window)

    def __init__(self):
        GObject.Object.__init__(self)

    def do_activate(self):
        # Find the status bar, add a new label to show the branch
        status_bar = self.window.get_statusbar()
        self._branch_label = Gtk.Label(None)
        self._branch_label.set_selectable(True)
        self._branch_label.set_single_line_mode(True)
        self._branch_label.show()
        
        # Add a container, so the Label does not overflow the vspace of the statusbar
        self._container = Gtk.Frame()
        self._container.show()
        self._container.add(self._branch_label)
        status_bar.pack_end(self._container, expand=False, fill=True, padding=0)
        
        # show all
        self.do_update_state()

    def do_deactivate(self):
        status_bar = self.window.get_statusbar()

        self.window = None
        self._plugin = None
        self._status_bar = None

    def do_update_state(self):
        label_text = ""
        try:
            file_path = self.window.get_active_document().get_location().get_path()
            dir_path = os.path.dirname(file_path)
            repo = git.Repo(dir_path)
            label_text = _("Git branch: ") + "<i>" + str(repo.active_branch) + "</i>"
        except Exception:
            pass
        except BaseException:
            pass
        finally:
            # Update the branch label
            self._branch_label.set_markup(label_text)

