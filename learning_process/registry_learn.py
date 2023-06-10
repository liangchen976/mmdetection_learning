from mmcv.utils import Registry

# import后 记得回车 不然可能会出红

# 创建转换器（converter）的注册器（registry）
# 传入的参数是为了便于分类，
CONVERTERS = Registry('converter')

@CONVERTERS.register_module()
class Converter1(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('我是Converter1')


@CONVERTERS.register_module()
class Converter2(object):
    def __init__(self, a, b):
        self.a = a
        self.b = b
        print('我是Converter2')

# converter1_cfg = dict(type='Converter1', a=2, b=33)
# converter1 = CONVERTERS.build(converter1_cfg)

# converter2_cfg = dict(type='Converter2', a=99, b=999)
# converter2 = CONVERTERS.build(converter2_cfg)
        
# print(converter1,converter2)

# 比如说现在我有很多种backbone 在跑程序的时候如果每次手动更改backbone的对应代码，会显得麻烦
# 如果能通过仅更改配置文件的方法就能改，那多好，那么就可以首先申请一个注册器，这个注册器专门就存放不同的backbone
BACKBONE = Registry('backbone')

# 我现在有两个backbone，一个是vgg，一个是resnet 将他们用注册器装饰，也就是赋予他们新的功能，也可以理解为BACKBONE为一个备胎库，要谁实例化，给他一个信号(配置文件)他就来了

# 进第一个备胎
@BACKBONE.register_module()
class VGG(object):
    def __init__(self, name, depth):
        self.name = name
        self.depth = depth
        print('我是VGG')

# 进第二个备胎
@BACKBONE.register_module()
class ResNet(object):
    def __init__(self, name, depth, norm=True):
        self.name = name
        self.depth = depth
        #是否需要norm
        self.norm = norm
        print('我是ResNet')

# 这里的type就是要哪个备胎响应，备胎名字，需要和声明的类名相同
# 下面是可能用到的工具人，在实验的时候可能有很多个，因为需要尝试探索。 
config_vgg = dict(type='VGG', name='Vgg', depth=18)
config_resnet = dict(type='ResNet', name='ResNet!', depth=101, norm = 'LayerNorm')

# 下面在训练的时候要用到某个backbone了
# 从备胎库捞一个
beitai_backbone = BACKBONE.build(config_vgg)
print(beitai_backbone)