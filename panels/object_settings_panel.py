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

        collision_only_row = layout.row()
        collision_only_row.enabled = props.collision.has_collision
        collision_only_row.prop(props.collision, "collision_only")

        collision_type_row = layout.row()
        collision_type_row.enabled = props.collision.has_collision
        collision_type_row.prop(props.collision, "collision_type")