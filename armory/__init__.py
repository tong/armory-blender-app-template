
import bpy, os
from bpy.app.handlers import persistent
# from addon_utils import check,paths,enable

@persistent
def load_post_handler(_):
    sdk_path = os.getenv('ARMSDK')
    bpy.ops.preferences.addon_enable(module="armory")
    bpy.context.preferences.addons['armory'].preferences.sdk_path = sdk_path
    bpy.ops.wm.save_userpref()

def register():
    bpy.app.handlers.load_post.append(load_post_handler)
    # bpy.app.handlers.load_post.append(load_pre_handler)
    # bpy.app.handlers.load_factory_preferences_post.append(load_handler_for_preferences)
    # bpy.app.handlers.load_factory_startup_post.append(load_handler_for_startup)

def unregister():
    bpy.app.handlers.load_post.remove(load_post_handler)
    # bpy.app.handlers.load_post.remove(load_pre_handler)
    # bpy.app.handlers.load_factory_preferences_post.remove(load_handler_for_preferences)
    # bpy.app.handlers.load_factory_startup_post.remove(load_handler_for_startup)
