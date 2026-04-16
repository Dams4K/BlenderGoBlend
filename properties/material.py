import bpy

SHADING_MODE = (
    ("UNSHADED", "Unshaded", "The object will not receive shadows. This is the fastest to render, but it disables all interactions with lights."),
    ("PER_PIXEL", "Per-Pixel", "The object will be shaded per pixel. Useful for realistic shading effects."),
    ("PER_VERTEX", "Per-Vertex", "The object will be shaded per vertex. Useful when you want cheaper shaders and do not care about visual quality.")
)

class GOBLEND_MaterialsProperties(bpy.types.PropertyGroup):
    shade_mode: bpy.props.EnumProperty(
        name="Shade Mode",
        items=SHADING_MODE,
        default="PER_PIXEL"
    )
