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

""" Defines a graph editor for UCTE CIM resources.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.traits.api \
    import HasTraits, Instance, Dict, Str, Property

from enthought.traits.ui.api \
    import View, Group, Item, HGroup, VGroup, Tabbed

from enthought.pyface.api import ImageResource

from envisage.resource.editor import Editor
from envisage.resource.resource_editor import ResourceEditor

from godot.ui.graph_editor import GraphEditor, GraphCanvas

from CIM import CommonInformationModel
from CIM14r05GraphEditor import graph_nodes#, graph_edges

#------------------------------------------------------------------------------
#  "UCTEGraphEditor" class:
#------------------------------------------------------------------------------

class UCTEGraphEditor(ResourceEditor):
    """ Defines a workbench editor for editing UCTE CIM resources with
        a view based on a graph control.
    """

    #--------------------------------------------------------------------------
    #  "UCTEGraphEditor" interface
    #--------------------------------------------------------------------------

    # Document edited by the editor.
    document = Instance(HasTraits)

    #--------------------------------------------------------------------------
    #  "TraitsUIEditor" interface
    #--------------------------------------------------------------------------

    def create_ui(self, parent):
        """ Creates the traits UI that represents the editor.
        """
        model = self.editor_input.load()

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
            canvas=GraphCanvas(node_children=["Elements"]),
            nodes=graph_nodes,# edges=graph_edges,
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
            id="UCTE.Plugin.GraphEditor.UCTEGraphEditor",
            help=False, resizable=True,
            undo=False, revert=False,
            width=0.3, height=0.3,
        )

        return view

    #--------------------------------------------------------------------------
    #  "GraphEditor" interface:
    #--------------------------------------------------------------------------

    def _on_select(self, object):
        """ Handle tree node selection.
        """
        # No properties view for the whole model.
        if isinstance(object, RegionContainer):
            self.selected = None
        else:
            self.selected = object

#------------------------------------------------------------------------------
#  "UCTEGraphEditorExtension" class:
#------------------------------------------------------------------------------

class UCTEGraphEditorExtension(Editor):
    """ Associates a graph editor with *.pkl files.
    """
    # The object contribution's globally unique identifier.
    id = "UCTE.Plugins.GraphEditor"

    # A name that will be used in the UI for this editor
    name = "UCTE Graph Editor"

    # An icon that will be used for all resources that match the
    # specified extensions
    image = ImageResource("cimug")

    # The contributed editor class
    editor_class = "UCTE.Plugin.GraphEditor:UCTEGraphEditor"

    # The list of file types understood by the editor
    extensions = [".pkl"]

    # If true, this editor will be used as the default editor for the type
    default = True

# EOF -------------------------------------------------------------------------
