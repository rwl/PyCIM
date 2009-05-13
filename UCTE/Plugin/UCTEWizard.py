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

from envisage.resource.wizard.new_resource_wizard import NewResourceWizard
from envisage.resource.resource_adapter import PickleFileIResourceAdapter

from UCTE import CommonInformationModel

#------------------------------------------------------------------------------
#  "NewUCTEWizard" class:
#------------------------------------------------------------------------------

class NewUCTEWizard(NewResourceWizard):
    """ A wizard for UCTE resource creation.
    """
    # The dialog title
    title = Str("New UCTE")

    extensions = [".pkl"]


    def get_resource(self, file):
        """ Returns the new adapted resource.
        """
        return PickleFileIResourceAdapter(file)


    def get_content(self, name):
        """ Returns the content for the new resource.
        """
        return CommonInformationModel()

#------------------------------------------------------------------------------
#  "NewUCTEWizardExtension" class:
#------------------------------------------------------------------------------

class NewUCTEWizardExtension(WizardExtension):
    """ Contributes a new UCTE CIM wizard.
    """
    # The wizard contribution's globally unique identifier.
    id = "cim.new_ucte_wizard"

    # Human readable identifier
    name = "UCTE"

    # The wizards's image (displayed on selection etc)
    image = ImageResource("cimug")

    # The class of contributed wizard
    wizard_class = "UCTE.Plugin.UCTEWizard:NewUCTEWizard"

    # A longer description of the wizard's function
    description = "Create a new UCTE Common Information Model resource"

# EOF -------------------------------------------------------------------------
