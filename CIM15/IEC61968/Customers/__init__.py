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

"""This package contains the core information classes that support customer billing applications.
"""

from CIM15.IEC61968.Customers.Tariff import Tariff
from CIM15.IEC61968.Customers.CustomerAccount import CustomerAccount
from CIM15.IEC61968.Customers.ServiceLocation import ServiceLocation
from CIM15.IEC61968.Customers.CustomerAgreement import CustomerAgreement
from CIM15.IEC61968.Customers.ServiceCategory import ServiceCategory
from CIM15.IEC61968.Customers.PricingStructure import PricingStructure
from CIM15.IEC61968.Customers.Customer import Customer

nsURI = "http://iec.ch/TC57/2010/CIM-schema-cim15#Customers"
nsPrefix = "cimCustomers"


class CustomerKind(str):
    """Values are: windMachine, residentialAndCommercial, internalUse, energyServiceScheduler, residentialAndStreetlight, residential, pumpingLoad, other, commercialIndustrial, energyServiceSupplier, residentialStreetlightOthers, residentialFarmService
    """
    pass

class RevenueKind(str):
    """Values are: irrigation, residential, nonResidential, industrial, other, commercial, streetLight
    """
    pass

class ServiceKind(str):
    """Values are: other, refuse, sewerage, electricity, heat, internet, rates, time, water, gas, tvLicence
    """
    pass
