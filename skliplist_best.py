import random

# 最高层数设置为4
MAX_LEVEL = 4


def randomLevel():
    """
    返回随机层数 如果大于最大层数则返回最大层数
    :return: random level
    """
    k = 1
    while random.randint(1, 100) % 2:
        print k
        k += 1
    k = k if k < MAX_LEVEL else MAX_LEVEL
    print k
    return k


def traversal(skiplist):
    """
    跳表的遍历功能
    对每一层的元素都进行遍历
    :param skiplist: 待遍历的跳表
    :return: None
    """
    level = skiplist.level
    i = level - 1
    while i >= 0:
        level_str = 'header'
        header = skiplist.header
        while header:
            level_str += ',%s,' % i
            level_str += ' -> %s' % header.key
            header = header.forward[i]
        print level_str
        i -= 1

class Node(object):
    def __init__(self, level, key, value):
        """
        跳表节点初始化
        :param level: 节点的层数
        :param key: 查询关键字
        :param value: 存储的信息
        """
        self.key = key
        self.value = value
        self.forward = [None] * level
class Skiplist(object):
    def __init__(self):
        self.level = 0
        self.header = Node(MAX_LEVEL,None,None)
        self.size = 0
    def search(self,key):
        i = self.level -1
        q = self.header
        while i >= 0:
            print 'level'
            print i
            print 'level_end'
            while q.forward[i] and q.forward[i].key <= key:
                print i
                print q.forward[i].key
                if q.forward[i].key == key:
                    return q.forward[i].key,q.forward[i].value,i
                q = q.forward[i]
            i -= 1
            print 'yuge'
            print i
            print 'lijie'
        return None,None,None
    def insert(self, key, value):
        """
        跳表插入操作
        :param key: 节点索引值
        :param value: 节点内容
        :return: Boolean 用于判断插入成功或失败
        """
        # 更新的最大层数为 MAX_LEVEL 层
        update = [None] * MAX_LEVEL

        i = self.level - 1
        q = None
        # 遍历所有的层数
        while i >= 0:
            q = self.header
            while q.forward[i] and q.forward[i].key < key:
                q = q.forward[i]
            update[i] = q
            i -= 1

        if q and q.key == key:
            return False

        k = randomLevel()
        # 如果随机数大于当前层数，采取加1层策略
        if k > self.level:
            i = self.level
            update[i] = self.header
            self.level += 1
            k = self.level

        q = Node(k, key, value)
        i = 0
        while i < k:
            q.forward[i] = update[i].forward[i]
            update[i].forward[i] = q
            i += 1

        self.size += 1

        return True
    def delete(self, key):
        """
        跳表删除操作
        :param key: 查找的关键字
        :return: Boolean 用于判断删除成功或失败
        """
        update = [None] * MAX_LEVEL
        i = self.level - 1
        q = None
        # 跟插入一样 找到要删除的位置
        while i >= 0:
            q = self.header
            while q.forward[i] and q.forward[i].key < key:
                q = q.forward[i]
            update[i] = q
            i -= 1
        if q and q.key == key:
            i = 0
            while i < self.level:
                if update[i].forward[i] == q:
                    update[i].forward[i] = q.forward[i]
                i += 1
            del q
            # 删除可能导致层数发生变化
            i = self.level - 1
            while i >= 0:
                if self.header.forward[i] is None:
                    self.level -= 1
                i -= 1

            self.size -= 1

            return True
        else:
            # 没有此节点，返回 False
            return False
