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

""" An extension to the Core and Wires packages that models information for protection equipment such as relays. These entities are used within training simulators and distribution network fault location applications.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM.Core import IdentifiedObject
from CIM.Core import Equipment
from CIM.Domain import Seconds
from CIM.Domain import CurrentFlow
from CIM.Domain import Voltage
from CIM.Domain import AngleRadians
from CIM.Domain import Frequency



from enthought.traits.api import Instance, List, Property, Int, Bool, Float
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "RecloseSequence" class:
#------------------------------------------------------------------------------

class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A breaker may have zero or more automatic reclosures after a trip occurs.
    Breaker = Instance("CIM.Wires.ProtectedSwitch",
        desc="A breaker may have zero or more automatic reclosures after a trip occurs.",
        transient=True,
        opposite="RecloseSequences",
        editor=InstanceEditor(name="_protectedswitchs"))

    def _get_protectedswitchs(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Wires.ProtectedSwitch" ]
        else:
            return []

    _protectedswitchs = Property(fget=_get_protectedswitchs)

    # Indicates the ordinal position of the reclose step relative to other steps in the sequence.
    recloseStep = Int(desc="Indicates the ordinal position of the reclose step relative to other steps in the sequence.")

    # Indicates the time lapse before the reclose step will execute a reclose.
    recloseDelay = Seconds(desc="Indicates the time lapse before the reclose step will execute a reclose.")

    #--------------------------------------------------------------------------
    #  Begin "RecloseSequence" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "recloseStep", "recloseDelay",
                label="Attributes"),
            VGroup("ModelingAuthoritySet", "Breaker",
                label="References"),
            dock="tab"),
        id="CIM.Protection.RecloseSequence",
        title="RecloseSequence",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RecloseSequence" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ProtectionEquipment" class:
#------------------------------------------------------------------------------

class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Protected switches operated by this ProtectionEquipment.
    Operates_Breakers = List(Instance("CIM.Wires.ProtectedSwitch"),
        desc="Protected switches operated by this ProtectionEquipment.")

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ConductingEquipments = List(Instance("CIM.Core.ConductingEquipment"),
        desc="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.")

    # The Unit for the Protection Equipment.
    Unit = Instance("CIM.Core.Unit",
        desc="The Unit for the Protection Equipment.",
        transient=True,
        opposite="ProtectionEquipments",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # Direction same as positive active power flow value.
    powerDirectionFlag = Bool(desc="Direction same as positive active power flow value.")

    # The time delay from detection of abnormal conditions to relay operation.
    relayDelayTime = Seconds(desc="The time delay from detection of abnormal conditions to relay operation.")

    # The minimum allowable value.
    lowLimit = Float(desc="The minimum allowable value.")

    # The maximum allowable value.
    highLimit = Float(desc="The maximum allowable value.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectionEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "powerDirectionFlag", "relayDelayTime", "lowLimit", "highLimit",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "Operates_Breakers", "ConductingEquipments", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Protection.ProtectionEquipment",
        title="ProtectionEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectionEquipment" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "CurrentRelay" class:
#------------------------------------------------------------------------------

class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Set true if the current relay has inverse time characteristic.
    inverseTimeFlag = Bool(desc="Set true if the current relay has inverse time characteristic.")

    # Inverse time delay #2 for current limit #2
    timeDelay2 = Seconds(desc="Inverse time delay #2 for current limit #2")

    # Current limit #1 for inverse time pickup
    currentLimit1 = CurrentFlow(desc="Current limit #1 for inverse time pickup")

    # Current limit #3 for inverse time pickup
    currentLimit3 = CurrentFlow(desc="Current limit #3 for inverse time pickup")

    # Current limit #2 for inverse time pickup
    currentLimit2 = CurrentFlow(desc="Current limit #2 for inverse time pickup")

    # Inverse time delay #1 for current limit #1
    timeDelay1 = Seconds(desc="Inverse time delay #1 for current limit #1")

    # Inverse time delay #3 for current limit #3
    timeDelay3 = Seconds(desc="Inverse time delay #3 for current limit #3")

    #--------------------------------------------------------------------------
    #  Begin "CurrentRelay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "powerDirectionFlag", "relayDelayTime", "lowLimit", "highLimit", "inverseTimeFlag", "timeDelay2", "currentLimit1", "currentLimit3", "currentLimit2", "timeDelay1", "timeDelay3",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "Operates_Breakers", "ConductingEquipments", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Protection.CurrentRelay",
        title="CurrentRelay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentRelay" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "SynchrocheckRelay" class:
#------------------------------------------------------------------------------

class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # The maximum allowable difference voltage across the open device
    maxVoltDiff = Voltage(desc="The maximum allowable difference voltage across the open device")

    # The maximum allowable voltage vector phase angle difference across the open device
    maxAngleDiff = AngleRadians(desc="The maximum allowable voltage vector phase angle difference across the open device")

    # The maximum allowable frequency difference across the open device
    maxFreqDiff = Frequency(desc="The maximum allowable frequency difference across the open device")

    #--------------------------------------------------------------------------
    #  Begin "SynchrocheckRelay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "mRID", "localName", "pathName", "description", "aliasName", "name", "equivalent", "normalIlyInService", "powerDirectionFlag", "relayDelayTime", "lowLimit", "highLimit", "maxVoltDiff", "maxAngleDiff", "maxFreqDiff",
                label="Attributes", columns=1),
            VGroup("ModelingAuthoritySet", "OperatedBy_Companies", "PsrLists", "Contains_Measurements", "OperatingShare", "OutageSchedule", "ReportingGroup", "PSRType", "OperationalLimitSet", "MemberOf_EquipmentContainer", "ContingencyEquipment", "Operates_Breakers", "ConductingEquipments", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM.Protection.SynchrocheckRelay",
        title="SynchrocheckRelay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchrocheckRelay" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
