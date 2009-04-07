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

from CIM13.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Enum, Bool
# <<< imports

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

    ContingencyElement = List(Instance("CIM13.Contingency.ContingencyElement"))

    # Set true if must study this contingency.
    mustStudy = EBoolean

    #--------------------------------------------------------------------------
    #  Begin contingency user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End contingency user definitions:
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

    Contingency = Instance("CIM13.Contingency.Contingency")

    #--------------------------------------------------------------------------
    #  Begin contingencyElement user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End contingencyElement user definitions:
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

    Equipment = Instance("CIM13.Core.Equipment")

    # The status for the associated equipment when in the contingency state.   This status is independent of the case to which the contingency is originally applied, but defines the equipment status when the contingency is applied.
    contingentStatus = ContingencyEquipmentStatusKind

    #--------------------------------------------------------------------------
    #  Begin contingencyEquipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End contingencyEquipment user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
