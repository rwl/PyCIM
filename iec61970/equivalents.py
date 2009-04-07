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

from iec61970.core import ConnectivityNodeContainer
from iec61970.core import ConductingEquipment
from iec61970.domain import Resistance
from iec61970.domain import Reactance
from iec61970.domain import Susceptance
from iec61970.domain import Conductance



from enthought.traits.api import Instance, List
# <<< imports

# >>> imports

#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "EquivalentNetwork" class:
#------------------------------------------------------------------------------

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The associated reduced equivalents.
    EquivalentEquipment = List(Instance("iec61970.equivalents.EquivalentEquipment"))

    #--------------------------------------------------------------------------
    #  Begin equivalentNetwork user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentNetwork user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentEquipment" class:
#------------------------------------------------------------------------------

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The equivalent where the reduced model belongs.
    EquivalentNetwork = Instance("iec61970.equivalents.EquivalentNetwork", allow_none=False)

    #--------------------------------------------------------------------------
    #  Begin equivalentEquipment user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentEquipment user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentBranch" class:
#------------------------------------------------------------------------------

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence series resistance of the reduced branch.
    r = Resistance

    # Positive sequence series reactance of the reduced branch.
    x = Reactance

    #--------------------------------------------------------------------------
    #  Begin equivalentBranch user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentBranch user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentShunt" class:
#------------------------------------------------------------------------------

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence shunt susceptance.
    b = Susceptance

    # Positive sequence shunt conductance.
    g = Conductance

    #--------------------------------------------------------------------------
    #  Begin equivalentShunt user definitions:
    #--------------------------------------------------------------------------

    #--------------------------------------------------------------------------
    #  End equivalentShunt user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
