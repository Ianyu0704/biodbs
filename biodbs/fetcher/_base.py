

class BaseAPI:
    def __init__(self):
        self._url_format = None
        self._params = {}

    def update_params(self, **kwargs):
        self._params.update(kwargs)

    @property
    def api(self):
        if self._url_format is None:
            raise NotImplementedError("This class must be inherited")
        return self._url_format.format(**self._params)

    def copy(self):
        new = self.__class__()
        new.update_params(**self._params)
        return new

    def apply(self, **params):
        new_api = self.copy()
        new_api.update_params(**params)
        return new_api
