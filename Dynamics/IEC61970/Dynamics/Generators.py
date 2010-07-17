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

from Dynamics.IEC61970.Dynamics import RotatingMachine
from Dynamics import Element
from Dynamics.IEC61970.Dynamics import AsynchronousMachine
from Dynamics.IEC61970.Domain import Reactance



from enthought.traits.api import Enum
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


SynchronousGeneratorType = Enum("typeJ", "typeF", "transient", "roundRotor", "salientPole")

IfdBaseType = Enum("iffl", "other", "ifnl", "ifag")

ParametersFormType = Enum("equivalentCircuit", "timeConstantReactance")

#------------------------------------------------------------------------------
#  "GenSync" class:
#------------------------------------------------------------------------------

class GenSync(RotatingMachine):
    """ Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).Synchronous generator model. A single standard synchronous model is defined for the CIM, with several variations indicated by the 'model type' attribute.  This model can be used for all types of synchronous machines (salient pole, solid iron rotor, etc.).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GenSync" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ratedS", "s1", "s12", "h", "d", "rs", "xls",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Generators.GenSync",
        title="GenSync",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenSync" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GenLoad" class:
#------------------------------------------------------------------------------

class GenLoad(Element):
    """ Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.Representation of a small generator as a negative load rather than a dynamic generator model. This practice is also referred to as 'netting' the generation with the load, i.e. taking the net value of load minus generation as the new load value.  For dynamic modeling purposes, each generator that does not have a dynamic load model must have a genLoad record.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GenLoad" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Generators.GenLoad",
        title="GenLoad",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenLoad" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GenAsync" class:
#------------------------------------------------------------------------------

class GenAsync(AsynchronousMachine):
    """ An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.An asynchronous (induction) generator with no external connection to the rotor windings, e.g., squirrel-cage induction machine.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    pass
    #--------------------------------------------------------------------------
    #  Begin "GenAsync" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ratedS", "s1", "s12", "h", "d", "rs", "xls", "rr1", "xp", "tpo", "xm", "xs", "rr2", "xlr1", "xlr2", "tppo", "xpp",
                label="Attributes", columns=1),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Generators.GenAsync",
        title="GenAsync",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenAsync" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "GenEquiv" class:
#------------------------------------------------------------------------------

class GenEquiv(RotatingMachine):
    """ An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.An equivalent representation of a synchronous generator as a constant internal voltage behind an impedance Ra plus Xp.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Equivalent reactance, also known as Xp.Equivalent reactance, also known as Xp.
    xp = Reactance(desc="Equivalent reactance, also known as Xp.Equivalent reactance, also known as Xp.")

    #--------------------------------------------------------------------------
    #  Begin "GenEquiv" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "ratedS", "s1", "s12", "h", "d", "rs", "xls", "xp",
                label="Attributes"),
            VGroup("Model",
                label="References"),
            dock="tab"),
        id="Dynamics.IEC61970.Dynamics.Generators.GenEquiv",
        title="GenEquiv",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "GenEquiv" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
