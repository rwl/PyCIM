# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE. See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA

from CIM14.IEC61970.Protection.ProtectionEquipment import ProtectionEquipment

class SynchrocheckRelay(ProtectionEquipment):
    """A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """

    def __init__(self, maxFreqDiff=0.0, maxVoltDiff=0.0, maxAngleDiff=0.0, *args, **kw_args):
        """Initialises a new 'SynchrocheckRelay' instance.

        @param maxFreqDiff: The maximum allowable frequency difference across the open device 
        @param maxVoltDiff: The maximum allowable difference voltage across the open device 
        @param maxAngleDiff: The maximum allowable voltage vector phase angle difference across the open device 
        """
        #: The maximum allowable frequency difference across the open device
        self.maxFreqDiff = maxFreqDiff

        #: The maximum allowable difference voltage across the open device
        self.maxVoltDiff = maxVoltDiff

        #: The maximum allowable voltage vector phase angle difference across the open device
        self.maxAngleDiff = maxAngleDiff

        super(SynchrocheckRelay, self).__init__(*args, **kw_args)

    _attrs = ["maxFreqDiff", "maxVoltDiff", "maxAngleDiff"]
    _attr_types = {"maxFreqDiff": float, "maxVoltDiff": float, "maxAngleDiff": float}
    _defaults = {"maxFreqDiff": 0.0, "maxVoltDiff": 0.0, "maxAngleDiff": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

