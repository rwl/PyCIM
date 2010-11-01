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

"""The package contains portions of the model defined byEnterprise Resource Planning (ERP) standards like those proposed by the Open Applications Group (OAG). It is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (as defined by OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeld 'Erp...' should be associated with the appropriate classes of that standard. In fact, definitions of 'Erp...' classes are based on OAG Nouns to facilitate this process.  TODO: The following has been copied from a very old version of draft Part 11, so the references are wrong, but we store the knowledge here to reuse later: 'The Enterprise Resource Planning (ERP) Support Package contains portions of the model defined by ERP standards like those proposed by the Open Applications Group (OAG). This package is provided to facilitate integration among electric utility applications (CIM) and enterprise resource planning (ERP) applications (OAG). Rather than inventing new CIM classes that accomplish similar functionality as in existing ERP models, the preferred approach is to use and extend ERP classes as appropriate in other packages. If a model other that the OAG standard is used as a basis for ERP integration, the utility classes labeled 'Erp...' should be associated with the appropriate classes of that standard.'
"""

ns_prefix = "cimInfERPSupport"
ns_uri = "http://iec.ch/TC57/CIM-generic#InfERPSupport"
