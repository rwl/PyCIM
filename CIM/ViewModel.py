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

import pickle

from os.path import splitext

from CIM import CommonInformationModel, Element

from CIM.Generation.Production \
    import GeneratingUnit, GenUnitOpCostCurve, GenUnitOpSchedule

from CIM.LoadModel \
    import Load, ConformLoadGroup, ConformLoadSchedule

from CIM.Wires \
    import SynchronousMachine

from enthought.traits.api \
    import Instance, List, Property, on_trait_change

from enthought.traits.ui.api \
    import View, Item, TreeEditor, TreeNode, HGroup

from enthought.pyface.api \
    import FileDialog, OK

from DesktopViewModel \
    import DesktopViewModel, frame_icon

from DesktopMenu \
    import menubar

from CIMReader import read_cim

#------------------------------------------------------------------------------
#  "FlatModel" class:
#------------------------------------------------------------------------------

class FlatModel(CommonInformationModel):

    core = Property(List(Instance(Element)), depends_on=["Elements"])

    def _get_core(self):
        """ Property getter.
        """
        return [element for element in self.Elements \
            if element.__module__.endswith("Core")]

    production = Property(List(Instance(Element)), depends_on=["Elements"])

    def _get_production(self):
        """ Property getter.
        """
        return [element for element in self.Elements \
            if element.__module__.endswith("Generation.Production")]

    loadModel = Property(List(Instance(Element)), depends_on=["Elements"])

    def _get_loadModel(self):
        """ Property getter.
        """
        return [element for element in self.Elements \
            if element.__module__.endswith("LoadModel")]

    measurement = Property(List(Instance(Element)), depends_on=["Elements"])

    def _get_measurement(self):
        """ Property getter.
        """
        return [element for element in self.Elements \
            if element.__module__.endswith("Meas")]

    topology = Property(List(Instance(Element)), depends_on=["Elements"])

    def _get_topology(self):
        """ Property getter.
        """
        return [element for element in self.Elements \
            if element.__module__.endswith("Topology")]

    wires = Property(List(Instance(Element)), depends_on=["Elements"])

    def _get_wires(self):
        """ Property getter.
        """
        return [element for element in self.Elements \
            if element.__module__.endswith("Wires")]

#------------------------------------------------------------------------------
#  Flat tree editor:
#------------------------------------------------------------------------------

flat_tree_editor = TreeEditor(
    nodes=[
        TreeNode(node_for=[CommonInformationModel], label="=Model",
            children="", view=View()),
        TreeNode(node_for=[CommonInformationModel], children="core",
            label="=Core", view=View()),
        TreeNode(node_for=[CommonInformationModel], children="production",
            label="=Production", view=View()),
        TreeNode(node_for=[CommonInformationModel], children="loadModel",
            label="=Load Model", view=View()),
        TreeNode(node_for=[CommonInformationModel], children="measurement",
            label="=Measurement", view=View()),
        TreeNode(node_for=[CommonInformationModel], children="topology",
            label="=Topology", view=View()),
        TreeNode(node_for=[CommonInformationModel], children="wires",
            label="=Wires", add=[SynchronousMachine], view=View()),
        TreeNode(node_for=[Load], label="name"),
        TreeNode(node_for=[ConformLoadGroup], label="name"),
        TreeNode(node_for=[SynchronousMachine], label="name"),
        TreeNode(node_for=[GeneratingUnit], label="name")
    ],
    orientation="horizontal", editable=True,
    on_dclick=lambda obj: obj.edit_traits(kind="livemodal")
)

#------------------------------------------------------------------------------
#  "CIMViewModel" class:
#------------------------------------------------------------------------------

class CIMViewModel(DesktopViewModel):
    """ Defines a view model for viewing Common Information Model elements.
    """

    def open_file(self, info):
        """ Handles the open action.
        """
        if not info.initialized:
            return # Escape.

        wc = "RDF/XML Files (*.xml,*.zip,*.gz,*.bz2)|*.xml;*.zip;*.gz;*.bz2|" \
            "Pickle Files (*.pkl)|*.pkl|All Files (*.*)|*.*"
        dialog = FileDialog( action   = "open",
                             wildcard = wc,
                             default_directory = self.wd )

        if dialog.open() == OK:
            # Index of the selected wildcard.
            wc_idx   = dialog.wildcard_index
            exts = [".xml", ".zip", ".gz", ".bz2"]
            file_ext = splitext(dialog.path)[1]

            # Parse the RDF/XML or Pickle file.
            if wc_idx == 0 or (wc_idx == 2 and file_ext in exts):
                elements = read_cim( dialog.path )
                self.model = FlatModel( Elements=elements )
                self.file = "" # Prevent 'Save' action overwriting XML files.

            else:
                fd = None
                try:
                    fd = open( dialog.path, "rb" )
                    self.model = pickle.load( fd )

                finally:
                    if fd is not None:
                        fd.close()

                self.file = dialog.path

            # Set the working directory to that of the opened file.
            self.wd = dialog.directory
        del dialog

    #--------------------------------------------------------------------------
    #  Views:
    #--------------------------------------------------------------------------

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
    machine = SynchronousMachine()
    model = FlatModel(Elements=[load, load_group, unit, machine])
    view_model = CIMViewModel(model=model)
    view_model.configure_traits()

# EOF -------------------------------------------------------------------------
