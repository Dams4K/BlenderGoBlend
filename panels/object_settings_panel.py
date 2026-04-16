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
        
        layout.prop(props, "layers")

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

        layout.prop(props.collision, "has_collision")

        collision_only_row = layout.row()
        collision_only_row.enabled = props.collision.has_collision
        collision_only_row.prop(props.collision, "collision_only")

        color_row = layout.row()
        color_row.enabled = props.collision.has_collision
        color_row.prop(props.collision, "color")
        
        shape_row = layout.row()
        shape_row.enabled = props.collision.has_collision
        shape_row.prop(props.collision, "collision_shape")

        layer_row = layout.row()
        layer_row.enabled = props.collision.has_collision
        layer_row.prop(props.collision, "layer")
        mask_row = layout.row()
        mask_row.enabled = props.collision.has_collision
        mask_row.prop(props.collision, "mask")

        collision_type_row = layout.row()
        collision_type_row.enabled = props.collision.has_collision
        collision_type_row.prop(props.collision, "collision_type")

class GOBLEND_PT_MaterialsSettings(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Godot Settings"
    bl_idname = "GOBLEND_PT_MaterialsSettings"
    bl_context = "material"

    def draw(self, context):
        layout = self.layout
        mat = context.material

        props = mat.goblend

        layout.prop(props, "unshaded")
    
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