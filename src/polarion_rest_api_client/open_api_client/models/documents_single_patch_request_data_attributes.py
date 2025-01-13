# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0

from typing import TYPE_CHECKING, Any, Dict, List, Type, TypeVar, Union

from attrs import define as _attrs_define
from attrs import field as _attrs_field

from ..types import UNSET, Unset

if TYPE_CHECKING:
    from ..models.documents_single_patch_request_data_attributes_home_page_content import (
        DocumentsSinglePatchRequestDataAttributesHomePageContent,
    )
    from ..models.documents_single_patch_request_data_attributes_outline_numbering import (
        DocumentsSinglePatchRequestDataAttributesOutlineNumbering,
    )
    from ..models.documents_single_patch_request_data_attributes_rendering_layouts_item import (
        DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem,
    )


T = TypeVar("T", bound="DocumentsSinglePatchRequestDataAttributes")


@_attrs_define
class DocumentsSinglePatchRequestDataAttributes:
    """
    Attributes:
        auto_suspect (Union[Unset, bool]):
        home_page_content (Union[Unset, DocumentsSinglePatchRequestDataAttributesHomePageContent]):
        outline_numbering (Union[Unset, DocumentsSinglePatchRequestDataAttributesOutlineNumbering]):
        rendering_layouts (Union[Unset, List['DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem']]):
        status (Union[Unset, str]):  Example: draft.
        title (Union[Unset, str]):  Example: Title.
        type (Union[Unset, str]):  Example: req_specification.
        uses_outline_numbering (Union[Unset, bool]):
    """

    auto_suspect: Union[Unset, bool] = UNSET
    home_page_content: Union[
        Unset, "DocumentsSinglePatchRequestDataAttributesHomePageContent"
    ] = UNSET
    outline_numbering: Union[
        Unset, "DocumentsSinglePatchRequestDataAttributesOutlineNumbering"
    ] = UNSET
    rendering_layouts: Union[
        Unset,
        List["DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem"],
    ] = UNSET
    status: Union[Unset, str] = UNSET
    title: Union[Unset, str] = UNSET
    type: Union[Unset, str] = UNSET
    uses_outline_numbering: Union[Unset, bool] = UNSET
    additional_properties: Dict[str, Any] = _attrs_field(
        init=False, factory=dict
    )

    def to_dict(self) -> Dict[str, Any]:
        auto_suspect = self.auto_suspect

        home_page_content: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.home_page_content, Unset):
            home_page_content = self.home_page_content.to_dict()

        outline_numbering: Union[Unset, Dict[str, Any]] = UNSET
        if not isinstance(self.outline_numbering, Unset):
            outline_numbering = self.outline_numbering.to_dict()

        rendering_layouts: Union[Unset, List[Dict[str, Any]]] = UNSET
        if not isinstance(self.rendering_layouts, Unset):
            rendering_layouts = []
            for rendering_layouts_item_data in self.rendering_layouts:
                rendering_layouts_item = rendering_layouts_item_data.to_dict()
                rendering_layouts.append(rendering_layouts_item)

        status = self.status

        title = self.title

        type = self.type

        uses_outline_numbering = self.uses_outline_numbering

        field_dict: Dict[str, Any] = {}
        field_dict.update(self.additional_properties)
        field_dict.update({})
        if auto_suspect is not UNSET:
            field_dict["autoSuspect"] = auto_suspect
        if home_page_content is not UNSET:
            field_dict["homePageContent"] = home_page_content
        if outline_numbering is not UNSET:
            field_dict["outlineNumbering"] = outline_numbering
        if rendering_layouts is not UNSET:
            field_dict["renderingLayouts"] = rendering_layouts
        if status is not UNSET:
            field_dict["status"] = status
        if title is not UNSET:
            field_dict["title"] = title
        if type is not UNSET:
            field_dict["type"] = type
        if uses_outline_numbering is not UNSET:
            field_dict["usesOutlineNumbering"] = uses_outline_numbering

        return field_dict

    @classmethod
    def from_dict(cls: Type[T], src_dict: Dict[str, Any]) -> T:
        from ..models.documents_single_patch_request_data_attributes_home_page_content import (
            DocumentsSinglePatchRequestDataAttributesHomePageContent,
        )
        from ..models.documents_single_patch_request_data_attributes_outline_numbering import (
            DocumentsSinglePatchRequestDataAttributesOutlineNumbering,
        )
        from ..models.documents_single_patch_request_data_attributes_rendering_layouts_item import (
            DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem,
        )

        d = src_dict.copy()
        auto_suspect = d.pop("autoSuspect", UNSET)

        _home_page_content = d.pop("homePageContent", UNSET)
        home_page_content: Union[
            Unset, DocumentsSinglePatchRequestDataAttributesHomePageContent
        ]
        if isinstance(_home_page_content, Unset):
            home_page_content = UNSET
        else:
            home_page_content = DocumentsSinglePatchRequestDataAttributesHomePageContent.from_dict(
                _home_page_content
            )

        _outline_numbering = d.pop("outlineNumbering", UNSET)
        outline_numbering: Union[
            Unset, DocumentsSinglePatchRequestDataAttributesOutlineNumbering
        ]
        if isinstance(_outline_numbering, Unset):
            outline_numbering = UNSET
        else:
            outline_numbering = DocumentsSinglePatchRequestDataAttributesOutlineNumbering.from_dict(
                _outline_numbering
            )

        rendering_layouts = []
        _rendering_layouts = d.pop("renderingLayouts", UNSET)
        for rendering_layouts_item_data in _rendering_layouts or []:
            rendering_layouts_item = DocumentsSinglePatchRequestDataAttributesRenderingLayoutsItem.from_dict(
                rendering_layouts_item_data
            )

            rendering_layouts.append(rendering_layouts_item)

        status = d.pop("status", UNSET)

        title = d.pop("title", UNSET)

        type = d.pop("type", UNSET)

        uses_outline_numbering = d.pop("usesOutlineNumbering", UNSET)

        documents_single_patch_request_data_attributes_obj = cls(
            auto_suspect=auto_suspect,
            home_page_content=home_page_content,
            outline_numbering=outline_numbering,
            rendering_layouts=rendering_layouts,
            status=status,
            title=title,
            type=type,
            uses_outline_numbering=uses_outline_numbering,
        )

        documents_single_patch_request_data_attributes_obj.additional_properties = (
            d
        )
        return documents_single_patch_request_data_attributes_obj

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
