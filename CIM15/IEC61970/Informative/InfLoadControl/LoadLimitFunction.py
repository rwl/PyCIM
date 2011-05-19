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

from CIM15.IEC61970.Informative.InfLoadControl.LoadMgmtFunction import LoadMgmtFunction

class LoadLimitFunction(LoadMgmtFunction):
    """A kind of LoadMgmtFunction that limits the customer load to a given value.A kind of LoadMgmtFunction that limits the customer load to a given value.
    """

    def __init__(self, disconnectTimeDelay=0.0, isAutoReconOp=False, reconnectTimeDelay=0.0, maximumLoad=0.0, *args, **kw_args):
        """Initialises a new 'LoadLimitFunction' instance.

        @param disconnectTimeDelay: From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations. 
        @param isAutoReconOp: True if the switch will reconnect automatically, otherwise it will reconnect under manual control. 
        @param reconnectTimeDelay: From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity. 
        @param maximumLoad: The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load. 
        """
        #: From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations.
        self.disconnectTimeDelay = disconnectTimeDelay

        #: True if the switch will reconnect automatically, otherwise it will reconnect under manual control.
        self.isAutoReconOp = isAutoReconOp

        #: From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity.
        self.reconnectTimeDelay = reconnectTimeDelay

        #: The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load.
        self.maximumLoad = maximumLoad

        super(LoadLimitFunction, self).__init__(*args, **kw_args)

    _attrs = ["disconnectTimeDelay", "isAutoReconOp", "reconnectTimeDelay", "maximumLoad"]
    _attr_types = {"disconnectTimeDelay": float, "isAutoReconOp": bool, "reconnectTimeDelay": float, "maximumLoad": float}
    _defaults = {"disconnectTimeDelay": 0.0, "isAutoReconOp": False, "reconnectTimeDelay": 0.0, "maximumLoad": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

