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

"""This package contains the core information classes that support customer billing applications.
"""

nsPrefix = "cimCustomers"
nsURI = "http://iec.ch/TC57/2009/CIM-schema-cim14#Customers"

from CIM14.IEC61968.Customers.Customer import Customer
from CIM14.IEC61968.Customers.CustomerAccount import CustomerAccount
from CIM14.IEC61968.Customers.ServiceCategory import ServiceCategory
from CIM14.IEC61968.Customers.PricingStructure import PricingStructure
from CIM14.IEC61968.Customers.ServiceLocation import ServiceLocation
from CIM14.IEC61968.Customers.CustomerAgreement import CustomerAgreement
from CIM14.IEC61968.Customers.Tariff import Tariff

