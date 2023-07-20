# Copyright DB Netz AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

import attr

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.projects_list_get_response_data_item import (
        ProjectsListGetResponseDataItem,
    )
    from ..models.projects_list_get_response_included_item import (
        ProjectsListGetResponseIncludedItem,
    )
    from ..models.projects_list_get_response_links import (
        ProjectsListGetResponseLinks,
    )
    from ..models.projects_list_get_response_meta import (
        ProjectsListGetResponseMeta,
    )


T = TypeVar("T", bound="ProjectsListGetResponse")


@attr.s(auto_attribs=True)
class ProjectsListGetResponse:
    """
    Attributes:
        meta (Union[Unset, ProjectsListGetResponseMeta]):
        data (Union[Unset, List['ProjectsListGetResponseDataItem']]):
        included (Union[Unset, List['ProjectsListGetResponseIncludedItem']]): Related entities might be returned, see <a
            href="https://docs.sw.siemens.com/en-US/doc/230235217/PL20221020258116340.xid2134849/xid2134871">Rest API User
            Guide</a>.
        links (Union[Unset, ProjectsListGetResponseLinks]):
    """

    meta: Union[Unset, "ProjectsListGetResponseMeta"] = UNSET
    data: Union[Unset, List["ProjectsListGetResponseDataItem"]] = UNSET
    included: Union[Unset, List["ProjectsListGetResponseIncludedItem"]] = UNSET
    links: Union[Unset, "ProjectsListGetResponseLinks"] = UNSET
    additional_properties: Dict[str, Any] = attr.ib(init=False, factory=dict)

    def to_dict(self) -> Dict[str, Any]:
        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        data: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.data, Unset):
            data = []
            for data_item_data in self.data:
                data_item = data_item_data.to_dict()

                data.append(data_item)

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
        if meta is not UNSET:
            field_dict["meta"] = meta
        if data is not UNSET:
            field_dict["data"] = data
        if included is not UNSET:
            field_dict["included"] = included
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.projects_list_get_response_data_item import (
            ProjectsListGetResponseDataItem,
        )
        from ..models.projects_list_get_response_included_item import (
            ProjectsListGetResponseIncludedItem,
        )
        from ..models.projects_list_get_response_links import (
            ProjectsListGetResponseLinks,
        )
        from ..models.projects_list_get_response_meta import (
            ProjectsListGetResponseMeta,
        )

        d = src_dict.copy()
        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, ProjectsListGetResponseMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = ProjectsListGetResponseMeta.from_dict(_meta)

        data = []
        _data = d.pop("data", UNSET)
        for data_item_data in _data or []:
            data_item = ProjectsListGetResponseDataItem.from_dict(
                data_item_data
            )

            data.append(data_item)

        included = []
        _included = d.pop("included", UNSET)
        for included_item_data in _included or []:
            included_item = ProjectsListGetResponseIncludedItem.from_dict(
                included_item_data
            )

            included.append(included_item)

        _links = d.pop("links", UNSET)
        links: Union[Unset, ProjectsListGetResponseLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = ProjectsListGetResponseLinks.from_dict(_links)

        projects_list_get_response = cls(
            meta=meta,
            data=data,
            included=included,
            links=links,
        )

        projects_list_get_response.additional_properties = d
        return projects_list_get_response

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
