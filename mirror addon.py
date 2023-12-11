bl_info = {
    "name": "Axis Mirror",
    "blender": (2, 80, 0),
    "category": "Object",
}

import bpy

class OBJECT_OT_axis_mirror(bpy.types.Operator):
    bl_idname = "object.axis_mirror"
    bl_label = "Axis Mirror"
    bl_options = {'REGISTER', 'UNDO'}

    axis: bpy.props.StringProperty()

    def execute(self, context):
        obj = bpy.context.active_object

        # Mirror modifiyesi ekleyerek objeyi yansıtma
        mirror_modifier = obj.modifiers.new(name="Mirror", type='MIRROR')
        
        if self.axis == 'X':
            mirror_modifier.use_axis[0] = True
        elif self.axis == 'Y':
            mirror_modifier.use_axis[1] = True
        elif self.axis == 'Z':
            mirror_modifier.use_axis[2] = True

        return {'FINISHED'}


class OBJECT_PT_axis_mirror_panel(bpy.types.Panel):
    bl_idname = "PT_Axis_Mirror_Panel"
    bl_label = "Axis Mirror"
    bl_space_type = 'VIEW_3D'
    bl_region_type = 'UI'
    bl_category = 'Tools'
    bl_context = "objectmode"

    def draw(self, context):
        layout = self.layout

        layout.label(text="Mirror Options:")

        row = layout.row()
        row.operator("object.axis_mirror", text="X Axis").axis = 'X'
        row.operator("object.axis_mirror", text="Y Axis").axis = 'Y'
        row.operator("object.axis_mirror", text="Z Axis").axis = 'Z'


def register():
    bpy.utils.register_class(OBJECT_OT_axis_mirror)
    bpy.utils.register_class(OBJECT_PT_axis_mirror_panel)


def unregister():
    bpy.utils.unregister_class(OBJECT_OT_axis_mirror)
    bpy.utils.unregister_class(OBJECT_PT_axis_mirror_panel)


if __name__ == "__main__":
    register()
