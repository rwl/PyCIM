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

""" Defines a wizard for import of CIM RDF/XML data files.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

import pickle as pickle

from os.path import exists, basename, splitext, join

from enthought.traits.api import \
    File, cached_property, Event, Str, Property, Instance

from enthought.io.api import File as IOFile
from enthought.traits.ui.api import View, Group, Item, Heading
from enthought.pyface.wizard.api import SimpleWizard, WizardPage
from enthought.envisage.ui.workbench.workbench_window import WorkbenchWindow

from envisage.resource.i_workspace import IWorkspace
from envisage.resource.wizard.file_import_page import FileImportPage
from envisage.resource.action.open_action import OpenAction

from envisage.resource.wizard.container_selection_page import \
    ContainerSelectionPage

from envisage.resource.resource_adapter import PickleFileIResourceAdapter

from CIM.CIMReader import read_cim
from CIM import Model

#------------------------------------------------------------------------------
#  Constants:
#------------------------------------------------------------------------------

WORKSPACE_VIEW = "envisage.resource.resource_view"

#------------------------------------------------------------------------------
#  "RDFXMLImportPage" class:
#------------------------------------------------------------------------------

class RDFXMLImportPage(FileImportPage):
    """ Defines a wizard page for CIM RDF/XML data file selection.
    """
    file_type = Str("CIM RDF/XML")

    data_file = File(exists=True,
        filter=["XML Files (*.xml)|*.xml|All Files (*.*)|*.*"])

#    traits_view = View(
#        Group(
#            Heading("CIM RDF/XML"),
#            Item("_label", style="readonly", show_label=False),
#            "_",
#        ),
#        Item("data_file")
#    )

#------------------------------------------------------------------------------
#  "RDFXMLImportWizard" class:
#------------------------------------------------------------------------------

class RDFXMLImportWizard(SimpleWizard):
    """ Defines a wizard for importing a CIM RDF/XML data file.
    """
    # The dialog title
    title = Str("Import CIM RDF/XML")

    #--------------------------------------------------------------------------
    #  "RDFXMLImportWizard" interface:
    #--------------------------------------------------------------------------

    window = Instance(WorkbenchWindow)

    finished = Event

    #--------------------------------------------------------------------------
    #  "object" interface:
    #--------------------------------------------------------------------------

    def __init__(self, window, **traits):
        """ Initialises the wizard instance.
        """
        self.window = window
        workspace = window.application.get_service(IWorkspace)

        csp = ContainerSelectionPage(id="container_page", workspace=workspace)
        mip = RDFXMLImportPage(id="file_page")

        self.pages = [csp, mip]

        super(RDFXMLImportWizard, self).__init__(**traits)


    def _finished_fired(self):
        """ Performs the network resource creation if the wizard is
            finished successfully.
        """
        workspace = self.window.application.get_service(IWorkspace)

        csp = self.pages[0]
        mip = self.pages[1]

        name, ext = splitext(basename(mip.data_file))

        file = IOFile(join(csp.directory, name+".pkl"))

        if not file.exists:
            # Parse the CIM RDF/XML data file.
            uri_element_map = read_cim(mip.data_file)
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
