# from typing import Any, Callable, Optional, Union
import tf.app as tf_app
import tf.advanced.app as tf_advanced_app

class GNTWrapper:
    def __init__(self):
        self._GNT = None

    @property
    def temp_ClassName(self) -> str:
        return self.GNT.__class__

    @property
    def GNT(self) -> tf_advanced_app.App:
        if self._GNT is None:
            self._GNT = tf_app.use('CenterBLC/N1904', version='1.0.0')
        return self._GNT