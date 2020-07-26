from .builder import DATASETS
from .coco import CocoDataset
@DATASETS.register_module()
class ifly_dataset(CocoDataset):
    CLASSES = ('firecrackers', 'handcuffs', 'knife', 'lighter',
               'nailpolish', 'powerbank', 'pressure', 'scissors', 'slingshot', 'zippooil')