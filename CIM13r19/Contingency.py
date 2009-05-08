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

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM13r19.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Enum, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


ContingencyEquipmentStatusKind = Enum("outOfService", "inService")

#------------------------------------------------------------------------------
#  "Contingency" class:
#------------------------------------------------------------------------------

class Contingency(IdentifiedObject):
    """ An event threatening system reliability, consisting of one or more contingency elements.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ContingencyElement = List(Instance("CIM13r19.Contingency.ContingencyElement"))

    # Set true if must study this contingency.
    mustStudy = Bool(desc="Set true if must study this contingency.")

    #--------------------------------------------------------------------------
    #  Begin "Contingency" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "mustStudy",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "ContingencyElement",
                label="References"),
            dock="tab"),
        id="CIM13r19.Contingency.Contingency",
        title="Contingency",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "Contingency" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ContingencyElement" class:
#------------------------------------------------------------------------------

class ContingencyElement(IdentifiedObject):
    """ An element of a system event to be studied by contingency analysis, representing a change in status of a single piece of equipment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Contingency = Instance("CIM13r19.Contingency.Contingency",
        transient=True,
        opposite="ContingencyElement",
        editor=InstanceEditor(name="_contingencys"))

    def _get_contingencys(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Contingency.Contingency" ]
        else:
            return []

    _contingencys = Property(fget=_get_contingencys)

    #--------------------------------------------------------------------------
    #  Begin "ContingencyElement" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Contingency",
                label="References"),
            dock="tab"),
        id="CIM13r19.Contingency.ContingencyElement",
        title="ContingencyElement",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ContingencyElement" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ContingencyEquipment" class:
#------------------------------------------------------------------------------

class ContingencyEquipment(ContingencyElement):
    """ A equipment to which the in service status is to change such as a power transformer or AC line segment.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    Equipment = Instance("CIM13r19.Core.Equipment",
        transient=True,
        opposite="ContingencyEquipment",
        editor=InstanceEditor(name="_equipments"))

    def _get_equipments(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Equipment" ]
        else:
            return []

    _equipments = Property(fget=_get_equipments)

    # The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied.
    contingentStatus = ContingencyEquipmentStatusKind(desc="The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied.")

    #--------------------------------------------------------------------------
    #  Begin "ContingencyEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "contingentStatus",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Contingency", "Equipment",
                label="References"),
            dock="tab"),
        id="CIM13r19.Contingency.ContingencyEquipment",
        title="ContingencyEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ContingencyEquipment" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
