from gettext import gettext as _

import gtk
import gedit

# Plug-in specific imports
import git
import urlparse

# gettext support
import gettext
import os.path

# Load localization messages
# gettext.install("gedit-git-branch-statusbar", os.path.join(os.path.dirname(__file__), "locale"))
# gettext.install("gedit-git-branch-statusbar", "/home/denis/Proyectos/gedit-git-branch-statusbar/locale")
gettext.bindtextdomain('gedit-git-branch-statusbar', '/home/denis/Proyectos/gedit-git-branch-statusbar/locale')
gettext.textdomain('gedit-git-branch-statusbar')

# Shows the Git branch of the current file on the status bar
class GitBranchPluginHelper:
    def __init__(self, plugin, window):
        self._window = window
        self._plugin = plugin

        # Find the status bar, add a new label to show the branch
        status_bar = window.get_statusbar()
        self._branch_label = gtk.Label(None)
        self._branch_label.set_selectable(True)
        self._branch_label.set_single_line_mode(True)
        self._branch_label.show()
        
        # Add a container, so the Label does not overflow the vspace of the statusbar
        self._container = gtk.Frame(None)
        self._container.show()
        status_bar.pack_end(self._container, expand=False, fill=True, padding=0)
        self._container.add(self._branch_label)
        
        # show all
        self.update_ui()

    def deactivate(self):
        status_bar = self._window.get_statusbar()
        status_bar.remove(self._container)
        self._window = None
        self._plugin = None
        self._status_bar = None

    def update_ui(self):
        label_text = ""
        try:
            # Get the current document URI
            document_uri = self._window.get_active_document().get_uri()
            # Get the file reference from the URI
            file_path = urlparse.urlparse(document_uri).path
            # Get a Git repo reference from the file path
            repo = git.Repo(file_path)
            label_text = _("Git branch: ") + "<i>" + repo.active_branch + "</i>"
        except Exception:
            pass
        except BaseException:
            pass
        finally:
            # Update the branch label
            self._branch_label.set_markup(label_text)


class GitBranchPlugin(gedit.Plugin):
    def __init__(self):
        gedit.Plugin.__init__(self)
        self._instances = {}

    def activate(self, window):
        self._instances[window] = GitBranchPluginHelper(self, window)

    def deactivate(self, window):
        self._instances[window].deactivate()
        del self._instances[window]

    def update_ui(self, window):
        self._instances[window].update_ui()

