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

from dynamics import Element
from dynamics.Domain import Resistance
from dynamics.Domain import Reactance




# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "VoltageCompensator" class:
#------------------------------------------------------------------------------

class VoltageCompensator(Element):
    """ A voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit IDA voltage compensator adjusts the terminal voltage feedback to the excitation system by adding a quantity that is proportional to the terminal current of the generator. It is linked to a specific generator by the Bus number and Unit ID
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Compensating (compounding) resistanceCompensating (compounding) resistance
    rcomp = Resistance(desc="Compensating (compounding) resistanceCompensating (compounding) resistance")

    # Compensating (compounding) reactanceCompensating (compounding) reactance
    xcomp = Reactance(desc="Compensating (compounding) reactanceCompensating (compounding) reactance")

    #--------------------------------------------------------------------------
    #  Begin "VoltageCompensator" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "rcomp", "xcomp",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.VoltageCompensator.VoltageCompensator",
        title="VoltageCompensator",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VoltageCompensator" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VcompIEEE" class:
#------------------------------------------------------------------------------

class VcompIEEE(VoltageCompensator):
    """ IEEE Voltage Compensation ModelIEEE Voltage Compensation Model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "VcompIEEE" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "rcomp", "xcomp",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.VoltageCompensator.VcompIEEE",
        title="VcompIEEE",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VcompIEEE" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "VcompCross" class:
#------------------------------------------------------------------------------

class VcompCross(VoltageCompensator):
    """ Voltage Compensation Model for Cross-Compound Generating UnitVoltage Compensation Model for Cross-Compound Generating Unit
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Cross-Compensating (compounding) reactanceCross-Compensating (compounding) reactance
    xcomp2 = Reactance(desc="Cross-Compensating (compounding) reactanceCross-Compensating (compounding) reactance")

    # Cross-Compensating (compounding) resistanceCross-Compensating (compounding) resistance
    rcomp2 = Resistance(desc="Cross-Compensating (compounding) resistanceCross-Compensating (compounding) resistance")

    #--------------------------------------------------------------------------
    #  Begin "VcompCross" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "rcomp", "xcomp", "xcomp2", "rcomp2",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.VoltageCompensator.VcompCross",
        title="VcompCross",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "VcompCross" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
