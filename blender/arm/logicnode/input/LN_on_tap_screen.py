from arm.logicnode.arm_nodes import *

# Class OnTapScreen
class OnTapScreen(ArmLogicTreeNode):
    """Activates the output when the given tap action is done."""
    bl_idname = 'LNOnTapScreen'
    bl_label = 'On Tap Screen'
    arm_section = 'Input'
    arm_version = 1

    def init(self, context):
        super(OnTapScreen, self).init(context)
        self.add_input('NodeSocketFloat', 'Duration')
        self.inputs[-1].default_value = 0.3
        self.add_input('NodeSocketFloat', 'Interval')
        self.inputs[-1].default_value = 0.0
        self.add_input('NodeSocketInt', 'Repeat')
        self.inputs[-1].default_value = 2
        self.add_output('ArmNodeSocketAction', 'Done')
        self.add_output('ArmNodeSocketAction', 'Fail')
        self.add_output('ArmNodeSocketAction', 'Tap')
        self.add_output('NodeSocketInt', 'Tap Number')
        self.add_output('NodeSocketVector', 'Coords')
