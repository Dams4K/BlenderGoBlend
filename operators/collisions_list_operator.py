import bpy

class GOBLEND_OT_AddCollision(bpy.types.Operator):
    bl_idname = "goblend.add_collision"
    bl_label = "Add Collision"

    def execute(self, context):
        obj = context.object
        obj.goblend.collisions.list.add()
        return {'FINISHED'}


class GOBLEND_OT_RemoveCollision(bpy.types.Operator):
    bl_idname = "goblend.remove_collision"
    bl_label = "Remove Collision"

    def execute(self, context):
        obj = context.object
        props = obj.goblend
        props.collisions.list.remove(props.collisions.list_index)
        props.collisions.list_index = max(0, props.collisions.list_index - 1)
        return {'FINISHED'}