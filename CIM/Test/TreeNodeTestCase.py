#------------------------------------------------------------------------------
# Copyright (C) 2009 Richard W. Lincoln
#
# This program is free software; you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation; version 2 dated June, 1991.
#
# This software is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANDABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program; if not, write to the Free Software Foundation,
# Inc., 51 Franklin St, Fifth Floor, Boston, MA 02110-1301 USA
#------------------------------------------------------------------------------

""" Test case for CIM adapters.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import sys
import unittest
import logging

from os.path import join, dirname

from enthought.traits.api import HasTraits, Str, List, Property, Instance

from enthought.traits.ui.api \
    import View, Item, Group, TreeEditor, TreeNode

from enthought.traits.ui.menu import Action, Menu

from CIM import Element

from CIM.Core \
    import GeographicalRegion, SubGeographicalRegion, Substation, \
    VoltageLevel, Bay

from CIM.Wires import Line

from CIM.CIMReader import read_cim

#from CIM13TreeEditor import tree_nodes, GeographicalRegionTreeNode, \
#    SubGeographicalRegionTreeNode, IdentifiedObjectTreeNode

from CIM13r19TreeNodeEditor \
    import tree_nodes, GeographicalRegion_TreeNode, \
    SubGeographicalRegion_TreeNode

#-------------------------------------------------------------------------------
#  Constants:
#-------------------------------------------------------------------------------

RDFXML_FILE = join(dirname(__file__), "Data", "10Bus.xml")

#------------------------------------------------------------------------------
#  "SubstationTreeNode" class:
#------------------------------------------------------------------------------

#class SubstationTreeNode(TreeNode):
#    """ Defines a tree node for a SubGeographicalRegion.
#    """
#
#    # Name of trait containing children (if '', the node is a leaf).
##    children = Str("Substations")
#
#    # Name of a trait containing a label.
#    label = Str("name")
#
#    tooltip = Str("=A collection of equipment for purposes other than generation or utilization, through which electric energy in bulk is passed for the purposes of switching or modifying its characteristics.")
#
#    # Name to use for a new instance.
#    name = Str("Substation")
#
#    # List of object classes than can be added or copied.
#    add = [VoltageLevel, Bay]
#
#    # List of object classes that can be moved.
#    move = [VoltageLevel, Bay]
#
#    # List of object classes and/or interfaces that the node applies to.
#    node_for = [Substation]
#
#    # Function for handling double-clicking an object
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")
#
#
#    def allows_children ( self, object ):
#        """ Returns whether this object can have children.
#        """
#        return True
#
#
#    def get_children ( self, object ):
#        """ Gets the object's children.
#        """
#        return ( getattr(object, "Contains_VoltageLevels") + \
#                 getattr(object, "Contains_Bays") )
#
#
#    def append_child ( self, object, child ):
#        """ Appends a child to the object's children.
#        """
#        if isinstance(child, VoltageLevel):
#            getattr( object, "Contains_VoltageLevels" ).append( child )
#        elif isinstance(child, Bay):
#            getattr( object, "Contains_Bays" ).append( child )
#        else:
#            pass

#------------------------------------------------------------------------------
#  "SubGeographicalRegionTreeNode" class:
#------------------------------------------------------------------------------

#class SubGeographicalRegionTreeNode(TreeNode):
#    """ Defines a tree node for a SubGeographicalRegion.
#    """
#
#    # Name of trait containing children (if '', the node is a leaf).
##    children = Str("Substations")
#
#    # Name of a trait containing a label.
#    label = Str("name")
#
#    tooltip = Str("=A subset of a geographical region of a power system network model.")
#
#    # Name to use for a new instance.
#    name = Str("SubGeographicalRegion")
#
#    # List of object classes than can be added or copied.
#    add = [Substation, Line]
#
#    # List of object classes that can be moved.
#    move = [Substation, Line]
#
#    # List of object classes and/or interfaces that the node applies to.
#    node_for = [SubGeographicalRegion]
#
#    # Function for handling double-clicking an object
#    on_dclick = lambda obj: obj.edit_traits(kind="livemodal")
#
#
#    def allows_children ( self, object ):
#        """ Returns whether this object can have children.
#        """
#        return True
#
#
#    def get_children ( self, object ):
#        """ Gets the object's children.
#        """
#        return ( getattr(object, "Substations") + getattr(object, "Lines") )
#
#
#    def append_child ( self, object, child ):
#        """ Appends a child to the object's children.
#        """
#        if isinstance(child, Substation):
#            getattr( object, "Substations" ).append( child )
#        elif isinstance(child, Line):
#            getattr( object, "Lines" ).append( child )
#        else:
#            pass

#------------------------------------------------------------------------------
#  CIM Tree Editor:
#------------------------------------------------------------------------------

#cim_tree_editor = TreeEditor(
#    nodes = [
#        TreeNode(node_for=[GeographicalRegion], label="name"),
#        TreeNode(node_for=[GeographicalRegion], label="=Regions",
#                 children="Regions"),
##        TreeNode(node_for=[SubGeographicalRegion], label="name"),
#        SubGeographicalRegionTreeNode(),
##        TreeNode(node_for=[SubGeographicalRegion], label="=Substations",
##                 children="Substations"),
##        TreeNode(node_for=[Substation], label="name"),
#        SubstationTreeNode(),
#        TreeNode(node_for=[Line], label="name"),
#        TreeNode(node_for=[Bay], label="name"),
#        TreeNode(node_for=[VoltageLevel], label="name")
#    ],
#    editable=True
#)

#------------------------------------------------------------------------------
#  "RegionContainer" class:
#------------------------------------------------------------------------------

class RegionContainer(HasTraits):

    elements = List( Instance(Element) )

    regions = Property(depends_on=["elements", "elements_items"])

    def _get_regions(self):
        """ Property getter.
        """
        return [e for e in self.elements if isinstance(e, GeographicalRegion)]

#------------------------------------------------------------------------------
#  "CommonInformationModel" class:
#------------------------------------------------------------------------------

class CommonInformationModel(HasTraits):

    # The root of the model tree:
    root = Instance(HasTraits)

    # The traits view to display:
    view = View(
        Item('root',
            editor=TreeEditor(
                nodes=[TreeNode(node_for=[RegionContainer], label="=Regions",
                    children="regions")] + tree_nodes
#                nodes=[GeographicalRegionTreeNode(),
#                       IdentifiedObjectTreeNode(),
#                       SubGeographicalRegionTreeNode()]
            ),
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True,
        buttons   = ["OK", "Cancel"]
    )

#-------------------------------------------------------------------------------
#  "AdapterTestCase" class:
#-------------------------------------------------------------------------------

class TreeNodeTestCase(unittest.TestCase):
    """ Defines a test case for the CIM tree nodes.
    """

    def setUp(self):
        """ The test runner will execute this method prior to each test.
        """
        pass


    def test_tree_editor(self):
        """ Test CIM tree editor.
        """
        bay1 = Bay(name="Bay 1")
        vl1 = VoltageLevel(name="VL 1")
        station1 = Substation(name="SS 1", Contains_VoltageLevels=[vl1],
                              Contains_Bays=[bay1])
        line1 = Line(name="L 1")
        sub_region1 = SubGeographicalRegion(name="SR 1",
            Substations=[station1], Lines=[line1])
        sub_region2 = SubGeographicalRegion(name="SR 2")
        region = GeographicalRegion(name="GR 1",
            Regions=[sub_region1, sub_region2])

#        container = RegionContainer( elements=read_cim( RDFXML_FILE ) )
        model = CommonInformationModel(root=region)
        model.configure_traits()

if __name__ == "__main__":
    unittest.main()

# EOF -------------------------------------------------------------------------
