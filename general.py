import bpy

ERROR = {"ERROR"}
INFO = {"INFO"}

CANCELLED = {"CANCELLED"}
FINISHED = {"FINISHED"}

class GOBLEND_GeneralProperties(bpy.types.PropertyGroup):
    exported: bpy.props.BoolProperty(
        name="Exported",
        default=True
    )