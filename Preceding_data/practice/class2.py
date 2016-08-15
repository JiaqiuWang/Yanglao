
def get_no_of_instances(cls_obj):
    return cls_obj.no_inst


class Kls(object):
    no_inst = 0

    def __init__(self):
        Kls.no_inst += 1

ik1 = Kls()
ik2 = Kls()
print(get_no_of_instances(Kls))

