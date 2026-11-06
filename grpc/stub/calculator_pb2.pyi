from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Optional as _Optional

DESCRIPTOR: _descriptor.FileDescriptor

class CalcRequest(_message.Message):
    __slots__ = ("a", "b")
    A_FIELD_NUMBER: _ClassVar[int]
    B_FIELD_NUMBER: _ClassVar[int]
    a: float
    b: float
    def __init__(self, a: _Optional[float] = ..., b: _Optional[float] = ...) -> None: ...

class CalcResponse(_message.Message):
    __slots__ = ("ans",)
    ANS_FIELD_NUMBER: _ClassVar[int]
    ans: float
    def __init__(self, ans: _Optional[float] = ...) -> None: ...
