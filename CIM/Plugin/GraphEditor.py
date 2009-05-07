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

""" Defines a graph editor for CIM resources.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Instance, Dict, Str, Property

from enthought.traits.ui.api \
    import View, Group, Item, HGroup, VGroup, Tabbed

from envisage.resource.resource_adapter import ResourceEditor

from CIM import CommonInformationModel

#------------------------------------------------------------------------------
#  "CIMGraphEditor" class:
#------------------------------------------------------------------------------

class CIMGraphEditor(ResourceEditor):
    """ Defines a workbench editor for editing CIM resources with
        a view based on a graph control.
    """

    #--------------------------------------------------------------------------
    #  "CIMGraphEditor" interface
    #--------------------------------------------------------------------------

    # Document edited by the editor.
    document = Instance(HasTraits)

    #--------------------------------------------------------------------------
    #  "TraitsUIEditor" interface
    #--------------------------------------------------------------------------

    def create_ui(self, parent):
        """ Creates the traits UI that represents the editor.
        """
        uri_element_map = self.editor_input.load()

        self.document = CommonInformationModel(
            Elements=uri_element_map.values())

        ui = self.edit_traits( view=self._create_view(), parent=parent,
            kind="subpanel" )

        # Event handler for document object modification.
        self.document.on_trait_change(self._on_modified)

        return ui

    #--------------------------------------------------------------------------
    #  "ResourceEditor" interface
    #--------------------------------------------------------------------------

    def _create_view(self):
        """ Create a view with a tree editor.
        """
        graph_editor = GraphEditor(
            nodes=cim_nodes, edges=cim_edges,
            on_select=self._on_select
        )

        view = View(
            Group(
                Item(
                    name="document", id=".document",
                    editor=graph_editor, resizable=True
                ),
                show_labels=False, show_border=False,
                orientation="vertical"
            ),
            id="CIM.Plugin.GraphEditor.CIMGraphEditor",
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


    def _on_select(self, object):
        """ Handle tree node selection.
        """
        # No properties view for the whole model.
        if isinstance(object, RegionContainer):
            self.selected = None
        else:
            self.selected = object

# EOF -------------------------------------------------------------------------
