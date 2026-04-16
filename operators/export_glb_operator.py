import bpy, os

from ..helper import *

def collection_resolve_export_dir_path(collection):
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

        if not collection.goblend.general.exported:
            self.report(ERROR, "This collection can't be exported")
            return CANCELLED
        
        export_dir_path = collection_resolve_export_dir_path(collection)
        export_path = os.path.join(export_dir_path, f"{collection.name}.glb")

        previous_selection = context.selected_objects

        bpy.ops.object.select_all(action="DESELECT")
        for obj in collection.objects:
            if obj.goblend.general.exported:
                obj.select_set(True)
        
        if collection.objects:
            context.view_layer.objects.active = collection.objects[0]

        bpy.ops.export_scene.gltf(
            filepath=export_path,
            export_format="GLTF_SEPARATE",

            use_selection=True,
            use_active_collection=False,
            
            export_yup=True,
            export_apply=True,

            export_texcoords=True,
            export_normals=True,
            export_tangents=False,

            export_materials="EXPORT",
            export_vertex_color="ACTIVE",

            export_texture_dir="textures/",

            export_extras=True,

            export_cameras=False,

            export_skins=True,
            export_leaf_bone=False,

            export_animations=True,
            export_force_sampling=True,

            export_optimize_animation_size=True,

            check_existing=False,
        )

        for col in collection.children:
            with context.temp_override(collection=col):
                bpy.ops.goblend.export_collection()

        bpy.ops.object.select_all(action="DESELECT")
        for obj in previous_selection:
            obj.select_set(True)

        self.report(INFO, f"exported in: {export_path}")
        return FINISHED