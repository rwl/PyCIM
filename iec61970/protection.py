# @copyright: 2009 Richard W. Lincoln
# @contact: r.w.lincoln@gmail.com
# @license: GPLv3

""" An extension to the Core and Wires packages that models information for protection equipment such as relays. These entities are used within training simulators and distribution network fault location applications.
"""
from iec61970.core import Equipment
from iec61970.core import IdentifiedObject
from iec61970.domain import CurrentFlow
from iec61970.domain import Boolean
from iec61970.domain import Seconds
from iec61970.domain import Float
from iec61970.domain import Integer
from iec61970.domain import AngleRadians
from iec61970.domain import Frequency
from iec61970.domain import Voltage
from iec61970.domain import String
from iec61970.domain import AbsoluteDateTime



from enthought.traits.api import HasTraits, Instance, List, Bool, Float, Int



class ProtectionEquipment(Equipment):
    """ An electrical device designed to respond to input conditions in a prescribed manner and after specified conditions are met to cause contact operation or similar abrupt change in associated electric control circuits, or simply to display the detected condition. Protection equipment are associated with conducting equipment and usually operate circuit breakers. For protection relays, the typeName attribute is a type identifier as specified by IEC 61850 with a Pro_ prefix, e.g. Pro_OVR for overvoltage relay.
    """
    # Protection equipment may be used to protect specific Conducting Equipment. Multiple equipment may be protected or monitored by multiple protection equipment.
    ConductingEquipments = List(Instance("iec61970.core.ConductingEquipment.ConductingEquipment"))
    # Circuit breakers may be operated by protection relays.
    Operates_Breakers = List(Instance("iec61970.wires.ProtectedSwitch.ProtectedSwitch"))
    Unit = Instance("iec61970.core.Unit.Unit", allow_none=False)
    # The time delay in seconds from detection of abnormal conditions to relay operation
    relayDelayTime = Seconds
    # The maximum allowable value.
    highLimit = Float
    # The minimum allowable value.
    lowLimit = Float
    # Direction same as positive active power flow value.
    powerDirectionFlag = Boolean

class RecloseSequence(IdentifiedObject):
    """ A reclose sequence (open and close) is defined for each possible reclosure of a breaker.
    """
    # A breaker may have zero or more automatic reclosures after a trip occurs.
    Breaker = Instance("iec61970.wires.ProtectedSwitch.ProtectedSwitch", allow_none=False)
    # Indicates the time lapse before the reclose step will execute a reclose.
    recloseDelay = Seconds
    # Indicates the ordinal position of the reclose step relative to other steps in the sequence.
    recloseStep = Integer

class ProtectionVersion(HasTraits):
    version = String
    date = AbsoluteDateTime

class CurrentRelay(ProtectionEquipment):
    """ A device that checks current flow values in any direction or designated direction
    """
    # Current limit #1 for inverse time pickup
    currentLimit1 = CurrentFlow
    # Current limit #2 for inverse time pickup
    currentLimit2 = CurrentFlow
    # Current limit #3 for inverse time pickup
    currentLimit3 = CurrentFlow
    # True/False flag that indicates whether or not the current relay has inverse time characteristic.
    inverseTimeFlag = Boolean
    # Inverse time delay #1 for current limit #1
    timeDelay1 = Seconds
    # Inverse time delay #2 for current limit #2
    timeDelay2 = Seconds
    # Inverse time delay #3 for current limit #3
    timeDelay3 = Seconds

class SynchrocheckRelay(ProtectionEquipment):
    """ A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """
    # The maximum allowable voltage vector phase angle difference across the open device
    maxAngleDiff = AngleRadians
    # The maximum allowable frequency difference across the open device
    maxFreqDiff = Frequency
    # The maximum allowable difference voltage across the open device
    maxVoltDiff = Voltage


