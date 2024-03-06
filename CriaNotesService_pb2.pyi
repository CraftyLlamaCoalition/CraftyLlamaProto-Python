from google.protobuf.internal import containers as _containers
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from typing import ClassVar as _ClassVar, Iterable as _Iterable, Mapping as _Mapping, Optional as _Optional, Union as _Union

DESCRIPTOR: _descriptor.FileDescriptor

class NewNoteRequest(_message.Message):
    __slots__ = ("user_id", "content")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    content: str
    def __init__(self, user_id: _Optional[str] = ..., content: _Optional[str] = ...) -> None: ...

class NoteRequest(_message.Message):
    __slots__ = ("user_id", "note_id")
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    NOTE_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    note_id: str
    def __init__(self, user_id: _Optional[str] = ..., note_id: _Optional[str] = ...) -> None: ...

class NoteContent(_message.Message):
    __slots__ = ("content",)
    CONTENT_FIELD_NUMBER: _ClassVar[int]
    content: str
    def __init__(self, content: _Optional[str] = ...) -> None: ...

class MultipleNotes(_message.Message):
    __slots__ = ("notes",)
    NOTES_FIELD_NUMBER: _ClassVar[int]
    notes: _containers.RepeatedCompositeFieldContainer[NoteContent]
    def __init__(self, notes: _Optional[_Iterable[_Union[NoteContent, _Mapping]]] = ...) -> None: ...

class User(_message.Message):
    __slots__ = ("user_id",)
    USER_ID_FIELD_NUMBER: _ClassVar[int]
    user_id: str
    def __init__(self, user_id: _Optional[str] = ...) -> None: ...

class Status(_message.Message):
    __slots__ = ("success",)
    SUCCESS_FIELD_NUMBER: _ClassVar[int]
    success: bool
    def __init__(self, success: bool = ...) -> None: ...
