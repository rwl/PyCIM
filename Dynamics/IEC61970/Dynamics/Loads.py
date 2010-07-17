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

from Dynamics import Element
from Dynamics.IEC61970.Domain import Resistance
from Dynamics.IEC61970.Domain import Reactance
from Dynamics.IEC61970.Domain import Seconds
from Dynamics.IEC61970.Domain import Voltage



from enthought.traits.api import Enum, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


StaticLoadType = Enum("ZIP2", "ZIP1", "exponential")

#------------------------------------------------------------------------------
#  "AggregateLoad" class:
#------------------------------------------------------------------------------

class AggregateLoad(Element):
    """ Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.Aggregate loads are used to represent all or part of the real and reactive load from a load in the static (power flow) data. This load is usually the aggregation of many individual load devices. The load models are approximate representation of the aggregate response of the load devices to system disturbances.   Models of loads for dynamic analysis may themselves be either static or dynamic. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage. A dynamic load model can used to represent the aggregate response of the motor components of the load.   Large industrial motors or groups of similar motors may be represented by individual motor models (synchronous or asynchronous) which are usually represented as generators with negative Pgen in the static (power flow) data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "AggregateLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.AggregateLoad",
        title="AggregateLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AggregateLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadStatic" class:
#------------------------------------------------------------------------------

class LoadStatic(AggregateLoad):
    """ General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.General Static Load Model. A static load model represents the sensitivity of the real and reactive power consumed by the load to the amplitude and frequency of the bus voltage.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    ep2 = Float

    ep1 = Float

    kp2 = Float

    ep3 = Float

    kp1 = Float

    kq4 = Float

    kq3 = Float

    kq2 = Float

    kq1 = Float

    eq1 = Float

    eq2 = Float

    kp4 = Float

    kp3 = Float

    eq3 = Float

    kqf = Float

    kpf = Float

    #--------------------------------------------------------------------------
    #  Begin "LoadStatic" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "kqf", "kpf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadStatic",
        title="LoadStatic",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadStatic" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadMotor" class:
#------------------------------------------------------------------------------

class LoadMotor(AggregateLoad):
    """ Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.Aggregate induction motor load. This model  is used to represent a fraction of an ordinary load as 'induction motor load'.  It allows load that is treated as ordinary constant power in power flow analysis to be represented by an induction motor in dynamic simulation.  Either a 'one-cage' or 'two-cage' model of the induction machine can be modeled.  Magnetic saturation is not modeled.  This model is intended for representation of aggregations of many motors dispersed through a load represented at a high voltage bus but where there is no information on the characteristics of individual motors.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Loading factor &ndash; ratio of initial P to motor MVA baseLoading factor &ndash; ratio of initial P to motor MVA base
    lfac = Float(desc="Loading factor &ndash; ratio of initial P to motor MVA baseLoading factor &ndash; ratio of initial P to motor MVA base")

    # Stator resistanceStator resistance
    ra = Resistance(desc="Stator resistanceStator resistance")

    # Damping factorDamping factor
    d = Float(desc="Damping factorDamping factor")

    # Synchronous reactanceSynchronous reactance
    ls = Reactance(desc="Synchronous reactanceSynchronous reactance")

    # Sub-transient rotor time constantSub-transient rotor time constant
    tppo = Seconds(desc="Sub-transient rotor time constantSub-transient rotor time constant")

    # Circuit breaker operating time (default = 999)Circuit breaker operating time (default = 999)
    tbkr = Seconds(desc="Circuit breaker operating time (default = 999)Circuit breaker operating time (default = 999)")

    # Sub-transient reactanceSub-transient reactance
    lpp = Reactance(desc="Sub-transient reactanceSub-transient reactance")

    # Transient rotor time constantTransient rotor time constant
    tpo = Seconds(desc="Transient rotor time constantTransient rotor time constant")

    # Inertia constantInertia constant
    h = Seconds(desc="Inertia constantInertia constant")

    # Transient reactanceTransient reactance
    lp = Reactance(desc="Transient reactanceTransient reactance")

    # Voltage threshold for tripping (default = 0)Voltage threshold for tripping (default = 0)
    vt = Voltage(desc="Voltage threshold for tripping (default = 0)Voltage threshold for tripping (default = 0)")

    # Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0)Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0)
    pfrac = Float(desc="Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0)Fraction of constant-power load to be represented                               by this motor model (between 1.0 and 0.0)")

    # Voltage trip pickup time (default = 999)Voltage trip pickup time (default = 999)
    tv = Seconds(desc="Voltage trip pickup time (default = 999)Voltage trip pickup time (default = 999)")

    #--------------------------------------------------------------------------
    #  Begin "LoadMotor" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "lfac", "ra", "d", "ls", "tppo", "tbkr", "lpp", "tpo", "h", "lp", "vt", "pfrac", "tv",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadMotor",
        title="LoadMotor",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadMotor" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadStaticBus" class:
#------------------------------------------------------------------------------

class LoadStaticBus(LoadStatic):
    """ Static load model associated with a single bus.Static load model associated with a single bus.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "LoadStaticBus" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "kqf", "kpf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadStaticBus",
        title="LoadStaticBus",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadStaticBus" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadStaticZone" class:
#------------------------------------------------------------------------------

class LoadStaticZone(LoadStatic):
    """ Static load associated with a zone.Static load associated with a zone.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "LoadStaticZone" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "kqf", "kpf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadStaticZone",
        title="LoadStaticZone",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadStaticZone" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadStaticArea" class:
#------------------------------------------------------------------------------

class LoadStaticArea(LoadStatic):
    """ Static load associated with an Area.Static load associated with an Area.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "LoadStaticArea" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "kqf", "kpf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadStaticArea",
        title="LoadStaticArea",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadStaticArea" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadStaticSystem" class:
#------------------------------------------------------------------------------

class LoadStaticSystem(LoadStatic):
    """ Static load associated with a specific system.Static load associated with a specific system.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "LoadStaticSystem" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "kqf", "kpf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadStaticSystem",
        title="LoadStaticSystem",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadStaticSystem" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "LoadStaticOwner" class:
#------------------------------------------------------------------------------

class LoadStaticOwner(LoadStatic):
    """ Static load associated with a single owner.Static load associated with a single owner.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "LoadStaticOwner" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ep2", "ep1", "kp2", "ep3", "kp1", "kq4", "kq3", "kq2", "kq1", "eq1", "eq2", "kp4", "kp3", "eq3", "kqf", "kpf",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Loads.LoadStaticOwner",
        title="LoadStaticOwner",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "LoadStaticOwner" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
