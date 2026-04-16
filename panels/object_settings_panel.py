import bpy

from .general_settings_panel import *

class GOBLEND_PT_ObjectSettings(GOBLEND_PT_GeneralSettings, bpy.types.Panel):
    bl_idname = gs_idname("Object")
    bl_context = "object"
    
    def draw(self, context):
        GOBLEND_PT_GeneralSettings.draw(self, context)

        layout = self.layout
        obj = context.object

        props = obj.goblend
        
        layout.prop(props, "layers")

class GOBLEND_UL_Collisions(bpy.types.UIList):
    def draw_item(self, context, layout, data, item, icon, active_data, active_propname):
        layout.prop(item, "name", text="", emboss=False)

class GOBLEND_PT_ObjectSettings_Collisions(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Collisions"
    bl_idname = "GOBLEND_PT_ObjectSettings_Collisions"
    bl_parent_id = gs_idname("Object")

    def draw(self, context):
        layout = self.layout
        obj = context.object

        props = obj.goblend

        collision_only_row = layout.row()
        collision_only_row.enabled = len(props.collisions) > 0
        collision_only_row.prop(props, "collision_only")

        collisions_row = layout.row()
        collisions_row.template_list(
            "GOBLEND_UL_Collisions",
            "",
            props,
            "collisions",
            props,
            "collision_index"
        )

        col = collisions_row.column(align=True)
        col.operator("goblend.add_collision", icon='ADD', text="")
        col.operator("goblend.remove_collision", icon='REMOVE', text="")

        if props.collisions:
            item = props.collisions[props.collision_index]

            col = layout.column()
            
            col.prop(item, "color")
            col.prop(item, "type")
            col.prop(item, "shape")
            col.prop(item, "layer")
            col.prop(item, "mask")

    
class GOBLEND_PT_ObjectSettings_Geometry(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Geometry"
    bl_idname = "GOBLEND_PT_ObjectSettings_Geometry"
    bl_parent_id = gs_idname("Object")

    def draw(self, context):
        layout = self.layout
        obj = context.object

        props = obj.goblend

        layout.prop(props.geometry, "cast_shadow")