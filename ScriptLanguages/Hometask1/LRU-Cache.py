"""Реализуйте LRU-кэш с тайм лимитами на каждый объект.
Предположим, что вам нужно кэшировать результаты запросов в базу данных, т.е. пары
некоторых параметров (ключей) и некоторых объектов (результатов). Однако кэш должен быть
ограниченным по количеству содержащихся в нем объектов, поэтому в некоторый момент времени
из кэша придется удалять некоторую запись. Политика вставки/удаления будет LRU, т.е.
удалять нужно элемент, доступ к которому не производился дольше всего. Также каждая запись
через некоторое время должна инвалидироваться (имеет TTL – time to live), т.е. становиться
недоступной и удаляться из кэша.
Реализуйте класс, описывающий такой кэш, предоставив весь необходимый интерфейс:
∙ удобное создание кэша с указанием размера и времени жизни записи по умолчанию,        #__init__
∙ возможность узнать текущее количество объектов,                                       # count_of_records
∙ возможность взять объект,                                                             # get_record, __getitem__
∙ возможность инвалидировать (удалить, по сути) объект и весь кэш,                      # delete_record, clear_cache
∙ возможность проверить наличие некоторого объекта,                                     # record_in_cache
∙ возможность изменить TTL (время жизни) добавляемого объекта по умолчанию,             # set_default_ttl
∙ возможность добавить новый объект (возможно, с другим TTL),                           # add_new_record, __setitem__
∙ другие вспомогательные методы.
Помните, что кэш должен быть максимально быстрым. Операцию проверки наличия и взятия
элемента из кэша постарайтесь сделать быстрее, чем добавление нового элемента в кэш.
Предусмотрите также некоторый набор юнит-тестов к вашему классу."""

# import hashlib
import time
import logging


class Cache:

    def __init__(self, cache_size: int = 10, ttl=4):
        self._cache_size = cache_size
        self._ttl = ttl
        self._records = {}

    def __getitem__(self, record_key):
        return self.get_record(record_key)

    # def __setitem__(self, key, value, ttl=None):
    #     self.add_new_record(key, value, ttl)

    def __setitem__(self, key, value_and_ttl):
        self.add_new_record(key, *value_and_ttl)

    def current_cache_size(self):
        """It's slow but correct, I think"""
        self._remove_expired_records()
        return len(self._records)

    def record_in_cache(self, record_key) -> bool:
        return record_key in self._records

    def get_record(self, record_key):
        """I have read that exception handling is the fastest way to get dict value and check cache miss"""
        try:
            if time.time() - self._records[record_key]["last_access"] > self._records[record_key]["ttl"]:
                raise KeyError
            self._records[record_key]["last_access"] = time.time()
            return self._records[record_key]["value"]
        except KeyError:
            logging.warning("Record with key {} doesn't exist or it's time-to-live was expired".format(str(record_key)))
            return None

    def set_default_ttl(self, new_ttl):
        self._ttl = new_ttl

    def add_new_record(self, record_key, record, ttl=None):
        if self.current_cache_size() >= self._cache_size:
            self._remove_expired_records()
            if self.current_cache_size() >= self._cache_size:
                self._remove_lru_record()

        try:
            if record_key is None:
                raise ValueError
            if ttl is None:
                real_ttl = self._ttl
            else:
                real_ttl = ttl
            self._records[record_key] = {"value": record, "last_access": time.time(), "ttl": real_ttl}
        except ValueError:
            print("Record Key must be not None!")

    def delete_record(self, record_key):
        """Actually this method does not delete record, just make it expired"""
        try:
            self._records[record_key]["last_access"] = -1
        except KeyError:
            logging.warning("There is no records with record key {}".format(str(record_key)))

    def clear_cache(self):
        self._records.clear()

    def _remove_lru_record(self):
        last_recently_used = (None, {"value": None, "last_access": time.time() + 10, "ttl": None})
        for rec in self._records.items():
            if rec[1]["last_access"] < last_recently_used[1]["last_access"]:
                last_recently_used = rec

        assert last_recently_used[
                   0] is not None, "We can't find any lru-record. It means that you configure your cache with mistakes."
        del self._records[last_recently_used[0]]

    def _remove_expired_records(self):
        """Delete expired
        If last_access < 0, it means that record is expired"""
        remove_list = []
        real_time = time.time()

        for rec in self._records.items():
            if rec[1]["last_access"] < 0 or real_time - rec[1]["last_access"] > rec[1]["ttl"]:
                remove_list.append(rec[0])
                continue

        for record_key in remove_list:
            del self._records[record_key]


if __name__ == "__main__":
    cache = Cache()
    # for i in range(20):
    #     print(i, " ", end="")
    #     cache.add_new_record(i, i * 10)
    # cache.add_new_record(21, 21 * 10, 20)
    # print()
    # cache.delete_record("123")
    # cache.delete_record(12)
    # time.sleep(5)
    # for i in range(10, 22):
    #     print(cache.get_record(i))
    cache["123"] = 121, 1
    time.sleep(2)
    print(cache["123"])

    print("DabudiDabudaj")
