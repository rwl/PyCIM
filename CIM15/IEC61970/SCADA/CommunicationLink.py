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

from CIM15.IEC61970.Core.PowerSystemResource import PowerSystemResource

class CommunicationLink(PowerSystemResource):
    """The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.The connection to remote units is through one or more communication links. Reduntant links may exist. The CommunicationLink class inherit PowerSystemResource. The intention is to allow CommunicationLinks to have Measurements. These Measurements can be used to model link status as operational, out of service, unit failure etc.
    """

    def __init__(self, RemoteUnits=None, *args, **kw_args):
        """Initialises a new 'CommunicationLink' instance.

        @param RemoteUnits: RTUs may be attached to communication links.
        """
        self._RemoteUnits = []
        self.RemoteUnits = [] if RemoteUnits is None else RemoteUnits

        super(CommunicationLink, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["RemoteUnits"]
    _many_refs = ["RemoteUnits"]

    def getRemoteUnits(self):
        """RTUs may be attached to communication links.
        """
        return self._RemoteUnits

    def setRemoteUnits(self, value):
        for p in self._RemoteUnits:
            filtered = [q for q in p.CommunicationLinks if q != self]
            self._RemoteUnits._CommunicationLinks = filtered
        for r in value:
            if self not in r._CommunicationLinks:
                r._CommunicationLinks.append(self)
        self._RemoteUnits = value

    RemoteUnits = property(getRemoteUnits, setRemoteUnits)

    def addRemoteUnits(self, *RemoteUnits):
        for obj in RemoteUnits:
            if self not in obj._CommunicationLinks:
                obj._CommunicationLinks.append(self)
            self._RemoteUnits.append(obj)

    def removeRemoteUnits(self, *RemoteUnits):
        for obj in RemoteUnits:
            if self in obj._CommunicationLinks:
                obj._CommunicationLinks.remove(self)
            self._RemoteUnits.remove(obj)

