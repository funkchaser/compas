from __future__ import print_function
from __future__ import absolute_import
from __future__ import division

from compas.scene import SceneObject


class GHArtist(SceneObject):
    """Base class for all GH artists."""

    def __init__(self, **kwargs):
        super(GHArtist, self).__init__(**kwargs)

    def clear(self):
        raise NotImplementedError
