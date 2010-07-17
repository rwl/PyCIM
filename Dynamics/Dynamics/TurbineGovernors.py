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
from dynamics.Domain import Frequency
from dynamics.Domain import ActivePower



from enthought.traits.api import Float, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "TurbineGovernor" class:
#------------------------------------------------------------------------------

class TurbineGovernor(Element):
    """ The turbine-governor determines the mechanical power (Pm) supplied to the generator modelThe turbine-governor determines the mechanical power (Pm) supplied to the generator model
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "TurbineGovernor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.TurbineGovernor",
        title="TurbineGovernor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TurbineGovernor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydro3" class:
#------------------------------------------------------------------------------

class GovHydro3(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydro3" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydro3",
        title="GovHydro3",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydro3" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydro2" class:
#------------------------------------------------------------------------------

class GovHydro2(TurbineGovernor):
    # Turbine denominator multiplierTurbine denominator multiplier
    bturb = Float(desc="Turbine denominator multiplierTurbine denominator multiplier")

    # Temporary droopTemporary droop
    rtemp = Float(desc="Temporary droopTemporary droop")

    # Water inertia time constantWater inertia time constant
    tw = Seconds(desc="Water inertia time constantWater inertia time constant")

    # Permanent droopPermanent droop
    rperm = Float(desc="Permanent droopPermanent droop")

    # Nonlinear gain point 1, p.u. gvNonlinear gain point 1, p.u. gv
    gv1 = Float(desc="Nonlinear gain point 1, p.u. gvNonlinear gain point 1, p.u. gv")

    # Nonlinear gain point 2, p.u. gvNonlinear gain point 2, p.u. gv
    gv2 = Float(desc="Nonlinear gain point 2, p.u. gvNonlinear gain point 2, p.u. gv")

    # Dashpot time constantDashpot time constant
    tr = Seconds(desc="Dashpot time constantDashpot time constant")

    # Turbine numerator multiplierTurbine numerator multiplier
    aturb = Float(desc="Turbine numerator multiplierTurbine numerator multiplier")

    # Pilot servo valve time constantPilot servo valve time constant
    tp = Seconds(desc="Pilot servo valve time constantPilot servo valve time constant")

    # Maximum gate opening velocityMaximum gate opening velocity
    uo = Float(desc="Maximum gate opening velocityMaximum gate opening velocity")

    # Nonlinear gain point 6, p.u. gvNonlinear gain point 6, p.u. gv
    gv6 = Float(desc="Nonlinear gain point 6, p.u. gvNonlinear gain point 6, p.u. gv")

    # Nonlinear gain point 5, p.u. gvNonlinear gain point 5, p.u. gv
    gv5 = Float(desc="Nonlinear gain point 5, p.u. gvNonlinear gain point 5, p.u. gv")

    # Nonlinear gain point 5, p.u. powerNonlinear gain point 5, p.u. power
    pgv5 = Float(desc="Nonlinear gain point 5, p.u. powerNonlinear gain point 5, p.u. power")

    # Nonlinear gain point 4, p.u. gvNonlinear gain point 4, p.u. gv
    gv4 = Float(desc="Nonlinear gain point 4, p.u. gvNonlinear gain point 4, p.u. gv")

    # Nonlinear gain point 6, p.u. powerNonlinear gain point 6, p.u. power
    pgv6 = Float(desc="Nonlinear gain point 6, p.u. powerNonlinear gain point 6, p.u. power")

    # Nonlinear gain point 3, p.u. gvNonlinear gain point 3, p.u. gv
    gv3 = Float(desc="Nonlinear gain point 3, p.u. gvNonlinear gain point 3, p.u. gv")

    # Nonlinear gain point 2, p.u. powerNonlinear gain point 2, p.u. power
    pgv2 = Float(desc="Nonlinear gain point 2, p.u. powerNonlinear gain point 2, p.u. power")

    # Nonlinear gain point 1, p.u. powerNonlinear gain point 1, p.u. power
    pgv1 = Float(desc="Nonlinear gain point 1, p.u. powerNonlinear gain point 1, p.u. power")

    # Intentional deadband widthIntentional deadband width
    db1 = Frequency(desc="Intentional deadband widthIntentional deadband width")

    # Nonlinear gain point 4, p.u. powerNonlinear gain point 4, p.u. power
    pgv4 = Float(desc="Nonlinear gain point 4, p.u. powerNonlinear gain point 4, p.u. power")

    # Turbine gainTurbine gain
    kturb = Float(desc="Turbine gainTurbine gain")

    # Unintentional deadbandUnintentional deadband
    db2 = ActivePower(desc="Unintentional deadbandUnintentional deadband")

    # Gate servo time constantGate servo time constant
    tg = Seconds(desc="Gate servo time constantGate servo time constant")

    # Maximum gate openingMaximum gate opening
    pmax = Float(desc="Maximum gate openingMaximum gate opening")

    # Nonlinear gain point 3, p.u. powerNonlinear gain point 3, p.u. power
    pgv3 = Float(desc="Nonlinear gain point 3, p.u. powerNonlinear gain point 3, p.u. power")

    # Base for power values (&gt; 0.)Base for power values (&gt; 0.)
    mwbase = ActivePower(desc="Base for power values (&gt; 0.)Base for power values (&gt; 0.)")

    # Maximum gate closing velocity (&lt;0.)Maximum gate closing velocity (&lt;0.)
    uc = Float(desc="Maximum gate closing velocity (&lt;0.)Maximum gate closing velocity (&lt;0.)")

    # Minimum gate openingMinimum gate opening
    pmin = Float(desc="Minimum gate openingMinimum gate opening")

    # Intentional db hysteresisIntentional db hysteresis
    eps = Frequency(desc="Intentional db hysteresisIntentional db hysteresis")

    #--------------------------------------------------------------------------
    #  Begin "GovHydro2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "bturb", "rtemp", "tw", "rperm", "gv1", "gv2", "tr", "aturb", "tp", "uo", "gv6", "gv5", "pgv5", "gv4", "pgv6", "gv3", "pgv2", "pgv1", "db1", "pgv4", "kturb", "db2", "tg", "pmax", "pgv3", "mwbase", "uc", "pmin", "eps",
                label="Attributes", columns=2),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydro2",
        title="GovHydro2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydro2" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovGAST" class:
#------------------------------------------------------------------------------

class GovGAST(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovGAST" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovGAST",
        title="GovGAST",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovGAST" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT1T" class:
#------------------------------------------------------------------------------

class GovWT1T(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT1T" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT1T",
        title="GovWT1T",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT1T" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT2P" class:
#------------------------------------------------------------------------------

class GovWT2P(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT2P" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT2P",
        title="GovWT2P",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT2P" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydroDD" class:
#------------------------------------------------------------------------------

class GovHydroDD(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydroDD" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydroDD",
        title="GovHydroDD",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydroDD" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydroWEH" class:
#------------------------------------------------------------------------------

class GovHydroWEH(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydroWEH" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydroWEH",
        title="GovHydroWEH",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydroWEH" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT3T" class:
#------------------------------------------------------------------------------

class GovWT3T(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT3T" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT3T",
        title="GovWT3T",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT3T" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydroPID" class:
#------------------------------------------------------------------------------

class GovHydroPID(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydroPID" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydroPID",
        title="GovHydroPID",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydroPID" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydro4" class:
#------------------------------------------------------------------------------

class GovHydro4(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydro4" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydro4",
        title="GovHydro4",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydro4" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovDUM" class:
#------------------------------------------------------------------------------

class GovDUM(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovDUM" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovDUM",
        title="GovDUM",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovDUM" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydroWPID" class:
#------------------------------------------------------------------------------

class GovHydroWPID(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydroWPID" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydroWPID",
        title="GovHydroWPID",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydroWPID" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT4P" class:
#------------------------------------------------------------------------------

class GovWT4P(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT4P" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT4P",
        title="GovWT4P",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT4P" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TLCFB1" class:
#------------------------------------------------------------------------------

class TLCFB1(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "TLCFB1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.TLCFB1",
        title="TLCFB1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TLCFB1" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovGASM" class:
#------------------------------------------------------------------------------

class GovGASM(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovGASM" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovGASM",
        title="GovGASM",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovGASM" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydroR" class:
#------------------------------------------------------------------------------

class GovHydroR(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydroR" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydroR",
        title="GovHydroR",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydroR" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteamFV2" class:
#------------------------------------------------------------------------------

class GovSteamFV2(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovSteamFV2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteamFV2",
        title="GovSteamFV2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteamFV2" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovRAV" class:
#------------------------------------------------------------------------------

class GovRAV(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovRAV" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovRAV",
        title="GovRAV",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovRAV" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovCT2" class:
#------------------------------------------------------------------------------

class GovCT2(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovCT2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovCT2",
        title="GovCT2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovCT2" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteam1" class:
#------------------------------------------------------------------------------

class GovSteam1(TurbineGovernor):
    """ IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)IEEE steam turbine/governor model  (with optional deadband and nonlinear valve gain added)
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Intentional db hysteresisIntentional db hysteresis
    eps = Frequency(desc="Intentional db hysteresisIntentional db hysteresis")

    # Maximum valve closing velocity, p.u./sec (&lt; 0.)Maximum valve closing velocity, p.u./sec (&lt; 0.)
    uc = Float(desc="Maximum valve closing velocity, p.u./sec (&lt; 0.)Maximum valve closing velocity, p.u./sec (&lt; 0.)")

    # Base for power values (&gt; 0.)Base for power values (&gt; 0.)
    mwbase = ActivePower(desc="Base for power values (&gt; 0.)Base for power values (&gt; 0.)")

    # Minimum valve opening (&gt;= 0.)Minimum valve opening (&gt;= 0.)
    pmin = Float(desc="Minimum valve opening (&gt;= 0.)Minimum valve opening (&gt;= 0.)")

    # Fraction of HP shaft power after second boiler passFraction of HP shaft power after second boiler pass
    k3 = Float(desc="Fraction of HP shaft power after second boiler passFraction of HP shaft power after second boiler pass")

    # Governor gain (reciprocal of droop) (&gt; 0.)Governor gain (reciprocal of droop) (&gt; 0.)
    k = Float(desc="Governor gain (reciprocal of droop) (&gt; 0.)Governor gain (reciprocal of droop) (&gt; 0.)")

    # Fraction of LP shaft power after first boiler passFraction of LP shaft power after first boiler pass
    k2 = Float(desc="Fraction of LP shaft power after first boiler passFraction of LP shaft power after first boiler pass")

    # Fraction of HP shaft power after first boiler passFraction of HP shaft power after first boiler pass
    k1 = Float(desc="Fraction of HP shaft power after first boiler passFraction of HP shaft power after first boiler pass")

    # Nonlinear gain power value point 1Nonlinear gain power value point 1
    pgv1 = Float(desc="Nonlinear gain power value point 1Nonlinear gain power value point 1")

    # Fraction of HP shaft power after fourth boiler passFraction of HP shaft power after fourth boiler pass
    k7 = Float(desc="Fraction of HP shaft power after fourth boiler passFraction of HP shaft power after fourth boiler pass")

    # Fraction of LP shaft power after third boiler passFraction of LP shaft power after third boiler pass
    k6 = Float(desc="Fraction of LP shaft power after third boiler passFraction of LP shaft power after third boiler pass")

    # Maximum valve opening (&gt; Pmin)Maximum valve opening (&gt; Pmin)
    pmax = Float(desc="Maximum valve opening (&gt; Pmin)Maximum valve opening (&gt; Pmin)")

    # Fraction of HP shaft power after third boiler passFraction of HP shaft power after third boiler pass
    k5 = Float(desc="Fraction of HP shaft power after third boiler passFraction of HP shaft power after third boiler pass")

    # Fraction of LP shaft power after second boiler passFraction of LP shaft power after second boiler pass
    k4 = Float(desc="Fraction of LP shaft power after second boiler passFraction of LP shaft power after second boiler pass")

    # Nonlinear gain valve position point 6Nonlinear gain valve position point 6
    gv6 = Float(desc="Nonlinear gain valve position point 6Nonlinear gain valve position point 6")

    # Time constant of third boiler passTime constant of third boiler pass
    t6 = Seconds(desc="Time constant of third boiler passTime constant of third boiler pass")

    # Nonlinear gain power value point 6Nonlinear gain power value point 6
    pgv6 = Float(desc="Nonlinear gain power value point 6Nonlinear gain power value point 6")

    # Time constant of fourth boiler pasTime constant of fourth boiler pas
    t7 = Seconds(desc="Time constant of fourth boiler pasTime constant of fourth boiler pas")

    # Nonlinear gain valve position point 5Nonlinear gain valve position point 5
    gv5 = Float(desc="Nonlinear gain valve position point 5Nonlinear gain valve position point 5")

    # Fraction of LP shaft power after fourth boiler passFraction of LP shaft power after fourth boiler pass
    k8 = Float(desc="Fraction of LP shaft power after fourth boiler passFraction of LP shaft power after fourth boiler pass")

    # Nonlinear gain valve position point 1Nonlinear gain valve position point 1
    gv1 = Float(desc="Nonlinear gain valve position point 1Nonlinear gain valve position point 1")

    # Governor lag time constantGovernor lag time constant
    t1 = Seconds(desc="Governor lag time constantGovernor lag time constant")

    # Governor lead time constantGovernor lead time constant
    t2 = Seconds(desc="Governor lead time constantGovernor lead time constant")

    # Nonlinear gain power value point 3Nonlinear gain power value point 3
    pgv3 = Float(desc="Nonlinear gain power value point 3Nonlinear gain power value point 3")

    # Intentional deadband widthIntentional deadband width
    db1 = Frequency(desc="Intentional deadband widthIntentional deadband width")

    # Valve positioner time constant (&gt; 0.)Valve positioner time constant (&gt; 0.)
    t3 = Seconds(desc="Valve positioner time constant (&gt; 0.)Valve positioner time constant (&gt; 0.)")

    # Maximum valve opening velocity (&gt; 0.)Maximum valve opening velocity (&gt; 0.)
    uo = Float(desc="Maximum valve opening velocity (&gt; 0.)Maximum valve opening velocity (&gt; 0.)")

    # Nonlinear gain power value point 2Nonlinear gain power value point 2
    pgv2 = Float(desc="Nonlinear gain power value point 2Nonlinear gain power value point 2")

    # Nonlinear gain valve position point 4Nonlinear gain valve position point 4
    gv4 = Float(desc="Nonlinear gain valve position point 4Nonlinear gain valve position point 4")

    # Nonlinear gain power value point 5Nonlinear gain power value point 5
    pgv5 = Float(desc="Nonlinear gain power value point 5Nonlinear gain power value point 5")

    # Inlet piping/steam bowl time constantInlet piping/steam bowl time constant
    t4 = Seconds(desc="Inlet piping/steam bowl time constantInlet piping/steam bowl time constant")

    # Nonlinear gain valve position point 2Nonlinear gain valve position point 2
    gv2 = Float(desc="Nonlinear gain valve position point 2Nonlinear gain valve position point 2")

    # Nonlinear gain valve position point 3Nonlinear gain valve position point 3
    gv3 = Float(desc="Nonlinear gain valve position point 3Nonlinear gain valve position point 3")

    # Time constant of second boiler passTime constant of second boiler pass
    t5 = Seconds(desc="Time constant of second boiler passTime constant of second boiler pass")

    # Nonlinear gain power value point 4Nonlinear gain power value point 4
    pgv4 = Float(desc="Nonlinear gain power value point 4Nonlinear gain power value point 4")

    # Unintentional deadbandUnintentional deadband
    db2 = ActivePower(desc="Unintentional deadbandUnintentional deadband")

    #--------------------------------------------------------------------------
    #  Begin "GovSteam1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "eps", "uc", "mwbase", "pmin", "k3", "k", "k2", "k1", "pgv1", "k7", "k6", "pmax", "k5", "k4", "gv6", "t6", "pgv6", "t7", "gv5", "k8", "gv1", "t1", "t2", "pgv3", "db1", "t3", "uo", "pgv2", "gv4", "pgv5", "t4", "gv2", "gv3", "t5", "pgv4", "db2",
                label="Attributes", columns=3),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteam1",
        title="GovSteam1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteam1" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteamCC" class:
#------------------------------------------------------------------------------

class GovSteamCC(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovSteamCC" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteamCC",
        title="GovSteamCC",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteamCC" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteamSGO" class:
#------------------------------------------------------------------------------

class GovSteamSGO(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovSteamSGO" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteamSGO",
        title="GovSteamSGO",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteamSGO" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteamFV3" class:
#------------------------------------------------------------------------------

class GovSteamFV3(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovSteamFV3" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteamFV3",
        title="GovSteamFV3",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteamFV3" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT3P" class:
#------------------------------------------------------------------------------

class GovWT3P(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT3P" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT3P",
        title="GovWT3P",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT3P" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT1P" class:
#------------------------------------------------------------------------------

class GovWT1P(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT1P" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT1P",
        title="GovWT1P",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT1P" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteam0" class:
#------------------------------------------------------------------------------

class GovSteam0(TurbineGovernor):
    """ A simplified steam turbine-governor model.A simplified steam turbine-governor model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Numerator time constant of T2/T3 blockNumerator time constant of T2/T3 block
    t2 = Seconds(desc="Numerator time constant of T2/T3 blockNumerator time constant of T2/T3 block")

    # Reheater time constantReheater time constant
    t3 = Seconds(desc="Reheater time constantReheater time constant")

    # Steam bowl time constantSteam bowl time constant
    t1 = Seconds(desc="Steam bowl time constantSteam bowl time constant")

    # Maximum valve position, p.u. of mwcapMaximum valve position, p.u. of mwcap
    vmax = Float(desc="Maximum valve position, p.u. of mwcapMaximum valve position, p.u. of mwcap")

    # Turbine damping coefficientTurbine damping coefficient
    dt = Float(desc="Turbine damping coefficientTurbine damping coefficient")

    # Permanent droopPermanent droop
    r = Float(desc="Permanent droopPermanent droop")

    # Minimum valve position, p.u. of mwcapMinimum valve position, p.u. of mwcap
    vmin = Float(desc="Minimum valve position, p.u. of mwcapMinimum valve position, p.u. of mwcap")

    # Base for power values  (&gt; 0.)Base for power values  (&gt; 0.)
    mwbase = ActivePower(desc="Base for power values  (&gt; 0.)Base for power values  (&gt; 0.)")

    #--------------------------------------------------------------------------
    #  Begin "GovSteam0" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "t2", "t3", "t1", "vmax", "dt", "r", "vmin", "mwbase",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteam0",
        title="GovSteam0",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteam0" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovCT1" class:
#------------------------------------------------------------------------------

class GovCT1(TurbineGovernor):
    """ General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.General model for any prime mover with a PID governor, used primarily for combustion turbine and combined cycle units.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Maximum rate of load limit decreaseMaximum rate of load limit decrease
    rdown = Float(desc="Maximum rate of load limit decreaseMaximum rate of load limit decrease")

    # Maximum valve position limitMaximum valve position limit
    vmax = Float(desc="Maximum valve position limitMaximum valve position limit")

    # No load fuel flowNo load fuel flow
    wfnl = Float(desc="No load fuel flowNo load fuel flow")

    # Governor derivative controller time constantGovernor derivative controller time constant
    tdgov = Seconds(desc="Governor derivative controller time constantGovernor derivative controller time constant")

    # Acceleration limiter setpointAcceleration limiter setpoint
    aset = Float(desc="Acceleration limiter setpointAcceleration limiter setpoint")

    # Permanent droopPermanent droop
    r = Float(desc="Permanent droopPermanent droop")

    # Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speedSwitch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed
    wfspd = Bool(desc="Switch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speedSwitch for fuel source characteristic = 0 for fuel flow independent of speed = 1 fuel flow proportional to speed")

    # Governor proportional gainGovernor proportional gain
    kpgov = Float(desc="Governor proportional gainGovernor proportional gain")

    # Minimum value for speed error signalMinimum value for speed error signal
    minerr = Float(desc="Minimum value for speed error signalMinimum value for speed error signal")

    # Temperature detection lead time constantTemperature detection lead time constant
    tsa = Seconds(desc="Temperature detection lead time constantTemperature detection lead time constant")

    # Actuator time constantActuator time constant
    tact = Seconds(desc="Actuator time constantActuator time constant")

    # Temperature detection lag time constantTemperature detection lag time constant
    tsb = Seconds(desc="Temperature detection lag time constantTemperature detection lag time constant")

    # Load limiter reference valueLoad limiter reference value
    ldref = Float(desc="Load limiter reference valueLoad limiter reference value")

    # Power controller (reset) gainPower controller (reset) gain
    kimw = Float(desc="Power controller (reset) gainPower controller (reset) gain")

    # Maximum value for speed error signalMaximum value for speed error signal
    maxerr = Float(desc="Maximum value for speed error signalMaximum value for speed error signal")

    # Minimum valve position limitMinimum valve position limit
    vmin = Float(desc="Minimum valve position limitMinimum valve position limit")

    # Base for power values (&gt; 0.)Base for power values (&gt; 0.)
    mwbase = ActivePower(desc="Base for power values (&gt; 0.)Base for power values (&gt; 0.)")

    # Minimum valve closing rateMinimum valve closing rate
    rclose = Float(desc="Minimum valve closing rateMinimum valve closing rate")

    # Electrical power transducer time constant, sec. (&gt;0.)Electrical power transducer time constant, sec. (&gt;0.)
    tpelec = Seconds(desc="Electrical power transducer time constant, sec. (&gt;0.)Electrical power transducer time constant, sec. (&gt;0.)")

    # Maximum rate of load limit increaseMaximum rate of load limit increase
    rup = Float(desc="Maximum rate of load limit increaseMaximum rate of load limit increase")

    # Turbine lag time constant, sec.  (&gt;0.)Turbine lag time constant, sec.  (&gt;0.)
    tb = Seconds(desc="Turbine lag time constant, sec.  (&gt;0.)Turbine lag time constant, sec.  (&gt;0.)")

    # Acceleration limiter gainAcceleration limiter gain
    ka = Float(desc="Acceleration limiter gainAcceleration limiter gain")

    # Acceleration limiter time constant (&gt;0.)Acceleration limiter time constant (&gt;0.)
    ta = Seconds(desc="Acceleration limiter time constant (&gt;0.)Acceleration limiter time constant (&gt;0.)")

    # Governor derivative gainGovernor derivative gain
    kdgov = Float(desc="Governor derivative gainGovernor derivative gain")

    # Turbine gain  (&gt;0.)Turbine gain  (&gt;0.)
    kturb = Float(desc="Turbine gain  (&gt;0.)Turbine gain  (&gt;0.)")

    # Speed governor dead bandSpeed governor dead band
    db = Float(desc="Speed governor dead bandSpeed governor dead band")

    # Transport time delay for diesel engineTransport time delay for diesel engine
    teng = Seconds(desc="Transport time delay for diesel engineTransport time delay for diesel engine")

    # Turbine lead time constant, sec.Turbine lead time constant, sec.
    tc = Seconds(desc="Turbine lead time constant, sec.Turbine lead time constant, sec.")

    # Maximum valve opening rateMaximum valve opening rate
    ropen = Float(desc="Maximum valve opening rateMaximum valve opening rate")

    # Speed sensitivity coefficientSpeed sensitivity coefficient
    dm = Float(desc="Speed sensitivity coefficientSpeed sensitivity coefficient")

    # Load limiter integral gain for PI controllerLoad limiter integral gain for PI controller
    kiload = Float(desc="Load limiter integral gain for PI controllerLoad limiter integral gain for PI controller")

    # Power controller setpointPower controller setpoint
    pmwset = ActivePower(desc="Power controller setpointPower controller setpoint")

    # Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke)Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke)
    rselect = Bool(desc="Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke)Feedback signal for droop  = 1 electrical power = 0 none (isochronous governor) = -1 fuel valve stroke ( true stroke) = -2 governor output ( requested stroke)")

    # Governor integral gainGovernor integral gain
    kigov = Float(desc="Governor integral gainGovernor integral gain")

    # Load limiter proportional gain for PI controllerLoad limiter proportional gain for PI controller
    kpload = Float(desc="Load limiter proportional gain for PI controllerLoad limiter proportional gain for PI controller")

    # Load Limiter time constant (&gt;0.)Load Limiter time constant (&gt;0.)
    tfload = Seconds(desc="Load Limiter time constant (&gt;0.)Load Limiter time constant (&gt;0.)")

    #--------------------------------------------------------------------------
    #  Begin "GovCT1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "rdown", "vmax", "wfnl", "tdgov", "aset", "r", "wfspd", "kpgov", "minerr", "tsa", "tact", "tsb", "ldref", "kimw", "maxerr", "vmin", "mwbase", "rclose", "tpelec", "rup", "tb", "ka", "ta", "kdgov", "kturb", "db", "teng", "tc", "ropen", "dm", "kiload", "pmwset", "rselect", "kigov", "kpload", "tfload",
                label="Attributes", columns=3),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovCT1",
        title="GovCT1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovCT1" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT2T" class:
#------------------------------------------------------------------------------

class GovWT2T(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT2T" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT2T",
        title="GovWT2T",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT2T" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydro1" class:
#------------------------------------------------------------------------------

class GovHydro1(TurbineGovernor):
    """ Hydro turbine-governor model.Hydro turbine-governor model.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Permanent droop (R) (&gt;0)Permanent droop (R) (&gt;0)
    rperm = Float(desc="Permanent droop (R) (&gt;0)Permanent droop (R) (&gt;0)")

    # Gate servo time constant (&gt;0)Gate servo time constant (&gt;0)
    tg = Seconds(desc="Gate servo time constant (&gt;0)Gate servo time constant (&gt;0)")

    # Filter time constant (&gt;0)Filter time constant (&gt;0)
    tf = Seconds(desc="Filter time constant (&gt;0)Filter time constant (&gt;0)")

    # Base for power values  (&gt; 0.)Base for power values  (&gt; 0.)
    mwbase = ActivePower(desc="Base for power values  (&gt; 0.)Base for power values  (&gt; 0.)")

    # Turbine gain (&gt;0)Turbine gain (&gt;0)
    at = Float(desc="Turbine gain (&gt;0)Turbine gain (&gt;0)")

    # No-load flow at nominal head (&gt;=0)No-load flow at nominal head (&gt;=0)
    qnl = Float(desc="No-load flow at nominal head (&gt;=0)No-load flow at nominal head (&gt;=0)")

    # Water inertia time constant (&gt;0)Water inertia time constant (&gt;0)
    tw = Seconds(desc="Water inertia time constant (&gt;0)Water inertia time constant (&gt;0)")

    # Turbine damping factor (&gt;=0)Turbine damping factor (&gt;=0)
    dturb = Float(desc="Turbine damping factor (&gt;=0)Turbine damping factor (&gt;=0)")

    # Temporary droop (r) (&gt;R)Temporary droop (r) (&gt;R)
    rtemp = Float(desc="Temporary droop (r) (&gt;R)Temporary droop (r) (&gt;R)")

    # Washout time constant (&gt;0)Washout time constant (&gt;0)
    tr = Seconds(desc="Washout time constant (&gt;0)Washout time constant (&gt;0)")

    #--------------------------------------------------------------------------
    #  Begin "GovHydro1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI", "rperm", "tg", "tf", "mwbase", "at", "qnl", "tw", "dturb", "rtemp", "tr",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydro1",
        title="GovHydro1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydro1" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydroPID2" class:
#------------------------------------------------------------------------------

class GovHydroPID2(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydroPID2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydroPID2",
        title="GovHydroPID2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydroPID2" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovWT4T" class:
#------------------------------------------------------------------------------

class GovWT4T(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovWT4T" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovWT4T",
        title="GovWT4T",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovWT4T" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovSteamEU" class:
#------------------------------------------------------------------------------

class GovSteamEU(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovSteamEU" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovSteamEU",
        title="GovSteamEU",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovSteamEU" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovHydro0" class:
#------------------------------------------------------------------------------

class GovHydro0(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovHydro0" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovHydro0",
        title="GovHydro0",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovHydro0" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovGASTWD" class:
#------------------------------------------------------------------------------

class GovGASTWD(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovGASTWD" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovGASTWD",
        title="GovGASTWD",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovGASTWD" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GovGAST2" class:
#------------------------------------------------------------------------------

class GovGAST2(TurbineGovernor):
    pass
    #--------------------------------------------------------------------------
    #  Begin "GovGAST2" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("URI",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="dynamics.Dynamics.TurbineGovernors.GovGAST2",
        title="GovGAST2",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GovGAST2" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
