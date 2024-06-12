import os
import maya.cmds as cmds


def getFbxPath():
    userProfileDir = os.getenv("USERPROFILE")
    saveDir = '{}/.copyPasteAssetFBX/exportAssetFBX'.format(userProfileDir)
    if not os.path.isdir(saveDir):
        os.makedirs(saveDir)
    fbxFile = '{}/exportAssetFBX.fbx'.format(saveDir)
    return fbxFile


def loadPlugin(pluginName):
    isLoaded = cmds.pluginInfo(pluginName, q=True, loaded=True)
    if not isLoaded:
        cmds.loadPlugin(pluginName)


def loadPluginFbx():
    plugins = ["fbxmaya", "gameFbxExporter"]
    for plugin in plugins:
        loadPlugin(plugin)


def importFBX():
    loadPluginFbx()
    fbxFile = getFbxPath()
    if os.path.isfile(fbxFile):
        cmds.file(fbxFile, i=True, type="FBX", ignoreVersion=True, mergeNamespacesOnClash=False, options="fbx", pr=True, importFrameRate=True, importTimeRange="override")


def exportFBX():
    loadPluginFbx()
    fbxFile = getFbxPath()
    cmds.file(fbxFile, force=True, options="groups=1;ptgroups=1;materials=0;smoothing=1;normals=1", typ="FBX export", pr=True, es=True)


def copyAssetFBX():
    exportFBX()


def pasteAssetFBX():
    importFBX()


if __name__ == '__main__':
    copyAssetFBX()
    # pasteAssetFBX()
