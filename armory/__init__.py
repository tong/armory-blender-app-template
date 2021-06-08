
import bpy
from bpy.app.handlers import persistent

@persistent
def load_handler(dummy):
    #bpy.ops.preferences.addon_enable(module="armory")
    bpy.ops.object.mode_set(mode='OBJECT')
    #bpy.ops.object.mode_set(mode='SCULPT')

def register():
    bpy.app.handlers.load_factory_startup_post.append(load_handler)

def unregister():
    bpy.app.handlers.load_factory_startup_post.remove(load_handler)
