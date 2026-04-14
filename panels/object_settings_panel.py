import bpy

from ..general import *
from .general_settings_panel import *

class GOBLEND_PT_ObjectSettings(GOBLEND_PT_GeneralSettings, bpy.types.Panel):
    bl_idname = gs_idname("Object")
    bl_context = "object"

    def draw(self, context):
        GOBLEND_PT_GeneralSettings.draw(self, context)

        layout = self.layout
        obj = context.object

        props = obj.goblend

        layout.prop(props.collision, "has_collision")

        row = layout.row()
        row.enabled = props.collision.has_collision
        row.prop(props.collision, "collision_type")