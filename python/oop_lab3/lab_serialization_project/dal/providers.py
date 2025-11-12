import pickle
import json
from abc import ABC, abstractmethod

class DataProvider(ABC):
    @abstractmethod
    def save(self, obj, filename):
        pass

    @abstractmethod
    def load(self, filename):
        pass


class PickleProvider(DataProvider):
    """Бінарна серіалізація (pickle)"""
    def save(self, obj, filename):
        with open(filename, 'wb') as f:
            pickle.dump(obj, f)

    def load(self, filename):
        with open(filename, 'rb') as f:
            return pickle.load(f)


class JSONProvider(DataProvider):
    """JSON серіалізація"""
    def save(self, obj, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump([o.__dict__ for o in obj], f, ensure_ascii=False, indent=2)

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return json.load(f)


class XMLProvider(DataProvider):
    """Проста XML серіалізація"""
    def save(self, obj, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            f.write('<Products>\\n')
            for p in obj:
                f.write(f'  <Product code=\"{p.code}\" name=\"{p.name}\" maker=\"{p.maker}\" price=\"{p.price}\" qty=\"{p.qty}\"/>\\n')
            f.write('</Products>')

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            return [line.strip() for line in f.readlines()]


class CustomProvider(DataProvider):
    """Користувацька (текстова) серіалізація"""
    def save(self, obj, filename):
        with open(filename, 'w', encoding='utf-8') as f:
            for o in obj:
                f.write('|'.join(f"{k}={v}" for k, v in o.__dict__.items()) + '\\n')

    def load(self, filename):
        with open(filename, 'r', encoding='utf-8') as f:
            lines = f.read().splitlines()
        result = []
        for line in lines:
            d = {}
            for kv in line.split('|'):
                k, v = kv.split('=') if '=' in kv else (kv, '')
                d[k] = v
            result.append(d)
        return result
