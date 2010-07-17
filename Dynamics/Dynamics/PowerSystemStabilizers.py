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
from dynamics.Domain import Seconds



from enthought.traits.api import Enum, Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


InputSignalCodeJ = Enum("6", "4", "5", "2", "3", "1")

#------------------------------------------------------------------------------
#  "PowerSystemStabilizer" class:
#------------------------------------------------------------------------------

class PowerSystemStabilizer(Element):
    """ A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.A PSS provides an input (Vs) to the excitation system model to improve damping of system oscillations.  A variety of input signals may be used depending on the particular design.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PowerSystemStabilizer" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PowerSystemStabilizer",
        title="PowerSystemStabilizer",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PowerSystemStabilizer" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssIEEE4B" class:
#------------------------------------------------------------------------------

class PssIEEE4B(PowerSystemStabilizer):
    """ PSS type IEEE PSS4BPSS type IEEE PSS4B
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssIEEE4B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssIEEE4B",
        title="PssIEEE4B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssIEEE4B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssIEEE2B" class:
#------------------------------------------------------------------------------

class PssIEEE2B(PowerSystemStabilizer):
    """ IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.IEEE (2005) PSS2B Model  This stabilizer model is designed to represent a variety of dual-input stabilizers, which normally use combinations of power and speed or frequency to derive the stabilizing signal.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Lead/lag time constantLead/lag time constant
    t10 = Seconds(desc="Lead/lag time constantLead/lag time constant")

    # Numerator constantNumerator constant
    a = Float(desc="Numerator constantNumerator constant")

    # Stabilizer gainStabilizer gain
    ks1 = Float(desc="Stabilizer gainStabilizer gain")

    # Gain on signal #2 input before ramp-tracking filterGain on signal #2 input before ramp-tracking filter
    ks3 = Float(desc="Gain on signal #2 input before ramp-tracking filterGain on signal #2 input before ramp-tracking filter")

    # Lead/lag time constantLead/lag time constant
    t11 = Seconds(desc="Lead/lag time constantLead/lag time constant")

    # Gain on signal #2Gain on signal #2
    ks2 = Float(desc="Gain on signal #2Gain on signal #2")

    # Stabilizer output min limitStabilizer output min limit
    vstmin = Float(desc="Stabilizer output min limitStabilizer output min limit")

    # Input signal #1 max limitInput signal #1 max limit
    vsi1max = Float(desc="Input signal #1 max limitInput signal #1 max limit")

    # Input signal #2 max limitInput signal #2 max limit
    vsi2max = Float(desc="Input signal #2 max limitInput signal #2 max limit")

    # Lag time constantLag time constant
    tb = Seconds(desc="Lag time constantLag time constant")

    # Lead/lag time constantLead/lag time constant
    t2 = Seconds(desc="Lead/lag time constantLead/lag time constant")

    # Lead constantLead constant
    ta = Seconds(desc="Lead constantLead constant")

    # Lead/lag time constantLead/lag time constant
    t1 = Seconds(desc="Lead/lag time constantLead/lag time constant")

    # Lead/lag time constantLead/lag time constant
    t4 = Seconds(desc="Lead/lag time constantLead/lag time constant")

    # Order of ramp tracking filterOrder of ramp tracking filter
    n = Bool(desc="Order of ramp tracking filterOrder of ramp tracking filter")

    # Lead/lag time constantLead/lag time constant
    t3 = Seconds(desc="Lead/lag time constantLead/lag time constant")

    # Denominator order of ramp tracking filterDenominator order of ramp tracking filter
    m = Bool(desc="Denominator order of ramp tracking filterDenominator order of ramp tracking filter")

    # Time constant on signal #1Time constant on signal #1
    t6 = Seconds(desc="Time constant on signal #1Time constant on signal #1")

    # Lead of ramp tracking filterLead of ramp tracking filter
    t8 = Seconds(desc="Lead of ramp tracking filterLead of ramp tracking filter")

    # Input signal #1 min limitInput signal #1 min limit
    vsi1min = Float(desc="Input signal #1 min limitInput signal #1 min limit")

    # Time constant on signal #2Time constant on signal #2
    t7 = Seconds(desc="Time constant on signal #2Time constant on signal #2")

    # Lag of ramp tracking filterLag of ramp tracking filter
    t9 = Seconds(desc="Lag of ramp tracking filterLag of ramp tracking filter")

    # Gain on signal #2 input after ramp-tracking filterGain on signal #2 input after ramp-tracking filter
    ks4 = Float(desc="Gain on signal #2 input after ramp-tracking filterGain on signal #2 input after ramp-tracking filter")

    # Second washout on signal #1Second washout on signal #1
    tw2 = Seconds(desc="Second washout on signal #1Second washout on signal #1")

    # First washout on signal #1First washout on signal #1
    tw1 = Seconds(desc="First washout on signal #1First washout on signal #1")

    # Second washout on signal #2Second washout on signal #2
    tw4 = Seconds(desc="Second washout on signal #2Second washout on signal #2")

    # Input signal #2 min limitInput signal #2 min limit
    vsi2min = Float(desc="Input signal #2 min limitInput signal #2 min limit")

    # First washout on signal #2First washout on signal #2
    tw3 = Seconds(desc="First washout on signal #2First washout on signal #2")

    # Stabilizer output max limitStabilizer output max limit
    vstmax = Float(desc="Stabilizer output max limitStabilizer output max limit")

    #--------------------------------------------------------------------------
    #  Begin "PssIEEE2B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "t10", "a", "ks1", "ks3", "t11", "ks2", "vstmin", "vsi1max", "vsi2max", "tb", "t2", "ta", "t1", "t4", "n", "t3", "m", "t6", "t8", "vsi1min", "t7", "t9", "ks4", "tw2", "tw1", "tw4", "vsi2min", "tw3", "vstmax",
                label="Attributes", columns=2),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssIEEE2B",
        title="PssIEEE2B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssIEEE2B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssSB4" class:
#------------------------------------------------------------------------------

class PssSB4(PowerSystemStabilizer):
    """ Power sensitive stabilizer modelPower sensitive stabilizer model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssSB4" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssSB4",
        title="PssSB4",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssSB4" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssSB" class:
#------------------------------------------------------------------------------

class PssSB(PowerSystemStabilizer):
    """ Dual input PSS, pss2a and transient stabilizerDual input PSS, pss2a and transient stabilizer
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssSB" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssSB",
        title="PssSB",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssSB" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssSK" class:
#------------------------------------------------------------------------------

class PssSK(PowerSystemStabilizer):
    """ PSS Slovakian type &ndash; three inputsPSS Slovakian type &ndash; three inputs
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssSK" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssSK",
        title="PssSK",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssSK" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssPTIST3" class:
#------------------------------------------------------------------------------

class PssPTIST3(PowerSystemStabilizer):
    """ PTI microprocessor-based stabilizer model type 3PTI microprocessor-based stabilizer model type 3
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssPTIST3" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssPTIST3",
        title="PssPTIST3",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssPTIST3" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssIEEE1A" class:
#------------------------------------------------------------------------------

class PssIEEE1A(PowerSystemStabilizer):
    """ PSS type IEEE PSS1APSS type IEEE PSS1A
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssIEEE1A" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssIEEE1A",
        title="PssIEEE1A",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssIEEE1A" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssIEEE3B" class:
#------------------------------------------------------------------------------

class PssIEEE3B(PowerSystemStabilizer):
    """ PSS type IEEE PSS3BPSS type IEEE PSS3B
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssIEEE3B" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssIEEE3B",
        title="PssIEEE3B",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssIEEE3B" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssWSCC" class:
#------------------------------------------------------------------------------

class PssWSCC(PowerSystemStabilizer):
    """ Dual input PSSDual input PSS
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssWSCC" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssWSCC",
        title="PssWSCC",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssWSCC" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssPTIST1" class:
#------------------------------------------------------------------------------

class PssPTIST1(PowerSystemStabilizer):
    """ PTI microprocessor-based stabilizer model type 1PTI microprocessor-based stabilizer model type 1
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssPTIST1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssPTIST1",
        title="PssPTIST1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssPTIST1" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "PssSH" class:
#------------------------------------------------------------------------------

class PssSH(PowerSystemStabilizer):
    """ Siemens H infinity PSSSiemens H infinity PSS
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "PssSH" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.PowerSystemStabilizers.PssSH",
        title="PssSH",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "PssSH" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
