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

from CIM14v13.IEC61970.Core.IdentifiedObject import IdentifiedObject

class MarketRole(IdentifiedObject):
    """Role an organisation plays in a market. Examples include one or more of values defined in MarketRoleKind.
    """

    def __init__(self, kind='other', status=None, Organisations=None, *args, **kw_args):
        """Initializes a new 'MarketRole' instance.

        @param kind: Kind of role an organisation plays in a market. Values are: "other", "transmissionServiceProvider", "planningAuthority", "reliabilityAuthority", "transmissionOwner", "transmissionPlanner", "generatorOperator", "energyServiceConsumer", "generatorOwner", "transmissionOperator", "complianceMonitor", "distributionProvider", "loadServingEntity", "interchangeAuthority", "purchasingSellingEntity", "resourcePlanner", "balancingAuthority", "competitiveRetailer", "standardsDeveloper"
        @param status:
        @param Organisations:
        """
        #: Kind of role an organisation plays in a market.Values are: "other", "transmissionServiceProvider", "planningAuthority", "reliabilityAuthority", "transmissionOwner", "transmissionPlanner", "generatorOperator", "energyServiceConsumer", "generatorOwner", "transmissionOperator", "complianceMonitor", "distributionProvider", "loadServingEntity", "interchangeAuthority", "purchasingSellingEntity", "resourcePlanner", "balancingAuthority", "competitiveRetailer", "standardsDeveloper"
        self.kind = kind

        self.status = status

        self._Organisations = []
        self.Organisations = [] if Organisations is None else Organisations

        super(MarketRole, self).__init__(*args, **kw_args)

    status = None

    def getOrganisations(self):
        
        return self._Organisations

    def setOrganisations(self, value):
        for p in self._Organisations:
            filtered = [q for q in p.MarketRoles if q != self]
            self._Organisations._MarketRoles = filtered
        for r in value:
            if self not in r._MarketRoles:
                r._MarketRoles.append(self)
        self._Organisations = value

    Organisations = property(getOrganisations, setOrganisations)

    def addOrganisations(self, *Organisations):
        for obj in Organisations:
            if self not in obj._MarketRoles:
                obj._MarketRoles.append(self)
            self._Organisations.append(obj)

    def removeOrganisations(self, *Organisations):
        for obj in Organisations:
            if self in obj._MarketRoles:
                obj._MarketRoles.remove(self)
            self._Organisations.remove(obj)

