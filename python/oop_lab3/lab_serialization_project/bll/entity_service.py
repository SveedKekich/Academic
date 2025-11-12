from dal.entity_context import EntityContext
from typing import List, Type, Any
from bll.exceptions import EntityServiceError

class EntityService:
    def __init__(self, context: EntityContext):
        self.context = context

    def save_all(self, items: List[Any]):
        try:
            self.context.save(items)
        except Exception as e:
            raise EntityServiceError(f"Помилка при збереженні: {e}")

    def load_all(self, cls: Type[Any]) -> List[Any]:
        try:
            data = self.context.load()
            if isinstance(data, list):
                result = []
                for d in data:
                    if isinstance(d, dict):
                        result.append(cls(**d))
                    else:
                        result.append(d)
                return result
            return []
        except Exception as e:
            raise EntityServiceError(f"Помилка при завантаженні: {e}")
