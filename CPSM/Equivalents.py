#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CPSM.Core import ConnectivityNodeContainer
from CPSM.Core import ConductingEquipment
from CPSM.Domain import Susceptance
from CPSM.Domain import Conductance
from CPSM.Domain import Reactance
from CPSM.Domain import Resistance



from enthought.traits.api import Instance, List, Property
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "EquivalentNetwork" class:
#------------------------------------------------------------------------------

class EquivalentNetwork(ConnectivityNodeContainer):
    """ A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.A class that represents an external meshed network that has been reduced to an electrically equivalent model. The ConnectivityNodes contained in the equivalent are intended to reflect internal nodes of the equivalent. The boundary Connectivity nodes where the equivalent connects outside itself are NOT contained by the equivalent.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The associated reduced equivalents.The associated reduced equivalents.
    EquivalentEquipments = List(Instance("CPSM.Equivalents.EquivalentEquipment"),
        desc="The associated reduced equivalents.The associated reduced equivalents.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentNetwork" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "ConnectivityNodes", "EquivalentEquipments",
                label="References"),
            dock="tab"),
        id="CPSM.Equivalents.EquivalentNetwork",
        title="EquivalentNetwork",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentNetwork" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentEquipment" class:
#------------------------------------------------------------------------------

class EquivalentEquipment(ConductingEquipment):
    """ The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.The class represents equivalent objects that are the result of a network reduction. The class is the base for equivalent objects of diferent types.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The equivalent where the reduced model belongs.The equivalent where the reduced model belongs.
    EquivalentNetwork = Instance("CPSM.Equivalents.EquivalentNetwork", allow_none=False,
        desc="The equivalent where the reduced model belongs.The equivalent where the reduced model belongs.",
        transient=True,
        opposite="EquivalentEquipments",
        editor=InstanceEditor(name="_equivalentnetworks"))

    def _get_equivalentnetworks(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CPSM.Equivalents.EquivalentNetwork" ]
        else:
            return []

    _equivalentnetworks = Property(fget=_get_equivalentnetworks)

    #--------------------------------------------------------------------------
    #  Begin "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "EquivalentNetwork",
                label="References"),
            dock="tab"),
        id="CPSM.Equivalents.EquivalentEquipment",
        title="EquivalentEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentEquipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentShunt" class:
#------------------------------------------------------------------------------

class EquivalentShunt(EquivalentEquipment):
    """ The class represents equivalent shunts.The class represents equivalent shunts.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence shunt susceptance.Positive sequence shunt susceptance.
    b = Susceptance(desc="Positive sequence shunt susceptance.Positive sequence shunt susceptance.")

    # Positive sequence shunt conductance.Positive sequence shunt conductance.
    g = Conductance(desc="Positive sequence shunt conductance.Positive sequence shunt conductance.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "b", "g",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "EquivalentNetwork",
                label="References"),
            dock="tab"),
        id="CPSM.Equivalents.EquivalentShunt",
        title="EquivalentShunt",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentShunt" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "EquivalentBranch" class:
#------------------------------------------------------------------------------

class EquivalentBranch(EquivalentEquipment):
    """ The class represents equivalent branches.The class represents equivalent branches.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Positive sequence series reactance of the reduced branch.Positive sequence series reactance of the reduced branch.
    x = Reactance(desc="Positive sequence series reactance of the reduced branch.Positive sequence series reactance of the reduced branch.")

    # Positive sequence series resistance of the reduced branch.Positive sequence series resistance of the reduced branch.
    r = Resistance(desc="Positive sequence series resistance of the reduced branch.Positive sequence series resistance of the reduced branch.")

    #--------------------------------------------------------------------------
    #  Begin "EquivalentBranch" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "pathName", "description", "aliasName", "name", "x", "r",
                label="Attributes"),
            VGroup("Model", "Contains_Measurements", "MemberOf_EquipmentContainer", "OperationalLimitSet", "BaseVoltage", "Terminals", "EquivalentNetwork",
                label="References"),
            dock="tab"),
        id="CPSM.Equivalents.EquivalentBranch",
        title="EquivalentBranch",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "EquivalentBranch" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
