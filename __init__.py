import bpy

from . import origin_to_selected
from . import reload_images
from . import separate_clone
from . import seams_from_sharp
from . import toggle_subd


bl_info = {
    'name': "Miniukof Blender Utils",
    'description': "Collection of simple utilities.",
    'author': "miniukof",
    'version': (0, 0, 1),
    'blender': (2, 77, 0),
    'category': "User",
}


def register():
    bpy.utils.register_module(__name__)

def unregister():
    bpy.utils.unregister_module(__name__)
