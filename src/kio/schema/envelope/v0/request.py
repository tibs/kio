"""
Generated from EnvelopeRequest.json.
"""

# ruff: noqa: A003

from dataclasses import dataclass
from dataclasses import field
from typing import ClassVar

from kio.schema.primitive import i16
from kio.schema.request_header.v2.header import RequestHeader


@dataclass(frozen=True, slots=True, kw_only=True)
class EnvelopeRequest:
    __version__: ClassVar[i16] = i16(0)
    __flexible__: ClassVar[bool] = True
    __api_key__: ClassVar[i16] = i16(58)
    __header_schema__: ClassVar[type[RequestHeader]] = RequestHeader
    request_data: bytes = field(metadata={"kafka_type": "bytes"})
    """The embedded request header and data."""
    request_principal: bytes | None = field(metadata={"kafka_type": "bytes"})
    """Value of the initial client principal when the request is redirected by a broker."""
    client_host_address: bytes = field(metadata={"kafka_type": "bytes"})
    """The original client's address in bytes."""
