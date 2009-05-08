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

from CIM13r19.Core import Equipment
from CIM13r19.Core import IdentifiedObject



from enthought.traits.api import Instance, List, Property, Float, Bool, Int
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ProtectionEquipment" class:
#------------------------------------------------------------------------------

class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # Circuit breakers may be operated by protection relays.
    Operates_Breakers = List(Instance("CIM13r19.Wires.ProtectedSwitch"),
        desc="Circuit breakers may be operated by protection relays.")

    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ConductingEquipments = List(Instance("CIM13r19.Core.ConductingEquipment"),
        desc="Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.")

    # The Protection Equipments having the Unit.
    Unit = Instance("CIM13r19.Core.Unit",
        desc="The Protection Equipments having the Unit.",
        transient=True,
        opposite="ProtectionEquipments",
        editor=InstanceEditor(name="_units"))

    def _get_units(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM13r19.Core.Unit" ]
        else:
            return []

    _units = Property(fget=_get_units)

    # Direction same as positive active power flow value.
    powerDirectionFlag = Bool(desc="Direction same as positive active power flow value.")

    # The minimum allowable value.
    lowLimit = Float(desc="The minimum allowable value.")

    # The maximum allowable value.
    highLimit = Float(desc="The maximum allowable value.")

    # The time delay from detection of abnormal conditions to relay operation.
    relayDelayTime = Float(desc="The time delay from detection of abnormal conditions to relay operation.")

    #--------------------------------------------------------------------------
    #  Begin "ProtectionEquipment" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "powerDirectionFlag", "lowLimit", "highLimit", "relayDelayTime",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Operates_Breakers", "ConductingEquipments", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Protection.ProtectionEquipment",
        title="ProtectionEquipment",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ProtectionEquipment" user definitions:
    #--------------------------------------------------------------------------

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
    Breaker = Instance("CIM13r19.Wires.ProtectedSwitch",
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
                    "CIM13r19.Wires.ProtectedSwitch" ]
        else:
            return []

    _protectedswitchs = Property(fget=_get_protectedswitchs)

    # Indicates the time lapse before the reclose step will execute a reclose.
    recloseDelay = Float(desc="Indicates the time lapse before the reclose step will execute a reclose.")

    # Indicates the ordinal position of the reclose step relative to other steps in the sequence.
    recloseStep = Int(desc="Indicates the ordinal position of the reclose step relative to other steps in the sequence.")

    #--------------------------------------------------------------------------
    #  Begin "RecloseSequence" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "recloseDelay", "recloseStep",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Breaker",
                label="References"),
            dock="tab"),
        id="CIM13r19.Protection.RecloseSequence",
        title="RecloseSequence",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "RecloseSequence" user definitions:
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
    maxVoltDiff = Float(desc="The maximum allowable difference voltage across the open device")

    # The maximum allowable frequency difference across the open device
    maxFreqDiff = Float(desc="The maximum allowable frequency difference across the open device")

    # The maximum allowable voltage vector phase angle difference across the open device
    maxAngleDiff = Float(desc="The maximum allowable voltage vector phase angle difference across the open device")

    #--------------------------------------------------------------------------
    #  Begin "SynchrocheckRelay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "powerDirectionFlag", "lowLimit", "highLimit", "relayDelayTime", "maxVoltDiff", "maxFreqDiff", "maxAngleDiff",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Operates_Breakers", "ConductingEquipments", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Protection.SynchrocheckRelay",
        title="SynchrocheckRelay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "SynchrocheckRelay" user definitions:
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

    # Current limit #3 for inverse time pickup
    currentLimit3 = Float(desc="Current limit #3 for inverse time pickup")

    # Current limit #1 for inverse time pickup
    currentLimit1 = Float(desc="Current limit #1 for inverse time pickup")

    # Inverse time delay #3 for current limit #3
    timeDelay3 = Float(desc="Inverse time delay #3 for current limit #3")

    # Set true if the current relay has inverse time characteristic.
    inverseTimeFlag = Bool(desc="Set true if the current relay has inverse time characteristic.")

    # Inverse time delay #1 for current limit #1
    timeDelay1 = Float(desc="Inverse time delay #1 for current limit #1")

    # Current limit #2 for inverse time pickup
    currentLimit2 = Float(desc="Current limit #2 for inverse time pickup")

    # Inverse time delay #2 for current limit #2
    timeDelay2 = Float(desc="Inverse time delay #2 for current limit #2")

    #--------------------------------------------------------------------------
    #  Begin "CurrentRelay" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("name", "localName", "description", "aliasName", "mRID", "pathName", "normalIlyInService", "powerDirectionFlag", "lowLimit", "highLimit", "relayDelayTime", "currentLimit3", "currentLimit1", "timeDelay3", "inverseTimeFlag", "timeDelay1", "currentLimit2", "timeDelay2",
                label="Attributes", columns=1),
            VGroup("Parent", "ModelingAuthoritySet", "PSRType", "OperatedBy_Companies", "ReportingGroup", "OperatingShare", "PsrLists", "OutageSchedule", "Contains_Measurements", "OperationalLimitSet", "ContingencyEquipment", "MemberOf_EquipmentContainer", "Operates_Breakers", "ConductingEquipments", "Unit",
                label="References", columns=1),
            dock="tab"),
        id="CIM13r19.Protection.CurrentRelay",
        title="CurrentRelay",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "CurrentRelay" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
