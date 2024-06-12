import os
import bpy


def getFbxPath():
    userProfileDir = os.getenv("USERPROFILE")
    saveDir = '{}/.copyPasteAssetFBX/exportAssetFBX'.format(userProfileDir)
    if not os.path.isdir(saveDir):
        os.makedirs(saveDir)
    fbxFile = '{}/exportAssetFBX.fbx'.format(saveDir)
    return fbxFile


def importFBX():
    fbxFile = getFbxPath()
    if os.path.isfile(fbxFile):
        bpy.ops.import_scene.fbx(filepath=fbxFile, anim_offset=0.0)
    
    
def exportFBX():
    fbxFile = getFbxPath()
    bpy.ops.export_scene.fbx(filepath=fbxFile, 
                             use_selection=True, 
                             use_mesh_modifiers=False, 
                             use_mesh_modifiers_render=False)


def copyAssetFBX():
    exportFBX()
    
    
def pasteAssetFBX():
    importFBX()


def iterHierarchyObjAll(obj):
    """
    blender object
    iter hierarchy object where object type is EMPTY or MESH
    and iter obj it self
    """
    objList = [obj, ]
    while objList:
        o = objList.pop(0)
        children = o.children
        if children:
            for child in children:
                objList.append(child)
        yield o


class AST_COPY_ASSET_FBX(bpy.types.Operator):
    """
        Copy Asset FBX
    """
    bl_idname = "ast.copy_asset_fbx"
    bl_label = "Copy Asset FBX"
    bl_options = {"REGISTER", "UNDO"}

    
    def execute(self, context):
        bpy.ops.ed.undo_push()
        selected_objects = context.selected_objects
        if selected_objects:
            for obj in selected_objects:
                for o in iterHierarchyObjAll(obj):
                    try:
                        o.select_set(True)
                    except Exception as e:
                        msg = str(e)
                        self.report({'INFO'}, msg)
        
        copyAssetFBX()
        return {'FINISHED'}
    
    
class AST_PASTE_ASSET_FBX(bpy.types.Operator):
    """
        Paste Asset FBX
    """
    bl_idname = "ast.paste_asset_fbx"
    bl_label = "Paste Asset FBX"
    bl_options = {"REGISTER", "UNDO"}

    
    def execute(self, context):
        bpy.ops.ed.undo_push()
        pasteAssetFBX()
        return {'FINISHED'}



class AST_PT_COPY_PASTE_FBX(bpy.types.Panel):
    """Asset Tools"""
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = "COPY_PASTE_FBX"
    bl_label = "COPY_PASTE_FBX"
    
    def draw(self, context):

        layout = self.layout

        row = layout.row()
        row.operator("ast.copy_asset_fbx", text="Copy FBX", icon="EXPORT")
        row.operator("ast.paste_asset_fbx", text="Paste FBX", icon="IMPORT")


classes = (
    AST_COPY_ASSET_FBX,
    AST_PASTE_ASSET_FBX,
    AST_PT_COPY_PASTE_FBX
)


def register():
    for cls in classes:
        bpy.utils.register_class(cls)


def unregister():
    for cls in reversed(classes):
        bpy.utils.unregister_class(cls)
