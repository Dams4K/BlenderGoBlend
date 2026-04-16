import bpy

class GOBLEND_OT_AddCollision(bpy.types.Operator):
    bl_idname = "goblend.add_collision"
    bl_label = "Add Collision"

    def execute(self, context):
        obj = context.object
        obj.goblend.collisions.add()
        return {'FINISHED'}


class GOBLEND_OT_RemoveCollision(bpy.types.Operator):
    bl_idname = "goblend.remove_collision"
    bl_label = "Remove Collision"

    def execute(self, context):
        obj = context.object
        props = obj.goblend
        props.collisions.remove(props.collision_index)
        props.collision_index = max(0, props.collision_index - 1)
        return {'FINISHED'}