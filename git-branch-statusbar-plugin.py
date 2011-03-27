from gettext import gettext as _

import gtk
import gedit

# Plug-in specific imports
import git
import urlparse

# Shows the Git branch of the current file on the status bar
class GitBranchPluginHelper:
    def __init__(self, plugin, window):
        self._window = window
        self._plugin = plugin

        # Find the status bar, add a new label to show the branch
        status_bar = window.get_statusbar()
        self._branch_label = gtk.Label("")
        status_bar.add(self._branch_label)
        self._branch_label.show()
        self.update_ui()

    def deactivate(self):
        status_bar = self._window.get_statusbar()
        status_bar.remove(self._branch_label)
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
            label_text = repo.active_branch
        except Exception:
            pass
        except BaseException:
            pass
        finally:
            # Update the branch label
            self._branch_label.set_text(label_text)


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
