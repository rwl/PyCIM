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

from enthought.traits.api import HasTraits, Property, Instance, adapts

from enthought.traits.ui.api \
    import View, Item, Group, ITreeNode, ITreeNodeAdapter, TreeEditor

from enthought.traits.ui.menu import Action, Menu

from CIM.Core import GeographicalRegion, SubGeographicalRegion, Substation

import CIM13Adapter

#------------------------------------------------------------------------------
#  "SubGeographicalRegionAdapter" class:
#------------------------------------------------------------------------------

#class SubGeographicalRegionAdapter(ITreeNodeAdapter):
#    """ Adapts a SubGeographicalRegion to implement the ITreeNode interface.
#    """
#
#    adapts(SubGeographicalRegion, ITreeNode)
#
#    #--------------------------------------------------------------------------
#    #  "ITreeNodeAdapter" interface:
#    #--------------------------------------------------------------------------
#
#    def allows_children(self):
#        """ Returns whether this object can have children.
#        """
#        return False
#
#
#    def get_label(self):
#        """ Gets the label to display for a specified object.
#        """
#        return self.adaptee.name

#------------------------------------------------------------------------------
#  "GeographicalRegionAdapter" class:
#------------------------------------------------------------------------------

#class GeographicalRegionAdapter(ITreeNodeAdapter):
#    """ Adapts a GeographicalRegion for display in a tree editor.
#    """
#
#    adapts(GeographicalRegion, ITreeNode)
#
#    #--------------------------------------------------------------------------
#    #  "ITreeNodeAdapter" interface:
#    #--------------------------------------------------------------------------
#
#    def allows_children(self):
#        """ Returns whether this object can have children.
#        """
#        return True
#
#
#    def has_children(self):
#        """ Returns whether the object has children.
#        """
#        return (len(self.adaptee.Regions) > 0)
#
#
#    def get_children(self):
#        """ Gets the object's children.
#        """
#        return self.adaptee.Regions
#
#
#    def get_children_id(self):
#        """ Gets the object's children identifier.
#        """
#        return 'Regions'
#
#
#    def append_child(self, child=None):
#        """ Appends a child to the object's children.
#        """
#        if child is not None:
#            self.adaptee.Regions.append(child)
#
#
#    def confirm_delete(self):
#        """ Checks whether a specified object can be deleted.
#
#        Returns
#        -------
#        * **True** if the object should be deleted with no further prompting.
#        * **False** if the object should not be deleted.
#        * Anything else: Caller should take its default action (which might
#          include prompting the user to confirm deletion).
#        """
#        return False
#
#
#    def delete_child(self, index):
#        """ Deletes a child at a specified index from the object's children.
#        """
#        if len(self.adaptee.Regions) > index:
#            self.adaptee.pop(index)
#
#
#    def when_children_replaced(self, listener, remove):
#        """ Sets up or removes a listener for children being replaced on a
#            specified object.
#        """
#        self.adaptee.on_trait_change(listener, 'Regions',
#                              remove=remove, dispatch='ui')
#
#
#    def get_label(self):
#        """ Gets the label to display for a specified object.
#        """
#        return self.adaptee.name
#
#
#    def get_menu(self):
#        """ Returns the right-click context menu for an object.
#        """
#        return Menu(*[
#            Action(name='Create Region',
#                action='node.adapter.append_child',
#            )]
#        )
#
#
#    def get_tooltip(self):
#        """ Gets the tooltip to display for a specified object.
#        """
#        return "A geographical region of a power system network model."
#
#
#    def get_icon(self, is_expanded):
#        """ Returns the icon for a specified object.
#        """
#        return '<open>'
#
#
#    def get_icon_path ( self ):
#        """ Returns the path used to locate an object's icon.
#        """
#        return ''
#
#
#    def get_name ( self ):
#        """ Returns the name to use when adding a new object instance
#            (displayed in the "New" submenu).
#        """
#        return ''
#
#
#    def get_view ( self ):
#        """ Gets the view to use when editing an object.
#        """
#        return None
#
#
#    def can_rename(self):
#        """ Returns whether the object's children can be renamed.
#        """
#        return True
#
#
#    def can_copy(self):
#        """ Returns whether the object's children can be copied.
#        """
#        return True
#
#
#    def can_delete(self):
#        """ Returns whether the object's children can be deleted.
#        """
#        return True
#
#
#    def can_delete_me ( self ):
#        """ Returns whether the object can be deleted.
#        """
#        return False
#
#
#    def can_auto_open(self):
#        """ Returns whether the object's children should be automatically
#            opened.
#        """
#        return True
#
#
#    def can_auto_close(self):
#        """ Returns whether the object's children should be automatically
#            closed.
#        """
#        return False
#
#
#    def click ( self ):
#        """ Handles an object being clicked.
#        """
#        pass
#
#
#    def dclick ( self ):
#        """ Handles an object being double-clicked.
#        """
#        pass


class CommonInformationModel(HasTraits):

    # The root of the model tree:
    root = Instance(GeographicalRegion)

    # The traits view to display:
    view = View(
        Item('root', editor=TreeEditor(editable=True, auto_open=True),
            show_label=False),
        width     = 0.33,
        height    = 0.50,
        resizable = True
    )

#-------------------------------------------------------------------------------
#  "AdapterTestCase" class:
#-------------------------------------------------------------------------------

class AdapterTestCase(unittest.TestCase):
    """ Defines a test case for the CIM adapters.
    """

    def setUp(self):
        """ The test runner will execute this method prior to each test.
        """
        pass


    def test_region_adapter(self):
        """ Test adapting GeographicalRegions to the ITreeNode interface.
        """
        station1 = Substation(name="SS 1")
        sub_region1 = SubGeographicalRegion(name="SR 1", Substations=[station1])
        sub_region2 = SubGeographicalRegion(name="SR 2")
        region = GeographicalRegion(name="GR 1",
            Regions=[sub_region1, sub_region2])

        model = CommonInformationModel(root=region)
        model.configure_traits()

# EOF -------------------------------------------------------------------------
