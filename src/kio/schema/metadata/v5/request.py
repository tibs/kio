"""
Generated from MetadataRequest.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.request_header.v1.header import RequestHeader
from kio.schema.types import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataRequestTopic:
    __version__: ClassVar[i16] = i16(5)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(3)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""


@dataclass(frozen=True, slots=True, kw_only=True)
class MetadataRequest:
    __version__: ClassVar[i16] = i16(5)
    __flexible__: ClassVar[bool] = False
    __api_key__: ClassVar[i16] = i16(3)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    topics: tuple[MetadataRequestTopic, ...]
    """The topics to fetch metadata for."""
    allow_auto_topic_creation: bool = field(
        metadata={"kafka_type": "bool"}, default=True
    )
    """If this is true, the broker may auto-create topics that we requested which do not already exist, if it is configured to do so."""
