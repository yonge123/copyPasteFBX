set /p maya_version="Maya 버전을 입력하세요 (기본값: 2022): "
set /p blender_version="Blender 버전을 입력하세요 (기본값: 3.6): "

if "%maya_version%"=="" (
    set maya_version=2022
)

if "%blender_version%"=="" (
    set blender_version=3.6
)


set blender_user_dir="%AppData%\Blender Foundation\Blender\%blender_version%"
set blender_startup_dir=%blender_user_dir%\scripts\startup
set blender_script_file=blender\copyPasteAssetFBX.py

if exist %blender_user_dir% (
    if exist %blender_startup_dir% (
        echo
    ) else (
        mkdir %blender_startup_dir%
    )

    copy %blender_script_file% %blender_startup_dir%
    explorer %blender_startup_dir% 
) else (
    echo The directory does not exist %blender_user_dir% 
    explorer %AppData%\Blender Foundation
)


set maya_user_dir=%UserProfile%\Documents\maya\%maya_version%
set maya_startup_dir=%maya_user_dir%\prefs\shelves
set maya_script_file=maya\shelf_CopyPasteAsset.mel

if exist %maya_user_dir% ( 
    if exist %maya_startup_dir% (
        echo
    ) else (
        mkdir %maya_startup_dir%
    )

    copy %maya_script_file% %maya_startup_dir%
    explorer %maya_startup_dir% 
) else (
    echo The directory does not exist %maya_user_dir% 
    explorer %UserProfile%\Documents\maya
)


set subpainter_user_dir="%UserProfile%\Documents\Adobe\Adobe Substance 3D Painter"
set subpainter_startup_dir=%subpainter_user_dir%\python\startup
set subpainter_script_file=substancepainter\python\startup\pasteAssetFBX.py

if exist %subpainter_user_dir% (
    if exist %subpainter_startup_dir% (
        echo
    ) else (
        mkdir %subpainter_startup_dir%
    )
    copy %subpainter_script_file% %subpainter_startup_dir%
    explorer %subpainter_startup_dir% 
) else (
    echo The directory does not exist %subpainter_user_dir% 
    explorer %UserProfile%\Documents\Adobe
)


pause
