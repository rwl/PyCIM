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

from CIM14v13.IEC61970.Core.PowerSystemResource import PowerSystemResource

class PrimeMover(PowerSystemResource):
    """The machine used to develop mechanical energy used to drive a generator.
    """

    def __init__(self, primeMoverRating=0.0, SynchronousMachines=None, **kw_args):
        """Initializes a new 'PrimeMover' instance.

        @param primeMoverRating: Rating of prime mover 
        @param SynchronousMachines: Synchronous machines this Prime mover drives.
        """
        #: Rating of prime mover
        self.primeMoverRating = primeMoverRating

        self._SynchronousMachines = []
        self.SynchronousMachines = [] if SynchronousMachines is None else SynchronousMachines

        super(PrimeMover, self).__init__(**kw_args)

    def getSynchronousMachines(self):
        """Synchronous machines this Prime mover drives.
        """
        return self._SynchronousMachines

    def setSynchronousMachines(self, value):
        for p in self._SynchronousMachines:
            filtered = [q for q in p.PrimeMovers if q != self]
            self._SynchronousMachines._PrimeMovers = filtered
        for r in value:
            if self not in r._PrimeMovers:
                r._PrimeMovers.append(self)
        self._SynchronousMachines = value

    SynchronousMachines = property(getSynchronousMachines, setSynchronousMachines)

    def addSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            if self not in obj._PrimeMovers:
                obj._PrimeMovers.append(self)
            self._SynchronousMachines.append(obj)

    def removeSynchronousMachines(self, *SynchronousMachines):
        for obj in SynchronousMachines:
            if self in obj._PrimeMovers:
                obj._PrimeMovers.remove(self)
            self._SynchronousMachines.remove(obj)

