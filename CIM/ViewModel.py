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

""" Defines a model for viewing Common Information Models.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Model

from CIM.Generation.Production \
    import GeneratingUnit, GenUnitOpCostCurve, GenUnitOpSchedule

from CIM.LoadModel \
    import Load, ConformLoadGroup, ConformLoadSchedule

from enthought.traits.api \
    import Instance, List, Property, on_trait_change

from enthought.traits.ui.api \
    import View, Item, TreeEditor, TreeNode, HGroup

# FIXME: Remove dependency on Pylon.
from pylon.ui.view_model.desktop_vm \
    import DesktopViewModel, frame_icon, menubar

#------------------------------------------------------------------------------
#  "FlatModel" class:
#------------------------------------------------------------------------------

class FlatModel(Model):

    Loads = Property(List(Instance(Load)), depends_on=["Contains"])

    ConformLoadGroups = Property(List(Instance(ConformLoadGroup)),
        depends_on=["Contains"])

    def _get_Loads(self):
        """ Property getter.
        """
        return [root for root in self.Contains if isinstance(root, Load)]

    def _get_ConformLoadGroups(self):
        """ Property getter.
        """
        return [r for r in self.Contains if isinstance(r, ConformLoadGroup)]

#    def _Loads_changed(self, new):
#        for load in new:
#            load._LoadGroups = self.ConformLoadGroups
#
#    def _Loads_items_changed(self, event):
#        for load in event.added:
#            load._LoadGroups = self.ConformLoadGroups

    @on_trait_change("Loads,ConformLoadGroups")
    def _SetLoadGroups(self):
        for load in self.Loads:
            load._LoadGroups = self.ConformLoadGroups

#------------------------------------------------------------------------------
#  Flat tree editor:
#------------------------------------------------------------------------------

flat_tree_editor = TreeEditor(
    nodes=[
#        TreeNode(node_for=[Model], label="=Model", children="",
#            view=View()),
        TreeNode(node_for=[Model], children="Contains",
                 label="=Model", add=[Load, ConformLoadGroup], view=View()),
        TreeNode(node_for=[Load], label="name"),
        TreeNode(node_for=[ConformLoadGroup], label="name"),
        TreeNode(node_for=[GeneratingUnit], label="name")
    ],
    orientation="horizontal", editable=True
)

#------------------------------------------------------------------------------
#  "CIMViewModel" class:
#------------------------------------------------------------------------------

class CIMViewModel(DesktopViewModel):

    traits_view = View( HGroup( Item("model",
                                     editor=flat_tree_editor,
                                     show_label=False ) ),
                        id        = "model_view_model.traits_view",
                        title     = "Common Information Model",
                        icon      = frame_icon,
                        resizable = True,
                        style     = "custom",
                        kind      = "live",
                        buttons   = [],
                        menubar   = menubar,
                        dock      = "vertical" )

if __name__ == "__main__":
    load_group = ConformLoadGroup(name="CLG1")
    load = Load(name="Load 1", LoadGroup=load_group)
    unit = GeneratingUnit()
    model = FlatModel(Contains=[load, load_group, unit])
    view_model = CIMViewModel(model=model)
    view_model.configure_traits()

# EOF -------------------------------------------------------------------------
