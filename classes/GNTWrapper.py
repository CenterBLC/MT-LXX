# from typing import Any, Callable, Optional, Union
from tf.core.api import Api
from tf.core.text import Text
from tf.core.locality import Locality
from tf.core.nodefeature import NodeFeatures
from tf.app import use
from tf.advanced.app import App

class GNTWrapper:
    def __init__(self):
        self._GNT: App = None
        self._F: NodeFeatures = None
        self._GNTApi: Api = None
        self._L: Locality = None
        self._T: Text = None

    @property
    def temp_ClassName(self) -> str:
        return str(type(self.GNT))
    
    @property
    def T(self) -> Text:
        if self._T is None:
            self._T = self.GNTApi.Text
        return self._T

    @property
    def L(self) -> Locality:
        if self._L is None:
            self._L = self.GNTApi.L
        return self._L

    @property
    def F(self) -> NodeFeatures:
        if self._F is None:
            self._F = self.GNTApi.F
        return self._F

    @property
    def GNTApi(self) -> Api:
        if self._GNTApi is None:
            self._GNTApi = self.GNT.api
        return self._GNTApi

    @property
    def GNT(self) -> App:
        if self._GNT is None:
            self._GNT = use('CenterBLC/N1904', version='1.0.0')
        return self._GNT