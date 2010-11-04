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

from CIM14v13.IEC61970.Core.RegularIntervalSchedule import RegularIntervalSchedule

class ReserveReqCurve(RegularIntervalSchedule):
    """A curve relating  reserve requirement versus time, showing the values of a specific reserve requirement for each unit of the period covered. The  curve can be based on 'absolute' time or on 'normalized' time.  X is time, typically expressed in absolute time Y1 is reserve requirement, typically expressed in MW
    """

    def __init__(self, ReserveReq=None, **kw_args):
        """Initializes a new 'ReserveReqCurve' instance.

        @param ReserveReq:
        """
        self._ReserveReq = None
        self.ReserveReq = ReserveReq

        super(ReserveReqCurve, self).__init__(**kw_args)

    def getReserveReq(self):
        
        return self._ReserveReq

    def setReserveReq(self, value):
        if self._ReserveReq is not None:
            self._ReserveReq._ReserveReqCurve = None

        self._ReserveReq = value
        if self._ReserveReq is not None:
            self._ReserveReq._ReserveReqCurve = self

    ReserveReq = property(getReserveReq, setReserveReq)

