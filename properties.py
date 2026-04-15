import bpy

from .general import *

COLLISION_TYPES = (
    ("AREA",            "Area",         "Area 3D node"          ),
    ("STATIC_BODY",     "StaticBody",   "StaticBody3D node"     ),
    ("RIGID_BODY",      "RigidBody",    "RigidBody3D node"      ),
    ("CHARACTER_BODY",  "CharacterBody", "CharacterBody3D node" )
)

class GOBLEND_CollisionProperties(bpy.types.PropertyGroup):
    has_collision: bpy.props.BoolProperty(
        name="Has Collision",
        default=False
    )
    collision_only: bpy.props.BoolProperty(
        name="Collision Only",
        default=False
    )
    collision_type: bpy.props.EnumProperty(
        name="Collision Type",
        items=COLLISION_TYPES,
        default="STATIC_BODY"
    )

class GOBLEND_ExportProperties(bpy.types.PropertyGroup):
    export_path: bpy.props.StringProperty(
        name="Export Path",
        subtype="DIR_PATH"
    )

class GOBLEND_ObjectProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    collision: bpy.props.PointerProperty(type=GOBLEND_CollisionProperties)

class GOBLEND_CollectionProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    export: bpy.props.PointerProperty(type=GOBLEND_ExportProperties)