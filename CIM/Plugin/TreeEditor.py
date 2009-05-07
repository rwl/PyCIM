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

""" Defines a tree editor for CIM resources.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Instance, Dict, Str, Property

from enthought.traits.ui.api \
    import View, Group, Item, HGroup, VGroup, Tabbed, TreeEditor, TreeNode

#from envisage.resource.resource_editor import ResourceEditor
from envisage.resource.resource_adapter import ResourceEditor

from CIM import Element
from CIM.Core import GeographicalRegion, VoltageLevel
#from CIM13TreeEditor import cim13_tree_editor
from CIM13r19TreeNodeEditor import tree_nodes

#------------------------------------------------------------------------------
#  "RegionContainer" class:
#------------------------------------------------------------------------------

class RegionContainer(HasTraits):
    """ Container of GeographicalRegion objects.
    """
    # All CIM elements.
#    elements = List( Instance(Element) )
    uri_element_map = Dict(Str, Element)

    # Subset of the CIM elements of type GeographicalRegion.
#    regions = Property(depends_on=["elements", "elements_items"])
    regions = Property(
        depends_on=["uri_element_map", "uri_element_map_items"])


    def _get_regions(self):
        """ Property getter.
        """
#        return [e for e in self.elements if isinstance(e, GeographicalRegion)]
        return [e for e in self.uri_element_map.values() \
            if isinstance(e, GeographicalRegion)]

#    def _set_regions(self, value):
#        """ Property setter.
#        """
#        uri = str( hash(value) )
#        self.uri_element_map[uri] = value
#
#        print "MAP", self.uri_element_map


RegionContainerNode = TreeNode(
    node_for=[RegionContainer],
    label="=CIM",
    children="",
    view=View()
)

RegionContainerRegionsNode = TreeNode(
    node_for=[RegionContainer],
    add=[GeographicalRegion],
    label="=Regions",
    children="regions",
    view=View()
)

#------------------------------------------------------------------------------
#  "CIMTreeEditor" class:
#------------------------------------------------------------------------------

class CIMTreeEditor(ResourceEditor):
    """ Defines a workbench editor for editing CIM resources with
        a view based on a tree control.
    """

    #--------------------------------------------------------------------------
    #  "CIMTreeEditor" interface
    #--------------------------------------------------------------------------

    # Document edited by the editor.
    document = Instance(RegionContainer)

    #--------------------------------------------------------------------------
    #  "TraitsUIEditor" interface
    #--------------------------------------------------------------------------

    def create_ui(self, parent):
        """ Creates the traits UI that represents the editor.
        """
        uri_element_map = self.editor_input.load()

        self.document = RegionContainer(
#            elements=uri_element_map.values()
            uri_element_map=uri_element_map
        )

        ui = self.edit_traits(
            view=self._create_view(), parent=parent, kind="subpanel"
        )

        # Event handler for document object modification.
        self.document.on_trait_change(self._on_modified)

        return ui

    #--------------------------------------------------------------------------
    #  "ResourceEditor" interface
    #--------------------------------------------------------------------------

    def _create_view(self):
        """ Create a view with a tree editor.
        """
        tree_editor = TreeEditor(
            nodes=[RegionContainerNode, RegionContainerRegionsNode] \
                + tree_nodes,
            on_select = self._on_select,
            on_dclick = self._on_dclick,
            editable=False
        )

        view = View(
            Group(
                Item(
                    name="document", id=".document",
                    editor=tree_editor, resizable=True
                ),
                show_labels=False, show_border=False,
                orientation="vertical"
            ),
            id="CIM.Plugin.TreeEditor.RegionTreeEditor",
            help=False, resizable=True,
            undo=False, revert=False,
            width=0.3, height=0.3,
        )

        return view

    #--------------------------------------------------------------------------
    #  "ResourceEditor" interface:
    #--------------------------------------------------------------------------

    def save(self):
        """ Saves the editor content.
        """
#        content = self.document.uri_element_map
#        self.editor_input.save(content)
        raise NotImplementedError


    def save_as(self):
        """ Saves the editor content to a new file name.
        """
        self.save


    def _on_dclick(self, object):
        """ Handle tree node activation.
        """
        object.edit_traits(parent=self.window.control, kind="livemodal")


    def _on_select(self, object):
        """ Handle tree node selection.
        """
        # No properties view for the whole model.
        if isinstance(object, RegionContainer):
            self.selected = None
        else:
            self.selected = object

# EOF -------------------------------------------------------------------------
