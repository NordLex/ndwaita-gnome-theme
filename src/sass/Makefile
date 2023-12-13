include ../Makefile.inc

THEMES_DIR=../../themes/

.PHONY: build clean

build: $(COLOR_VARIANTS) Oslo

$(COLOR_VARIANTS):
	mkdir -p $(THEMES_DIR)/NdWaita-$@-Light/gnome-shell
	mkdir -p $(THEMES_DIR)/NdWaita-$@-Dark/gnome-shell
	mkdir -p $(THEMES_DIR)/NdWaita-$@-Darkest/gnome-shell
	sed -e '/$$selected_bg_color/c $$selected_bg_color: $(COLOR_$@);' \
	    -e '/$$selected_fg_color/c $$selected_fg_color: $(TEXT_COLOR_$@);' gnome-shell.scss | $(SCSS) > $(THEMES_DIR)/NdWaita-$@-Light/gnome-shell/gnome-shell.css
	sed -e '/$$selected_bg_color/c $$selected_bg_color: $(COLOR_$@);' \
	    -e '/$$selected_fg_color/c $$selected_fg_color: $(TEXT_COLOR_$@);' gnome-shell-dark.scss | $(SCSS) > $(THEMES_DIR)/NdWaita-$@-Dark/gnome-shell/gnome-shell.css
	sed -e '/$$selected_bg_color/c $$selected_bg_color: $(COLOR_$@);' \
	    -e '/$$selected_fg_color/c $$selected_fg_color: $(TEXT_COLOR_$@);' gnome-shell-darkest.scss | $(SCSS) > $(THEMES_DIR)/NdWaita-$@-Darkest/gnome-shell/gnome-shell.css

Oslo:
	mkdir -p $(THEMES_DIR)/NdWaita-Oslo/gnome-shell
	mkdir -p $(THEMES_DIR)/NdWaita-Oslo-Dark/gnome-shell
	$(SCSS) gnome-shell-oslo.scss > $(THEMES_DIR)/NdWaita-Oslo/gnome-shell/gnome-shell.css
	$(SCSS) gnome-shell-oslo-dark.scss > $(THEMES_DIR)/NdWaita-Oslo-Dark/gnome-shell/gnome-shell.css

clean:
