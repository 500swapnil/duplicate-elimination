from itertools import islice
from itertools import zip_longest
import time

class BtreeNode(object):
    def __init__(self, leaf=False):
        self.keys = []
        self.children = []
        self.leaf = leaf
        

class BTree(object):
    def __init__(self, t):
        self.t = t
        self.root = BtreeNode(leaf=True)
                
    def insert(self, k):
        r = self.root
        if  (2*self.t) - 1 != len(r.keys):  
            self.insert_not_full(r, k)
            return

        s = BtreeNode()
        self.root = s
        s.children.insert(0, r)      

        self.split(s, 0)            
        self.insert_not_full(s, k)
            

    def insert_not_full(self, x, k):
        i = len(x.keys) - 1
        if not x.leaf:
            while i >= 0:
                i -= 1
                if i<0 or k >= x.keys[i]:
                    break
            i += 1
            if len(x.children[i].keys) != (2*self.t) - 1:
                self.insert_not_full(x.children[i], k)
            else:
                self.split(x, i)
                if not k <= x.keys[i]:
                    i += 1
                self.insert_not_full(x.children[i], k)
        else:
            x.keys.append(0)
            while i >= 0:
                x.keys[i+1] = x.keys[i]
                i -= 1
                if i<0 or k >= x.keys[i]:
                    break
            x.keys[i+1] = k
    

    def split(self, x, i):
        y = x.children[i]
        z = BtreeNode(leaf=y.leaf)
        
        x.children.insert(i+1, z)
        x.keys.insert(i, y.keys[self.t-1])

        z.keys = y.keys[self.t:(2*self.t - 1)]
        y.keys = y.keys[0:(self.t-1)]
        
        if y.leaf:
            return
        z.children = y.children[t:(2*self.t)]
        y.children = y.children[0:(self.t-1)]  
      
    def search(self, k, x=None):
        if not isinstance(x, BtreeNode):
            return self.search(k, self.root)

        i = 0
        while i < len(x.keys):   
            i += 1
            if i>=len(x.keys) or k <= x.keys[i]:
                break

        if i < len(x.keys) and k == x.keys[i]:       
                return (x, i)
        
        if not x.leaf:                                
            return self.search(k, x.children[i])
                                         
        return None

output_buffer = []
output_file = 'output.txt'
B = 40
start_time = 0

def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def btree_open(R,n,M):
    f = open(R,'r',M)
    o = open(output_file, "w+")
    btree = BTree(1000000)
    input_iterator = iter(f)
    start_time = time.time()
    while True:
        piece = list(islice(input_iterator, B))
        if not piece:
            if output_buffer != []:
                for line in output_buffer:
                    o.write("%s\n" %(line))

            btree_close(f,o)
            break
        output_chunk = Getnext(piece,n,btree,f,o)
        if output_chunk is None:
            continue
        for line in output_chunk:
                    o.write("%s\n" %(line))
        output_buffer = []
    return time.time()-start_time

def Getnext( piece, n, btree, f, o):
    for line in piece:
        line = line.strip()
        hash_value=hash(line)
        if(btree.search(hash_value) == None):
            btree.insert(hash_value)
            if len(output_buffer)>=B:
                return output_buffer
            output_buffer.append(line)
    return None


def btree_close(ip_file_object,op_file_object):
    ip_file_object.close()
    op_file_object.close()

def main( R, n, M):
    return btree_open(R,n,M)

    



        