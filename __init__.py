import bpy

# from properties import Property

class Property:
    def __init__(self, var_name: str, name: str, clazz, **kwargs):
        self.var_name = var_name
        self.name = name
        self.property = clazz(name=name, **kwargs)

COLLISION_TYPES = (
    ("AREA",            "Area",         "Area 3D node"          ),
    ("STATIC_BODY",     "StaticBody",   "StaticBody3D node"     ),
    ("RIGID_BODY",      "RigidBody",    "RigidBody3D node"      ),
    ("CHARACTER_BODY",  "CharacterBody", "CharacterBody3D node" )
)

has_collision = Property(
    "has_collision",
    "Has Collision",
    bpy.props.BoolProperty,
    default=False
)

collision_type = Property(
    "collision_type",
    "Collision Type",
    bpy.props.EnumProperty,
    items=COLLISION_TYPES,
    default="STATIC_BODY"
)

class GOBLEND_PT_GodotSettings(bpy.types.Panel):
    bl_label = "Godot Settings"
    bl_idname = "GOBLEND_PT_GodotSettings"
    bl_space_type = "PROPERTIES"
    bl_region_type = "WINDOW"
    bl_context = "object"

    def draw(self, context):
        layout = self.layout
        obj = context.object

        layout.prop(obj, has_collision.var_name)

        row = layout.row()
        row.enabled = obj.has_collision
        row.prop(obj, collision_type.var_name)

def register():
    bpy.types.Object.has_collision = has_collision.property
    bpy.types.Object.collision_type = collision_type.property

    bpy.utils.register_class(GOBLEND_PT_GodotSettings)

def unregister():
    del bpy.types.Object.has_collision
    del bpy.types.Object.collision_type
    
    bpy.utils.unregister_class(GOBLEND_PT_GodotSettings)
    
if __name__ == "__main__":
    register()