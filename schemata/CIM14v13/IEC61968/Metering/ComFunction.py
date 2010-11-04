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

class ComFunction(DeviceFunction):
    """Communication function of communication equipment or a device such as a meter.
    """

    def __init__(self, twoWay=False, amrAddress='', amrRouter='', **kw_args):
        """Initializes a new 'ComFunction' instance.

        @param twoWay: True when the AMR module can both send and receive messages. Default is false (i.e., module can only send). 
        @param amrAddress: Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter. 
        @param amrRouter: Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters. 
        """
        #: True when the AMR module can both send and receive messages. Default is false (i.e., module can only send).
        self.twoWay = twoWay

        #: Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter.
        self.amrAddress = amrAddress

        #: Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters.
        self.amrRouter = amrRouter

        super(ComFunction, self).__init__(**kw_args)

