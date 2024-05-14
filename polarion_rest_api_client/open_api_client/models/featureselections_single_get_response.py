# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.featureselections_single_get_response_data import (
        FeatureselectionsSingleGetResponseData,
    )
    from ..models.featureselections_single_get_response_included_item import (
        FeatureselectionsSingleGetResponseIncludedItem,
    )
    from ..models.featureselections_single_get_response_links import (
        FeatureselectionsSingleGetResponseLinks,
    )


T = TypeVar("T", bound="FeatureselectionsSingleGetResponse")


@_attrs_define
class FeatureselectionsSingleGetResponse:
    """
    Attributes:
        data (Union[Unset, FeatureselectionsSingleGetResponseData]):
        included (Union[Unset, List['FeatureselectionsSingleGetResponseIncludedItem']]): Related entities might be
            returned, see <a href="https://docs.sw.siemens.com/en-
            US/doc/230235217/PL20231017526942799.polarion_help_sc.xid2134849/xid2134871" target="_blank">REST API User
            Guide</a>.
        links (Union[Unset, FeatureselectionsSingleGetResponseLinks]):
    """

    data: Union[Unset, "FeatureselectionsSingleGetResponseData"] = UNSET
    included: Union[
        Unset, List["FeatureselectionsSingleGetResponseIncludedItem"]
    ] = UNSET
    links: Union[Unset, "FeatureselectionsSingleGetResponseLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        data: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.data, Unset):
            data = self.data.to_dict()

        included: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.included, Unset):
            included = []
            for included_item_data in self.included:
                included_item = included_item_data.to_dict()
                included.append(included_item)

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.featureselections_single_get_response_data import (
            FeatureselectionsSingleGetResponseData,
        )
        from ..models.featureselections_single_get_response_included_item import (
            FeatureselectionsSingleGetResponseIncludedItem,
        )
        from ..models.featureselections_single_get_response_links import (
            FeatureselectionsSingleGetResponseLinks,
        )

        d = src_dict.copy()
        _data = d.pop("data", UNSET)
        data: Union[Unset, FeatureselectionsSingleGetResponseData]
        if isinstance(_data, Unset):
            data = UNSET
        else:
            data = FeatureselectionsSingleGetResponseData.from_dict(_data)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = (
                FeatureselectionsSingleGetResponseIncludedItem.from_dict(
                    included_item_data
                )
            )

            included.append(included_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, FeatureselectionsSingleGetResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = FeatureselectionsSingleGetResponseLinks.from_dict(_links)

        featureselections_single_get_response_obj = cls(
            data=data,
            included=included,
            links=links,
        )

        featureselections_single_get_response_obj.additional_properties = d
        return featureselections_single_get_response_obj

    @property
    def additional_keys(self) -> List[str]:
        return list(self.additional_properties.keys())

    def __getitem__(self, key: str) -> Any:
        return self.additional_properties[key]

    def __setitem__(self, key: str, value: Any) -> None:
        self.additional_properties[key] = value

    def __delitem__(self, key: str) -> None:
        del self.additional_properties[key]

    def __contains__(self, key: str) -> bool:
        return key in self.additional_properties
