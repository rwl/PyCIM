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

class MarketRole(IdentifiedObject):
    """Role of a market player.Role of a market player.
    """

    def __init__(self, kind="transmissionOperator", status=None, MarketParticipants=None, *args, **kw_args):
        """Initialises a new 'MarketRole' instance.

        @param kind: Kind of role an organisation plays in a market. Values are: "transmissionOperator", "complianceMonitor", "standardsDeveloper", "interchangeAuthority", "energyServiceConsumer", "planningAuthority", "other", "purchasingSellingEntity", "competitiveRetailer", "transmissionOwner", "transmissionServiceProvider", "generatorOperator", "balancingAuthority", "loadServingEntity", "transmissionPlanner", "distributionProvider", "reliabilityAuthority", "resourcePlanner", "generatorOwner"
        @param status:
        @param MarketParticipants: All market participants with this role.
        """
        #: Kind of role an organisation plays in a market. Values are: "transmissionOperator", "complianceMonitor", "standardsDeveloper", "interchangeAuthority", "energyServiceConsumer", "planningAuthority", "other", "purchasingSellingEntity", "competitiveRetailer", "transmissionOwner", "transmissionServiceProvider", "generatorOperator", "balancingAuthority", "loadServingEntity", "transmissionPlanner", "distributionProvider", "reliabilityAuthority", "resourcePlanner", "generatorOwner"
        self.kind = kind

        self.status = status

        self._MarketParticipants = []
        self.MarketParticipants = [] if MarketParticipants is None else MarketParticipants

        super(MarketRole, self).__init__(*args, **kw_args)

    _attrs = ["kind"]
    _attr_types = {"kind": str}
    _defaults = {"kind": "transmissionOperator"}
    _enums = {"kind": "MarketRoleKind"}
    _refs = ["status", "MarketParticipants"]
    _many_refs = ["MarketParticipants"]

    status = None

    def getMarketParticipants(self):
        """All market participants with this role.
        """
        return self._MarketParticipants

    def setMarketParticipants(self, value):
        for p in self._MarketParticipants:
            filtered = [q for q in p.MarketRoles if q != self]
            self._MarketParticipants._MarketRoles = filtered
        for r in value:
            if self not in r._MarketRoles:
                r._MarketRoles.append(self)
        self._MarketParticipants = value

    MarketParticipants = property(getMarketParticipants, setMarketParticipants)

    def addMarketParticipants(self, *MarketParticipants):
        for obj in MarketParticipants:
            if self not in obj._MarketRoles:
                obj._MarketRoles.append(self)
            self._MarketParticipants.append(obj)

    def removeMarketParticipants(self, *MarketParticipants):
        for obj in MarketParticipants:
            if self in obj._MarketRoles:
                obj._MarketRoles.remove(self)
            self._MarketParticipants.remove(obj)

