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

""" Defines a wizard for CIM resource creation.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import pickle as pickle
from os.path import expanduser, join, exists, splitext

from enthought.io.api import File as IOFile

from enthought.traits.api import \
    HasTraits, Directory, Bool, Str, Float, Property, Instance, \
    cached_property, Event

from enthought.traits.ui.api import \
    View, Item, Group, Label, Heading, DirectoryEditor

from enthought.traits.ui.menu import OKCancelButtons
from enthought.pyface.wizard.api import SimpleWizard, WizardPage
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from envisage.resource.i_workspace import IWorkspace
from envisage.resource.action.open_action import OpenAction

from envisage.resource.wizard.container_selection_page import \
    ContainerSelectionPage

from envisage.resource.resource_adapter import PickleFileIResourceAdapter

from CIM.Core import GeographicalRegion

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

WORKSPACE_VIEW = "envisage.resource.workspace_view"

#------------------------------------------------------------------------------
#  "CIMWizardPage" class:
#------------------------------------------------------------------------------

class CIMWizardPage(WizardPage):
    """ Wizard page for CIM creation.
    """
    # Name for the new file resource.
    model_name = Str

    csp = Instance(ContainerSelectionPage)

    # Absolute path for the project
    abs_path = Property(Str, depends_on=["model_name"])

    # A label with advice
    _label = Property(
        Str("Create a new network model resource."),
        depends_on=["model_name"]
    )

    # Has the network's name been changed
    _named = Bool(False)

    # The default view
    traits_view = View(
        Group(
            Heading("CIM"),
            Item("_label", style="readonly", show_label=False),
            "_",
        ),
        Item("model_name")
    )

    @cached_property
    def _get_abs_path(self):
        """ Property getter.
        """
        return join(self.csp.directory, self.model_name)


    @cached_property
    def _get__label(self):
        """ Property getter
        """
        name = self.model_name

        if (exists(self.abs_path)) and (len(name) != 0):
            l = "A model with that name already exists."
            self.complete = False
        elif len(name) == 0 and self._named:
            l = "Model name must be specified."
            self.complete = False
        elif not name.endswith(".pkl"):
            l = "The model file name must end in '.pkl'."
            self.complete = False
        elif len(name) == 0:
            l = "Create a new CIM resource."
            self.complete = False
        else:
            l = "Create a new CIM resource."
            self.complete = True

        return l


    def _model_name_changed(self):
        """ Sets a flag when the name is changed.
        """
        self._named = True

    #--------------------------------------------------------------------------
    #  "WizardPage" interface:
    #--------------------------------------------------------------------------

    def create_page(self, parent):
        """ Creates the wizard page.
        """
        ui = self.edit_traits(parent=parent, kind="subpanel")
        return ui.control

#------------------------------------------------------------------------------
#  "CIMWizard" class:
#------------------------------------------------------------------------------

class CIMWizard(SimpleWizard):
    """ A wizard for CIM resource creation.
    """
    # The dialog title
    title = Str("New CIM")

    #--------------------------------------------------------------------------
    #  "NetworkWizard" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    finished = Event

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, window, **traits):
        """ Initialises the wizard.
        """
        self.window = window
        workspace = window.application.get_service(IWorkspace)

        csp = ContainerSelectionPage(id="container_page", workspace=workspace)
        nwp = CIMWizardPage(id="model_page", csp=csp)

        self.pages = [csp, nwp]

        super(CIMWizard, self).__init__(**traits)

    #--------------------------------------------------------------------------
    #  "CIMWizard" interface:
    #--------------------------------------------------------------------------

    def _finished_fired(self):
        """ Performs the network resource creation if the wizard is
            finished successfully.
        """
        workspace = self.window.application.get_service(IWorkspace)

        csp = self.pages[0]
        nwp = self.pages[1]

        file = IOFile(join(csp.directory, nwp.model_name))
        if not file.exists:
            name, ext = splitext(nwp.model_name)

            default = GeographicalRegion(name=name)
            uri = str( hash(default) )
            uri_element_map = {uri: default}
            # Adapt the new file to a persistent resource.
            resource = PickleFileIResourceAdapter(file)
            resource.save( uri_element_map )

        self._open_resource(file)

        self._refresh_container(workspace)


    def _open_resource(self, file):
        """ Makes the file the current selection and opens it.
        """
        self.window.selection = [file]
        OpenAction(window=self.window).perform(event=None)


    def _refresh_container(self, container):
        """ Refreshes the workspace tree view.
        """
        view = self.window.get_view_by_id(WORKSPACE_VIEW)
        if view is not None:
            view.tree_viewer.refresh(container)

# EOF -------------------------------------------------------------------------
