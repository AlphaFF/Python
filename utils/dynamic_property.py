from collections import abc
import keyword

d = {"Schedule": {"conferences": [{" serial": 115}], "events": [
    {"serial": 34505, "name": "Why Schools Don ´ t Use Open Source to Teach Programming",
     "event_type": "40-minute conference session", "time_start": "2014-07-23 11: 30: 00",
     "time_stop": "2014-07-23 12: 10: 00", "venue_serial": 1462,
     "description": "Aside from the fact that high school programming...",
     "website_url": "http:// oscon.com/ oscon2014/ public/ schedule/ detail/ 34505", "speakers": [157509],
     "categories": [" Education"]}], "speakers": [
    {"serial": 157509, "name": "Robert Lefkowitz", "photo": None, "url": "http:// sharewave.com/", "position": "CTO",
     "affiliation": "Sharewave", "twitter": "sharewaveteam",
     "bio": "Robert ´ r0ml ´ Lefkowitz is the CTO at Sharewave,a startup..."}],
                  "venues": [{"serial": 1462, "name": "F151", "category": "Conference Venues"}]}}


class FrozenJSON:
    def __init__(self, mapping):
        self._data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self._data[key] = value

    def __getattr__(self, item):
        if hasattr(self._data, item):
            return getattr(self._data, item)
        else:
            return FrozenJSON.build(self._data[item])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj


# if __name__ == '__main__':
#     # FrozenJSON.build(d)
#     grad = FrozenJSON({'name': [1, 2, 3], 'age': '20'})
#     print(grad.name)
#     pass


# 构造对象的伪代码
def object_maker(the_class, some_arg):
    new_object = the_class.__new__(some_arg)
    if isinstance(new_object, the_class):
        the_class.__init__(new_object, some_arg)
    return new_object


## 特性的工厂函数
def quantity(name):
    def qty_getter(instance):
        return instance.__dict__[name]

    def qty_setter(instance, value):
        if value > 0:
            instance.__dict__[name] = value
        else:
            raise ValueError('value must be > 0')

    return property(qty_getter, qty_setter)


# 特性管理的其实是实例属性的存取
class LineItem:
    weight = quantity('weight')
    price = quantity('price')

    def __init__(self, desciption, weight, price):
        self.desciption = desciption
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


# if __name__ == '__main__':
#     nutmsg = LineItem('nutmsg', 8, 12.5)
#     print(nutmsg.weight, ',', nutmsg.price)
#     print(nutmsg.__dict__)
#     print(sorted(vars(nutmsg).items()))


# 描述符形式
class Quantity:
    def __init__(self, storage_name):
        self.storage_name = storage_name

    def __set__(self, instance, value):
        if value < 0:
            instance.__dict__[self.storage_name] = value
        else:
            raise ValueError('value must be > 0')


class LineItem:
    weight = Quantity('weight')
    price = Quantity('price')

    def __init__(self, description, weight, price):
        self.description = description
        self.weight = weight
        self.price = price

    def subtotal(self):
        return self.weight * self.price


        











