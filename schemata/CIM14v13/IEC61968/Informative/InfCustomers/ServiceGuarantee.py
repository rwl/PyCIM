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

from CIM14v13.IEC61968.Common.Document import Document

class ServiceGuarantee(Document):
    """A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.
    """

    def __init__(self, automaticPay=False, serviceRequirement='', payAmount=0.0, applicationPeriod=None, *args, **kw_args):
        """Initializes a new 'ServiceGuarantee' instance.

        @param automaticPay: True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment. 
        @param serviceRequirement: Explanation of the requirement and conditions for satisfying it. 
        @param payAmount: Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'. 
        @param applicationPeriod: Period in which this service guantee applies.
        """
        #: True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment.
        self.automaticPay = automaticPay

        #: Explanation of the requirement and conditions for satisfying it.
        self.serviceRequirement = serviceRequirement

        #: Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'.
        self.payAmount = payAmount

        self.applicationPeriod = applicationPeriod

        super(ServiceGuarantee, self).__init__(*args, **kw_args)

    # Period in which this service guantee applies.
    applicationPeriod = None

