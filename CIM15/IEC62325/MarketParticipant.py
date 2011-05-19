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

from CIM15.IEC61968.Common.Organisation import Organisation

class MarketParticipant(Organisation):

    def __init__(self, MarketRoles=None, *args, **kw_args):
        """Initialises a new 'MarketParticipant' instance.

        @param MarketRoles: All roles of this market participant.
        """
        self._MarketRoles = []
        self.MarketRoles = [] if MarketRoles is None else MarketRoles

        super(MarketParticipant, self).__init__(*args, **kw_args)

    _attrs = []
    _attr_types = {}
    _defaults = {}
    _enums = {}
    _refs = ["MarketRoles"]
    _many_refs = ["MarketRoles"]

    def getMarketRoles(self):
        """All roles of this market participant.
        """
        return self._MarketRoles

    def setMarketRoles(self, value):
        for p in self._MarketRoles:
            filtered = [q for q in p.MarketParticipants if q != self]
            self._MarketRoles._MarketParticipants = filtered
        for r in value:
            if self not in r._MarketParticipants:
                r._MarketParticipants.append(self)
        self._MarketRoles = value

    MarketRoles = property(getMarketRoles, setMarketRoles)

    def addMarketRoles(self, *MarketRoles):
        for obj in MarketRoles:
            if self not in obj._MarketParticipants:
                obj._MarketParticipants.append(self)
            self._MarketRoles.append(obj)

    def removeMarketRoles(self, *MarketRoles):
        for obj in MarketRoles:
            if self in obj._MarketParticipants:
                obj._MarketParticipants.remove(self)
            self._MarketRoles.remove(obj)

