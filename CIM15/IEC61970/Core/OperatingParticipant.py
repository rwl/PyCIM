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

from CIM15.IEC61970.Core.IdentifiedObject import IdentifiedObject

class OperatingParticipant(IdentifiedObject):
    """An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.An operator of multiple PowerSystemResource objects. Note multple OperatingParticipants may operate the same PowerSystemResource object.   This can be used for modeling jointly owned units where each owner operates as a contractual share.
    """

    def __init__(self, OperatingShare=None, *args, **kw_args):
        """Initialises a new 'OperatingParticipant' instance.

        @param OperatingShare: The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
        """
        self._OperatingShare = []
        self.OperatingShare = [] if OperatingShare is None else OperatingShare

        super(OperatingParticipant, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["OperatingShare"]
    _many_refs = ["OperatingShare"]

    def getOperatingShare(self):
        """The operating shares of an operating participant.   An operating participant can be reused for any number of PSR's.
        """
        return self._OperatingShare

    def setOperatingShare(self, value):
        for x in self._OperatingShare:
            x.OperatingParticipant = None
        for y in value:
            y._OperatingParticipant = self
        self._OperatingShare = value

    OperatingShare = property(getOperatingShare, setOperatingShare)

    def addOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj.OperatingParticipant = self

    def removeOperatingShare(self, *OperatingShare):
        for obj in OperatingShare:
            obj.OperatingParticipant = None

