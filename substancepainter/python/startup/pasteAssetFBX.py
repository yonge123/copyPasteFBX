import os

# Substance 3D Painter modules
import substance_painter.ui
import substance_painter.export
import substance_painter.project
import substance_painter.textureset

# PySide module to build custom UI
try:
    from PySide6.QtGui import QAction
except Exception as e:
    from PySide2.QtWidgets import QAction
    print(e)


plugin_widgets = []


def getFbxPath():
    userProfileDir = os.getenv("USERPROFILE")
    saveDir = '{}/.copyPasteAssetFBX/exportAssetFBX'.format(userProfileDir)
    if not os.path.isdir(saveDir):
        os.makedirs(saveDir)
    fbxFile = '{}/exportAssetFBX.fbx'.format(saveDir)
    return saveDir, fbxFile


def importFBX():
    # A few declarations used in this example:
    workFolder, meshFile = getFbxPath()
    templateFile = workFolder+"/MyTemplate.spt"
    mySettings = substance_painter.project.Settings(
        import_cameras=True,
        default_texture_resolution=4096,
        normal_map_format=substance_painter.project.NormalMapFormat.OpenGL)

    # This should print nothing if you just opened Substance 3D Painter,
    # since no project is opened:
 
    if substance_painter.project.is_open():
        print("There is already a project opened!")


    # Create a project from a file, import cameras from the file, and set up
    # the project for OpenGL:
    substance_painter.project.create(mesh_file_path=meshFile, settings=mySettings)

    # Show the current state of the project:
    if substance_painter.project.is_open():
        print("The project was successfully created.")
    if substance_painter.project.needs_saving():
        print("The project hasn't been saved yet.")
    # At this stage the file path is empty:
    print("The file path of the project is: '{0}'".format(substance_painter.project.file_path()))


def start_plugin():
    # Create a text widget for a menu
    Action = QtWidgets.QAction("Import Asset FBX",
                                triggered=importFBX)

    # Add this widget to the existing File menu of the application
    substance_painter.ui.add_action(
        substance_painter.ui.ApplicationMenu.File,
        Action )

    # Store the widget for proper cleanup later when stopping the plugin
    plugin_widgets.append(Action)


def close_plugin():
    # Remove all widgets that have been added to the UI
    for widget in plugin_widgets:
        substance_painter.ui.delete_ui_element(widget)

    plugin_widgets.clear()


if __name__ == "__main__":
    start_plugin()
