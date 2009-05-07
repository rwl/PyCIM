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

""" CIM plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.envisage.api import Plugin, ExtensionPoint
from enthought.traits.api import Instance, List

#------------------------------------------------------------------------------
#  "CIMPlugin" class:
#------------------------------------------------------------------------------

class CIMPlugin(Plugin):
    """ CIM plug-in.
    """
    # Extension point IDs
    PERSPECTIVES = "enthought.envisage.ui.workbench.perspectives"

    NEW_WIZARDS = "envisage.resource.new_wizards"
    EDITORS = "envisage.resource.editors"
    IMPORT_WIZARDS = "envisage.resource.import_wizards"

    # Unique plugin identifier
    id = "cim.cim_plugin"

    # Human readable plugin name
    name = "CIM"

    #--------------------------------------------------------------------------
    #  Extensions (Contributions):
    #--------------------------------------------------------------------------

    # Contributed perspectives:
    perspectives = List(contributes_to=PERSPECTIVES)

    # Contributed new resource wizards:
    new_wizards = List(contributes_to=NEW_WIZARDS)

    # Contributed resource editors:
    editors = List(contributes_to=EDITORS)

    # Contributed import wizards.
    import_wizards = List(contributes_to=IMPORT_WIZARDS)

    #--------------------------------------------------------------------------
    #  "CIMPlugin" interface:
    #--------------------------------------------------------------------------

    def _perspectives_default(self):
        """ Trait initialiser.
        """
        from CIMPerspective import CIMPerspective
        return [CIMPerspective]


    def _new_wizards_default(self):
        """ Trait initialiser.
        """
        from WizardExtension import CIMWizardExtension
        return [CIMWizardExtension]


    def _editors_default(self):
        """ Trait initialiser.
        """
        from EditorExtension \
            import CIMTreeEditorExtension, CIMGraphEditorExtension
        return [CIMTreeEditorExtension, CIMGraphEditorExtension]


    def _import_wizards_default(self):
        """ Trait initialiser.
        """
        from WizardExtension import RDFXMLImportWizardExtension
        return [RDFXMLImportWizardExtension]

# EOF -------------------------------------------------------------------------
