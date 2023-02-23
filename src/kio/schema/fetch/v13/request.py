"""
Generated from FetchRequest.json.
"""
import uuid
from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i8
from kio.schema.primitive import i32
from kio.schema.primitive import i64
from kio.schema.types import BrokerId


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchPartition:
    __flexible__: ClassVar[bool] = True
    partition: i32 = field(metadata={"kafka_type": "int32"})
    """The partition index."""
    current_leader_epoch: i32 = field(metadata={"kafka_type": "int32"}, default=i32(-1))
    """The current leader epoch of the partition."""
    fetch_offset: i64 = field(metadata={"kafka_type": "int64"})
    """The message offset."""
    last_fetched_epoch: i32 = field(metadata={"kafka_type": "int32"}, default=i32(-1))
    """The epoch of the last fetched record or -1 if there is none"""
    log_start_offset: i64 = field(metadata={"kafka_type": "int64"}, default=i64(-1))
    """The earliest available offset of the follower replica.  The field is only used when the request is sent by the follower."""
    partition_max_bytes: i32 = field(metadata={"kafka_type": "int32"})
    """The maximum bytes to fetch from this partition.  See KIP-74 for cases where this limit may not be honored."""


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchTopic:
    __flexible__: ClassVar[bool] = True
    topic_id: uuid.UUID = field(metadata={"kafka_type": "uuid"})
    """The unique topic ID"""
    partitions: tuple[FetchPartition, ...]
    """The partitions to fetch."""


@dataclass(frozen=True, slots=True, kw_only=True)
class ForgottenTopic:
    __flexible__: ClassVar[bool] = True
    topic_id: uuid.UUID = field(metadata={"kafka_type": "uuid"})
    """The unique topic ID"""
    partitions: tuple[i32, ...] = field(metadata={"kafka_type": "int32"}, default=())
    """The partitions indexes to forget."""


@dataclass(frozen=True, slots=True, kw_only=True)
class FetchRequest:
    __flexible__: ClassVar[bool] = True
    cluster_id: str | None = field(metadata={"kafka_type": "string"}, default=None)
    """The clusterId if known. This is used to validate metadata fetches prior to broker registration."""
    replica_id: BrokerId = field(metadata={"kafka_type": "int32"})
    """The broker ID of the follower, of -1 if this request is from a consumer."""
    max_wait_ms: i32 = field(metadata={"kafka_type": "int32"})
    """The maximum time in milliseconds to wait for the response."""
    min_bytes: i32 = field(metadata={"kafka_type": "int32"})
    """The minimum bytes to accumulate in the response."""
    max_bytes: i32 = field(metadata={"kafka_type": "int32"}, default=i32(2147483647))
    """The maximum bytes to fetch.  See KIP-74 for cases where this limit may not be honored."""
    isolation_level: i8 = field(metadata={"kafka_type": "int8"}, default=i8(0))
    """This setting controls the visibility of transactional records. Using READ_UNCOMMITTED (isolation_level = 0) makes all records visible. With READ_COMMITTED (isolation_level = 1), non-transactional and COMMITTED transactional records are visible. To be more concrete, READ_COMMITTED returns all data from offsets smaller than the current LSO (last stable offset), and enables the inclusion of the list of aborted transactions in the result, which allows consumers to discard ABORTED transactional records"""
    session_id: i32 = field(metadata={"kafka_type": "int32"}, default=i32(0))
    """The fetch session ID."""
    session_epoch: i32 = field(metadata={"kafka_type": "int32"}, default=i32(-1))
    """The fetch session epoch, which is used for ordering requests in a session."""
    topics: tuple[FetchTopic, ...]
    """The topics to fetch."""
    forgotten_topics_data: tuple[ForgottenTopic, ...]
    """In an incremental fetch request, the partitions to remove."""
    rack_id: str = field(metadata={"kafka_type": "string"}, default="")
    """Rack ID of the consumer making this request"""