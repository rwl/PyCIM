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

from CIM14v13.IEC61968.Informative.InfLoadControl.LoadMgmtFunction import LoadMgmtFunction

class LoadLimitFunction(LoadMgmtFunction):
    """A kind of LoadMgmtFunction that limits the customer load to a given value.
    """

    def __init__(self, isAutoReconOp=False, disconnectTimeDelay=0.0, reconnectTimeDelay=0.0, maximumLoad=0.0, **kw_args):
        """Initializes a new 'LoadLimitFunction' instance.

        @param isAutoReconOp: True if the switch will reconnect automatically, otherwise it will reconnect under manual control. 
        @param disconnectTimeDelay: From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations. 
        @param reconnectTimeDelay: From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity. 
        @param maximumLoad: The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load. 
        """
        #: True if the switch will reconnect automatically, otherwise it will reconnect under manual control.
        self.isAutoReconOp = isAutoReconOp

        #: From the point when the maximumLoad threshold is crossed there may be a finite delay before the switch actually disconnects the load. Typically this is to buffer against transient load fluctuations.
        self.disconnectTimeDelay = disconnectTimeDelay

        #: From the point when the load recovers from an overload condition and crosses the maximumLoad threshold going down, there may be a finite time delay before the switch actually reconnects the load. Typically this is to give overload conditions sufficient time to clear, thus preventing unnecessary load switching activity.
        self.reconnectTimeDelay = reconnectTimeDelay

        #: The power level, to which the customer load is being limited when this function activates. When the maximum load is exceeded the switch will typically open to shed the complete customer load.
        self.maximumLoad = maximumLoad

        super(LoadLimitFunction, self).__init__(**kw_args)

