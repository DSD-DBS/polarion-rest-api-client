# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..models.testrun_comments_list_get_response_data_item_type import (
    TestrunCommentsListGetResponseDataItemType,
)
from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.testrun_comments_list_get_response_data_item_attributes import (
        TestrunCommentsListGetResponseDataItemAttributes,
    )
    from ..models.testrun_comments_list_get_response_data_item_links import (
        TestrunCommentsListGetResponseDataItemLinks,
    )
    from ..models.testrun_comments_list_get_response_data_item_meta import (
        TestrunCommentsListGetResponseDataItemMeta,
    )
    from ..models.testrun_comments_list_get_response_data_item_relationships import (
        TestrunCommentsListGetResponseDataItemRelationships,
    )


T = TypeVar("T", bound="TestrunCommentsListGetResponseDataItem")


@_attrs_define
class TestrunCommentsListGetResponseDataItem:
    """
    Attributes:
        type (Union[Unset, TestrunCommentsListGetResponseDataItemType]):
        id (Union[Unset, str]):  Example: MyProjectId/MyTestRunId/MyCommentId.
        revision (Union[Unset, str]):  Example: 1234.
        attributes (Union[Unset, TestrunCommentsListGetResponseDataItemAttributes]):
        relationships (Union[Unset, TestrunCommentsListGetResponseDataItemRelationships]):
        meta (Union[Unset, TestrunCommentsListGetResponseDataItemMeta]):
        links (Union[Unset, TestrunCommentsListGetResponseDataItemLinks]):
    """

    type: Union[Unset, TestrunCommentsListGetResponseDataItemType] = UNSET
    id: Union[Unset, str] = UNSET
    revision: Union[Unset, str] = UNSET
    attributes: Union[
        Unset, "TestrunCommentsListGetResponseDataItemAttributes"
    ] = UNSET
    relationships: Union[
        Unset, "TestrunCommentsListGetResponseDataItemRelationships"
    ] = UNSET
    meta: Union[Unset, "TestrunCommentsListGetResponseDataItemMeta"] = UNSET
    links: Union[Unset, "TestrunCommentsListGetResponseDataItemLinks"] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        type: Union[Unset, str] = UNSET
        if not isinstance(self.type, Unset):
            type = self.type.value

        id = self.id

        revision = self.revision

        attributes: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.attributes, Unset):
            attributes = self.attributes.to_dict()

        relationships: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.relationships, Unset):
            relationships = self.relationships.to_dict()

        meta: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.meta, Unset):
            meta = self.meta.to_dict()

        links: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.links, Unset):
            links = self.links.to_dict()

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if type is not UNSET:
            field_dict["type"] = type
        if id is not UNSET:
            field_dict["id"] = id
        if revision is not UNSET:
            field_dict["revision"] = revision
        if attributes is not UNSET:
            field_dict["attributes"] = attributes
        if relationships is not UNSET:
            field_dict["relationships"] = relationships
        if meta is not UNSET:
            field_dict["meta"] = meta
        if links is not UNSET:
            field_dict["links"] = links

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.testrun_comments_list_get_response_data_item_attributes import (
            TestrunCommentsListGetResponseDataItemAttributes,
        )
        from ..models.testrun_comments_list_get_response_data_item_links import (
            TestrunCommentsListGetResponseDataItemLinks,
        )
        from ..models.testrun_comments_list_get_response_data_item_meta import (
            TestrunCommentsListGetResponseDataItemMeta,
        )
        from ..models.testrun_comments_list_get_response_data_item_relationships import (
            TestrunCommentsListGetResponseDataItemRelationships,
        )

        d = src_dict.copy()
        _type = d.pop("type", UNSET)
        type: Union[Unset, TestrunCommentsListGetResponseDataItemType]
        if isinstance(_type, Unset):
            type = UNSET
        else:
            type = TestrunCommentsListGetResponseDataItemType(_type)

        id = d.pop("id", UNSET)

        revision = d.pop("revision", UNSET)

        _attributes = d.pop("attributes", UNSET)
        attributes: Union[
            Unset, TestrunCommentsListGetResponseDataItemAttributes
        ]
        if isinstance(_attributes, Unset):
            attributes = UNSET
        else:
            attributes = (
                TestrunCommentsListGetResponseDataItemAttributes.from_dict(
                    _attributes
                )
            )

        _relationships = d.pop("relationships", UNSET)
        relationships: Union[
            Unset, TestrunCommentsListGetResponseDataItemRelationships
        ]
        if isinstance(_relationships, Unset):
            relationships = UNSET
        else:
            relationships = (
                TestrunCommentsListGetResponseDataItemRelationships.from_dict(
                    _relationships
                )
            )

        _meta = d.pop("meta", UNSET)
        meta: Union[Unset, TestrunCommentsListGetResponseDataItemMeta]
        if isinstance(_meta, Unset):
            meta = UNSET
        else:
            meta = TestrunCommentsListGetResponseDataItemMeta.from_dict(_meta)

        _links = d.pop("links", UNSET)
        links: Union[Unset, TestrunCommentsListGetResponseDataItemLinks]
        if isinstance(_links, Unset):
            links = UNSET
        else:
            links = TestrunCommentsListGetResponseDataItemLinks.from_dict(
                _links
            )

        testrun_comments_list_get_response_data_item_obj = cls(
            type=type,
            id=id,
            revision=revision,
            attributes=attributes,
            relationships=relationships,
            meta=meta,
            links=links,
        )

        testrun_comments_list_get_response_data_item_obj.additional_properties = (
            d
        )
        return testrun_comments_list_get_response_data_item_obj

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