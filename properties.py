import bpy

from .general import *

COLLISION_TYPES = (
    ("AREA",            "Area",         "Area 3D node"          ),
    ("STATIC_BODY",     "StaticBody",   "StaticBody3D node"     ),
    ("RIGID_BODY",      "RigidBody",    "RigidBody3D node"      ),
    ("CHARACTER_BODY",  "CharacterBody", "CharacterBody3D node" )
)

CAST_SHADOW_TYPES = (
    ("OFF", "Off", "Will not cast any shadows. Use this to improve performance for small geometry that is unlikely to cast noticeable shadows (such as debris)."),
    ("ON", "On", """Will cast shadows from all visible faces in the GeometryInstance3D.

Will take culling into account, so faces not being rendered will not be taken into account when shadow casting."""),
    ("DOUBLE_SIDED", "Double-Sided", """Will cast shadows from all visible faces in the GeometryInstance3D.

Will not take culling into account, so all faces will be taken into account when shadow casting."""),
    ("SHADOWS_ONLY", "Shadows Only", """Will only show the shadows casted from this object.

In other words, the actual mesh will not be visible, only the shadows casted from the mesh will be."""),
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
    layer: bpy.props.BoolVectorProperty(
        name="Layer",
        size=32,
        subtype='LAYER',
        default= (True,) + (False,) * 31
    )
    mask: bpy.props.BoolVectorProperty(
        name="Mask",
        size=32,
        subtype='LAYER',
        default= (True,) + (False,) * 31
    )

class GOBLEND_ExportProperties(bpy.types.PropertyGroup):
    export_path: bpy.props.StringProperty(
        name="Export Path",
        subtype="DIR_PATH"
    )

class GOBLEND_MaterialsProperties(bpy.types.PropertyGroup):
    unshaded: bpy.props.BoolProperty(
        name="Unshaded",
        default=False
    )

class GOBLEND_GeometryProperties(bpy.types.PropertyGroup):
    cast_shadow: bpy.props.EnumProperty(
        name="Cast Shadow",
        items=CAST_SHADOW_TYPES,
        default="ON"
    )

class GOBLEND_ObjectProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    collision: bpy.props.PointerProperty(type=GOBLEND_CollisionProperties)
    materials: bpy.props.PointerProperty(type=GOBLEND_MaterialsProperties)
    layers: bpy.props.BoolVectorProperty(
        name="Layers",
        size=20,
        subtype='LAYER',
        default= (True,) + (False,) * 19
    )
    geometry: bpy.props.PointerProperty(type=GOBLEND_GeometryProperties)

class GOBLEND_CollectionProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    export: bpy.props.PointerProperty(type=GOBLEND_ExportProperties)