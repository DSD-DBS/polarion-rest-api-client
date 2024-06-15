# Copyright DB InfraGO AG and contributors
# SPDX-License-Identifier: Apache-2.0
"""Implementation of the documents client."""
import urllib.parse

from polarion_rest_api_client import data_models as dm
from polarion_rest_api_client.open_api_client import models as api_models
from polarion_rest_api_client.open_api_client import types as oa_types
from polarion_rest_api_client.open_api_client.api.documents import get_document

from . import base_classes as bc


class Documents(bc.UpdatableItemsClient[dm.Document]):
    """A client to work with documents in Polarion."""

    def get(
        self,
        space_id: str,
        document_name: str,
        fields: dict[str, str] | None = None,
        include: str | None | oa_types.Unset = None,
        revision: str | None | oa_types.Unset = None,
    ) -> dm.Document | None:
        """Return the document with the given document_name and space_id."""
        if include is None:
            include = oa_types.UNSET

        if revision is None:
            revision = oa_types.UNSET

        if " " in space_id or " " in document_name:
            space_id = urllib.parse.quote(
                space_id, safe="/", encoding=None, errors=None
            )
            document_name = urllib.parse.quote(
                document_name, safe="/", encoding=None, errors=None
            )
        if fields is None:
            fields = self._client.default_fields.documents

        sparse_fields = self._build_sparse_fields(fields)
        response = get_document.sync_detailed(
            self._project_id,
            space_id,
            document_name,
            client=self._client.client,
            fields=sparse_fields,
            include=include,
            revision=revision,
        )

        self._raise_on_error(response)

        document_response = response.parsed

        if isinstance(
            document_response, api_models.DocumentsSingleGetResponse
        ) and (data := document_response.data):
            if not getattr(data.meta, "errors", []):
                assert (attributes := data.attributes)
                assert isinstance(data.id, str)
                home_page_content = self._handle_text_content(
                    attributes.home_page_content
                )

                return dm.Document(
                    id=data.id,
                    module_folder=self.unset_to_none(attributes.module_folder),
                    module_name=self.unset_to_none(attributes.module_name),
                    type=self.unset_to_none(attributes.type),
                    status=self.unset_to_none(attributes.status),
                    home_page_content=home_page_content,
                )
        return None

    def _update(self, to_update: dm.Document | list[dm.Document]):
        raise NotImplementedError

    def get_multi(
        self, *args, page_size=100, page_number=1, **kwargs
    ) -> tuple[list[dm.Document], bool]:
        """Return a list of documents - Not implemented yet."""
        raise NotImplementedError

    def _create(self, items: dm.Document | list[dm.Document]):
        raise NotImplementedError

    def _delete(self, items: dm.Document | list[dm.Document]):
        raise NotImplementedError
