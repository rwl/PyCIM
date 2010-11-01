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

from CIM14v13.IEC61968.Common.Agreement import Agreement

class OpenAccessProduct(Agreement):
    """Contracts for services offered commercially.
    """

    def __init__(self, ProvidedBy_TransmissionService=None, AncillaryServices=None, *args, **kw_args):
        """Initializes a new 'OpenAccessProduct' instance.

        @param ProvidedBy_TransmissionService: A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
        @param AncillaryServices: AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
        """
        self._ProvidedBy_TransmissionService = []
        self.ProvidedBy_TransmissionService = [] if ProvidedBy_TransmissionService is None else ProvidedBy_TransmissionService

        self._AncillaryServices = []
        self.AncillaryServices = [] if AncillaryServices is None else AncillaryServices

        super(OpenAccessProduct, self).__init__(*args, **kw_args)

    def getProvidedBy_TransmissionService(self):
        """A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
        """
        return self._ProvidedBy_TransmissionService

    def setProvidedBy_TransmissionService(self, value):
        for x in self._ProvidedBy_TransmissionService:
            x._TransContractFor = None
        for y in value:
            y._TransContractFor = self
        self._ProvidedBy_TransmissionService = value

    ProvidedBy_TransmissionService = property(getProvidedBy_TransmissionService, setProvidedBy_TransmissionService)

    def addProvidedBy_TransmissionService(self, *ProvidedBy_TransmissionService):
        for obj in ProvidedBy_TransmissionService:
            obj._TransContractFor = self
            self._ProvidedBy_TransmissionService.append(obj)

    def removeProvidedBy_TransmissionService(self, *ProvidedBy_TransmissionService):
        for obj in ProvidedBy_TransmissionService:
            obj._TransContractFor = None
            self._ProvidedBy_TransmissionService.remove(obj)

    def getAncillaryServices(self):
        """AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
        """
        return self._AncillaryServices

    def setAncillaryServices(self, value):
        for x in self._AncillaryServices:
            x._OpenAccessProduct = None
        for y in value:
            y._OpenAccessProduct = self
        self._AncillaryServices = value

    AncillaryServices = property(getAncillaryServices, setAncillaryServices)

    def addAncillaryServices(self, *AncillaryServices):
        for obj in AncillaryServices:
            obj._OpenAccessProduct = self
            self._AncillaryServices.append(obj)

    def removeAncillaryServices(self, *AncillaryServices):
        for obj in AncillaryServices:
            obj._OpenAccessProduct = None
            self._AncillaryServices.remove(obj)

