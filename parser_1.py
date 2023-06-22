from ast import *

from ast_1 import AssignmentNode, ExpressionNode

class Parser:
    def p_program_empty(self, p):
        """
        """
    def p_program_statements(self,p):
        """
        """

    def p_statements_command(self, p):
        """"""
    def p_command_command(self,p):
        """"""

    def p_command_assignment_expression(self, p):
        assign_node = AssignmentNode()
        assign_node.set_nodeLabel("ASSIGNMENT")
        assign_node.set_target_id("v_" + p[1])
        assign_node.set_treeDepth(self.get_tree_depth())
        assign_node.setParent(self.tree.get_current_node())

        self.tree.get_current_node().add_child(assign_node)

        expression_node = ExpressionNode()