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

from CIM15.IEC61968.Metering.EndDeviceFunction import EndDeviceFunction

class ConnectDisconnectFunction(EndDeviceFunction):
    """A function that will disconnect or reconnect the customer's load under defined conditions.A function that will disconnect or reconnect the customer's load under defined conditions.
    """

    def __init__(self, isDelayedDiscon=False, eventCount=0, isRemoteAutoReconOp=False, isRemoteAutoDisconOp=False, isLocalAutoDisconOp=False, isLocalAutoReconOp=False, isConnected=False, rcdInfo=None, Switches=None, *args, **kw_args):
        """Initialises a new 'ConnectDisconnectFunction' instance.

        @param isDelayedDiscon: If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting. 
        @param eventCount: Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared. 
        @param isRemoteAutoReconOp: If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually. 
        @param isRemoteAutoDisconOp: If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually. 
        @param isLocalAutoDisconOp: (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually. 
        @param isLocalAutoReconOp: If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually. 
        @param isConnected: True if this function is in the connected state. 
        @param rcdInfo: Information on remote connect disconnect switch.
        @param Switches:
        """
        #: If set true, the switch may disconnect the service at the end of a specified time delay after the disconnect signal had been given. If set false, the switch may disconnect the service immediately after the disconnect signal had been given. This is typically the case for over current circuit-breakers which are classified as either instantaneous or slow acting.
        self.isDelayedDiscon = isDelayedDiscon

        #: Running cumulative count of (connect or disconnect) events, for the lifetime of this function or until the value is cleared.
        self.eventCount = eventCount

        #: If set true and if reconnection can be operated remotely, then the operation happens automatically. If false and if reconnection can be operated remotely, then the operation happens manually.
        self.isRemoteAutoReconOp = isRemoteAutoReconOp

        #: If set true and if disconnection can be operated remotely, then the operation happens automatically. If set false and if disconnection can be operated remotely, then the operation happens manually.
        self.isRemoteAutoDisconOp = isRemoteAutoDisconOp

        #: (if disconnection can be operated locally) If set true, the operation happens automatically, otherwise it happens manually.
        self.isLocalAutoDisconOp = isLocalAutoDisconOp

        #: If set true and if reconnection can be operated locally, then the operation happens automatically. Otherwise, it is manually.
        self.isLocalAutoReconOp = isLocalAutoReconOp

        #: True if this function is in the connected state.
        self.isConnected = isConnected

        self.rcdInfo = rcdInfo

        self._Switches = []
        self.Switches = [] if Switches is None else Switches

        super(ConnectDisconnectFunction, self).__init__(*args, **kw_args)

    _attrs = ["isDelayedDiscon", "eventCount", "isRemoteAutoReconOp", "isRemoteAutoDisconOp", "isLocalAutoDisconOp", "isLocalAutoReconOp", "isConnected"]
    _attr_types = {"isDelayedDiscon": bool, "eventCount": int, "isRemoteAutoReconOp": bool, "isRemoteAutoDisconOp": bool, "isLocalAutoDisconOp": bool, "isLocalAutoReconOp": bool, "isConnected": bool}
    _defaults = {"isDelayedDiscon": False, "eventCount": 0, "isRemoteAutoReconOp": False, "isRemoteAutoDisconOp": False, "isLocalAutoDisconOp": False, "isLocalAutoReconOp": False, "isConnected": False}
    _enums = {}
    _refs = ["rcdInfo", "Switches"]
    _many_refs = ["Switches"]

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

