import bpy

from ..general import *
from .general_settings_panel import *


class GOBLEND_PT_CollectionSettings(GOBLEND_PT_GeneralSettings, bpy.types.Panel):
    bl_idname = gs_idname("Collection")
    bl_context = "collection"

    def draw(self, context):
        GOBLEND_PT_GeneralSettings.draw(self, context)

        layout = self.layout
        col = context.collection

        props = col.goblend

        layout.prop(props.export, "export_path")
        layout.operator("goblend.export_collection", text="Export")