# coding=utf-8
# pylint: disable=too-many-lines
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for license information.
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is regenerated.
# --------------------------------------------------------------------------

import datetime
import sys
from typing import Any, Dict, List, Optional, TYPE_CHECKING, Union

from .. import _serialization

if sys.version_info >= (3, 9):
    from collections.abc import MutableMapping
else:
    from typing import MutableMapping  # type: ignore  # pylint: disable=ungrouped-imports
if sys.version_info >= (3, 8):
    from typing import Literal  # pylint: disable=no-name-in-module, ungrouped-imports
else:
    from typing_extensions import Literal  # type: ignore  # pylint: disable=ungrouped-imports

if TYPE_CHECKING:
    # pylint: disable=unused-import,ungrouped-imports
    from .. import models as _models
JSON = MutableMapping[str, Any]  # pylint: disable=unsubscriptable-object


class Resource(_serialization.Model):
    """Common fields that are returned in the response for all Azure Resource Manager resources.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.servicenetworking.models.SystemData
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.id = None
        self.name = None
        self.type = None
        self.system_data = None


class TrackedResource(Resource):
    """The resource model definition for an Azure Resource Manager tracked top level resource which
    has 'tags' and a 'location'.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.servicenetworking.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.location = location


class Association(TrackedResource):
    """Association Subresource of Traffic Controller.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.servicenetworking.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar association_type: Association Type. Default value is "subnets".
    :vartype association_type: str
    :ivar subnet: Association Subnet.
    :vartype subnet: ~azure.mgmt.servicenetworking.models.AssociationSubnet
    :ivar provisioning_state: Provisioning State. Known values are: "Succeeded", "Failed",
     "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.mgmt.servicenetworking.models.ProvisioningState
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "association_type": {"key": "properties.associationType", "type": "str"},
        "subnet": {"key": "properties.subnet", "type": "AssociationSubnet"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        association_type: Optional[Literal["subnets"]] = None,
        subnet: Optional["_models.AssociationSubnet"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword association_type: Association Type. Default value is "subnets".
        :paramtype association_type: str
        :keyword subnet: Association Subnet.
        :paramtype subnet: ~azure.mgmt.servicenetworking.models.AssociationSubnet
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.association_type = association_type
        self.subnet = subnet
        self.provisioning_state = None


class AssociationListResult(_serialization.Model):
    """The response of a Traffic Controller Association list operation.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The Association items on this page. Required.
    :vartype value: list[~azure.mgmt.servicenetworking.models.Association]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Association]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: List["_models.Association"], next_link: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value: The Association items on this page. Required.
        :paramtype value: list[~azure.mgmt.servicenetworking.models.Association]
        :keyword next_link: The link to the next page of items.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class AssociationSubnet(_serialization.Model):
    """Association Subnet.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Association ID. Required.
    :vartype id: str
    """

    _validation = {
        "id": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, *, id: str, **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        """
        :keyword id: Association ID. Required.
        :paramtype id: str
        """
        super().__init__(**kwargs)
        self.id = id


class AssociationUpdate(_serialization.Model):
    """The type used for update operations of the Association.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar properties: The updatable properties of the Association.
    :vartype properties: ~azure.mgmt.servicenetworking.models.AssociationUpdateProperties
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "properties": {"key": "properties", "type": "AssociationUpdateProperties"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.AssociationUpdateProperties"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword properties: The updatable properties of the Association.
        :paramtype properties: ~azure.mgmt.servicenetworking.models.AssociationUpdateProperties
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.properties = properties


class AssociationUpdateProperties(_serialization.Model):
    """The updatable properties of the Association.

    :ivar association_type: Association Type. Default value is "subnets".
    :vartype association_type: str
    :ivar subnet: Association Subnet.
    :vartype subnet: ~azure.mgmt.servicenetworking.models.AssociationSubnet
    """

    _attribute_map = {
        "association_type": {"key": "associationType", "type": "str"},
        "subnet": {"key": "subnet", "type": "AssociationSubnet"},
    }

    def __init__(
        self,
        *,
        association_type: Optional[Literal["subnets"]] = None,
        subnet: Optional["_models.AssociationSubnet"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword association_type: Association Type. Default value is "subnets".
        :paramtype association_type: str
        :keyword subnet: Association Subnet.
        :paramtype subnet: ~azure.mgmt.servicenetworking.models.AssociationSubnet
        """
        super().__init__(**kwargs)
        self.association_type = association_type
        self.subnet = subnet


class ErrorAdditionalInfo(_serialization.Model):
    """The resource management error additional info.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar type: The additional info type.
    :vartype type: str
    :ivar info: The additional info.
    :vartype info: JSON
    """

    _validation = {
        "type": {"readonly": True},
        "info": {"readonly": True},
    }

    _attribute_map = {
        "type": {"key": "type", "type": "str"},
        "info": {"key": "info", "type": "object"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.type = None
        self.info = None


class ErrorDetail(_serialization.Model):
    """The error detail.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar code: The error code.
    :vartype code: str
    :ivar message: The error message.
    :vartype message: str
    :ivar target: The error target.
    :vartype target: str
    :ivar details: The error details.
    :vartype details: list[~azure.mgmt.servicenetworking.models.ErrorDetail]
    :ivar additional_info: The error additional info.
    :vartype additional_info: list[~azure.mgmt.servicenetworking.models.ErrorAdditionalInfo]
    """

    _validation = {
        "code": {"readonly": True},
        "message": {"readonly": True},
        "target": {"readonly": True},
        "details": {"readonly": True},
        "additional_info": {"readonly": True},
    }

    _attribute_map = {
        "code": {"key": "code", "type": "str"},
        "message": {"key": "message", "type": "str"},
        "target": {"key": "target", "type": "str"},
        "details": {"key": "details", "type": "[ErrorDetail]"},
        "additional_info": {"key": "additionalInfo", "type": "[ErrorAdditionalInfo]"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.code = None
        self.message = None
        self.target = None
        self.details = None
        self.additional_info = None


class ErrorResponse(_serialization.Model):
    """Common error response for all Azure Resource Manager APIs to return error details for failed
    operations. (This also follows the OData error response format.).

    :ivar error: The error object.
    :vartype error: ~azure.mgmt.servicenetworking.models.ErrorDetail
    """

    _attribute_map = {
        "error": {"key": "error", "type": "ErrorDetail"},
    }

    def __init__(self, *, error: Optional["_models.ErrorDetail"] = None, **kwargs: Any) -> None:
        """
        :keyword error: The error object.
        :paramtype error: ~azure.mgmt.servicenetworking.models.ErrorDetail
        """
        super().__init__(**kwargs)
        self.error = error


class Frontend(TrackedResource):
    """Frontend Subresource of Traffic Controller.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.servicenetworking.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar mode: Frontend Mode (Optional). Default value is "public".
    :vartype mode: str
    :ivar ip_address_version: Frontend IP Address Version (Optional). Known values are: "IPv4" and
     "IPv6".
    :vartype ip_address_version: str or
     ~azure.mgmt.servicenetworking.models.FrontendIPAddressVersion
    :ivar public_ip_address: Frontend Public IP Address (Optional).
    :vartype public_ip_address: ~azure.mgmt.servicenetworking.models.FrontendPropertiesIPAddress
    :ivar provisioning_state: test doc. Known values are: "Succeeded", "Failed", "Canceled",
     "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.mgmt.servicenetworking.models.ProvisioningState
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "mode": {"key": "properties.mode", "type": "str"},
        "ip_address_version": {"key": "properties.ipAddressVersion", "type": "str"},
        "public_ip_address": {"key": "properties.publicIPAddress", "type": "FrontendPropertiesIPAddress"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(
        self,
        *,
        location: str,
        tags: Optional[Dict[str, str]] = None,
        mode: Optional[Literal["public"]] = None,
        ip_address_version: Optional[Union[str, "_models.FrontendIPAddressVersion"]] = None,
        public_ip_address: Optional["_models.FrontendPropertiesIPAddress"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        :keyword mode: Frontend Mode (Optional). Default value is "public".
        :paramtype mode: str
        :keyword ip_address_version: Frontend IP Address Version (Optional). Known values are: "IPv4"
         and "IPv6".
        :paramtype ip_address_version: str or
         ~azure.mgmt.servicenetworking.models.FrontendIPAddressVersion
        :keyword public_ip_address: Frontend Public IP Address (Optional).
        :paramtype public_ip_address: ~azure.mgmt.servicenetworking.models.FrontendPropertiesIPAddress
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.mode = mode
        self.ip_address_version = ip_address_version
        self.public_ip_address = public_ip_address
        self.provisioning_state = None


class FrontendListResult(_serialization.Model):
    """The response of a Traffic Controller Frontend list operation.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The Frontend items on this page. Required.
    :vartype value: list[~azure.mgmt.servicenetworking.models.Frontend]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Frontend]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, *, value: List["_models.Frontend"], next_link: Optional[str] = None, **kwargs: Any) -> None:
        """
        :keyword value: The Frontend items on this page. Required.
        :paramtype value: list[~azure.mgmt.servicenetworking.models.Frontend]
        :keyword next_link: The link to the next page of items.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class FrontendPropertiesIPAddress(_serialization.Model):
    """Frontend IP Address.

    All required parameters must be populated in order to send to Azure.

    :ivar id: IP Address. Required.
    :vartype id: str
    """

    _validation = {
        "id": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, *, id: str, **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        """
        :keyword id: IP Address. Required.
        :paramtype id: str
        """
        super().__init__(**kwargs)
        self.id = id


class FrontendUpdate(_serialization.Model):
    """The type used for update operations of the Frontend.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar properties: The updatable properties of the Frontend.
    :vartype properties: ~azure.mgmt.servicenetworking.models.FrontendUpdateProperties
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "properties": {"key": "properties", "type": "FrontendUpdateProperties"},
    }

    def __init__(
        self,
        *,
        tags: Optional[Dict[str, str]] = None,
        properties: Optional["_models.FrontendUpdateProperties"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword properties: The updatable properties of the Frontend.
        :paramtype properties: ~azure.mgmt.servicenetworking.models.FrontendUpdateProperties
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.properties = properties


class FrontendUpdateProperties(_serialization.Model):
    """The updatable properties of the Frontend.

    :ivar mode: Frontend Mode (Optional). Default value is "public".
    :vartype mode: str
    :ivar ip_address_version: Frontend IP Address Type (Optional). Known values are: "IPv4" and
     "IPv6".
    :vartype ip_address_version: str or
     ~azure.mgmt.servicenetworking.models.FrontendIPAddressVersion
    :ivar public_ip_address: Frontend Public IP Address (Optional).
    :vartype public_ip_address: ~azure.mgmt.servicenetworking.models.FrontendPropertiesIPAddress
    """

    _attribute_map = {
        "mode": {"key": "mode", "type": "str"},
        "ip_address_version": {"key": "ipAddressVersion", "type": "str"},
        "public_ip_address": {"key": "publicIPAddress", "type": "FrontendPropertiesIPAddress"},
    }

    def __init__(
        self,
        *,
        mode: Optional[Literal["public"]] = None,
        ip_address_version: Optional[Union[str, "_models.FrontendIPAddressVersion"]] = None,
        public_ip_address: Optional["_models.FrontendPropertiesIPAddress"] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword mode: Frontend Mode (Optional). Default value is "public".
        :paramtype mode: str
        :keyword ip_address_version: Frontend IP Address Type (Optional). Known values are: "IPv4" and
         "IPv6".
        :paramtype ip_address_version: str or
         ~azure.mgmt.servicenetworking.models.FrontendIPAddressVersion
        :keyword public_ip_address: Frontend Public IP Address (Optional).
        :paramtype public_ip_address: ~azure.mgmt.servicenetworking.models.FrontendPropertiesIPAddress
        """
        super().__init__(**kwargs)
        self.mode = mode
        self.ip_address_version = ip_address_version
        self.public_ip_address = public_ip_address


class Operation(_serialization.Model):
    """Details of a REST API operation, returned from the Resource Provider Operations API.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar name: The name of the operation, as per Resource-Based Access Control (RBAC). Examples:
     "Microsoft.Compute/virtualMachines/write", "Microsoft.Compute/virtualMachines/capture/action".
    :vartype name: str
    :ivar is_data_action: Whether the operation applies to data-plane. This is "true" for
     data-plane operations and "false" for ARM/control-plane operations.
    :vartype is_data_action: bool
    :ivar display: Localized display information for this particular operation.
    :vartype display: ~azure.mgmt.servicenetworking.models.OperationDisplay
    :ivar origin: The intended executor of the operation; as in Resource Based Access Control
     (RBAC) and audit logs UX. Default value is "user,system". Known values are: "user", "system",
     and "user,system".
    :vartype origin: str or ~azure.mgmt.servicenetworking.models.Origin
    :ivar action_type: Enum. Indicates the action type. "Internal" refers to actions that are for
     internal only APIs. "Internal"
    :vartype action_type: str or ~azure.mgmt.servicenetworking.models.ActionType
    """

    _validation = {
        "name": {"readonly": True},
        "is_data_action": {"readonly": True},
        "origin": {"readonly": True},
        "action_type": {"readonly": True},
    }

    _attribute_map = {
        "name": {"key": "name", "type": "str"},
        "is_data_action": {"key": "isDataAction", "type": "bool"},
        "display": {"key": "display", "type": "OperationDisplay"},
        "origin": {"key": "origin", "type": "str"},
        "action_type": {"key": "actionType", "type": "str"},
    }

    def __init__(self, *, display: Optional["_models.OperationDisplay"] = None, **kwargs: Any) -> None:
        """
        :keyword display: Localized display information for this particular operation.
        :paramtype display: ~azure.mgmt.servicenetworking.models.OperationDisplay
        """
        super().__init__(**kwargs)
        self.name = None
        self.is_data_action = None
        self.display = display
        self.origin = None
        self.action_type = None


class OperationDisplay(_serialization.Model):
    """Localized display information for this particular operation.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar provider: The localized friendly form of the resource provider name, e.g. "Microsoft
     Monitoring Insights" or "Microsoft Compute".
    :vartype provider: str
    :ivar resource: The localized friendly name of the resource type related to this operation.
     E.g. "Virtual Machines" or "Job Schedule Collections".
    :vartype resource: str
    :ivar operation: The concise, localized friendly name for the operation; suitable for
     dropdowns. E.g. "Create or Update Virtual Machine", "Restart Virtual Machine".
    :vartype operation: str
    :ivar description: The short, localized friendly description of the operation; suitable for
     tool tips and detailed views.
    :vartype description: str
    """

    _validation = {
        "provider": {"readonly": True},
        "resource": {"readonly": True},
        "operation": {"readonly": True},
        "description": {"readonly": True},
    }

    _attribute_map = {
        "provider": {"key": "provider", "type": "str"},
        "resource": {"key": "resource", "type": "str"},
        "operation": {"key": "operation", "type": "str"},
        "description": {"key": "description", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.provider = None
        self.resource = None
        self.operation = None
        self.description = None


class OperationListResult(_serialization.Model):
    """A list of REST API operations supported by an Azure Resource Provider. It contains an URL link
    to get the next set of results.

    Variables are only populated by the server, and will be ignored when sending a request.

    :ivar value: List of operations supported by the resource provider.
    :vartype value: list[~azure.mgmt.servicenetworking.models.Operation]
    :ivar next_link: URL to get the next set of operation list results (if there are any).
    :vartype next_link: str
    """

    _validation = {
        "value": {"readonly": True},
        "next_link": {"readonly": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[Operation]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(self, **kwargs: Any) -> None:
        """ """
        super().__init__(**kwargs)
        self.value = None
        self.next_link = None


class ResourceID(_serialization.Model):
    """Resource ID definition used by parent to reference child resources.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Resource ID of child resource. Required.
    :vartype id: str
    """

    _validation = {
        "id": {"required": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
    }

    def __init__(self, *, id: str, **kwargs: Any) -> None:  # pylint: disable=redefined-builtin
        """
        :keyword id: Resource ID of child resource. Required.
        :paramtype id: str
        """
        super().__init__(**kwargs)
        self.id = id


class SystemData(_serialization.Model):
    """Metadata pertaining to creation and last modification of the resource.

    :ivar created_by: The identity that created the resource.
    :vartype created_by: str
    :ivar created_by_type: The type of identity that created the resource. Known values are:
     "User", "Application", "ManagedIdentity", and "Key".
    :vartype created_by_type: str or ~azure.mgmt.servicenetworking.models.CreatedByType
    :ivar created_at: The timestamp of resource creation (UTC).
    :vartype created_at: ~datetime.datetime
    :ivar last_modified_by: The identity that last modified the resource.
    :vartype last_modified_by: str
    :ivar last_modified_by_type: The type of identity that last modified the resource. Known values
     are: "User", "Application", "ManagedIdentity", and "Key".
    :vartype last_modified_by_type: str or ~azure.mgmt.servicenetworking.models.CreatedByType
    :ivar last_modified_at: The timestamp of resource last modification (UTC).
    :vartype last_modified_at: ~datetime.datetime
    """

    _attribute_map = {
        "created_by": {"key": "createdBy", "type": "str"},
        "created_by_type": {"key": "createdByType", "type": "str"},
        "created_at": {"key": "createdAt", "type": "iso-8601"},
        "last_modified_by": {"key": "lastModifiedBy", "type": "str"},
        "last_modified_by_type": {"key": "lastModifiedByType", "type": "str"},
        "last_modified_at": {"key": "lastModifiedAt", "type": "iso-8601"},
    }

    def __init__(
        self,
        *,
        created_by: Optional[str] = None,
        created_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        created_at: Optional[datetime.datetime] = None,
        last_modified_by: Optional[str] = None,
        last_modified_by_type: Optional[Union[str, "_models.CreatedByType"]] = None,
        last_modified_at: Optional[datetime.datetime] = None,
        **kwargs: Any
    ) -> None:
        """
        :keyword created_by: The identity that created the resource.
        :paramtype created_by: str
        :keyword created_by_type: The type of identity that created the resource. Known values are:
         "User", "Application", "ManagedIdentity", and "Key".
        :paramtype created_by_type: str or ~azure.mgmt.servicenetworking.models.CreatedByType
        :keyword created_at: The timestamp of resource creation (UTC).
        :paramtype created_at: ~datetime.datetime
        :keyword last_modified_by: The identity that last modified the resource.
        :paramtype last_modified_by: str
        :keyword last_modified_by_type: The type of identity that last modified the resource. Known
         values are: "User", "Application", "ManagedIdentity", and "Key".
        :paramtype last_modified_by_type: str or ~azure.mgmt.servicenetworking.models.CreatedByType
        :keyword last_modified_at: The timestamp of resource last modification (UTC).
        :paramtype last_modified_at: ~datetime.datetime
        """
        super().__init__(**kwargs)
        self.created_by = created_by
        self.created_by_type = created_by_type
        self.created_at = created_at
        self.last_modified_by = last_modified_by
        self.last_modified_by_type = last_modified_by_type
        self.last_modified_at = last_modified_at


class TrafficController(TrackedResource):
    """Concrete tracked resource types can be created by aliasing this type using a specific property
    type.

    Variables are only populated by the server, and will be ignored when sending a request.

    All required parameters must be populated in order to send to Azure.

    :ivar id: Fully qualified resource ID for the resource. Ex -
     /subscriptions/{subscriptionId}/resourceGroups/{resourceGroupName}/providers/{resourceProviderNamespace}/{resourceType}/{resourceName}.
    :vartype id: str
    :ivar name: The name of the resource.
    :vartype name: str
    :ivar type: The type of the resource. E.g. "Microsoft.Compute/virtualMachines" or
     "Microsoft.Storage/storageAccounts".
    :vartype type: str
    :ivar system_data: Azure Resource Manager metadata containing createdBy and modifiedBy
     information.
    :vartype system_data: ~azure.mgmt.servicenetworking.models.SystemData
    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar location: The geo-location where the resource lives. Required.
    :vartype location: str
    :ivar configuration_endpoints: Configuration Endpoints.
    :vartype configuration_endpoints: list[str]
    :ivar frontends: Frontends References List.
    :vartype frontends: list[~azure.mgmt.servicenetworking.models.ResourceID]
    :ivar associations: Associations References List.
    :vartype associations: list[~azure.mgmt.servicenetworking.models.ResourceID]
    :ivar provisioning_state: The status of the last operation. Known values are: "Succeeded",
     "Failed", "Canceled", "Provisioning", "Updating", "Deleting", and "Accepted".
    :vartype provisioning_state: str or ~azure.mgmt.servicenetworking.models.ProvisioningState
    """

    _validation = {
        "id": {"readonly": True},
        "name": {"readonly": True},
        "type": {"readonly": True},
        "system_data": {"readonly": True},
        "location": {"required": True},
        "configuration_endpoints": {"readonly": True},
        "frontends": {"readonly": True},
        "associations": {"readonly": True},
        "provisioning_state": {"readonly": True},
    }

    _attribute_map = {
        "id": {"key": "id", "type": "str"},
        "name": {"key": "name", "type": "str"},
        "type": {"key": "type", "type": "str"},
        "system_data": {"key": "systemData", "type": "SystemData"},
        "tags": {"key": "tags", "type": "{str}"},
        "location": {"key": "location", "type": "str"},
        "configuration_endpoints": {"key": "properties.configurationEndpoints", "type": "[str]"},
        "frontends": {"key": "properties.frontends", "type": "[ResourceID]"},
        "associations": {"key": "properties.associations", "type": "[ResourceID]"},
        "provisioning_state": {"key": "properties.provisioningState", "type": "str"},
    }

    def __init__(self, *, location: str, tags: Optional[Dict[str, str]] = None, **kwargs: Any) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword location: The geo-location where the resource lives. Required.
        :paramtype location: str
        """
        super().__init__(tags=tags, location=location, **kwargs)
        self.configuration_endpoints = None
        self.frontends = None
        self.associations = None
        self.provisioning_state = None


class TrafficControllerListResult(_serialization.Model):
    """The response of a TrafficController list operation.

    All required parameters must be populated in order to send to Azure.

    :ivar value: The TrafficController items on this page. Required.
    :vartype value: list[~azure.mgmt.servicenetworking.models.TrafficController]
    :ivar next_link: The link to the next page of items.
    :vartype next_link: str
    """

    _validation = {
        "value": {"required": True},
    }

    _attribute_map = {
        "value": {"key": "value", "type": "[TrafficController]"},
        "next_link": {"key": "nextLink", "type": "str"},
    }

    def __init__(
        self, *, value: List["_models.TrafficController"], next_link: Optional[str] = None, **kwargs: Any
    ) -> None:
        """
        :keyword value: The TrafficController items on this page. Required.
        :paramtype value: list[~azure.mgmt.servicenetworking.models.TrafficController]
        :keyword next_link: The link to the next page of items.
        :paramtype next_link: str
        """
        super().__init__(**kwargs)
        self.value = value
        self.next_link = next_link


class TrafficControllerUpdate(_serialization.Model):
    """The type used for update operations of the TrafficController.

    :ivar tags: Resource tags.
    :vartype tags: dict[str, str]
    :ivar properties: The updatable properties of the TrafficController.
    :vartype properties: JSON
    """

    _attribute_map = {
        "tags": {"key": "tags", "type": "{str}"},
        "properties": {"key": "properties", "type": "object"},
    }

    def __init__(
        self, *, tags: Optional[Dict[str, str]] = None, properties: Optional[JSON] = None, **kwargs: Any
    ) -> None:
        """
        :keyword tags: Resource tags.
        :paramtype tags: dict[str, str]
        :keyword properties: The updatable properties of the TrafficController.
        :paramtype properties: JSON
        """
        super().__init__(**kwargs)
        self.tags = tags
        self.properties = properties
