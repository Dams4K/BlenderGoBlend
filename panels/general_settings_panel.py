import bpy

from ..general import *

class GOBLEND_PT_GeneralSettings:
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Godot Settings"
    bl_idname = "GOBLEND_PT_GeneralSettings"

    def draw(self, context):
        layout = self.layout
        target = self.get_target(context)
        if target is None: return

        props = target.goblend
        layout.prop(props.general, "exported")
        layout.separator()
    
    def get_target(self, context):
        if context.object: return context.object
        if context.collection: return context.collection
        return None


def gs_idname(name: str) -> str:
    return f"{GOBLEND_PT_GeneralSettings.bl_idname}_{name}"
