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

from CIM14v13.IEC61970.Core.Curve import Curve

class InadvertentAccount(Curve):
    """An account for tracking inadvertent interchange versus time for each control area. A control area may have more than one inadvertent account in order to track inadvertent over one or more specific tie points in addition to the usual overall net inadvertent. Separate accounts would also be used to track designated time periods, such as on-peak and off-peak.
    """

    def __init__(self, HostControlArea=None, **kw_args):
        """Initializes a new 'InadvertentAccount' instance.

        @param HostControlArea: A control area can have one or more net inadvertent interchange accounts
        """
        self._HostControlArea = None
        self.HostControlArea = HostControlArea

        super(InadvertentAccount, self).__init__(**kw_args)

    def getHostControlArea(self):
        """A control area can have one or more net inadvertent interchange accounts
        """
        return self._HostControlArea

    def setHostControlArea(self, value):
        if self._HostControlArea is not None:
            filtered = [x for x in self.HostControlArea.InadvertentAccounts if x != self]
            self._HostControlArea._InadvertentAccounts = filtered

        self._HostControlArea = value
        if self._HostControlArea is not None:
            self._HostControlArea._InadvertentAccounts.append(self)

    HostControlArea = property(getHostControlArea, setHostControlArea)

