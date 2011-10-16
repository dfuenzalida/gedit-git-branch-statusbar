# Languages available
PO = en es

PREFIX ?= /usr

FILES = git-branch-statusbar-plugin.plugin git-branch-statusbar-plugin.py

all: po-data
	@echo "\n\nTo install type: sudo make install"

po-dir:
	for lang in $(PO); do mkdir -p locale/$$lang/LC_MESSAGES/ ;done

po-data: po-dir
	for lang in $(PO); do msgfmt locale/$$lang/gedit-git-branch-statusbar.po -o locale/$$lang/LC_MESSAGES/gedit-git-branch-statusbar.mo; done

make-install-po-dirs:
	for lang in $(PO); do mkdir -p $(DESTDIR)$(PREFIX)/share/locale/$$lang/LC_MESSAGES; done

install-po:
	for lang in $(PO); do install -m 644 locale/$$lang/LC_MESSAGES/* $(DESTDIR)$(PREFIX)/share/locale/$$lang/LC_MESSAGES/; done

install: make-install-po-dirs install-po
	mkdir -p $(DESTDIR)$(PREFIX)/lib/gedit/plugins
	for file in $(FILES); do install -m 755 $$file $(DESTDIR)$(PREFIX)/lib/gedit/plugins ; done

