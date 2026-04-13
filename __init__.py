import bpy

bl_info = {
    "name": "GoBlend",
    "author": "Dams4K",
    "version": (1, 0),
    "blender": (5, 1, 0)
}

ERROR = {"ERROR"}
INFO = {"INFO"}

CANCELLED = {"CANCELLED"}
FINISHED = {"FINISHED"}

COLLISION_TYPES = (
    ("AREA",            "Area",         "Area 3D node"          ),
    ("STATIC_BODY",     "StaticBody",   "StaticBody3D node"     ),
    ("RIGID_BODY",      "RigidBody",    "RigidBody3D node"      ),
    ("CHARACTER_BODY",  "CharacterBody", "CharacterBody3D node" )
)

class GOBLEND_GeneralProperties(bpy.types.PropertyGroup):
    exported: bpy.props.BoolProperty(
        name="Exported",
        default=True
    )

class GOBLEND_CollisionProperties(bpy.types.PropertyGroup):
    has_collision: bpy.props.BoolProperty(
        name="Has Collision",
        default=False
    )
    collision_type: bpy.props.EnumProperty(
        name="Collision Type",
        items=COLLISION_TYPES,
        default="STATIC_BODY"
    )

class GOBLEND_ExportProperties(bpy.types.PropertyGroup):
    export_path: bpy.props.StringProperty(
        name="Export Path",
        subtype="DIR_PATH"
    )

class GOBLEND_ObjectProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    collision: bpy.props.PointerProperty(type=GOBLEND_CollisionProperties)

class GOBLEND_CollectionProperties(bpy.types.PropertyGroup):
    general: bpy.props.PointerProperty(type=GOBLEND_GeneralProperties)
    export: bpy.props.PointerProperty(type=GOBLEND_ExportProperties)


def collection_resolve_export_path(collection):
    root = bpy.context.scene.collection
    return _export_path_walk_collection_tree(root.goblend.export.export_path, root, collection)

def _export_path_walk_collection_tree(inherited_path: str, current, target):
    if current == target:
        return inherited_path
    
    for child in current.children:
        current_path = child.goblend.export.export_path or inherited_path

        result = _export_path_walk_collection_tree(current_path, child, target)
        if result:
            return result
    
    return ""



class GOBLEND_OT_ExportCollection(bpy.types.Operator):
    bl_idname = "goblend.export_collection"
    bl_label = "Export"

    def execute(self, context):
        collection = context.collection
        if collection is None:
            self.report(ERROR, "No collection selected")
            return CANCELLED

        export_path = collection_resolve_export_path(collection)
        self.report(INFO, f"exported in: {export_path}")

        return FINISHED

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

classes = (
    GOBLEND_GeneralProperties,
    GOBLEND_CollisionProperties,
    GOBLEND_ExportProperties,

    GOBLEND_ObjectProperties,
    GOBLEND_CollectionProperties,
    
    GOBLEND_PT_ObjectSettings,
    GOBLEND_PT_CollectionSettings,
    GOBLEND_OT_ExportCollection
)

def register():
    for cls in classes:
        bpy.utils.register_class(cls)

    bpy.types.Object.goblend = bpy.props.PointerProperty(type=GOBLEND_ObjectProperties)
    bpy.types.Collection.goblend = bpy.props.PointerProperty(type=GOBLEND_CollectionProperties)

def unregister():
    del bpy.types.Object.goblend
    del bpy.types.Collection.goblend
    
    for cls in classes:
        bpy.utils.unregister_class(cls)
    
if __name__ == "__main__":
    register()