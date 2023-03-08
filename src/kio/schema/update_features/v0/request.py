"""
Generated from UpdateFeaturesRequest.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.primitive import i32
from kio.schema.request_header.v2.header import RequestHeader


@dataclass(frozen=True, slots=True, kw_only=True)
class FeatureUpdateKey:
    __version__: ClassVar[i16] = i16(0)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(57)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    feature: str = field(metadata={"kafka_type": "string"})
    """The name of the finalized feature to be updated."""
    max_version_level: i16 = field(metadata={"kafka_type": "int16"})
    """The new maximum version level for the finalized feature. A value >= 1 is valid. A value < 1, is special, and can be used to request the deletion of the finalized feature."""
    allow_downgrade: bool = field(metadata={"kafka_type": "bool"})
    """DEPRECATED in version 1 (see DowngradeType). When set to true, the finalized feature version level is allowed to be downgraded/deleted. The downgrade request will fail if the new maximum version level is a value that's not lower than the existing maximum finalized version level."""


@dataclass(frozen=True, slots=True, kw_only=True)
class UpdateFeaturesRequest:
    __version__: ClassVar[i16] = i16(0)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(57)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    timeout_ms: i32 = field(metadata={"kafka_type": "int32"}, default=i32(60000))
    """How long to wait in milliseconds before timing out the request."""
    feature_updates: tuple[FeatureUpdateKey, ...]
    """The list of updates to finalized features."""
