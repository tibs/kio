"""
Generated from ListOffsetsResponse.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.response_header.v1.header import ResponseHeader
from kio.schema.types import TopicName
from kio.static.constants import ErrorCode
from kio.static.primitive import i16
from kio.static.primitive import i32
from kio.static.primitive import i32Timedelta
from kio.static.primitive import i64


@dataclass(frozen=True, slots=True, kw_only=True)
class ListOffsetsPartitionResponse:
    __version__: ClassVar[i16] = i16(8)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(2)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    partition_index: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    error_code: ErrorCode = field(metadata={"kafka_type": "error_code"})
    """The partition error code, or 0 if there was no error."""
    timestamp: i64 = field(metadata={"kafka_type": "int64"}, default=i64(-1))
    """The timestamp associated with the returned offset."""
    offset: i64 = field(metadata={"kafka_type": "int64"}, default=i64(-1))
    """The returned offset."""
    leader_epoch: i32 = field(metadata={"kafka_type": "int32"}, default=i32(-1))


@dataclass(frozen=True, slots=True, kw_only=True)
class ListOffsetsTopicResponse:
    __version__: ClassVar[i16] = i16(8)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(2)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    name: TopicName = field(metadata={"kafka_type": "string"})
    """The topic name"""
    partitions: tuple[ListOffsetsPartitionResponse, ...]
    """Each partition in the response."""


@dataclass(frozen=True, slots=True, kw_only=True)
class ListOffsetsResponse:
    __version__: ClassVar[i16] = i16(8)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(2)
    __header_schema__: ClassVar[type[ResponseHeader]] = ResponseHeader
    throttle_time: i32Timedelta = field(metadata={"kafka_type": "timedelta_i32"})
    """The duration in milliseconds for which the request was throttled due to a quota violation, or zero if the request did not violate any quota."""
    topics: tuple[ListOffsetsTopicResponse, ...]
    """Each topic in the response."""