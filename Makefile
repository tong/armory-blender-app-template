PROJECT=armory
BLENDER_VERSION=2.93

BLENDER_DIR = $(HOME)/.config/blender/$(BLENDER_VERSION)
TPL_DIR = $(BLENDER_DIR)/scripts/startup/bl_app_templates_user
CFG_DIR = $(BLENDER_DIR)/config/$(PROJECT)

install:
	mkdir -p $(TPL_DIR)
	cp -r ./armory $(TPL_DIR)
	mkdir -p $(CFG_DIR)
	cp startup.blend userpref.blend $(CFG_DIR)

uninstall:
	rm -rf $(TPL_DIR)
	rm -rf $(CFG_DIR)
