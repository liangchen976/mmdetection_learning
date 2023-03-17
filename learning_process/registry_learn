from mmcv.utils import Registry

# import后 记得回车 不然可能会出红

# 创建转换器（converter）的注册器（registry）
CONVERTERS = Registry('converter')

@CONVERTERS.register_module()
class Converter1(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b

converter1_cfg = dict(type='Converter1', a=2, b=33)
converter1 = CONVERTERS.build(converter1_cfg)
        
print(converter1)