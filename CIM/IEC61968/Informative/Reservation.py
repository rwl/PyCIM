#------------------------------------------------------------------------------
# Copyright (C) 2010 Richard Lincoln
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#------------------------------------------------------------------------------

""" This package includes information for Transaction Scheduling for Energy, Generation Capacity, Transmission, and Ancillary Services.
"""
#------------------------------------------------------------------------------
#  Imports:
#------------------------------------------------------------------------------

from CIM import Element
from CIM.IEC61970.Core import IdentifiedObject
from CIM.IEC61970.Domain import ActivePower



from enthought.traits.api import Instance, List, Property, Str, Date, Bool
# <<< imports
# @generated
from enthought.traits.ui.api import View, Group, Item, HGroup, VGroup, Tabbed, VGrid, InstanceEditor
# >>> imports
#------------------------------------------------------------------------------
#  Trait definitions:
#------------------------------------------------------------------------------


#------------------------------------------------------------------------------
#  "ReservationVersion" class:
#------------------------------------------------------------------------------

class ReservationVersion(Element):
    version = Str

    date = Date

    #--------------------------------------------------------------------------
    #  Begin "ReservationVersion" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "version", "date",
                label="Attributes"),
            VGroup("Parent",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.ReservationVersion",
        title="ReservationVersion",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ReservationVersion" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TiePoint" class:
#------------------------------------------------------------------------------

class TiePoint(IdentifiedObject):
    """ Site of an interface between interchange areas. The tie point can be a network branch (e.g., transmission line or transformer) or a switching device. For transmission lines, the interchange area boundary is usually at a designated point such as the middle of the line. Line end metering is then corrected for line losses.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A tiepoint may be declared as a service point.
    Declared_ServicePoint = Instance("CIM.IEC61968.Informative.Reservation.ServicePoint",
        desc="A tiepoint may be declared as a service point.",
        transient=True,
        opposite="Declare_TiePoint",
        editor=InstanceEditor(name="_servicepoints"))

    def _get_servicepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.ServicePoint" ]
        else:
            return []

    _servicepoints = Property(fget=_get_servicepoints)

    # A measurement is made on the A side of a tie point
    For_Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"),
        desc="A measurement is made on the A side of a tie point")

    # A measurement is made on the B side of a tie point
    By_Measurements = List(Instance("CIM.IEC61970.Meas.Measurement"),
        desc="A measurement is made on the B side of a tie point")

    # The MW rating of the tie point
    tiePointMWRating = ActivePower(desc="The MW rating of the tie point")

    #--------------------------------------------------------------------------
    #  Begin "TiePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName", "tiePointMWRating",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "Declared_ServicePoint", "For_Measurements", "By_Measurements",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.TiePoint",
        title="TiePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TiePoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionService" class:
#------------------------------------------------------------------------------

class TransmissionService(IdentifiedObject):
    """ Transmission products along posted transmission path.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transmission product is offered as a transmission service along a transmission path.
    OfferedAs = List(Instance("CIM.IEC61968.Informative.Financial.TransmissionProduct"),
        desc="A transmission product is offered as a transmission service along a transmission path.")

    # A transmission service is offered on a transmission path.
    Offering = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionPath"),
        desc="A transmission service is offered on a transmission path.")

    # A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.
    TransContractFor = Instance("CIM.IEC61968.Informative.Financial.OpenAccessProduct",
        desc="A TransmissionService is sold according to the terms of a particular OpenAccessProduct agreement.",
        transient=True,
        opposite="ProvidedBy_TransmissionService",
        editor=InstanceEditor(name="_openaccessproducts"))

    def _get_openaccessproducts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.OpenAccessProduct" ]
        else:
            return []

    _openaccessproducts = Property(fget=_get_openaccessproducts)

    # A transmission schedule posts the available transmission capacity for a transmission line.
    ScheduledBy = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.AvailableTransmissionCapacity"),
        desc="A transmission schedule posts the available transmission capacity for a transmission line.")

    # The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).
    Offers = Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider",
        desc="The combination of a TransmissionProduct on a TransmissionPath is a TransmissionService, for which the TransmissionProvider must post one or two ATC's (AvailableTransmissionCapacity - Amount of possible flow by  direction).",
        transient=True,
        opposite="OfferedBy",
        editor=InstanceEditor(name="_transmissionproviders"))

    def _get_transmissionproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.TransmissionProvider" ]
        else:
            return []

    _transmissionproviders = Property(fget=_get_transmissionproviders)

    # A service reservation reserves a particular transmission service.
    ReservedBy_ServiceReservation = List(Instance("CIM.IEC61968.Informative.Reservation.ServiceReservation"),
        desc="A service reservation reserves a particular transmission service.")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionService" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "OfferedAs", "Offering", "TransContractFor", "ScheduledBy", "Offers", "ReservedBy_ServiceReservation",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.TransmissionService",
        title="TransmissionService",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionService" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ServicePoint" class:
#------------------------------------------------------------------------------

class ServicePoint(IdentifiedObject):
    """ Each ServicePoint is contained within (or on the boundary of) an ElectronicIinterchangeArea. ServicePoints are defined termination points of a transmission path (down to distribution level or to a customer - generation or consumption or both).
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A CustomerConsumer may have one or more ServicePoints.
    CustomerConsumer = Instance("CIM.IEC61968.Informative.Financial.CustomerConsumer",
        desc="A CustomerConsumer may have one or more ServicePoints.",
        transient=True,
        opposite="ServicePoint",
        editor=InstanceEditor(name="_customerconsumers"))

    def _get_customerconsumers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.CustomerConsumer" ]
        else:
            return []

    _customerconsumers = Property(fget=_get_customerconsumers)

    # A tiepoint may be declared as a service point.
    Declare_TiePoint = Instance("CIM.IEC61968.Informative.Reservation.TiePoint",
        desc="A tiepoint may be declared as a service point.",
        transient=True,
        opposite="Declared_ServicePoint",
        editor=InstanceEditor(name="_tiepoints"))

    def _get_tiepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.TiePoint" ]
        else:
            return []

    _tiepoints = Property(fget=_get_tiepoints)

    # An EnergyProduct injects energy into a service point.
    EnergyProducts = List(Instance("CIM.IEC61968.Informative.EnergyScheduling.EnergyProduct"),
        desc="An EnergyProduct injects energy into a service point.")

    # A TransmissionProvider registers one or more ServicePoints.
    TransmissionProvider = Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider",
        desc="A TransmissionProvider registers one or more ServicePoints.",
        transient=True,
        opposite="ServicePoint",
        editor=InstanceEditor(name="_transmissionproviders"))

    def _get_transmissionproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.TransmissionProvider" ]
        else:
            return []

    _transmissionproviders = Property(fget=_get_transmissionproviders)

    # A transmission path has a 'point-of-delivery' service point
    HasAPOD_ = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionPath"),
        desc="A transmission path has a 'point-of-delivery' service point")

    # A transmission path has a 'point-of-receipt' service point
    HasAPOR_ = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionPath"),
        desc="A transmission path has a 'point-of-receipt' service point")

    # A transmission path's service point is part of an interchange area
    MemberOf = Instance("CIM.IEC61968.Informative.EnergyScheduling.SubControlArea",
        desc="A transmission path's service point is part of an interchange area",
        transient=True,
        opposite="PartOf",
        editor=InstanceEditor(name="_subcontrolareas"))

    def _get_subcontrolareas(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.SubControlArea" ]
        else:
            return []

    _subcontrolareas = Property(fget=_get_subcontrolareas)

    # A GenerationProvider has one or more ServicePoints where energy is injected into the network.
    GenerationProvider = Instance("CIM.IEC61968.Informative.Financial.GenerationProvider",
        desc="A GenerationProvider has one or more ServicePoints where energy is injected into the network.",
        transient=True,
        opposite="ServicePoint",
        editor=InstanceEditor(name="_generationproviders"))

    def _get_generationproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.GenerationProvider" ]
        else:
            return []

    _generationproviders = Property(fget=_get_generationproviders)

    #--------------------------------------------------------------------------
    #  Begin "ServicePoint" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "CustomerConsumer", "Declare_TiePoint", "EnergyProducts", "TransmissionProvider", "HasAPOD_", "HasAPOR_", "MemberOf", "GenerationProvider",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.ServicePoint",
        title="ServicePoint",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServicePoint" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "ServiceReservation" class:
#------------------------------------------------------------------------------

class ServiceReservation(Element):
    """ A ServiceReservation is a reservation for either AncillaryServices or TransmissionServices. In the case of TransmissionServices, this is the right to some amount of AvailableTransmissionCapacity for a product on a path in a direction for some specific period of time
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A Marketer holds title to a ServiceReservation.
    Holds = Instance("CIM.IEC61968.Informative.Financial.Marketer",
        desc="A Marketer holds title to a ServiceReservation.",
        transient=True,
        opposite="HeldBy",
        editor=InstanceEditor(name="_marketers"))

    def _get_marketers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.Marketer" ]
        else:
            return []

    _marketers = Property(fget=_get_marketers)

    # A ServiceReservation may be resold by a Marketer.
    Resells = Instance("CIM.IEC61968.Informative.Financial.Marketer",
        desc="A ServiceReservation may be resold by a Marketer.",
        transient=True,
        opposite="ResoldBy",
        editor=InstanceEditor(name="_marketers"))

    def _get_marketers(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.Marketer" ]
        else:
            return []

    _marketers = Property(fget=_get_marketers)

    # A ServiceReservation guarantees a certain AncillaryService.
    Reserves_AncillaryServices = List(Instance("CIM.IEC61968.Informative.Reservation.AncillaryService"),
        desc="A ServiceReservation guarantees a certain AncillaryService.")

    # A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.
    Sells = Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider",
        desc="A TransmissionProvider sells the right to transmit energy across the wires in a ServiceReservation.",
        transient=True,
        opposite="SoldBy",
        editor=InstanceEditor(name="_transmissionproviders"))

    def _get_transmissionproviders(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.TransmissionProvider" ]
        else:
            return []

    _transmissionproviders = Property(fget=_get_transmissionproviders)

    # A service reservation reserves a particular transmission service.
    Reserves_TransmissionService = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionService"),
        desc="A service reservation reserves a particular transmission service.")

    #--------------------------------------------------------------------------
    #  Begin "ServiceReservation" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID",
                label="Attributes"),
            VGroup("Parent", "Holds", "Resells", "Reserves_AncillaryServices", "Sells", "Reserves_TransmissionService",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.ServiceReservation",
        title="ServiceReservation",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "ServiceReservation" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "TransmissionPath" class:
#------------------------------------------------------------------------------

class TransmissionPath(Element):
    """ An electrical connection, link, or line consisting of one or more parallel transmission elements between two areas of the interconnected electric systems, or portions thereof. TransmissionCorridor and TransmissionRightOfWay refer to legal aspects. The TransmissionPath refers to the segments between a TransmissionProvider's ServicePoints.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A transmission service is offered on a transmission path.
    OfferedOn = List(Instance("CIM.IEC61968.Informative.Reservation.TransmissionService"),
        desc="A transmission service is offered on a transmission path.")

    # A transmission path has a 'point-of-delivery' service point
    DeliveryPointFor = Instance("CIM.IEC61968.Informative.Reservation.ServicePoint",
        desc="A transmission path has a 'point-of-delivery' service point",
        transient=True,
        opposite="HasAPOD_",
        editor=InstanceEditor(name="_servicepoints"))

    def _get_servicepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.ServicePoint" ]
        else:
            return []

    _servicepoints = Property(fget=_get_servicepoints)

    # A transmission path has a 'point-of-receipt' service point
    PointOfReceiptFor = Instance("CIM.IEC61968.Informative.Reservation.ServicePoint",
        desc="A transmission path has a 'point-of-receipt' service point",
        transient=True,
        opposite="HasAPOR_",
        editor=InstanceEditor(name="_servicepoints"))

    def _get_servicepoints(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.ServicePoint" ]
        else:
            return []

    _servicepoints = Property(fget=_get_servicepoints)

    # A transmission product is located on a transmission path.
    LocatedOn = List(Instance("CIM.IEC61968.Informative.Financial.TransmissionProduct"),
        desc="A transmission product is located on a transmission path.")

    # A TransmissionPath is contained in a TransmissionCorridor.
    For = Instance("CIM.IEC61968.Informative.EnergyScheduling.TransmissionCorridor",
        desc="A TransmissionPath is contained in a TransmissionCorridor.",
        transient=True,
        opposite="ContainedIn",
        editor=InstanceEditor(name="_transmissioncorridors"))

    def _get_transmissioncorridors(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.EnergyScheduling.TransmissionCorridor" ]
        else:
            return []

    _transmissioncorridors = Property(fget=_get_transmissioncorridors)

    # The total transmission capability of a transmission path in the reference direction
    totalTransferCapability = ActivePower(desc="The total transmission capability of a transmission path in the reference direction")

    # Flag which indicates if the transmission path is also a designated interconnection 'parallel path'
    parallelPathFlag = Bool(desc="Flag which indicates if the transmission path is also a designated interconnection 'parallel path'")

    # The available transmission capability of a transmission path for the reference direction
    availTransferCapability = ActivePower(desc="The available transmission capability of a transmission path for the reference direction")

    #--------------------------------------------------------------------------
    #  Begin "TransmissionPath" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "totalTransferCapability", "parallelPathFlag", "availTransferCapability",
                label="Attributes"),
            VGroup("Parent", "OfferedOn", "DeliveryPointFor", "PointOfReceiptFor", "LocatedOn", "For",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.TransmissionPath",
        title="TransmissionPath",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "TransmissionPath" user definitions:
    #--------------------------------------------------------------------------

#------------------------------------------------------------------------------
#  "AncillaryService" class:
#------------------------------------------------------------------------------

class AncillaryService(IdentifiedObject):
    """ All of these services relate  to various aspects of insuring that the production of energy matches consumption of energy at any given time.  They are very critical to the security and reliability of the interconnected network. Some examples of AncillaryServices include Operating/Supplemental Reserve, Energy Imbalance Service, Operating/Spinning Reserve, Reactive Supply and Voltage Control, and Regulation and Frequency Response.
    """

    #--------------------------------------------------------------------------
    #  Trait definitions:
    #--------------------------------------------------------------------------

    # A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.
    TransmissionProviders = List(Instance("CIM.IEC61968.Informative.Financial.TransmissionProvider"),
        desc="A TransmissionProvider offers AncillaryServices. One type of AncillaryServices is a shipping and handling fee to manage the services purchased, another is the reactive power support used to control the voltage on the  transmission system.  This is the amount needed to support the path or amount necessary to maintain the proper voltage at a ServicePoint.")

    # Sale of ancillary services provided by ControlAreaOperators.
    ControlAreaOperator = Instance("CIM.IEC61968.Informative.Financial.ControlAreaOperator",
        desc="Sale of ancillary services provided by ControlAreaOperators.",
        transient=True,
        opposite="AncillaryService",
        editor=InstanceEditor(name="_controlareaoperators"))

    def _get_controlareaoperators(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.ControlAreaOperator" ]
        else:
            return []

    _controlareaoperators = Property(fget=_get_controlareaoperators)

    # A ServiceReservation guarantees a certain AncillaryService.
    ReservedBy_ServiceReservation = Instance("CIM.IEC61968.Informative.Reservation.ServiceReservation",
        desc="A ServiceReservation guarantees a certain AncillaryService.",
        transient=True,
        opposite="Reserves_AncillaryServices",
        editor=InstanceEditor(name="_servicereservations"))

    def _get_servicereservations(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Reservation.ServiceReservation" ]
        else:
            return []

    _servicereservations = Property(fget=_get_servicereservations)

    # AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.
    OpenAccessProduct = Instance("CIM.IEC61968.Informative.Financial.OpenAccessProduct",
        desc="AncillaryServices are sold through a contract which offers a particular OpenAccessProduct.",
        transient=True,
        opposite="AncillaryServices",
        editor=InstanceEditor(name="_openaccessproducts"))

    def _get_openaccessproducts(self):
        """ Property getter.
        """
        if self.Parent is not None:
            return [e for e in self.Parent.Elements \
                if "%s.%s" % (e.__module__, e.__class__.__name__) == \
                    "CIM.IEC61968.Informative.Financial.OpenAccessProduct" ]
        else:
            return []

    _openaccessproducts = Property(fget=_get_openaccessproducts)

    #--------------------------------------------------------------------------
    #  Begin "AncillaryService" user definitions:
    #--------------------------------------------------------------------------

    # @generated
    traits_view = View(Tabbed(
            VGroup("UUID", "description", "mRID", "name", "pathName", "localName", "aliasName",
                label="Attributes"),
            VGroup("Parent", "ModelingAuthoritySet", "TransmissionProviders", "ControlAreaOperator", "ReservedBy_ServiceReservation", "OpenAccessProduct",
                label="References"),
            dock="tab"),
        id="CIM.IEC61968.Informative.Reservation.AncillaryService",
        title="AncillaryService",
        buttons=["OK", "Cancel", "Help"],
        resizable=False)

    #--------------------------------------------------------------------------
    #  End "AncillaryService" user definitions:
    #--------------------------------------------------------------------------



# EOF -------------------------------------------------------------------------
