include ../../Makefile.inc

THEMES_DIR=../../../themes/

.PHONY: build clean

build: $(COLOR_VARIANTS) Oslo

$(COLOR_VARIANTS):
	mkdir -p $(THEMES_DIR)/NdWaita-$@-Light/gnome-shell/assets
	mkdir -p $(THEMES_DIR)/NdWaita-$@-Dark/gnome-shell/assets
	mkdir -p $(THEMES_DIR)/NdWaita-$@-Darkest/gnome-shell/assets
	cp assets/* $(THEMES_DIR)NdWaita-$@-Light/gnome-shell/assets/
	sed 's/$(DEFAULT_THEME_COLOR)/$(COLOR_$@)/gi' -i $(THEMES_DIR)NdWaita-$@-Light/gnome-shell/assets/*
	cp $(THEMES_DIR)NdWaita-$@-Light/gnome-shell/assets/* $(THEMES_DIR)NdWaita-$@-Dark/gnome-shell/assets/
	cp $(THEMES_DIR)NdWaita-$@-Light/gnome-shell/assets/* $(THEMES_DIR)NdWaita-$@-Darkest/gnome-shell/assets/

Oslo:
	mkdir -p $(THEMES_DIR)/NdWaita-Oslo/gnome-shell/assets
	mkdir -p $(THEMES_DIR)/NdWaita-Oslo-Dark/gnome-shell/assets
	cp assets/* $(THEMES_DIR)/NdWaita-Oslo/gnome-shell/assets/
	cp assets/* $(THEMES_DIR)/NdWaita-Oslo-Dark/gnome-shell/assets/

clean:
