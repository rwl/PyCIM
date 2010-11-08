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

from CIM14.IEC61970.Generation.GenerationDynamics.SteamSupply import SteamSupply

class PWRSteamSupply(SteamSupply):
    """Pressurized water reactor used as a steam supply to a steam turbine
    """

    def __init__(self, pressureCG=0.0, throttlePressureSP=0.0, coldLegFBLagTC=0.0, hotLegSteamGain=0.0, coreHTLagTC2=0.0, coreHTLagTC1=0.0, coreNeutronicsHT=0.0, coldLegFBLeadTC1=0.0, feedbackFactor=0.0, coreNeutronicsEffTC=0.0, steamFlowFG=0.0, steamPressureDropLagTC=0.0, steamPressureFG=0.0, coldLegFG1=0.0, throttlePressureFactor=0.0, coldLegFBLeadTC2=0.0, hotLegToColdLegGain=0.0, coldLegFG2=0.0, hotLegLagTC=0.0, coldLegLagTC=0.0, *args, **kw_args):
        """Initialises a new 'PWRSteamSupply' instance.

        @param pressureCG: Pressure Control Gain 
        @param throttlePressureSP: Throttle Pressure Setpoint 
        @param coldLegFBLagTC: Cold Leg Feedback Lag Time Constant 
        @param hotLegSteamGain: Hot Leg Steam Gain 
        @param coreHTLagTC2: Core Heat Transfer Lag Time Constant 
        @param coreHTLagTC1: Core Heat Transfer Lag Time Constant 
        @param coreNeutronicsHT: Core Neutronics And Heat Transfer 
        @param coldLegFBLeadTC1: Cold Leg Feedback Lead Time Constant 
        @param feedbackFactor: Feedback Factor 
        @param coreNeutronicsEffTC: Core Neutronics Effective Time Constant 
        @param steamFlowFG: Steam Flow Feedback Gain 
        @param steamPressureDropLagTC: Steam Pressure Drop Lag Time Constant 
        @param steamPressureFG: Steam Pressure Feedback Gain 
        @param coldLegFG1: Cold Leg Feedback Gain 1 
        @param throttlePressureFactor: Throttle Pressure Factor 
        @param coldLegFBLeadTC2: Cold Leg Feedback Lead Time Constant 
        @param hotLegToColdLegGain: Hot Leg To Cold Leg Gain 
        @param coldLegFG2: Cold Leg Feedback Gain 2 
        @param hotLegLagTC: Hot Leg Lag Time Constant 
        @param coldLegLagTC: Cold Leg Lag Time Constant 
        """
        #: Pressure Control Gain
        self.pressureCG = pressureCG

        #: Throttle Pressure Setpoint
        self.throttlePressureSP = throttlePressureSP

        #: Cold Leg Feedback Lag Time Constant
        self.coldLegFBLagTC = coldLegFBLagTC

        #: Hot Leg Steam Gain
        self.hotLegSteamGain = hotLegSteamGain

        #: Core Heat Transfer Lag Time Constant
        self.coreHTLagTC2 = coreHTLagTC2

        #: Core Heat Transfer Lag Time Constant
        self.coreHTLagTC1 = coreHTLagTC1

        #: Core Neutronics And Heat Transfer
        self.coreNeutronicsHT = coreNeutronicsHT

        #: Cold Leg Feedback Lead Time Constant
        self.coldLegFBLeadTC1 = coldLegFBLeadTC1

        #: Feedback Factor
        self.feedbackFactor = feedbackFactor

        #: Core Neutronics Effective Time Constant
        self.coreNeutronicsEffTC = coreNeutronicsEffTC

        #: Steam Flow Feedback Gain
        self.steamFlowFG = steamFlowFG

        #: Steam Pressure Drop Lag Time Constant
        self.steamPressureDropLagTC = steamPressureDropLagTC

        #: Steam Pressure Feedback Gain
        self.steamPressureFG = steamPressureFG

        #: Cold Leg Feedback Gain 1
        self.coldLegFG1 = coldLegFG1

        #: Throttle Pressure Factor
        self.throttlePressureFactor = throttlePressureFactor

        #: Cold Leg Feedback Lead Time Constant
        self.coldLegFBLeadTC2 = coldLegFBLeadTC2

        #: Hot Leg To Cold Leg Gain
        self.hotLegToColdLegGain = hotLegToColdLegGain

        #: Cold Leg Feedback Gain 2
        self.coldLegFG2 = coldLegFG2

        #: Hot Leg Lag Time Constant
        self.hotLegLagTC = hotLegLagTC

        #: Cold Leg Lag Time Constant
        self.coldLegLagTC = coldLegLagTC

        super(PWRSteamSupply, self).__init__(*args, **kw_args)

    _attrs = ["pressureCG", "throttlePressureSP", "coldLegFBLagTC", "hotLegSteamGain", "coreHTLagTC2", "coreHTLagTC1", "coreNeutronicsHT", "coldLegFBLeadTC1", "feedbackFactor", "coreNeutronicsEffTC", "steamFlowFG", "steamPressureDropLagTC", "steamPressureFG", "coldLegFG1", "throttlePressureFactor", "coldLegFBLeadTC2", "hotLegToColdLegGain", "coldLegFG2", "hotLegLagTC", "coldLegLagTC"]
    _attr_types = {"pressureCG": float, "throttlePressureSP": float, "coldLegFBLagTC": float, "hotLegSteamGain": float, "coreHTLagTC2": float, "coreHTLagTC1": float, "coreNeutronicsHT": float, "coldLegFBLeadTC1": float, "feedbackFactor": float, "coreNeutronicsEffTC": float, "steamFlowFG": float, "steamPressureDropLagTC": float, "steamPressureFG": float, "coldLegFG1": float, "throttlePressureFactor": float, "coldLegFBLeadTC2": float, "hotLegToColdLegGain": float, "coldLegFG2": float, "hotLegLagTC": float, "coldLegLagTC": float}
    _defaults = {"pressureCG": 0.0, "throttlePressureSP": 0.0, "coldLegFBLagTC": 0.0, "hotLegSteamGain": 0.0, "coreHTLagTC2": 0.0, "coreHTLagTC1": 0.0, "coreNeutronicsHT": 0.0, "coldLegFBLeadTC1": 0.0, "feedbackFactor": 0.0, "coreNeutronicsEffTC": 0.0, "steamFlowFG": 0.0, "steamPressureDropLagTC": 0.0, "steamPressureFG": 0.0, "coldLegFG1": 0.0, "throttlePressureFactor": 0.0, "coldLegFBLeadTC2": 0.0, "hotLegToColdLegGain": 0.0, "coldLegFG2": 0.0, "hotLegLagTC": 0.0, "coldLegLagTC": 0.0}
    _enums = {}
    _refs = []
    _many_refs = []

