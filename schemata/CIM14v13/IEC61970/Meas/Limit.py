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

class Limit(IdentifiedObject):
    """Specifies one limit value for a Measurement. A Measurement typically has several limits that are kept together by the LimitSet class. The actual meaning and use of a Limit instance (i.e., if it is an alarm or warning limit or if it is a high or low limit) is not captured in the Limit class. However the name of a Limit instance may indicate both meaning and use.
    """

    def __init__(self, Procedures=None, **kw_args):
        """Initializes a new 'Limit' instance.

        @param Procedures:
        """
        self._Procedures = []
        self.Procedures = [] if Procedures is None else Procedures

        super(Limit, self).__init__(**kw_args)

    def getProcedures(self):
        
        return self._Procedures

    def setProcedures(self, value):
        for p in self._Procedures:
            filtered = [q for q in p.Limits if q != self]
            self._Procedures._Limits = filtered
        for r in value:
            if self not in r._Limits:
                r._Limits.append(self)
        self._Procedures = value

    Procedures = property(getProcedures, setProcedures)

    def addProcedures(self, *Procedures):
        for obj in Procedures:
            if self not in obj._Limits:
                obj._Limits.append(self)
            self._Procedures.append(obj)

    def removeProcedures(self, *Procedures):
        for obj in Procedures:
            if self in obj._Limits:
                obj._Limits.remove(self)
            self._Procedures.remove(obj)

