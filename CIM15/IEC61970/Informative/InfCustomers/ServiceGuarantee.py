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

from CIM15.IEC61968.Common.Document import Document

class ServiceGuarantee(Document):
    """A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.A service guarantee, often imposed by a regulator, defines conditions that, if not satisfied, will result in the utility making a monetary payment to the customer. Note that guarantee's identifier is in the 'name' attribute and the status of the guarantee is in the 'Status.status' attribute. Example service requirements include: 1) If power is not restored within 24 hours, customers can claim $50 for residential customers or $100 for commercial and industrial customers. In addition for each extra period of 12 hours the customer's supply has not been activated, the customer can claim $25. 2) If a customer has a question about their electricity bill, the utility will investigate and respond to the inquiry within 15 working days. If utility fails to meet its guarantee, utility will automatically pay the customer $50.
    """

    def __init__(self, automaticPay=False, payAmount=0.0, serviceRequirement='', applicationPeriod=None, *args, **kw_args):
        """Initialises a new 'ServiceGuarantee' instance.

        @param automaticPay: True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment. 
        @param payAmount: Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'. 
        @param serviceRequirement: Explanation of the requirement and conditions for satisfying it. 
        @param applicationPeriod: Period in which this service guantee applies.
        """
        #: True if utility must autmatically pay the specified amount whenever the condition is not satisified, otherwise customer must make a claim to receive payment.
        self.automaticPay = automaticPay

        #: Amount to be paid by the service provider to the customer for each violation of the 'serviceRequirement'.
        self.payAmount = payAmount

        #: Explanation of the requirement and conditions for satisfying it.
        self.serviceRequirement = serviceRequirement

        self.applicationPeriod = applicationPeriod

        super(ServiceGuarantee, self).__init__(*args, **kw_args)

    _attrs = ["automaticPay", "payAmount", "serviceRequirement"]
    _attr_types = {"automaticPay": bool, "payAmount": float, "serviceRequirement": str}
    _defaults = {"automaticPay": False, "payAmount": 0.0, "serviceRequirement": ''}
    _enums = {}
    _refs = ["applicationPeriod"]
    _many_refs = []

    # Period in which this service guantee applies.
    applicationPeriod = None

