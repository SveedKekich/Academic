from typing import Generic, TypeVar, List, Protocol

T = TypeVar("T")


class HasId(Protocol):
    id: str


class BaseRepository(Generic[T]):

    def get_all(self) -> List[T]:
        raise NotImplementedError

    def get_by_id(self, entity_id: str) -> T:
        raise NotImplementedError

    def add(self, entity: T) -> None:
        raise NotImplementedError

    def update(self, entity: T) -> None:
        raise NotImplementedError

    def delete(self, entity_id: str) -> None:
        raise NotImplementedError
