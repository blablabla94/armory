from arm.logicnode.arm_nodes import *

class SetVisibleNode(ArmLogicTreeNode):
    """Sets whether the given object is visible.

    @seeNode Get Object Visible"""
    bl_idname = 'LNSetVisibleNode'
    bl_label = 'Set Object Visible'
    arm_section = 'props'
    arm_version = 1

    property0: EnumProperty(
        items = [('Object', 'Object', 'Object'),
                 ('Mesh', 'Mesh', 'Mesh'),
                 ('Shadow', 'Shadow', 'Shadow'),
                 ],
        name='', default='Object')

    def init(self, context):
        super(SetVisibleNode, self).init(context)
        self.add_input('ArmNodeSocketAction', 'In')
        self.add_input('ArmNodeSocketObject', 'Object')
        self.add_input('NodeSocketBool', 'Visible')
        self.add_input('NodeSocketBool', 'Children')
        self.add_output('ArmNodeSocketAction', 'Out')

    def draw_buttons(self, context, layout):
        layout.prop(self, 'property0')
