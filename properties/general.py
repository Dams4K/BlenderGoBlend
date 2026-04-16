import bpy

class GOBLEND_GeneralProperties(bpy.types.PropertyGroup):
    exported: bpy.props.BoolProperty(
        name="Exported",
        default=True
    )