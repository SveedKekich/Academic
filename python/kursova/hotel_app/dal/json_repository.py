import json
from dataclasses import asdict, is_dataclass
from datetime import date, datetime
from pathlib import Path
from typing import Generic, TypeVar, List, Type, Optional, Any

from .base_repository import BaseRepository, HasId

T = TypeVar("T", bound=HasId)


class JsonRepository(BaseRepository[T], Generic[T]):

    def __init__(self, filename: str, model_cls: Type[T]):
        self._path = Path(filename)
        self._model_cls: Type[T] = model_cls

        if not self._path.parent.exists():
            self._path.parent.mkdir(parents=True, exist_ok=True)

        if not self._path.exists():
            self._path.write_text("[]", encoding="utf-8")

    def _read_raw(self) -> List[dict]:
        text = self._path.read_text(encoding="utf-8").strip()
        if not text:
            return []
        try:
            data = json.loads(text)
        except json.JSONDecodeError:
            return []
        if not isinstance(data, list):
            return []
        return data

    def _write_raw(self, data: List[dict]) -> None:
        self._path.write_text(
            json.dumps(data, ensure_ascii=False, indent=2),
            encoding="utf-8",
        )

    def _dict_to_model(self, d: dict) -> T:
        from_dict = getattr(self._model_cls, "from_dict", None)
        if callable(from_dict):
            return from_dict(d) 
        return self._model_cls(**d)  

    def _model_to_dict(self, obj: T) -> dict:
        if is_dataclass(obj):
            d = asdict(obj)
        elif hasattr(obj, "__dict__"):
            d = dict(obj.__dict__)
        else:
            raise TypeError(f"Неможливо серіалізувати об'єкт типу {type(obj)}")

        for k, v in list(d.items()):
            if isinstance(v, (date, datetime)):
                d[k] = v.isoformat()
        return d

    def _read_all(self) -> List[T]:
        raw_list = self._read_raw()
        return [self._dict_to_model(d) for d in raw_list]

    def _write_all(self, items: List[T]) -> None:
        data = [self._model_to_dict(item) for item in items]
        self._write_raw(data)


    def get_all(self) -> List[T]:
        return self._read_all()

    def get_by_id(self, entity_id: str) -> T:
        for item in self._read_all():
            if item.id == entity_id:
                return item
        from ..bll.exceptions import NotFoundError
        raise NotFoundError(f"Entity with id={entity_id} not found")

    def add(self, entity: T) -> None:
        items = self._read_all()
        items.append(entity)
        self._write_all(items)

    def update(self, entity: T) -> None:
        items = self._read_all()
        for i, existing in enumerate(items):
            if existing.id == entity.id:
                items[i] = entity
                self._write_all(items)
                return
        from ..bll.exceptions import NotFoundError
        raise NotFoundError(f"Entity with id={entity.id} not found")

    def delete(self, entity_id: str) -> None:
        items = self._read_all()
        new_items = [x for x in items if x.id != entity_id]
        self._write_all(new_items)
