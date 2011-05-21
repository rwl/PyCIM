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

from CIM14.Element import Element

class OperatingShare(Element):
    """Specifies the contract relationship between a PowerSystemResource and a contract participant.
    """

    def __init__(self, percentage=0.0, PowerSystemResource=None, OperatingParticipant=None, *args, **kw_args):
        """Initialises a new 'OperatingShare' instance.

        @param percentage: Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%. 
        @param PowerSystemResource: The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
        @param OperatingParticipant: The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
        """
        #: Percentage ownership for this device.   The percentage indicates the percentage ownership of the PSROwner for the PowerSystemResource.  The total percentage ownership for a PowerSystemResource should add to 100%.
        self.percentage = percentage

        self._PowerSystemResource = None
        self.PowerSystemResource = PowerSystemResource

        self._OperatingParticipant = None
        self.OperatingParticipant = OperatingParticipant

        super(OperatingShare, self).__init__(*args, **kw_args)

    _attrs = ["percentage"]
    _attr_types = {"percentage": float}
    _defaults = {"percentage": 0.0}
    _enums = {}
    _refs = ["PowerSystemResource", "OperatingParticipant"]
    _many_refs = []

    def getPowerSystemResource(self):
        """The PowerSystemResource to which the attribues apply.   The percentage ownership of all owners of a PowerSystemResource should add to 100%.
        """
        return self._PowerSystemResource

    def setPowerSystemResource(self, value):
        if self._PowerSystemResource is not None:
            filtered = [x for x in self.PowerSystemResource.OperatingShare if x != self]
            self._PowerSystemResource._OperatingShare = filtered

        self._PowerSystemResource = value
        if self._PowerSystemResource is not None:
            if self not in self._PowerSystemResource._OperatingShare:
                self._PowerSystemResource._OperatingShare.append(self)

    PowerSystemResource = property(getPowerSystemResource, setPowerSystemResource)

    def getOperatingParticipant(self):
        """The linkage to a owners  and its linkage attributes like percentage ownership.   The ownership percentage should add to 100% for all owners of a PowerSystemResource, but a PSROwner may own any percentage of any number of PowerSystemResource objects.
        """
        return self._OperatingParticipant

    def setOperatingParticipant(self, value):
        if self._OperatingParticipant is not None:
            filtered = [x for x in self.OperatingParticipant.OperatingShare if x != self]
            self._OperatingParticipant._OperatingShare = filtered

        self._OperatingParticipant = value
        if self._OperatingParticipant is not None:
            if self not in self._OperatingParticipant._OperatingShare:
                self._OperatingParticipant._OperatingShare.append(self)

    OperatingParticipant = property(getOperatingParticipant, setOperatingParticipant)

