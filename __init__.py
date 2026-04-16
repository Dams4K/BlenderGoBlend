import bpy

from .operators import *
from .panels import *

from .properties import *

bl_info = {
    "name": "GoBlend",
    "author": "Dams4K",
    "version": (1, 0),
    "blender": (5, 1, 0)
}

ERROR = {"ERROR"}
INFO = {"INFO"}

CANCELLED = {"CANCELLED"}
FINISHED = {"FINISHED"}

classes = (
    GOBLEND_GeneralProperties,
    GOBLEND_CollisionProperties,
    GOBLEND_ExportProperties,
    GOBLEND_MaterialsProperties,
    GOBLEND_GeometryProperties,

    GOBLEND_ObjectProperties,
    GOBLEND_CollectionProperties,
    
    GOBLEND_PT_ObjectSettings,
    GOBLEND_PT_ObjectSettings_Collisions,
    GOBLEND_PT_ObjectSettings_Materials,
    GOBLEND_PT_ObjectSettings_Geometry,
    GOBLEND_PT_CollectionSettings,
    GOBLEND_OT_ExportCollection
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.goblend = bpy.props.PointerProperty(type=GOBLEND_ObjectProperties)
    bpy.types.Collection.goblend = bpy.props.PointerProperty(type=GOBLEND_CollectionProperties)

def unregister():
    del bpy.types.Object.goblend
    del bpy.types.Collection.goblend
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
if __name__ == "__main__":
    register()