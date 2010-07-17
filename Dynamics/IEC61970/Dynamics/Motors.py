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

from Dynamics.IEC61970.Dynamics import AsynchronousMachine
from Dynamics import Element
from Dynamics.IEC61970.Dynamics import RotatingMachine



from enthought.traits.api import Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "MotorAsync" class:
#------------------------------------------------------------------------------

class MotorAsync(AsynchronousMachine):
    """ An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.An asynchronous (induction) motor with no external connection to the rotor windings, e.g., a squirrel-cage induction motor.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MotorAsync" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ratedS", "s1", "s12", "h", "d", "rs", "xls", "rr1", "xp", "tpo", "xm", "xs", "rr2", "xlr1", "xlr2", "tppo", "xpp",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Motors.MotorAsync",
        title="MotorAsync",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MotorAsync" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MechanicalLoad" class:
#------------------------------------------------------------------------------

class MechanicalLoad(Element):
    """ A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.A mechanical load represents the variation in a motor's shaft torque or power as a function of shaft speed.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MechanicalLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Motors.MechanicalLoad",
        title="MechanicalLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MechanicalLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchronousMotorType" class:
#------------------------------------------------------------------------------

class SynchronousMotorType(Element):
    """ Type of synchronous motorType of synchronous motor
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "SynchronousMotorType" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Motors.SynchronousMotorType",
        title="SynchronousMotorType",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchronousMotorType" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MotorSync" class:
#------------------------------------------------------------------------------

class MotorSync(RotatingMachine):
    """ A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.A large industrial motor or group of similar motors.  They are represented as <b>generators with negative Pgen</b> in the static (power flow) data.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "MotorSync" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ratedS", "s1", "s12", "h", "d", "rs", "xls",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Motors.MotorSync",
        title="MotorSync",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MotorSync" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "MechLoad1" class:
#------------------------------------------------------------------------------

class MechLoad1(MechanicalLoad):
    """ Mechanical load model 1Mechanical load model 1
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Speed squared coefficientSpeed squared coefficient
    b = Float(desc="Speed squared coefficientSpeed squared coefficient")

    # Speed squared coefficientSpeed squared coefficient
    a = Float(desc="Speed squared coefficientSpeed squared coefficient")

    # Speed to the exponent coefficientSpeed to the exponent coefficient
    d = Float(desc="Speed to the exponent coefficientSpeed to the exponent coefficient")

    # ExponentExponent
    e = Float(desc="ExponentExponent")

    #--------------------------------------------------------------------------
    #  Begin "MechLoad1" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "b", "a", "d", "e",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Motors.MechLoad1",
        title="MechLoad1",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "MechLoad1" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
