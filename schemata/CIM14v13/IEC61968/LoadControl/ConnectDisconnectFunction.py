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

from CIM14v13.IEC61968.Metering.DeviceFunction import DeviceFunction

class ConnectDisconnectFunction(DeviceFunction):
    """A function that will disconnect or reconnect the customer's load under defined conditions.
    """

    def __init__(self, isDelayedDiscon=False, isConnected=False, eventCount=0, isLocalAutoDisconOp=False, isRemoteAutoDisconOp=False, isRemoteAutoReconOp=False, isLocalAutoReconOp=False, rcdInfo=None, Switches=None, **kw_args):
        """Initializes a new 'ConnectDisconnectFunction' instance.

        @param isDelayedDiscon: If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting. 
        @param isConnected: True if this function is in the connected state. 
        @param eventCount: Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared. 
        @param isLocalAutoDisconOp: (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually. 
        @param isRemoteAutoDisconOp: If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually. 
        @param isRemoteAutoReconOp: If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually. 
        @param isLocalAutoReconOp: If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually. 
        @param rcdInfo: Information on remote connect disconnect switch.
        @param Switches:
        """
        #: If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting.
        self.isDelayedDiscon = isDelayedDiscon

        #: True if this function is in the connected state.
        self.isConnected = isConnected

        #: Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared.
        self.eventCount = eventCount

        #: (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually.
        self.isLocalAutoDisconOp = isLocalAutoDisconOp

        #: If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually.
        self.isRemoteAutoDisconOp = isRemoteAutoDisconOp

        #: If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually.
        self.isRemoteAutoReconOp = isRemoteAutoReconOp

        #: If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually.
        self.isLocalAutoReconOp = isLocalAutoReconOp

        self.rcdInfo = rcdInfo

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        super(ConnectDisconnectFunction, self).__init__(**kw_args)

    # Information on remote connect disconnect switch.
    rcdInfo = None

    def getSwitches(self):
        
        return self._Switches

    def setSwitches(self, value):
        for p in self._Switches:
            filtered = [q for q in p.ConnectDisconnectFunctions if q != self]
            self._Switches._ConnectDisconnectFunctions = filtered
        for r in value:
            if self not in r._ConnectDisconnectFunctions:
                r._ConnectDisconnectFunctions.append(self)
        self._Switches = value

    Switches = property(getSwitches, setSwitches)

    def addSwitches(self, *Switches):
        for obj in Switches:
            if self not in obj._ConnectDisconnectFunctions:
                obj._ConnectDisconnectFunctions.append(self)
            self._Switches.append(obj)

    def removeSwitches(self, *Switches):
        for obj in Switches:
            if self in obj._ConnectDisconnectFunctions:
                obj._ConnectDisconnectFunctions.remove(self)
            self._Switches.remove(obj)

