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

COLLISION_SHAPE = (
    ("TRIMESH", "Trimesh", """A 3D trimesh shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

Being just a collection of interconnected triangles, ConcavePolygonShape3D is the most freely configurable single 3D shape. It can be used to form polyhedra of any nature, or even shapes that don't enclose a volume. However, ConcavePolygonShape3D is hollow even if the interconnected triangles do enclose a volume, which often makes it unsuitable for physics or detection.

Note: When used for collision, ConcavePolygonShape3D is intended to work with static CollisionShape3D nodes like StaticBody3D and will likely not behave well for CharacterBody3Ds or RigidBody3Ds in a mode other than Static.

Warning: Physics bodies that are small have a chance to clip through this shape when moving fast. This happens because on one frame, the physics body may be on the "outside" of the shape, and on the next frame it may be "inside" it. ConcavePolygonShape3D is hollow, so it won't detect a collision.

Performance: Due to its complexity, ConcavePolygonShape3D is the slowest 3D collision shape to check collisions against. Its use should generally be limited to level geometry. For convex geometry, ConvexPolygonShape3D should be used. For dynamic physics bodies that need concave collision, several ConvexPolygonShape3Ds can be used to represent its collision by using convex decomposition; see ConvexPolygonShape3D's documentation for instructions."""),
    ("CONVEX", "Convex", """A 3D convex polyhedron shape, intended for use in physics. Usually used to provide a shape for a CollisionShape3D.

ConvexPolygonShape3D is solid, which means it detects collisions from objects that are fully inside it, unlike ConcavePolygonShape3D which is hollow. This makes it more suitable for both detection and physics.

Convex decomposition: A concave polyhedron can be split up into several convex polyhedra. This allows dynamic physics bodies to have complex concave collisions (at a performance cost) and can be achieved by using several ConvexPolygonShape3D nodes. To generate a convex decomposition from a mesh, select the MeshInstance3D node, go to the Mesh menu that appears above the viewport, and choose Create Multiple Convex Collision Siblings. Alternatively, MeshInstance3D.create_multiple_convex_collisions() can be called in a script to perform this decomposition at run-time.

Performance: ConvexPolygonShape3D is faster to check collisions against compared to ConcavePolygonShape3D, but it is slower than primitive collision shapes such as SphereShape3D and BoxShape3D. Its use should generally be limited to medium-sized objects that cannot have their collision accurately represented by primitive shapes."""),
    ("BOUNDARIES", "Boundaries", "Box shape"),
)

SHADING_MODE = (
    ("UNSHADED", "Unshaded", "The object will not receive shadows. This is the fastest to render, but it disables all interactions with lights."),
    ("PER_PIXEL", "Per-Pixel", "The object will be shaded per pixel. Useful for realistic shading effects."),
    ("PER_VERTEX", "Per-Vertex", "The object will be shaded per vertex. Useful when you want cheaper shaders and do not care about visual quality.")
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
    collision_shape: bpy.props.EnumProperty(
        name="Shape",
        items=COLLISION_SHAPE,
        default="TRIMESH"
    )
    color: bpy.props.FloatVectorProperty(
        name="Color",
        subtype="COLOR",
        size=4,
        min=0.0,
        max=1.0,
        default=(0.0, 0.319, 0.448, 0.42)
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
    shade_mode: bpy.props.EnumProperty(
        name="Shade Mode",
        items=SHADING_MODE,
        default="PER_PIXEL"
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