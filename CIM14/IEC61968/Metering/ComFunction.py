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

from CIM14.IEC61968.Metering.DeviceFunction import DeviceFunction

class ComFunction(DeviceFunction):
    """Communication function of communication equipment or a device such as a meter.
    """

    def __init__(self, amrRouter='', twoWay=False, amrAddress='', *args, **kw_args):
        """Initialises a new 'ComFunction' instance.

        @param amrRouter: Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters. 
        @param twoWay: True when the AMR module can both send and receive messages. Default is false (i.e., module can only send). 
        @param amrAddress: Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter. 
        """
        #: Communication ID number (e.g. port number, serial number, data collector ID, etc.) of the parent device associated to this AMR module. Note: If someone swaps out a meter, they may inadvertently disrupt the AMR system. Some technologies route readings from nearby meters through a common collection point on an electricity meter. Removal of such a meter disrupts AMR for numerous nearby meters.
        self.amrRouter = amrRouter

        #: True when the AMR module can both send and receive messages. Default is false (i.e., module can only send).
        self.twoWay = twoWay

        #: Communication ID number (e.g. serial number, IP address, telephone number, etc.) of the AMR module which serves this meter.
        self.amrAddress = amrAddress

        super(ComFunction, self).__init__(*args, **kw_args)

    _attrs = ["amrRouter", "twoWay", "amrAddress"]
    _attr_types = {"amrRouter": str, "twoWay": bool, "amrAddress": str}
    _defaults = {"amrRouter": '', "twoWay": False, "amrAddress": ''}
    _enums = {}
    _refs = []
    _many_refs = []

