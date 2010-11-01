# Copyright (C) 2010 Richard Lincoln
#
# This library is free software; you can redistribute it and/or
# modify it under the terms of the GNU Lesser General Public
# License as published by the Free Software Foundation; either
# version 2.1 of the License, or (at your option) any later version.
#
# This library is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# Lesser General Public License for more details.
#
# You should have received a copy of the GNU Lesser General Public
# License along with this library; if not, write to the Free Software
# Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston, MA, USA


from cim15v01.iec61968.asset_models import AssetModel
from cim15v01.iec61968.common import Document
from cim15v01.iec61970.core import IdentifiedObject

# <<< imports
# @generated
# >>> imports

ns_prefix = "cimInfAssetModels"

ns_uri = "http://iec.ch/TC57/CIM-generic#InfAssetModels"

class ElectricalAssetModel(AssetModel):
    """ Documentation for a type of ElectricalAsset of a particular product model made by a manufacturer.
    """
    # <<< electrical_asset_model
    # @generated
    def __init__(self, electrical_infos=None, *args, **kw_args):
        """ Initialises a new 'ElectricalAssetModel' instance.

        @param electrical_infos:
        """

        self._electrical_infos = []
        if electrical_infos is not None:
            self.electrical_infos = electrical_infos
        else:
            self.electrical_infos = []


        super(ElectricalAssetModel, self).__init__(*args, **kw_args)
    # >>> electrical_asset_model

    # <<< electrical_infos
    # @generated
    def get_electrical_infos(self):
        """ 
        """
        return self._electrical_infos

    def set_electrical_infos(self, value):
        for p in self._electrical_infos:
            filtered = [q for q in p.electrical_asset_models if q != self]
            self._electrical_infos._electrical_asset_models = filtered
        for r in value:
            if self not in r._electrical_asset_models:
                r._electrical_asset_models.append(self)
        self._electrical_infos = value

    electrical_infos = property(get_electrical_infos, set_electrical_infos)

    def add_electrical_infos(self, *electrical_infos):
        for obj in electrical_infos:
            if self not in obj._electrical_asset_models:
                obj._electrical_asset_models.append(self)
            self._electrical_infos.append(obj)

    def remove_electrical_infos(self, *electrical_infos):
        for obj in electrical_infos:
            if self in obj._electrical_asset_models:
                obj._electrical_asset_models.remove(self)
            self._electrical_infos.remove(obj)
    # >>> electrical_infos



class VehicleAssetModel(AssetModel):
    """ Documentation for a type of a vehicle of a particular product model made by a manufacturer.
    """
    # <<< vehicle_asset_model
    # @generated
    def __init__(self, vehicles=None, vehicle_type_asset=None, *args, **kw_args):
        """ Initialises a new 'VehicleAssetModel' instance.

        @param vehicles:
        @param vehicle_type_asset:
        """

        self._vehicles = []
        if vehicles is not None:
            self.vehicles = vehicles
        else:
            self.vehicles = []

        self._vehicle_type_asset = None
        self.vehicle_type_asset = vehicle_type_asset


        super(VehicleAssetModel, self).__init__(*args, **kw_args)
    # >>> vehicle_asset_model

    # <<< vehicles
    # @generated
    def get_vehicles(self):
        """ 
        """
        return self._vehicles

    def set_vehicles(self, value):
        for x in self._vehicles:
            x._vehicle_asset_model = None
        for y in value:
            y._vehicle_asset_model = self
        self._vehicles = value

    vehicles = property(get_vehicles, set_vehicles)

    def add_vehicles(self, *vehicles):
        for obj in vehicles:
            obj._vehicle_asset_model = self
            self._vehicles.append(obj)

    def remove_vehicles(self, *vehicles):
        for obj in vehicles:
            obj._vehicle_asset_model = None
            self._vehicles.remove(obj)
    # >>> vehicles

    # <<< vehicle_type_asset
    # @generated
    def get_vehicle_type_asset(self):
        """ 
        """
        return self._vehicle_type_asset

    def set_vehicle_type_asset(self, value):
        if self._vehicle_type_asset is not None:
            filtered = [x for x in self.vehicle_type_asset.vehicle_asset_models if x != self]
            self._vehicle_type_asset._vehicle_asset_models = filtered

        self._vehicle_type_asset = value
        if self._vehicle_type_asset is not None:
            self._vehicle_type_asset._vehicle_asset_models.append(self)

    vehicle_type_asset = property(get_vehicle_type_asset, set_vehicle_type_asset)
    # >>> vehicle_type_asset



class WorkEquipmentAssetModel(AssetModel):
    """ Documentation for a type of an equipment used for work of a particular product model made by a manufacturer.
    """
    # <<< work_equipment_asset_model
    # @generated
    def __init__(self, work_equipment_type_asset=None, work_equipment_assets=None, *args, **kw_args):
        """ Initialises a new 'WorkEquipmentAssetModel' instance.

        @param work_equipment_type_asset:
        @param work_equipment_assets:
        """

        self._work_equipment_type_asset = None
        self.work_equipment_type_asset = work_equipment_type_asset

        self._work_equipment_assets = []
        if work_equipment_assets is not None:
            self.work_equipment_assets = work_equipment_assets
        else:
            self.work_equipment_assets = []


        super(WorkEquipmentAssetModel, self).__init__(*args, **kw_args)
    # >>> work_equipment_asset_model

    # <<< work_equipment_type_asset
    # @generated
    def get_work_equipment_type_asset(self):
        """ 
        """
        return self._work_equipment_type_asset

    def set_work_equipment_type_asset(self, value):
        if self._work_equipment_type_asset is not None:
            filtered = [x for x in self.work_equipment_type_asset.work_equipment_asset_models if x != self]
            self._work_equipment_type_asset._work_equipment_asset_models = filtered

        self._work_equipment_type_asset = value
        if self._work_equipment_type_asset is not None:
            self._work_equipment_type_asset._work_equipment_asset_models.append(self)

    work_equipment_type_asset = property(get_work_equipment_type_asset, set_work_equipment_type_asset)
    # >>> work_equipment_type_asset

    # <<< work_equipment_assets
    # @generated
    def get_work_equipment_assets(self):
        """ 
        """
        return self._work_equipment_assets

    def set_work_equipment_assets(self, value):
        for x in self._work_equipment_assets:
            x._work_equipment_asset_model = None
        for y in value:
            y._work_equipment_asset_model = self
        self._work_equipment_assets = value

    work_equipment_assets = property(get_work_equipment_assets, set_work_equipment_assets)

    def add_work_equipment_assets(self, *work_equipment_assets):
        for obj in work_equipment_assets:
            obj._work_equipment_asset_model = self
            self._work_equipment_assets.append(obj)

    def remove_work_equipment_assets(self, *work_equipment_assets):
        for obj in work_equipment_assets:
            obj._work_equipment_asset_model = None
            self._work_equipment_assets.remove(obj)
    # >>> work_equipment_assets



class AssetModelCatalogueItem(Document):
    """ Provides pricing and other relevant information about a specific manufacturer's product (i.e., AssetModel), and its price from a given supplier. A single AssetModel may be availble from multiple suppliers. Note that manufacturer and supplier are both types of organisation, which the association is inherited from Document.
    """
    # <<< asset_model_catalogue_item
    # @generated
    def __init__(self, unit_cost=0.0, erp_quote_line_items=None, erp_poline_items=None, asset_model=None, asset_model_catalogue=None, *args, **kw_args):
        """ Initialises a new 'AssetModelCatalogueItem' instance.

        @param unit_cost: Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        @param erp_quote_line_items:
        @param erp_poline_items:
        @param asset_model:
        @param asset_model_catalogue:
        """
        # Unit cost for an asset model from a specific supplier, either for a unit cost or cost per unit length. Cost is for material or asset only and does not include labor to install/construct or configure it. 
        self.unit_cost = unit_cost


        self._erp_quote_line_items = []
        if erp_quote_line_items is not None:
            self.erp_quote_line_items = erp_quote_line_items
        else:
            self.erp_quote_line_items = []

        self._erp_poline_items = []
        if erp_poline_items is not None:
            self.erp_poline_items = erp_poline_items
        else:
            self.erp_poline_items = []

        self._asset_model = None
        self.asset_model = asset_model

        self._asset_model_catalogue = None
        self.asset_model_catalogue = asset_model_catalogue


        super(AssetModelCatalogueItem, self).__init__(*args, **kw_args)
    # >>> asset_model_catalogue_item

    # <<< erp_quote_line_items
    # @generated
    def get_erp_quote_line_items(self):
        """ 
        """
        return self._erp_quote_line_items

    def set_erp_quote_line_items(self, value):
        for x in self._erp_quote_line_items:
            x._asset_model_catalogue_item = None
        for y in value:
            y._asset_model_catalogue_item = self
        self._erp_quote_line_items = value

    erp_quote_line_items = property(get_erp_quote_line_items, set_erp_quote_line_items)

    def add_erp_quote_line_items(self, *erp_quote_line_items):
        for obj in erp_quote_line_items:
            obj._asset_model_catalogue_item = self
            self._erp_quote_line_items.append(obj)

    def remove_erp_quote_line_items(self, *erp_quote_line_items):
        for obj in erp_quote_line_items:
            obj._asset_model_catalogue_item = None
            self._erp_quote_line_items.remove(obj)
    # >>> erp_quote_line_items

    # <<< erp_poline_items
    # @generated
    def get_erp_poline_items(self):
        """ 
        """
        return self._erp_poline_items

    def set_erp_poline_items(self, value):
        for x in self._erp_poline_items:
            x._asset_model_catalogue_item = None
        for y in value:
            y._asset_model_catalogue_item = self
        self._erp_poline_items = value

    erp_poline_items = property(get_erp_poline_items, set_erp_poline_items)

    def add_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._asset_model_catalogue_item = self
            self._erp_poline_items.append(obj)

    def remove_erp_poline_items(self, *erp_poline_items):
        for obj in erp_poline_items:
            obj._asset_model_catalogue_item = None
            self._erp_poline_items.remove(obj)
    # >>> erp_poline_items

    # <<< asset_model
    # @generated
    def get_asset_model(self):
        """ 
        """
        return self._asset_model

    def set_asset_model(self, value):
        if self._asset_model is not None:
            filtered = [x for x in self.asset_model.asset_model_catalogue_items if x != self]
            self._asset_model._asset_model_catalogue_items = filtered

        self._asset_model = value
        if self._asset_model is not None:
            self._asset_model._asset_model_catalogue_items.append(self)

    asset_model = property(get_asset_model, set_asset_model)
    # >>> asset_model

    # <<< asset_model_catalogue
    # @generated
    def get_asset_model_catalogue(self):
        """ 
        """
        return self._asset_model_catalogue

    def set_asset_model_catalogue(self, value):
        if self._asset_model_catalogue is not None:
            filtered = [x for x in self.asset_model_catalogue.asset_model_catalogue_items if x != self]
            self._asset_model_catalogue._asset_model_catalogue_items = filtered

        self._asset_model_catalogue = value
        if self._asset_model_catalogue is not None:
            self._asset_model_catalogue._asset_model_catalogue_items.append(self)

    asset_model_catalogue = property(get_asset_model_catalogue, set_asset_model_catalogue)
    # >>> asset_model_catalogue



class ToolAssetModel(AssetModel):
    """ Documentation for a type of a tool of a particular product model made by a manufacturer.
    """
    # <<< tool_asset_model
    # @generated
    def __init__(self, tools=None, tool_type_asset=None, *args, **kw_args):
        """ Initialises a new 'ToolAssetModel' instance.

        @param tools:
        @param tool_type_asset:
        """

        self._tools = []
        if tools is not None:
            self.tools = tools
        else:
            self.tools = []

        self._tool_type_asset = None
        self.tool_type_asset = tool_type_asset


        super(ToolAssetModel, self).__init__(*args, **kw_args)
    # >>> tool_asset_model

    # <<< tools
    # @generated
    def get_tools(self):
        """ 
        """
        return self._tools

    def set_tools(self, value):
        for x in self._tools:
            x._tool_asset_model = None
        for y in value:
            y._tool_asset_model = self
        self._tools = value

    tools = property(get_tools, set_tools)

    def add_tools(self, *tools):
        for obj in tools:
            obj._tool_asset_model = self
            self._tools.append(obj)

    def remove_tools(self, *tools):
        for obj in tools:
            obj._tool_asset_model = None
            self._tools.remove(obj)
    # >>> tools

    # <<< tool_type_asset
    # @generated
    def get_tool_type_asset(self):
        """ 
        """
        return self._tool_type_asset

    def set_tool_type_asset(self, value):
        if self._tool_type_asset is not None:
            filtered = [x for x in self.tool_type_asset.tool_asset_models if x != self]
            self._tool_type_asset._tool_asset_models = filtered

        self._tool_type_asset = value
        if self._tool_type_asset is not None:
            self._tool_type_asset._tool_asset_models.append(self)

    tool_type_asset = property(get_tool_type_asset, set_tool_type_asset)
    # >>> tool_type_asset



class TapChangerAssetModel(AssetModel):
    """ Documentation for a type of a tap changer of a particular product model made by a manufacturer.
    """
    # <<< tap_changer_asset_model
    # @generated
    def __init__(self, switching_kind='vacuum', neutral_step=0, low_step=0, frequency=0.0, step_voltage_increment=0.0, rated_current=0.0, initial_delay=0.0, tap_count=0, rated_voltage=0.0, step_phase_increment=0.0, subsequent_delay=0.0, high_step=0, rated_apparent_power=0.0, phase_count=0, bil=0.0, tap_changer_assets=None, *args, **kw_args):
        """ Initialises a new 'TapChangerAssetModel' instance.

        @param switching_kind: Switching kind of tap changer. Values are: "vacuum", "reactive", "other", "resistive"
        @param neutral_step: The neutral tap step position for this type of winding. 
        @param low_step: Lowest possible tap step position, retard from neutral 
        @param frequency: Frequency at which stated device ratings apply, typically 50Hz or 60Hz. 
        @param step_voltage_increment: Tap step increment, in per cent of nominal voltage, per step position. 
        @param rated_current: Rated current. 
        @param initial_delay: Maximum allowed delay for initial tap changer operation (first step change) 
        @param tap_count: Number of taps. 
        @param rated_voltage: Rated voltage. 
        @param step_phase_increment: Phase shift, in degrees, per step position 
        @param subsequent_delay: Maximum allowed delay for isubsequent tap changer operations 
        @param high_step: Highest possible tap step position, advance from neutral 
        @param rated_apparent_power: Rated apparent power. 
        @param phase_count: Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute. 
        @param bil: Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        @param tap_changer_assets:
        """
        # Switching kind of tap changer. Values are: "vacuum", "reactive", "other", "resistive"
        self.switching_kind = switching_kind

        # The neutral tap step position for this type of winding. 
        self.neutral_step = neutral_step

        # Lowest possible tap step position, retard from neutral 
        self.low_step = low_step

        # Frequency at which stated device ratings apply, typically 50Hz or 60Hz. 
        self.frequency = frequency

        # Tap step increment, in per cent of nominal voltage, per step position. 
        self.step_voltage_increment = step_voltage_increment

        # Rated current. 
        self.rated_current = rated_current

        # Maximum allowed delay for initial tap changer operation (first step change) 
        self.initial_delay = initial_delay

        # Number of taps. 
        self.tap_count = tap_count

        # Rated voltage. 
        self.rated_voltage = rated_voltage

        # Phase shift, in degrees, per step position 
        self.step_phase_increment = step_phase_increment

        # Maximum allowed delay for isubsequent tap changer operations 
        self.subsequent_delay = subsequent_delay

        # Highest possible tap step position, advance from neutral 
        self.high_step = high_step

        # Rated apparent power. 
        self.rated_apparent_power = rated_apparent_power

        # Number of potential phases the asset supports, typically 0, 1 or 3. The actual phases connected are determined from 'ConductingEquipment.phases' attribute in the ConductingEquipment subclass associated with the asset or from 'ElectricalAsset.phaseCode' attribute. 
        self.phase_count = phase_count

        # Basic Insulation Level (BIL) for switchgear, insulators, etc. A reference insulation level expressed as the impulse crest voltage of a nominal wave, typically 1.2 X 50 microsecond. This is a measure of the ability of the insulation to withstand very high voltage surges. 
        self.bil = bil


        self._tap_changer_assets = []
        if tap_changer_assets is not None:
            self.tap_changer_assets = tap_changer_assets
        else:
            self.tap_changer_assets = []


        super(TapChangerAssetModel, self).__init__(*args, **kw_args)
    # >>> tap_changer_asset_model

    # <<< tap_changer_assets
    # @generated
    def get_tap_changer_assets(self):
        """ 
        """
        return self._tap_changer_assets

    def set_tap_changer_assets(self, value):
        for x in self._tap_changer_assets:
            x._tap_changer_asset_model = None
        for y in value:
            y._tap_changer_asset_model = self
        self._tap_changer_assets = value

    tap_changer_assets = property(get_tap_changer_assets, set_tap_changer_assets)

    def add_tap_changer_assets(self, *tap_changer_assets):
        for obj in tap_changer_assets:
            obj._tap_changer_asset_model = self
            self._tap_changer_assets.append(obj)

    def remove_tap_changer_assets(self, *tap_changer_assets):
        for obj in tap_changer_assets:
            obj._tap_changer_asset_model = None
            self._tap_changer_assets.remove(obj)
    # >>> tap_changer_assets



class CabinetModel(AssetModel):
    """ Documentation for a type of Cabinet of a particular product model made by a manufacturer.
    """
    # <<< cabinet_model
    # @generated
    def __init__(self, cabinets=None, cabinet_type_asset=None, *args, **kw_args):
        """ Initialises a new 'CabinetModel' instance.

        @param cabinets:
        @param cabinet_type_asset:
        """

        self._cabinets = []
        if cabinets is not None:
            self.cabinets = cabinets
        else:
            self.cabinets = []

        self._cabinet_type_asset = None
        self.cabinet_type_asset = cabinet_type_asset


        super(CabinetModel, self).__init__(*args, **kw_args)
    # >>> cabinet_model

    # <<< cabinets
    # @generated
    def get_cabinets(self):
        """ 
        """
        return self._cabinets

    def set_cabinets(self, value):
        for x in self._cabinets:
            x._cabinet_model = None
        for y in value:
            y._cabinet_model = self
        self._cabinets = value

    cabinets = property(get_cabinets, set_cabinets)

    def add_cabinets(self, *cabinets):
        for obj in cabinets:
            obj._cabinet_model = self
            self._cabinets.append(obj)

    def remove_cabinets(self, *cabinets):
        for obj in cabinets:
            obj._cabinet_model = None
            self._cabinets.remove(obj)
    # >>> cabinets

    # <<< cabinet_type_asset
    # @generated
    def get_cabinet_type_asset(self):
        """ 
        """
        return self._cabinet_type_asset

    def set_cabinet_type_asset(self, value):
        if self._cabinet_type_asset is not None:
            filtered = [x for x in self.cabinet_type_asset.cabinet_models if x != self]
            self._cabinet_type_asset._cabinet_models = filtered

        self._cabinet_type_asset = value
        if self._cabinet_type_asset is not None:
            self._cabinet_type_asset._cabinet_models.append(self)

    cabinet_type_asset = property(get_cabinet_type_asset, set_cabinet_type_asset)
    # >>> cabinet_type_asset



class CompositeSwitchAssetModel(AssetModel):
    """ Documentation for a type of a composite switch asset of a particular product model made by a manufacturer.
    """
    # <<< composite_switch_asset_model
    # @generated
    def __init__(self, composite_switch_info=None, composite_switch_assets=None, composite_switch_type_asset=None, *args, **kw_args):
        """ Initialises a new 'CompositeSwitchAssetModel' instance.

        @param composite_switch_info:
        @param composite_switch_assets:
        @param composite_switch_type_asset:
        """

        self._composite_switch_info = None
        self.composite_switch_info = composite_switch_info

        self._composite_switch_assets = []
        if composite_switch_assets is not None:
            self.composite_switch_assets = composite_switch_assets
        else:
            self.composite_switch_assets = []

        self._composite_switch_type_asset = None
        self.composite_switch_type_asset = composite_switch_type_asset


        super(CompositeSwitchAssetModel, self).__init__(*args, **kw_args)
    # >>> composite_switch_asset_model

    # <<< composite_switch_info
    # @generated
    def get_composite_switch_info(self):
        """ 
        """
        return self._composite_switch_info

    def set_composite_switch_info(self, value):
        if self._composite_switch_info is not None:
            self._composite_switch_info._composite_switch_asset_model = None

        self._composite_switch_info = value
        if self._composite_switch_info is not None:
            self._composite_switch_info._composite_switch_asset_model = self

    composite_switch_info = property(get_composite_switch_info, set_composite_switch_info)
    # >>> composite_switch_info

    # <<< composite_switch_assets
    # @generated
    def get_composite_switch_assets(self):
        """ 
        """
        return self._composite_switch_assets

    def set_composite_switch_assets(self, value):
        for x in self._composite_switch_assets:
            x._composite_switch_asset_model = None
        for y in value:
            y._composite_switch_asset_model = self
        self._composite_switch_assets = value

    composite_switch_assets = property(get_composite_switch_assets, set_composite_switch_assets)

    def add_composite_switch_assets(self, *composite_switch_assets):
        for obj in composite_switch_assets:
            obj._composite_switch_asset_model = self
            self._composite_switch_assets.append(obj)

    def remove_composite_switch_assets(self, *composite_switch_assets):
        for obj in composite_switch_assets:
            obj._composite_switch_asset_model = None
            self._composite_switch_assets.remove(obj)
    # >>> composite_switch_assets

    # <<< composite_switch_type_asset
    # @generated
    def get_composite_switch_type_asset(self):
        """ 
        """
        return self._composite_switch_type_asset

    def set_composite_switch_type_asset(self, value):
        if self._composite_switch_type_asset is not None:
            filtered = [x for x in self.composite_switch_type_asset.composite_switch_asset_models if x != self]
            self._composite_switch_type_asset._composite_switch_asset_models = filtered

        self._composite_switch_type_asset = value
        if self._composite_switch_type_asset is not None:
            self._composite_switch_type_asset._composite_switch_asset_models.append(self)

    composite_switch_type_asset = property(get_composite_switch_type_asset, set_composite_switch_type_asset)
    # >>> composite_switch_type_asset



class AssetModelCatalogue(IdentifiedObject):
    """ Catalogue of available types of products and materials that are used to build or install, maintain or operate an Asset. Each catalogue item is for a specific product (AssetModel) available from a specific supplier.
    """
    # <<< asset_model_catalogue
    # @generated
    def __init__(self, status=None, asset_model_catalogue_items=None, *args, **kw_args):
        """ Initialises a new 'AssetModelCatalogue' instance.

        @param status:
        @param asset_model_catalogue_items:
        """

        self.status = status

        self._asset_model_catalogue_items = []
        if asset_model_catalogue_items is not None:
            self.asset_model_catalogue_items = asset_model_catalogue_items
        else:
            self.asset_model_catalogue_items = []


        super(AssetModelCatalogue, self).__init__(*args, **kw_args)
    # >>> asset_model_catalogue

    # <<< status
    # @generated
    status = None
    # >>> status

    # <<< asset_model_catalogue_items
    # @generated
    def get_asset_model_catalogue_items(self):
        """ 
        """
        return self._asset_model_catalogue_items

    def set_asset_model_catalogue_items(self, value):
        for x in self._asset_model_catalogue_items:
            x._asset_model_catalogue = None
        for y in value:
            y._asset_model_catalogue = self
        self._asset_model_catalogue_items = value

    asset_model_catalogue_items = property(get_asset_model_catalogue_items, set_asset_model_catalogue_items)

    def add_asset_model_catalogue_items(self, *asset_model_catalogue_items):
        for obj in asset_model_catalogue_items:
            obj._asset_model_catalogue = self
            self._asset_model_catalogue_items.append(obj)

    def remove_asset_model_catalogue_items(self, *asset_model_catalogue_items):
        for obj in asset_model_catalogue_items:
            obj._asset_model_catalogue = None
            self._asset_model_catalogue_items.remove(obj)
    # >>> asset_model_catalogue_items



class TransformerAssetModel(AssetModel):
    """ Documentation for a type of a transformer of a particular product model made by a manufacturer.
    """
    # <<< transformer_asset_model
    # @generated
    def __init__(self, function='other', construction_kind='padmount_dead_front', winding_insulation_kind='other', oil_preservation_kind='nitrogen_blanket', core_kind='core', auto_transformer=False, reconfig_winding=False, day_over_load_rating=0.0, alt_secondary_nom_voltage=0.0, alt_primary_nom_voltage=0.0, core_coils_weight=0.0, solid_insulation_weight=0.0, hour_over_load_rating=0.0, neutral_bil=0.0, transformer_assets=None, transformer_info=None, *args, **kw_args):
        """ Initialises a new 'TransformerAssetModel' instance.

        @param function: Function of this transformer. Values are: "other", "voltage_regulator", "secondary_transformer", "autotransformer", "power_transformer"
        @param construction_kind: Kind of construction for this transformer. Values are: "padmount_dead_front", "one_phase", "unknown", "valut", "padmounted", "aerial", "underground", "padmount_live_front", "network", "vault_three_phase", "subway", "dry_type", "padmount_loop_through", "overhead", "three_phase", "padmount_feed_through"
        @param winding_insulation_kind: Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, other Values are: "other", "nomex", "paper", "thermally_upgraded_paper"
        @param oil_preservation_kind: Kind of oil preservation system. Values are: "nitrogen_blanket", "free_breathing", "conservator", "other"
        @param core_kind: Core kind of this transformer product. Values are: "core", "shell"
        @param auto_transformer: True if this is an autotransformer, false otherwise. 
        @param reconfig_winding: True if windings can be re-configured to result in a different input or output voltage. 
        @param day_over_load_rating: 24-hour overload rating. 
        @param alt_secondary_nom_voltage: Nominal voltage rating for alternate configuration for secondary winding. 
        @param alt_primary_nom_voltage: Nominal voltage rating for alternate configuration for primary winding. 
        @param core_coils_weight: Weight of core and coils in transformer. 
        @param solid_insulation_weight: Weight of solid insultation in transformer. 
        @param hour_over_load_rating: 1-hour overload rating. 
        @param neutral_bil: Basic Insulation Level of Neutral 
        @param transformer_assets:
        @param transformer_info:
        """
        # Function of this transformer. Values are: "other", "voltage_regulator", "secondary_transformer", "autotransformer", "power_transformer"
        self.function = function

        # Kind of construction for this transformer. Values are: "padmount_dead_front", "one_phase", "unknown", "valut", "padmounted", "aerial", "underground", "padmount_live_front", "network", "vault_three_phase", "subway", "dry_type", "padmount_loop_through", "overhead", "three_phase", "padmount_feed_through"
        self.construction_kind = construction_kind

        # Type of insultation used for transformer windings: Paper, Thermally Upgraded Paper, Nomex, other Values are: "other", "nomex", "paper", "thermally_upgraded_paper"
        self.winding_insulation_kind = winding_insulation_kind

        # Kind of oil preservation system. Values are: "nitrogen_blanket", "free_breathing", "conservator", "other"
        self.oil_preservation_kind = oil_preservation_kind

        # Core kind of this transformer product. Values are: "core", "shell"
        self.core_kind = core_kind

        # True if this is an autotransformer, false otherwise. 
        self.auto_transformer = auto_transformer

        # True if windings can be re-configured to result in a different input or output voltage. 
        self.reconfig_winding = reconfig_winding

        # 24-hour overload rating. 
        self.day_over_load_rating = day_over_load_rating

        # Nominal voltage rating for alternate configuration for secondary winding. 
        self.alt_secondary_nom_voltage = alt_secondary_nom_voltage

        # Nominal voltage rating for alternate configuration for primary winding. 
        self.alt_primary_nom_voltage = alt_primary_nom_voltage

        # Weight of core and coils in transformer. 
        self.core_coils_weight = core_coils_weight

        # Weight of solid insultation in transformer. 
        self.solid_insulation_weight = solid_insulation_weight

        # 1-hour overload rating. 
        self.hour_over_load_rating = hour_over_load_rating

        # Basic Insulation Level of Neutral 
        self.neutral_bil = neutral_bil


        self._transformer_assets = []
        if transformer_assets is not None:
            self.transformer_assets = transformer_assets
        else:
            self.transformer_assets = []

        self._transformer_info = None
        self.transformer_info = transformer_info


        super(TransformerAssetModel, self).__init__(*args, **kw_args)
    # >>> transformer_asset_model

    # <<< transformer_assets
    # @generated
    def get_transformer_assets(self):
        """ 
        """
        return self._transformer_assets

    def set_transformer_assets(self, value):
        for x in self._transformer_assets:
            x._transformer_asset_model = None
        for y in value:
            y._transformer_asset_model = self
        self._transformer_assets = value

    transformer_assets = property(get_transformer_assets, set_transformer_assets)

    def add_transformer_assets(self, *transformer_assets):
        for obj in transformer_assets:
            obj._transformer_asset_model = self
            self._transformer_assets.append(obj)

    def remove_transformer_assets(self, *transformer_assets):
        for obj in transformer_assets:
            obj._transformer_asset_model = None
            self._transformer_assets.remove(obj)
    # >>> transformer_assets

    # <<< transformer_info
    # @generated
    def get_transformer_info(self):
        """ 
        """
        return self._transformer_info

    def set_transformer_info(self, value):
        if self._transformer_info is not None:
            filtered = [x for x in self.transformer_info.transformer_asset_models if x != self]
            self._transformer_info._transformer_asset_models = filtered

        self._transformer_info = value
        if self._transformer_info is not None:
            self._transformer_info._transformer_asset_models.append(self)

    transformer_info = property(get_transformer_info, set_transformer_info)
    # >>> transformer_info



class TowerAssetModel(AssetModel):
    """ A type of tower supplied by a given manufacturer or constructed from a common design.
    """
    # <<< tower_asset_model
    # @generated
    def __init__(self, tower_type_asset=None, towers=None, *args, **kw_args):
        """ Initialises a new 'TowerAssetModel' instance.

        @param tower_type_asset:
        @param towers:
        """

        self._tower_type_asset = None
        self.tower_type_asset = tower_type_asset

        self._towers = []
        if towers is not None:
            self.towers = towers
        else:
            self.towers = []


        super(TowerAssetModel, self).__init__(*args, **kw_args)
    # >>> tower_asset_model

    # <<< tower_type_asset
    # @generated
    def get_tower_type_asset(self):
        """ 
        """
        return self._tower_type_asset

    def set_tower_type_asset(self, value):
        if self._tower_type_asset is not None:
            filtered = [x for x in self.tower_type_asset.tower_asset_models if x != self]
            self._tower_type_asset._tower_asset_models = filtered

        self._tower_type_asset = value
        if self._tower_type_asset is not None:
            self._tower_type_asset._tower_asset_models.append(self)

    tower_type_asset = property(get_tower_type_asset, set_tower_type_asset)
    # >>> tower_type_asset

    # <<< towers
    # @generated
    def get_towers(self):
        """ 
        """
        return self._towers

    def set_towers(self, value):
        for x in self._towers:
            x._tower_asset_model = None
        for y in value:
            y._tower_asset_model = self
        self._towers = value

    towers = property(get_towers, set_towers)

    def add_towers(self, *towers):
        for obj in towers:
            obj._tower_asset_model = self
            self._towers.append(obj)

    def remove_towers(self, *towers):
        for obj in towers:
            obj._tower_asset_model = None
            self._towers.remove(obj)
    # >>> towers



class PoleModel(AssetModel):
    """ A type of pole supplied by a given manufacturer.
    """
    # <<< pole_model
    # @generated
    def __init__(self, species_type='', classification='', pole_type_asset=None, poles=None, *args, **kw_args):
        """ Initialises a new 'PoleModel' instance.

        @param species_type: Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown. 
        @param classification: Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown. 
        @param pole_type_asset:
        @param poles:
        """
        # Pole species. Aluminum, Aluminum Davit, Concrete, Fiberglass, Galvanized Davit, Galvanized, Steel Davit Primed, Steel Davit, Steel Standard Primed, Steel, Truncated, Wood-Treated, Wood-Hard, Wood-Salt Treated, Wood-Soft, Wood, Other, Unknown. 
        self.species_type = species_type

        # Pole class: 1, 2, 3, 4, 5, 6, 7, H1, H2, Other, Unknown. 
        self.classification = classification


        self._pole_type_asset = None
        self.pole_type_asset = pole_type_asset

        self._poles = []
        if poles is not None:
            self.poles = poles
        else:
            self.poles = []


        super(PoleModel, self).__init__(*args, **kw_args)
    # >>> pole_model

    # <<< pole_type_asset
    # @generated
    def get_pole_type_asset(self):
        """ 
        """
        return self._pole_type_asset

    def set_pole_type_asset(self, value):
        if self._pole_type_asset is not None:
            filtered = [x for x in self.pole_type_asset.pole_models if x != self]
            self._pole_type_asset._pole_models = filtered

        self._pole_type_asset = value
        if self._pole_type_asset is not None:
            self._pole_type_asset._pole_models.append(self)

    pole_type_asset = property(get_pole_type_asset, set_pole_type_asset)
    # >>> pole_type_asset

    # <<< poles
    # @generated
    def get_poles(self):
        """ 
        """
        return self._poles

    def set_poles(self, value):
        for x in self._poles:
            x._pole_model = None
        for y in value:
            y._pole_model = self
        self._poles = value

    poles = property(get_poles, set_poles)

    def add_poles(self, *poles):
        for obj in poles:
            obj._pole_model = self
            self._poles.append(obj)

    def remove_poles(self, *poles):
        for obj in poles:
            obj._pole_model = None
            self._poles.remove(obj)
    # >>> poles



class AssetFunctionAssetModel(AssetModel):
    """ Documentation for a type of an asset function of a particular product model made by a manufacturer.(Organisation). Asset Functions are typically component parts of Assets or Asset Containers.
    """
    # <<< asset_function_asset_model
    # @generated
    def __init__(self, asset_function_type_asset=None, asset_functions=None, *args, **kw_args):
        """ Initialises a new 'AssetFunctionAssetModel' instance.

        @param asset_function_type_asset:
        @param asset_functions:
        """

        self._asset_function_type_asset = None
        self.asset_function_type_asset = asset_function_type_asset

        self._asset_functions = []
        if asset_functions is not None:
            self.asset_functions = asset_functions
        else:
            self.asset_functions = []


        super(AssetFunctionAssetModel, self).__init__(*args, **kw_args)
    # >>> asset_function_asset_model

    # <<< asset_function_type_asset
    # @generated
    def get_asset_function_type_asset(self):
        """ 
        """
        return self._asset_function_type_asset

    def set_asset_function_type_asset(self, value):
        if self._asset_function_type_asset is not None:
            filtered = [x for x in self.asset_function_type_asset.asset_function_asset_models if x != self]
            self._asset_function_type_asset._asset_function_asset_models = filtered

        self._asset_function_type_asset = value
        if self._asset_function_type_asset is not None:
            self._asset_function_type_asset._asset_function_asset_models.append(self)

    asset_function_type_asset = property(get_asset_function_type_asset, set_asset_function_type_asset)
    # >>> asset_function_type_asset

    # <<< asset_functions
    # @generated
    def get_asset_functions(self):
        """ 
        """
        return self._asset_functions

    def set_asset_functions(self, value):
        for x in self._asset_functions:
            x._asset_function_asset_model = None
        for y in value:
            y._asset_function_asset_model = self
        self._asset_functions = value

    asset_functions = property(get_asset_functions, set_asset_functions)

    def add_asset_functions(self, *asset_functions):
        for obj in asset_functions:
            obj._asset_function_asset_model = self
            self._asset_functions.append(obj)

    def remove_asset_functions(self, *asset_functions):
        for obj in asset_functions:
            obj._asset_function_asset_model = None
            self._asset_functions.remove(obj)
    # >>> asset_functions



class ConductorAssetModel(AssetModel):
    """ A type of conductor made by a particular manufacturer (Organisation). Its ElectricalProperties are defined as being per unit length (which is defined by the unitLength attribute)
    """
    # <<< conductor_asset_model
    # @generated
    def __init__(self, conductor_assets=None, conductor_info=None, *args, **kw_args):
        """ Initialises a new 'ConductorAssetModel' instance.

        @param conductor_assets:
        @param conductor_info:
        """

        self._conductor_assets = []
        if conductor_assets is not None:
            self.conductor_assets = conductor_assets
        else:
            self.conductor_assets = []

        self._conductor_info = None
        self.conductor_info = conductor_info


        super(ConductorAssetModel, self).__init__(*args, **kw_args)
    # >>> conductor_asset_model

    # <<< conductor_assets
    # @generated
    def get_conductor_assets(self):
        """ 
        """
        return self._conductor_assets

    def set_conductor_assets(self, value):
        for x in self._conductor_assets:
            x._conductor_asset_model = None
        for y in value:
            y._conductor_asset_model = self
        self._conductor_assets = value

    conductor_assets = property(get_conductor_assets, set_conductor_assets)

    def add_conductor_assets(self, *conductor_assets):
        for obj in conductor_assets:
            obj._conductor_asset_model = self
            self._conductor_assets.append(obj)

    def remove_conductor_assets(self, *conductor_assets):
        for obj in conductor_assets:
            obj._conductor_asset_model = None
            self._conductor_assets.remove(obj)
    # >>> conductor_assets

    # <<< conductor_info
    # @generated
    def get_conductor_info(self):
        """ 
        """
        return self._conductor_info

    def set_conductor_info(self, value):
        if self._conductor_info is not None:
            self._conductor_info._conductor_asset_model = None

        self._conductor_info = value
        if self._conductor_info is not None:
            self._conductor_info._conductor_asset_model = self

    conductor_info = property(get_conductor_info, set_conductor_info)
    # >>> conductor_info



class ComFunctionAssetModel(ElectricalAssetModel):
    """ Documentation for a type of communication function of a particular product model made by a manufacturer.
    """
    # <<< com_function_asset_model
    # @generated
    def __init__(self, com_function_type_asset=None, *args, **kw_args):
        """ Initialises a new 'ComFunctionAssetModel' instance.

        @param com_function_type_asset:
        """

        self._com_function_type_asset = None
        self.com_function_type_asset = com_function_type_asset


        super(ComFunctionAssetModel, self).__init__(*args, **kw_args)
    # >>> com_function_asset_model

    # <<< com_function_type_asset
    # @generated
    def get_com_function_type_asset(self):
        """ 
        """
        return self._com_function_type_asset

    def set_com_function_type_asset(self, value):
        if self._com_function_type_asset is not None:
            filtered = [x for x in self.com_function_type_asset.com_function_asset_models if x != self]
            self._com_function_type_asset._com_function_asset_models = filtered

        self._com_function_type_asset = value
        if self._com_function_type_asset is not None:
            self._com_function_type_asset._com_function_asset_models.append(self)

    com_function_type_asset = property(get_com_function_type_asset, set_com_function_type_asset)
    # >>> com_function_type_asset



class SwitchAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a switch asset of a particular product model made by a manufacturer.
    """
    # <<< switch_asset_model
    # @generated
    def __init__(self, switch_type_asset=None, switch_assets=None, switch_info=None, *args, **kw_args):
        """ Initialises a new 'SwitchAssetModel' instance.

        @param switch_type_asset:
        @param switch_assets:
        @param switch_info:
        """

        self._switch_type_asset = None
        self.switch_type_asset = switch_type_asset

        self._switch_assets = []
        if switch_assets is not None:
            self.switch_assets = switch_assets
        else:
            self.switch_assets = []

        self._switch_info = None
        self.switch_info = switch_info


        super(SwitchAssetModel, self).__init__(*args, **kw_args)
    # >>> switch_asset_model

    # <<< switch_type_asset
    # @generated
    def get_switch_type_asset(self):
        """ 
        """
        return self._switch_type_asset

    def set_switch_type_asset(self, value):
        if self._switch_type_asset is not None:
            filtered = [x for x in self.switch_type_asset.switch_asset_models if x != self]
            self._switch_type_asset._switch_asset_models = filtered

        self._switch_type_asset = value
        if self._switch_type_asset is not None:
            self._switch_type_asset._switch_asset_models.append(self)

    switch_type_asset = property(get_switch_type_asset, set_switch_type_asset)
    # >>> switch_type_asset

    # <<< switch_assets
    # @generated
    def get_switch_assets(self):
        """ 
        """
        return self._switch_assets

    def set_switch_assets(self, value):
        for x in self._switch_assets:
            x._switch_asset_model = None
        for y in value:
            y._switch_asset_model = self
        self._switch_assets = value

    switch_assets = property(get_switch_assets, set_switch_assets)

    def add_switch_assets(self, *switch_assets):
        for obj in switch_assets:
            obj._switch_asset_model = self
            self._switch_assets.append(obj)

    def remove_switch_assets(self, *switch_assets):
        for obj in switch_assets:
            obj._switch_asset_model = None
            self._switch_assets.remove(obj)
    # >>> switch_assets

    # <<< switch_info
    # @generated
    def get_switch_info(self):
        """ 
        """
        return self._switch_info

    def set_switch_info(self, value):
        if self._switch_info is not None:
            self._switch_info._switch_asset_model = None

        self._switch_info = value
        if self._switch_info is not None:
            self._switch_info._switch_asset_model = self

    switch_info = property(get_switch_info, set_switch_info)
    # >>> switch_info



class MeterAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a meter asset of a particular product model made by a manufacturer.
    """
    # <<< meter_asset_model
    # @generated
    def __init__(self, k_vah_meter=False, interval_data_meter=False, max_register_count=0, wire_count=0, k_h=0.0, time_of_use_meter=False, form='', register_ratio=0.0, demand_meter=False, reactive_meter=False, load_profile_meter=False, kwh_meter=False, q_meter=False, meter_type_asset=None, meter_assets=None, *args, **kw_args):
        """ Initialises a new 'MeterAssetModel' instance.

        @param k_vah_meter: True when the meter is capable of metering apparent energy in kVAh. 
        @param interval_data_meter: True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity). 
        @param max_register_count: Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset. 
        @param wire_count: Number of wires. 
        @param k_h: Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        @param time_of_use_meter: True when the meter or meter+AMR module are capable of offering TOU data. 
        @param form: Meter form number. 
        @param register_ratio: Meter register ratio. 
        @param demand_meter: True when the meter or installed AMR option is capable of capturing demand data. 
        @param reactive_meter: True when the meter is capable of metering reactive energy in kVArh. 
        @param load_profile_meter: True when the meter or the installed AMR option is capable of capturing kWh interval data. 
        @param kwh_meter: True when the meter is capable of metering real energy in kWh. 
        @param q_meter: True when the meter is capable of metering reactive energy in kQh. 
        @param meter_type_asset:
        @param meter_assets:
        """
        # True when the meter is capable of metering apparent energy in kVAh. 
        self.k_vah_meter = k_vah_meter

        # True when the meter or the installed AMR option is capable of capturing interval data for a user selectable measurement (kWh, Volts, or some other billing or engineering quantity). 
        self.interval_data_meter = interval_data_meter

        # Maximum number of registers this meter model can support. The actual number in use is based on the number of Registers associated with a given MeterAsset. 
        self.max_register_count = max_register_count

        # Number of wires. 
        self.wire_count = wire_count

        # Meter kh (watthour) constant. This constant is the number of watthours that must be applied to the meter to cause one disk revolution for an electromechanical meter or the number of watthours represented by one increment pulse for an electronic meter. 
        self.k_h = k_h

        # True when the meter or meter+AMR module are capable of offering TOU data. 
        self.time_of_use_meter = time_of_use_meter

        # Meter form number. 
        self.form = form

        # Meter register ratio. 
        self.register_ratio = register_ratio

        # True when the meter or installed AMR option is capable of capturing demand data. 
        self.demand_meter = demand_meter

        # True when the meter is capable of metering reactive energy in kVArh. 
        self.reactive_meter = reactive_meter

        # True when the meter or the installed AMR option is capable of capturing kWh interval data. 
        self.load_profile_meter = load_profile_meter

        # True when the meter is capable of metering real energy in kWh. 
        self.kwh_meter = kwh_meter

        # True when the meter is capable of metering reactive energy in kQh. 
        self.q_meter = q_meter


        self._meter_type_asset = None
        self.meter_type_asset = meter_type_asset

        self._meter_assets = []
        if meter_assets is not None:
            self.meter_assets = meter_assets
        else:
            self.meter_assets = []


        super(MeterAssetModel, self).__init__(*args, **kw_args)
    # >>> meter_asset_model

    # <<< meter_type_asset
    # @generated
    def get_meter_type_asset(self):
        """ 
        """
        return self._meter_type_asset

    def set_meter_type_asset(self, value):
        if self._meter_type_asset is not None:
            filtered = [x for x in self.meter_type_asset.meter_asset_models if x != self]
            self._meter_type_asset._meter_asset_models = filtered

        self._meter_type_asset = value
        if self._meter_type_asset is not None:
            self._meter_type_asset._meter_asset_models.append(self)

    meter_type_asset = property(get_meter_type_asset, set_meter_type_asset)
    # >>> meter_type_asset

    # <<< meter_assets
    # @generated
    def get_meter_assets(self):
        """ 
        """
        return self._meter_assets

    def set_meter_assets(self, value):
        for x in self._meter_assets:
            x._meter_asset_model = None
        for y in value:
            y._meter_asset_model = self
        self._meter_assets = value

    meter_assets = property(get_meter_assets, set_meter_assets)

    def add_meter_assets(self, *meter_assets):
        for obj in meter_assets:
            obj._meter_asset_model = self
            self._meter_assets.append(obj)

    def remove_meter_assets(self, *meter_assets):
        for obj in meter_assets:
            obj._meter_asset_model = None
            self._meter_assets.remove(obj)
    # >>> meter_assets



class FACTSDeviceAssetModel(ElectricalAssetModel):
    """ A particular model of FACTS device provided from a manufacturer. A FACTS devices are used for the dynamic control of voltage, impedance and phase angle of high voltage AC transmission lines. FACTS device types include: - SVC = Static Var Compensator - STATCOM = Static Synchronous Compensator - TCPAR = Thyristor Controlled Phase-Angle Regulator - TCSC = Thyristor Controlled Series Capacitor - TCVL = Thyristor Controlled Voltage Limiter - TSBR = Thyristor Switched Braking Resistor - TSSC = Thyristor Switched Series Capacitor - UPFC = Unified Power Flow Controller
    """
    # <<< factsdevice_asset_model
    # @generated
    def __init__(self, factsdevice_assets=None, factsdevice_type_asset=None, *args, **kw_args):
        """ Initialises a new 'FACTSDeviceAssetModel' instance.

        @param factsdevice_assets:
        @param factsdevice_type_asset:
        """

        self._factsdevice_assets = []
        if factsdevice_assets is not None:
            self.factsdevice_assets = factsdevice_assets
        else:
            self.factsdevice_assets = []

        self._factsdevice_type_asset = None
        self.factsdevice_type_asset = factsdevice_type_asset


        super(FACTSDeviceAssetModel, self).__init__(*args, **kw_args)
    # >>> factsdevice_asset_model

    # <<< factsdevice_assets
    # @generated
    def get_factsdevice_assets(self):
        """ 
        """
        return self._factsdevice_assets

    def set_factsdevice_assets(self, value):
        for x in self._factsdevice_assets:
            x._factsdevice_asset_model = None
        for y in value:
            y._factsdevice_asset_model = self
        self._factsdevice_assets = value

    factsdevice_assets = property(get_factsdevice_assets, set_factsdevice_assets)

    def add_factsdevice_assets(self, *factsdevice_assets):
        for obj in factsdevice_assets:
            obj._factsdevice_asset_model = self
            self._factsdevice_assets.append(obj)

    def remove_factsdevice_assets(self, *factsdevice_assets):
        for obj in factsdevice_assets:
            obj._factsdevice_asset_model = None
            self._factsdevice_assets.remove(obj)
    # >>> factsdevice_assets

    # <<< factsdevice_type_asset
    # @generated
    def get_factsdevice_type_asset(self):
        """ 
        """
        return self._factsdevice_type_asset

    def set_factsdevice_type_asset(self, value):
        if self._factsdevice_type_asset is not None:
            filtered = [x for x in self.factsdevice_type_asset.factsdevice_asset_models if x != self]
            self._factsdevice_type_asset._factsdevice_asset_models = filtered

        self._factsdevice_type_asset = value
        if self._factsdevice_type_asset is not None:
            self._factsdevice_type_asset._factsdevice_asset_models.append(self)

    factsdevice_type_asset = property(get_factsdevice_type_asset, set_factsdevice_type_asset)
    # >>> factsdevice_type_asset



class RecloserAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a recloser asset of a particular product model made by a manufacturer.
    """
    # <<< recloser_asset_model
    # @generated
    def __init__(self, recloser_info=None, recloser_type_asset=None, recloser_assets=None, *args, **kw_args):
        """ Initialises a new 'RecloserAssetModel' instance.

        @param recloser_info:
        @param recloser_type_asset:
        @param recloser_assets:
        """

        self._recloser_info = None
        self.recloser_info = recloser_info

        self._recloser_type_asset = None
        self.recloser_type_asset = recloser_type_asset

        self._recloser_assets = []
        if recloser_assets is not None:
            self.recloser_assets = recloser_assets
        else:
            self.recloser_assets = []


        super(RecloserAssetModel, self).__init__(*args, **kw_args)
    # >>> recloser_asset_model

    # <<< recloser_info
    # @generated
    def get_recloser_info(self):
        """ 
        """
        return self._recloser_info

    def set_recloser_info(self, value):
        if self._recloser_info is not None:
            filtered = [x for x in self.recloser_info.recloser_asset_models if x != self]
            self._recloser_info._recloser_asset_models = filtered

        self._recloser_info = value
        if self._recloser_info is not None:
            self._recloser_info._recloser_asset_models.append(self)

    recloser_info = property(get_recloser_info, set_recloser_info)
    # >>> recloser_info

    # <<< recloser_type_asset
    # @generated
    def get_recloser_type_asset(self):
        """ 
        """
        return self._recloser_type_asset

    def set_recloser_type_asset(self, value):
        if self._recloser_type_asset is not None:
            filtered = [x for x in self.recloser_type_asset.recloser_asset_models if x != self]
            self._recloser_type_asset._recloser_asset_models = filtered

        self._recloser_type_asset = value
        if self._recloser_type_asset is not None:
            self._recloser_type_asset._recloser_asset_models.append(self)

    recloser_type_asset = property(get_recloser_type_asset, set_recloser_type_asset)
    # >>> recloser_type_asset

    # <<< recloser_assets
    # @generated
    def get_recloser_assets(self):
        """ 
        """
        return self._recloser_assets

    def set_recloser_assets(self, value):
        for x in self._recloser_assets:
            x._recloser_asset_model = None
        for y in value:
            y._recloser_asset_model = self
        self._recloser_assets = value

    recloser_assets = property(get_recloser_assets, set_recloser_assets)

    def add_recloser_assets(self, *recloser_assets):
        for obj in recloser_assets:
            obj._recloser_asset_model = self
            self._recloser_assets.append(obj)

    def remove_recloser_assets(self, *recloser_assets):
        for obj in recloser_assets:
            obj._recloser_asset_model = None
            self._recloser_assets.remove(obj)
    # >>> recloser_assets



class ShuntCompensatorAssetModel(ElectricalAssetModel):
    """ For application as shunt capacitor or reactor or switchable bank of shunt capacitors or reactors, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer (Organisation). There are typically many instances of an asset associated with a single asset model.
    """
    # <<< shunt_compensator_asset_model
    # @generated
    def __init__(self, shunt_compensator_assets=None, shunt_compensator_type_asset=None, shunt_impedance_info=None, *args, **kw_args):
        """ Initialises a new 'ShuntCompensatorAssetModel' instance.

        @param shunt_compensator_assets:
        @param shunt_compensator_type_asset:
        @param shunt_impedance_info:
        """

        self._shunt_compensator_assets = []
        if shunt_compensator_assets is not None:
            self.shunt_compensator_assets = shunt_compensator_assets
        else:
            self.shunt_compensator_assets = []

        self._shunt_compensator_type_asset = None
        self.shunt_compensator_type_asset = shunt_compensator_type_asset

        self._shunt_impedance_info = None
        self.shunt_impedance_info = shunt_impedance_info


        super(ShuntCompensatorAssetModel, self).__init__(*args, **kw_args)
    # >>> shunt_compensator_asset_model

    # <<< shunt_compensator_assets
    # @generated
    def get_shunt_compensator_assets(self):
        """ 
        """
        return self._shunt_compensator_assets

    def set_shunt_compensator_assets(self, value):
        for x in self._shunt_compensator_assets:
            x._shunt_compensator_asset_model = None
        for y in value:
            y._shunt_compensator_asset_model = self
        self._shunt_compensator_assets = value

    shunt_compensator_assets = property(get_shunt_compensator_assets, set_shunt_compensator_assets)

    def add_shunt_compensator_assets(self, *shunt_compensator_assets):
        for obj in shunt_compensator_assets:
            obj._shunt_compensator_asset_model = self
            self._shunt_compensator_assets.append(obj)

    def remove_shunt_compensator_assets(self, *shunt_compensator_assets):
        for obj in shunt_compensator_assets:
            obj._shunt_compensator_asset_model = None
            self._shunt_compensator_assets.remove(obj)
    # >>> shunt_compensator_assets

    # <<< shunt_compensator_type_asset
    # @generated
    def get_shunt_compensator_type_asset(self):
        """ 
        """
        return self._shunt_compensator_type_asset

    def set_shunt_compensator_type_asset(self, value):
        if self._shunt_compensator_type_asset is not None:
            filtered = [x for x in self.shunt_compensator_type_asset.shunt_compensator_asset_models if x != self]
            self._shunt_compensator_type_asset._shunt_compensator_asset_models = filtered

        self._shunt_compensator_type_asset = value
        if self._shunt_compensator_type_asset is not None:
            self._shunt_compensator_type_asset._shunt_compensator_asset_models.append(self)

    shunt_compensator_type_asset = property(get_shunt_compensator_type_asset, set_shunt_compensator_type_asset)
    # >>> shunt_compensator_type_asset

    # <<< shunt_impedance_info
    # @generated
    def get_shunt_impedance_info(self):
        """ 
        """
        return self._shunt_impedance_info

    def set_shunt_impedance_info(self, value):
        if self._shunt_impedance_info is not None:
            self._shunt_impedance_info._shunt_compensator_asset_model = None

        self._shunt_impedance_info = value
        if self._shunt_impedance_info is not None:
            self._shunt_impedance_info._shunt_compensator_asset_model = self

    shunt_impedance_info = property(get_shunt_impedance_info, set_shunt_impedance_info)
    # >>> shunt_impedance_info



class SVCAssetModel(FACTSDeviceAssetModel):
    """ Documentation for a type of a Static Var Compensator of a particular product model made by a manufacturer.
    """
    # <<< svcasset_model
    # @generated
    def __init__(self, svc_info=None, svctype_asset=None, svcassets=None, *args, **kw_args):
        """ Initialises a new 'SVCAssetModel' instance.

        @param svc_info:
        @param svctype_asset:
        @param svcassets:
        """

        self._svc_info = None
        self.svc_info = svc_info

        self._svctype_asset = None
        self.svctype_asset = svctype_asset

        self._svcassets = []
        if svcassets is not None:
            self.svcassets = svcassets
        else:
            self.svcassets = []


        super(SVCAssetModel, self).__init__(*args, **kw_args)
    # >>> svcasset_model

    # <<< svc_info
    # @generated
    def get_svc_info(self):
        """ 
        """
        return self._svc_info

    def set_svc_info(self, value):
        if self._svc_info is not None:
            self._svc_info._svcasset_model = None

        self._svc_info = value
        if self._svc_info is not None:
            self._svc_info._svcasset_model = self

    svc_info = property(get_svc_info, set_svc_info)
    # >>> svc_info

    # <<< svctype_asset
    # @generated
    def get_svctype_asset(self):
        """ 
        """
        return self._svctype_asset

    def set_svctype_asset(self, value):
        if self._svctype_asset is not None:
            filtered = [x for x in self.svctype_asset.svcasset_models if x != self]
            self._svctype_asset._svcasset_models = filtered

        self._svctype_asset = value
        if self._svctype_asset is not None:
            self._svctype_asset._svcasset_models.append(self)

    svctype_asset = property(get_svctype_asset, set_svctype_asset)
    # >>> svctype_asset

    # <<< svcassets
    # @generated
    def get_svcassets(self):
        """ 
        """
        return self._svcassets

    def set_svcassets(self, value):
        for x in self._svcassets:
            x._svcasset_model = None
        for y in value:
            y._svcasset_model = self
        self._svcassets = value

    svcassets = property(get_svcassets, set_svcassets)

    def add_svcassets(self, *svcassets):
        for obj in svcassets:
            obj._svcasset_model = self
            self._svcassets.append(obj)

    def remove_svcassets(self, *svcassets):
        for obj in svcassets:
            obj._svcasset_model = None
            self._svcassets.remove(obj)
    # >>> svcassets



class BreakerAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a breaker asset of a particular product model made by a manufacturer.
    """
    # <<< breaker_asset_model
    # @generated
    def __init__(self, breaker_info=None, breaker_assets=None, breaker_type_asset=None, *args, **kw_args):
        """ Initialises a new 'BreakerAssetModel' instance.

        @param breaker_info:
        @param breaker_assets:
        @param breaker_type_asset:
        """

        self._breaker_info = None
        self.breaker_info = breaker_info

        self._breaker_assets = []
        if breaker_assets is not None:
            self.breaker_assets = breaker_assets
        else:
            self.breaker_assets = []

        self._breaker_type_asset = None
        self.breaker_type_asset = breaker_type_asset


        super(BreakerAssetModel, self).__init__(*args, **kw_args)
    # >>> breaker_asset_model

    # <<< breaker_info
    # @generated
    def get_breaker_info(self):
        """ 
        """
        return self._breaker_info

    def set_breaker_info(self, value):
        if self._breaker_info is not None:
            filtered = [x for x in self.breaker_info.breaker_asset_models if x != self]
            self._breaker_info._breaker_asset_models = filtered

        self._breaker_info = value
        if self._breaker_info is not None:
            self._breaker_info._breaker_asset_models.append(self)

    breaker_info = property(get_breaker_info, set_breaker_info)
    # >>> breaker_info

    # <<< breaker_assets
    # @generated
    def get_breaker_assets(self):
        """ 
        """
        return self._breaker_assets

    def set_breaker_assets(self, value):
        for x in self._breaker_assets:
            x._breaker_asset_model = None
        for y in value:
            y._breaker_asset_model = self
        self._breaker_assets = value

    breaker_assets = property(get_breaker_assets, set_breaker_assets)

    def add_breaker_assets(self, *breaker_assets):
        for obj in breaker_assets:
            obj._breaker_asset_model = self
            self._breaker_assets.append(obj)

    def remove_breaker_assets(self, *breaker_assets):
        for obj in breaker_assets:
            obj._breaker_asset_model = None
            self._breaker_assets.remove(obj)
    # >>> breaker_assets

    # <<< breaker_type_asset
    # @generated
    def get_breaker_type_asset(self):
        """ 
        """
        return self._breaker_type_asset

    def set_breaker_type_asset(self, value):
        if self._breaker_type_asset is not None:
            filtered = [x for x in self.breaker_type_asset.breaker_asset_models if x != self]
            self._breaker_type_asset._breaker_asset_models = filtered

        self._breaker_type_asset = value
        if self._breaker_type_asset is not None:
            self._breaker_type_asset._breaker_asset_models.append(self)

    breaker_type_asset = property(get_breaker_type_asset, set_breaker_type_asset)
    # >>> breaker_type_asset



class GeneratorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of generation equipment of a particular product model made by a manufacturer.
    """
    # <<< generator_asset_model
    # @generated
    def __init__(self, generator_assets=None, generator_type_asset=None, *args, **kw_args):
        """ Initialises a new 'GeneratorAssetModel' instance.

        @param generator_assets:
        @param generator_type_asset:
        """

        self._generator_assets = []
        if generator_assets is not None:
            self.generator_assets = generator_assets
        else:
            self.generator_assets = []

        self._generator_type_asset = None
        self.generator_type_asset = generator_type_asset


        super(GeneratorAssetModel, self).__init__(*args, **kw_args)
    # >>> generator_asset_model

    # <<< generator_assets
    # @generated
    def get_generator_assets(self):
        """ 
        """
        return self._generator_assets

    def set_generator_assets(self, value):
        for x in self._generator_assets:
            x._generator_asset_model = None
        for y in value:
            y._generator_asset_model = self
        self._generator_assets = value

    generator_assets = property(get_generator_assets, set_generator_assets)

    def add_generator_assets(self, *generator_assets):
        for obj in generator_assets:
            obj._generator_asset_model = self
            self._generator_assets.append(obj)

    def remove_generator_assets(self, *generator_assets):
        for obj in generator_assets:
            obj._generator_asset_model = None
            self._generator_assets.remove(obj)
    # >>> generator_assets

    # <<< generator_type_asset
    # @generated
    def get_generator_type_asset(self):
        """ 
        """
        return self._generator_type_asset

    def set_generator_type_asset(self, value):
        if self._generator_type_asset is not None:
            filtered = [x for x in self.generator_type_asset.generator_asset_models if x != self]
            self._generator_type_asset._generator_asset_models = filtered

        self._generator_type_asset = value
        if self._generator_type_asset is not None:
            self._generator_type_asset._generator_asset_models.append(self)

    generator_type_asset = property(get_generator_type_asset, set_generator_type_asset)
    # >>> generator_type_asset



class ResistorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a resistor asset of a particular product model made by a manufacturer.
    """
    # <<< resistor_asset_model
    # @generated
    def __init__(self, resistor_type_asset=None, resistor_assets=None, *args, **kw_args):
        """ Initialises a new 'ResistorAssetModel' instance.

        @param resistor_type_asset:
        @param resistor_assets:
        """

        self._resistor_type_asset = None
        self.resistor_type_asset = resistor_type_asset

        self._resistor_assets = []
        if resistor_assets is not None:
            self.resistor_assets = resistor_assets
        else:
            self.resistor_assets = []


        super(ResistorAssetModel, self).__init__(*args, **kw_args)
    # >>> resistor_asset_model

    # <<< resistor_type_asset
    # @generated
    def get_resistor_type_asset(self):
        """ 
        """
        return self._resistor_type_asset

    def set_resistor_type_asset(self, value):
        if self._resistor_type_asset is not None:
            filtered = [x for x in self.resistor_type_asset.resistor_asset_models if x != self]
            self._resistor_type_asset._resistor_asset_models = filtered

        self._resistor_type_asset = value
        if self._resistor_type_asset is not None:
            self._resistor_type_asset._resistor_asset_models.append(self)

    resistor_type_asset = property(get_resistor_type_asset, set_resistor_type_asset)
    # >>> resistor_type_asset

    # <<< resistor_assets
    # @generated
    def get_resistor_assets(self):
        """ 
        """
        return self._resistor_assets

    def set_resistor_assets(self, value):
        for x in self._resistor_assets:
            x._resistor_asset_model = None
        for y in value:
            y._resistor_asset_model = self
        self._resistor_assets = value

    resistor_assets = property(get_resistor_assets, set_resistor_assets)

    def add_resistor_assets(self, *resistor_assets):
        for obj in resistor_assets:
            obj._resistor_asset_model = self
            self._resistor_assets.append(obj)

    def remove_resistor_assets(self, *resistor_assets):
        for obj in resistor_assets:
            obj._resistor_asset_model = None
            self._resistor_assets.remove(obj)
    # >>> resistor_assets



class SurgeProtectorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of an SurgeProtector asset of a particular product model made by a manufacturer.
    """
    # <<< surge_protector_asset_model
    # @generated
    def __init__(self, surge_protector_type_asset=None, surge_protector_assets=None, *args, **kw_args):
        """ Initialises a new 'SurgeProtectorAssetModel' instance.

        @param surge_protector_type_asset:
        @param surge_protector_assets:
        """

        self._surge_protector_type_asset = None
        self.surge_protector_type_asset = surge_protector_type_asset

        self._surge_protector_assets = []
        if surge_protector_assets is not None:
            self.surge_protector_assets = surge_protector_assets
        else:
            self.surge_protector_assets = []


        super(SurgeProtectorAssetModel, self).__init__(*args, **kw_args)
    # >>> surge_protector_asset_model

    # <<< surge_protector_type_asset
    # @generated
    def get_surge_protector_type_asset(self):
        """ 
        """
        return self._surge_protector_type_asset

    def set_surge_protector_type_asset(self, value):
        if self._surge_protector_type_asset is not None:
            filtered = [x for x in self.surge_protector_type_asset.surge_protector_asset_models if x != self]
            self._surge_protector_type_asset._surge_protector_asset_models = filtered

        self._surge_protector_type_asset = value
        if self._surge_protector_type_asset is not None:
            self._surge_protector_type_asset._surge_protector_asset_models.append(self)

    surge_protector_type_asset = property(get_surge_protector_type_asset, set_surge_protector_type_asset)
    # >>> surge_protector_type_asset

    # <<< surge_protector_assets
    # @generated
    def get_surge_protector_assets(self):
        """ 
        """
        return self._surge_protector_assets

    def set_surge_protector_assets(self, value):
        for x in self._surge_protector_assets:
            x._surge_protector_asset_model = None
        for y in value:
            y._surge_protector_asset_model = self
        self._surge_protector_assets = value

    surge_protector_assets = property(get_surge_protector_assets, set_surge_protector_assets)

    def add_surge_protector_assets(self, *surge_protector_assets):
        for obj in surge_protector_assets:
            obj._surge_protector_asset_model = self
            self._surge_protector_assets.append(obj)

    def remove_surge_protector_assets(self, *surge_protector_assets):
        for obj in surge_protector_assets:
            obj._surge_protector_asset_model = None
            self._surge_protector_assets.remove(obj)
    # >>> surge_protector_assets



class ProtectionEquipmentAssetModel(ElectricalAssetModel):
    """ Documentation for a type of protection equipment asset of a particular product model made by a manufacturer.
    """
    # <<< protection_equipment_asset_model
    # @generated
    def __init__(self, protection_equipment_assets=None, protection_equipment_type_asset=None, *args, **kw_args):
        """ Initialises a new 'ProtectionEquipmentAssetModel' instance.

        @param protection_equipment_assets:
        @param protection_equipment_type_asset:
        """

        self._protection_equipment_assets = []
        if protection_equipment_assets is not None:
            self.protection_equipment_assets = protection_equipment_assets
        else:
            self.protection_equipment_assets = []

        self._protection_equipment_type_asset = None
        self.protection_equipment_type_asset = protection_equipment_type_asset


        super(ProtectionEquipmentAssetModel, self).__init__(*args, **kw_args)
    # >>> protection_equipment_asset_model

    # <<< protection_equipment_assets
    # @generated
    def get_protection_equipment_assets(self):
        """ 
        """
        return self._protection_equipment_assets

    def set_protection_equipment_assets(self, value):
        for x in self._protection_equipment_assets:
            x._protection_equipment_asset_model = None
        for y in value:
            y._protection_equipment_asset_model = self
        self._protection_equipment_assets = value

    protection_equipment_assets = property(get_protection_equipment_assets, set_protection_equipment_assets)

    def add_protection_equipment_assets(self, *protection_equipment_assets):
        for obj in protection_equipment_assets:
            obj._protection_equipment_asset_model = self
            self._protection_equipment_assets.append(obj)

    def remove_protection_equipment_assets(self, *protection_equipment_assets):
        for obj in protection_equipment_assets:
            obj._protection_equipment_asset_model = None
            self._protection_equipment_assets.remove(obj)
    # >>> protection_equipment_assets

    # <<< protection_equipment_type_asset
    # @generated
    def get_protection_equipment_type_asset(self):
        """ 
        """
        return self._protection_equipment_type_asset

    def set_protection_equipment_type_asset(self, value):
        if self._protection_equipment_type_asset is not None:
            filtered = [x for x in self.protection_equipment_type_asset.protection_equipment_asset_models if x != self]
            self._protection_equipment_type_asset._protection_equipment_asset_models = filtered

        self._protection_equipment_type_asset = value
        if self._protection_equipment_type_asset is not None:
            self._protection_equipment_type_asset._protection_equipment_asset_models.append(self)

    protection_equipment_type_asset = property(get_protection_equipment_type_asset, set_protection_equipment_type_asset)
    # >>> protection_equipment_type_asset



class PotentialTransformerAssetModel(ElectricalAssetModel):
    """ A particular model supplied by a manufacturer of a Potential Transformer (PT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """
    # <<< potential_transformer_asset_model
    # @generated
    def __init__(self, potential_transformer_type_asset=None, potential_transformer_info=None, potential_transformer_assets=None, *args, **kw_args):
        """ Initialises a new 'PotentialTransformerAssetModel' instance.

        @param potential_transformer_type_asset:
        @param potential_transformer_info:
        @param potential_transformer_assets:
        """

        self._potential_transformer_type_asset = None
        self.potential_transformer_type_asset = potential_transformer_type_asset

        self._potential_transformer_info = None
        self.potential_transformer_info = potential_transformer_info

        self._potential_transformer_assets = []
        if potential_transformer_assets is not None:
            self.potential_transformer_assets = potential_transformer_assets
        else:
            self.potential_transformer_assets = []


        super(PotentialTransformerAssetModel, self).__init__(*args, **kw_args)
    # >>> potential_transformer_asset_model

    # <<< potential_transformer_type_asset
    # @generated
    def get_potential_transformer_type_asset(self):
        """ 
        """
        return self._potential_transformer_type_asset

    def set_potential_transformer_type_asset(self, value):
        if self._potential_transformer_type_asset is not None:
            filtered = [x for x in self.potential_transformer_type_asset.potential_transformer_asset_models if x != self]
            self._potential_transformer_type_asset._potential_transformer_asset_models = filtered

        self._potential_transformer_type_asset = value
        if self._potential_transformer_type_asset is not None:
            self._potential_transformer_type_asset._potential_transformer_asset_models.append(self)

    potential_transformer_type_asset = property(get_potential_transformer_type_asset, set_potential_transformer_type_asset)
    # >>> potential_transformer_type_asset

    # <<< potential_transformer_info
    # @generated
    def get_potential_transformer_info(self):
        """ 
        """
        return self._potential_transformer_info

    def set_potential_transformer_info(self, value):
        if self._potential_transformer_info is not None:
            filtered = [x for x in self.potential_transformer_info.potential_transformer_asset_models if x != self]
            self._potential_transformer_info._potential_transformer_asset_models = filtered

        self._potential_transformer_info = value
        if self._potential_transformer_info is not None:
            self._potential_transformer_info._potential_transformer_asset_models.append(self)

    potential_transformer_info = property(get_potential_transformer_info, set_potential_transformer_info)
    # >>> potential_transformer_info

    # <<< potential_transformer_assets
    # @generated
    def get_potential_transformer_assets(self):
        """ 
        """
        return self._potential_transformer_assets

    def set_potential_transformer_assets(self, value):
        for x in self._potential_transformer_assets:
            x._potential_transformer_asset_model = None
        for y in value:
            y._potential_transformer_asset_model = self
        self._potential_transformer_assets = value

    potential_transformer_assets = property(get_potential_transformer_assets, set_potential_transformer_assets)

    def add_potential_transformer_assets(self, *potential_transformer_assets):
        for obj in potential_transformer_assets:
            obj._potential_transformer_asset_model = self
            self._potential_transformer_assets.append(obj)

    def remove_potential_transformer_assets(self, *potential_transformer_assets):
        for obj in potential_transformer_assets:
            obj._potential_transformer_asset_model = None
            self._potential_transformer_assets.remove(obj)
    # >>> potential_transformer_assets



class BushingModel(ElectricalAssetModel):
    """ Documentation for a type of a bushing of a particular product model made by a manufacturer.
    """
    # <<< bushing_model
    # @generated
    def __init__(self, insulation_kind='paperoil', bushing_asset=None, *args, **kw_args):
        """ Initialises a new 'BushingModel' instance.

        @param insulation_kind: Kind of insulation used in this bushing model. Values are: "paperoil", "compound", "other", "solid_porcelain"
        @param bushing_asset:
        """
        # Kind of insulation used in this bushing model. Values are: "paperoil", "compound", "other", "solid_porcelain"
        self.insulation_kind = insulation_kind


        self._bushing_asset = None
        self.bushing_asset = bushing_asset


        super(BushingModel, self).__init__(*args, **kw_args)
    # >>> bushing_model

    # <<< bushing_asset
    # @generated
    def get_bushing_asset(self):
        """ 
        """
        return self._bushing_asset

    def set_bushing_asset(self, value):
        if self._bushing_asset is not None:
            self._bushing_asset._bushing_model = None

        self._bushing_asset = value
        if self._bushing_asset is not None:
            self._bushing_asset._bushing_model = self

    bushing_asset = property(get_bushing_asset, set_bushing_asset)
    # >>> bushing_asset



class CurrentTransformerAssetModel(ElectricalAssetModel):
    """ A particular model supplied by a manufacturer of a Current Transformer (CT), wich is used to measure electrical qualities of the circuit that is being protected and/or monitored.
    """
    # <<< current_transformer_asset_model
    # @generated
    def __init__(self, current_transformer_type_asset=None, current_transformer_info=None, current_transformer_assets=None, *args, **kw_args):
        """ Initialises a new 'CurrentTransformerAssetModel' instance.

        @param current_transformer_type_asset:
        @param current_transformer_info:
        @param current_transformer_assets:
        """

        self._current_transformer_type_asset = None
        self.current_transformer_type_asset = current_transformer_type_asset

        self._current_transformer_info = None
        self.current_transformer_info = current_transformer_info

        self._current_transformer_assets = []
        if current_transformer_assets is not None:
            self.current_transformer_assets = current_transformer_assets
        else:
            self.current_transformer_assets = []


        super(CurrentTransformerAssetModel, self).__init__(*args, **kw_args)
    # >>> current_transformer_asset_model

    # <<< current_transformer_type_asset
    # @generated
    def get_current_transformer_type_asset(self):
        """ 
        """
        return self._current_transformer_type_asset

    def set_current_transformer_type_asset(self, value):
        if self._current_transformer_type_asset is not None:
            filtered = [x for x in self.current_transformer_type_asset.current_transformer_asset_models if x != self]
            self._current_transformer_type_asset._current_transformer_asset_models = filtered

        self._current_transformer_type_asset = value
        if self._current_transformer_type_asset is not None:
            self._current_transformer_type_asset._current_transformer_asset_models.append(self)

    current_transformer_type_asset = property(get_current_transformer_type_asset, set_current_transformer_type_asset)
    # >>> current_transformer_type_asset

    # <<< current_transformer_info
    # @generated
    def get_current_transformer_info(self):
        """ 
        """
        return self._current_transformer_info

    def set_current_transformer_info(self, value):
        if self._current_transformer_info is not None:
            filtered = [x for x in self.current_transformer_info.current_transformer_assert_models if x != self]
            self._current_transformer_info._current_transformer_assert_models = filtered

        self._current_transformer_info = value
        if self._current_transformer_info is not None:
            self._current_transformer_info._current_transformer_assert_models.append(self)

    current_transformer_info = property(get_current_transformer_info, set_current_transformer_info)
    # >>> current_transformer_info

    # <<< current_transformer_assets
    # @generated
    def get_current_transformer_assets(self):
        """ 
        """
        return self._current_transformer_assets

    def set_current_transformer_assets(self, value):
        for x in self._current_transformer_assets:
            x._current_transformer_asset_model = None
        for y in value:
            y._current_transformer_asset_model = self
        self._current_transformer_assets = value

    current_transformer_assets = property(get_current_transformer_assets, set_current_transformer_assets)

    def add_current_transformer_assets(self, *current_transformer_assets):
        for obj in current_transformer_assets:
            obj._current_transformer_asset_model = self
            self._current_transformer_assets.append(obj)

    def remove_current_transformer_assets(self, *current_transformer_assets):
        for obj in current_transformer_assets:
            obj._current_transformer_asset_model = None
            self._current_transformer_assets.remove(obj)
    # >>> current_transformer_assets



class FaultIndicatorAssetModel(ElectricalAssetModel):
    """ Documentation for a type of an FaultIndicator asset of a particular product model made by a manufacturer.
    """
    # <<< fault_indicator_asset_model
    # @generated
    def __init__(self, fault_indicator_type_asset=None, fault_indicator_assets=None, *args, **kw_args):
        """ Initialises a new 'FaultIndicatorAssetModel' instance.

        @param fault_indicator_type_asset:
        @param fault_indicator_assets:
        """

        self._fault_indicator_type_asset = None
        self.fault_indicator_type_asset = fault_indicator_type_asset

        self._fault_indicator_assets = []
        if fault_indicator_assets is not None:
            self.fault_indicator_assets = fault_indicator_assets
        else:
            self.fault_indicator_assets = []


        super(FaultIndicatorAssetModel, self).__init__(*args, **kw_args)
    # >>> fault_indicator_asset_model

    # <<< fault_indicator_type_asset
    # @generated
    def get_fault_indicator_type_asset(self):
        """ 
        """
        return self._fault_indicator_type_asset

    def set_fault_indicator_type_asset(self, value):
        if self._fault_indicator_type_asset is not None:
            filtered = [x for x in self.fault_indicator_type_asset.fault_indicator_asset_models if x != self]
            self._fault_indicator_type_asset._fault_indicator_asset_models = filtered

        self._fault_indicator_type_asset = value
        if self._fault_indicator_type_asset is not None:
            self._fault_indicator_type_asset._fault_indicator_asset_models.append(self)

    fault_indicator_type_asset = property(get_fault_indicator_type_asset, set_fault_indicator_type_asset)
    # >>> fault_indicator_type_asset

    # <<< fault_indicator_assets
    # @generated
    def get_fault_indicator_assets(self):
        """ 
        """
        return self._fault_indicator_assets

    def set_fault_indicator_assets(self, value):
        for x in self._fault_indicator_assets:
            x._fault_indicator_asset_model = None
        for y in value:
            y._fault_indicator_asset_model = self
        self._fault_indicator_assets = value

    fault_indicator_assets = property(get_fault_indicator_assets, set_fault_indicator_assets)

    def add_fault_indicator_assets(self, *fault_indicator_assets):
        for obj in fault_indicator_assets:
            obj._fault_indicator_asset_model = self
            self._fault_indicator_assets.append(obj)

    def remove_fault_indicator_assets(self, *fault_indicator_assets):
        for obj in fault_indicator_assets:
            obj._fault_indicator_asset_model = None
            self._fault_indicator_assets.remove(obj)
    # >>> fault_indicator_assets



class StreetlightAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a streelight of a particular product model made by a manufacturer.
    """
    # <<< streetlight_asset_model
    # @generated
    def __init__(self, lamp_kind='high_pressure_sodium', light_rating=0.0, streetlights=None, streetlight_type_assets=None, *args, **kw_args):
        """ Initialises a new 'StreetlightAssetModel' instance.

        @param lamp_kind: Lamp kind supplied from manufacturer (vs. one that has been replaced in the field). Values are: "high_pressure_sodium", "other", "metal_halide", "mercury_vapor"
        @param light_rating: Power rating of light as supplied by the manufacturer. 
        @param streetlights:
        @param streetlight_type_assets:
        """
        # Lamp kind supplied from manufacturer (vs. one that has been replaced in the field). Values are: "high_pressure_sodium", "other", "metal_halide", "mercury_vapor"
        self.lamp_kind = lamp_kind

        # Power rating of light as supplied by the manufacturer. 
        self.light_rating = light_rating


        self._streetlights = []
        if streetlights is not None:
            self.streetlights = streetlights
        else:
            self.streetlights = []

        self._streetlight_type_assets = []
        if streetlight_type_assets is not None:
            self.streetlight_type_assets = streetlight_type_assets
        else:
            self.streetlight_type_assets = []


        super(StreetlightAssetModel, self).__init__(*args, **kw_args)
    # >>> streetlight_asset_model

    # <<< streetlights
    # @generated
    def get_streetlights(self):
        """ 
        """
        return self._streetlights

    def set_streetlights(self, value):
        for x in self._streetlights:
            x._streetlight_asset_model = None
        for y in value:
            y._streetlight_asset_model = self
        self._streetlights = value

    streetlights = property(get_streetlights, set_streetlights)

    def add_streetlights(self, *streetlights):
        for obj in streetlights:
            obj._streetlight_asset_model = self
            self._streetlights.append(obj)

    def remove_streetlights(self, *streetlights):
        for obj in streetlights:
            obj._streetlight_asset_model = None
            self._streetlights.remove(obj)
    # >>> streetlights

    # <<< streetlight_type_assets
    # @generated
    def get_streetlight_type_assets(self):
        """ 
        """
        return self._streetlight_type_assets

    def set_streetlight_type_assets(self, value):
        for p in self._streetlight_type_assets:
            filtered = [q for q in p.streetlight_asset_models if q != self]
            self._streetlight_type_assets._streetlight_asset_models = filtered
        for r in value:
            if self not in r._streetlight_asset_models:
                r._streetlight_asset_models.append(self)
        self._streetlight_type_assets = value

    streetlight_type_assets = property(get_streetlight_type_assets, set_streetlight_type_assets)

    def add_streetlight_type_assets(self, *streetlight_type_assets):
        for obj in streetlight_type_assets:
            if self not in obj._streetlight_asset_models:
                obj._streetlight_asset_models.append(self)
            self._streetlight_type_assets.append(obj)

    def remove_streetlight_type_assets(self, *streetlight_type_assets):
        for obj in streetlight_type_assets:
            if self in obj._streetlight_asset_models:
                obj._streetlight_asset_models.remove(self)
            self._streetlight_type_assets.remove(obj)
    # >>> streetlight_type_assets



class SeriesCompensatorAssetModel(ElectricalAssetModel):
    """ For application as a series capacitor or reactor, this is documentation for a type of a capacitor or reactor of a particular product model made by a manufacturer.
    """
    # <<< series_compensator_asset_model
    # @generated
    def __init__(self, series_compensator_asset=None, shunt_compensator_type_asset=None, *args, **kw_args):
        """ Initialises a new 'SeriesCompensatorAssetModel' instance.

        @param series_compensator_asset:
        @param shunt_compensator_type_asset:
        """

        self._series_compensator_asset = None
        self.series_compensator_asset = series_compensator_asset

        self._shunt_compensator_type_asset = None
        self.shunt_compensator_type_asset = shunt_compensator_type_asset


        super(SeriesCompensatorAssetModel, self).__init__(*args, **kw_args)
    # >>> series_compensator_asset_model

    # <<< series_compensator_asset
    # @generated
    def get_series_compensator_asset(self):
        """ 
        """
        return self._series_compensator_asset

    def set_series_compensator_asset(self, value):
        if self._series_compensator_asset is not None:
            self._series_compensator_asset._series_compensator_asset_model = None

        self._series_compensator_asset = value
        if self._series_compensator_asset is not None:
            self._series_compensator_asset._series_compensator_asset_model = self

    series_compensator_asset = property(get_series_compensator_asset, set_series_compensator_asset)
    # >>> series_compensator_asset

    # <<< shunt_compensator_type_asset
    # @generated
    def get_shunt_compensator_type_asset(self):
        """ 
        """
        return self._shunt_compensator_type_asset

    def set_shunt_compensator_type_asset(self, value):
        if self._shunt_compensator_type_asset is not None:
            filtered = [x for x in self.shunt_compensator_type_asset.shunt_compensator_asset_models if x != self]
            self._shunt_compensator_type_asset._shunt_compensator_asset_models = filtered

        self._shunt_compensator_type_asset = value
        if self._shunt_compensator_type_asset is not None:
            self._shunt_compensator_type_asset._shunt_compensator_asset_models.append(self)

    shunt_compensator_type_asset = property(get_shunt_compensator_type_asset, set_shunt_compensator_type_asset)
    # >>> shunt_compensator_type_asset



class BusbarAssetModel(ElectricalAssetModel):
    """ Documentation for a type of a busbar asset of a particular product model made by a manufacturer.
    """
    # <<< busbar_asset_model
    # @generated
    def __init__(self, busbar_assets=None, busbar_asset_model=None, *args, **kw_args):
        """ Initialises a new 'BusbarAssetModel' instance.

        @param busbar_assets:
        @param busbar_asset_model:
        """

        self._busbar_assets = []
        if busbar_assets is not None:
            self.busbar_assets = busbar_assets
        else:
            self.busbar_assets = []

        self._busbar_asset_model = None
        self.busbar_asset_model = busbar_asset_model


        super(BusbarAssetModel, self).__init__(*args, **kw_args)
    # >>> busbar_asset_model

    # <<< busbar_assets
    # @generated
    def get_busbar_assets(self):
        """ 
        """
        return self._busbar_assets

    def set_busbar_assets(self, value):
        for x in self._busbar_assets:
            x._busbar_asset_model = None
        for y in value:
            y._busbar_asset_model = self
        self._busbar_assets = value

    busbar_assets = property(get_busbar_assets, set_busbar_assets)

    def add_busbar_assets(self, *busbar_assets):
        for obj in busbar_assets:
            obj._busbar_asset_model = self
            self._busbar_assets.append(obj)

    def remove_busbar_assets(self, *busbar_assets):
        for obj in busbar_assets:
            obj._busbar_asset_model = None
            self._busbar_assets.remove(obj)
    # >>> busbar_assets

    # <<< busbar_asset_model
    # @generated
    def get_busbar_asset_model(self):
        """ 
        """
        return self._busbar_asset_model

    def set_busbar_asset_model(self, value):
        if self._busbar_asset_model is not None:
            filtered = [x for x in self.busbar_asset_model.busbar_type_assets if x != self]
            self._busbar_asset_model._busbar_type_assets = filtered

        self._busbar_asset_model = value
        if self._busbar_asset_model is not None:
            self._busbar_asset_model._busbar_type_assets.append(self)

    busbar_asset_model = property(get_busbar_asset_model, set_busbar_asset_model)
    # >>> busbar_asset_model



# <<< inf_asset_models
# @generated
# >>> inf_asset_models
