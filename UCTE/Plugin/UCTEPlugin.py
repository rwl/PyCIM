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

""" UCTE plug-in.
"""

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from enthought.envisage.api import Plugin, ExtensionPoint
from enthought.traits.api import Instance, List

#------------------------------------------------------------------------------
#  "UCTEPlugin" class:
#------------------------------------------------------------------------------

class UCTEPlugin(Plugin):
    """ UCTE plug-in.
    """
    # Extension point IDs
    NEW_WIZARDS = "envisage.resource.new_wizards"
    EDITORS = "envisage.resource.editors"
    ACTION_SETS = "enthought.envisage.ui.workbench.action_sets"

    # Unique plugin identifier
    id = "cim.ucte_plugin"

    # Human readable plugin name
    name = "UCTE"

    #--------------------------------------------------------------------------
    #  Extensions (Contributions):
    #--------------------------------------------------------------------------

    # Contributed new resource wizards:
    new_wizards = List(contributes_to=NEW_WIZARDS)

    # Contributed resource editors:
    editors = List(contributes_to=EDITORS)

    # Contributed action sets:
    action_sets = List(contributes_to=ACTION_SETS)

    #--------------------------------------------------------------------------
    #  "UCTEPlugin" interface:
    #--------------------------------------------------------------------------

    def _new_wizards_default(self):
        """ Trait initialiser.
        """
        from UCTEWizard import NewUCTEWizardExtension
        return [NewUCTEWizardExtension]


    def _editors_default(self):
        """ Trait initialiser.
        """
        from UCTETreeEditor import UCTETreeEditorExtension
        from UCTEGraphEditor import UCTEGraphEditorExtension

        return [UCTETreeEditorExtension, UCTEGraphEditorExtension]


#    def _action_sets_default(self):
#        """ Trait initialiser.
#        """
#        from ActionSet import CIMWorkbenchActionSet
#
#        return [CIMWorkbenchActionSet]

# EOF -------------------------------------------------------------------------
