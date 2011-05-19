# Copyright (C) 2010-2011 Richard Lincoln
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to
# deal in the Software without restriction, including without limitation the
# rights to use, copy, modify, merge, publish, distribute, sublicense, and/or
# sell copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING
# FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS
# IN THE SOFTWARE.

from CIM15.IEC61970.Protection.ProtectionEquipment import ProtectionEquipment

class SynchrocheckRelay(ProtectionEquipment):
    """A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.A device that operates when two AC circuits are within the desired limits of frequency, phase angle, and voltage, to permit or to cause the paralleling of these two circuits. Used to prevent the paralleling of non-synchronous topological islands.
    """

    def __init__(self, maxFreqDiff=0.0, maxAngleDiff=0.0, maxVoltDiff=0.0, *args, **kw_args):
        """Initialises a new 'SynchrocheckRelay' instance.

        @param maxFreqDiff: The maximum allowable frequency difference across the open device 
        @param maxAngleDiff: The maximum allowable voltage vector phase angle difference across the open device 
        @param maxVoltDiff: The maximum allowable difference voltage across the open device 
        """
        #: The maximum allowable frequency difference across the open device
        self.maxFreqDiff = maxFreqDiff

        #: The maximum allowable voltage vector phase angle difference across the open device
        self.maxAngleDiff = maxAngleDiff

        #: The maximum allowable difference voltage across the open device
        self.maxVoltDiff = maxVoltDiff

        super(SynchrocheckRelay, self).__init__(*args, **kw_args)

    _attrs = ["maxFreqDiff", "maxAngleDiff", "maxVoltDiff"]
    _attr_types = {"maxFreqDiff": float, "maxAngleDiff": float, "maxVoltDiff": float}
    _defaults = {"maxFreqDiff": 0.0, "maxAngleDiff": 0.0, "maxVoltDiff": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

