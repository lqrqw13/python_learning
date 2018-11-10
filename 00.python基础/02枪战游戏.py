class Person(object):
    def __init__(self, name):
        self.name = name
        self.gun = None
        self.HP = 100
    def anzhuang_bullet(self, clip_temp, bullet_temp):
        clip_temp.contain_bullet(bullet_temp)
    def anzhuang_clip(self, gun_temp, clip_temp):
        gun_temp.contain_clip(clip_temp)
    def equip_gun(self, gun_temp):
        self.gun = gun_temp
    def __str__(self):
        if self.gun:
            return '{}, {}, HP是{}%,'.format(self.name, self.gun, self.HP)
        else:
            return '{}没有枪,HP是{}%'.format(self.name, self.HP)

class Gun(object):
    def __init__(self, name):
        self.name = name
        self.clip = None
    def contain_clip(self, clip_temp):
        self.clip = clip_temp
    def __str__(self):
        if self.clip:
            return '枪的信息为{}，弹夹信息为{}'.format(self.name, self.clip)
        else:
            return '枪的信息为{},没有弹夹'.format(self.name)

class Clip(object):
    def __init__(self, max_num):
        self.max_num = max_num
        self.bullet_list = []
    def contain_bullet(self, bullet_temp):
        self.bullet_list.append(bullet_temp)

    def __str__(self):
        return '弹夹的信息 {}/{}'.format(len(self.bullet_list), self.max_num)



class Bullet(object):
    def __init__(self, damage):
        self.damage = damage

def main():
    '''用来控制整个程序的流程'''
    gunslinger  = Person('反恐精英')#创建枪手对象
    gun = Gun('AK47')#创建枪对象
    clip = Clip(30)#创建弹夹对象
    bullet = Bullet(10)#创建子弹对象
    for i in range(15):
        gunslinger.anzhuang_bullet(clip,bullet)#枪手装子弹
    gunslinger.anzhuang_clip(gun, clip)#枪手上弹夹
    print(clip)#for test
    print(gun)#for test
    gunslinger.equip_gun(gun)#枪手拿起枪
    print(gunslinger)
    hostile = Person('恐怖分子')#创建一个敌人
    print(hostile)
    
    #枪手射击
    

if __name__ =='__main__':
    main()
