"""
Generated from WriteTxnMarkersResponse.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32
from kio.schema.response_header.v1.header import ResponseHeader
from kio.schema.types import ProducerId
from kio.schema.types import TopicName


@dataclass(frozen=True, slots=True, kw_only=True)
class WritableTxnMarkerPartitionResult:
    __version__: ClassVar[i16] = i16(1)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(27)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    partition_index: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    error_code: i16 = field(metadata={"kafka_type": "int16"})
    """The error code, or 0 if there was no error."""


@dataclass(frozen=True, slots=True, kw_only=True)
class WritableTxnMarkerTopicResult:
    __version__: ClassVar[i16] = i16(1)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(27)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name."""
    partitions: tuple[WritableTxnMarkerPartitionResult, ...]
    """The results by partition."""


@dataclass(frozen=True, slots=True, kw_only=True)
class WritableTxnMarkerResult:
    __version__: ClassVar[i16] = i16(1)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(27)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    producer_id: ProducerId = field(metadata={"kafka_type": "int64"})
    """The current producer ID in use by the transactional ID."""
    topics: tuple[WritableTxnMarkerTopicResult, ...]
    """The results by topic."""


@dataclass(frozen=True, slots=True, kw_only=True)
class WriteTxnMarkersResponse:
    __version__: ClassVar[i16] = i16(1)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(27)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    markers: tuple[WritableTxnMarkerResult, ...]
    """The results for writing makers."""
