import bpy
from .general import *

class GOBLEND_ExportProperties(bpy.types.PropertyGroup):
    export_path: bpy.props.StringProperty(
        name="Export Path",
        subtype="DIR_PATH"
    )

class GOBLEND_CollectionProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    export: bpy.props.PointerProperty(type=GOBLEND_ExportProperties)