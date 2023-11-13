import maya.cmds as cmds

def change_color(color):
    selected_objects = cmds.ls(selection=True)

    if not selected_objects:
        cmds.error("Select object(s) before running change_color().")

    if color < 0 or color > 31:
        color = 0
        cmds.warning("Color argument must be within the range of 0 to 31. Value set to default of 0.")

    for obj in selected_objects:
        shapes = cmds.listRelatives(obj, shapes=True) or []

        for shape in shapes:
            cmds.setAttr(f"{shape}.overrideEnabled", 1)
            cmds.setAttr(f"{shape}.overrideColor", color)

change_color(17)