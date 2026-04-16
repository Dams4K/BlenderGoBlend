import bpy

class GOBLEND_PT_MaterialsSettings(bpy.types.Panel):
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_label = "Godot Settings"
    bl_idname = "GOBLEND_PT_MaterialsSettings"
    bl_context = "material"

    @classmethod
    def poll(cls, context):
        return context.material is not None

    def draw(self, context):
        layout = self.layout
        mat = context.material
        if mat == None:
            return

        props = mat.goblend

        layout.prop(props, "shade_mode")