class ModelsMixin:

    def to_dict(self):
        data = {}
        for field in self._meta.fields:
            key = field.name
            value = getattr(self, key)
            data[key] = value
        return data
