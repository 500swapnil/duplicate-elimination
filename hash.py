from itertools import islice
from itertools import zip_longest
import time

hash_map = {}
output_buffer = []
B = 40
output_file = 'output.txt'
        
def grouper(iterable, n, fillvalue=None):
    args = [iter(iterable)] * n
    return zip_longest(*args, fillvalue=fillvalue)


def hash_open(R,n,M):
    f = open(R,'r',M)
    o = open(output_file, "w+")
    input_iterator = iter(f)
    start_time = time.time()
    while True:
        piece = list(islice(input_iterator, B))
        if not piece:
            if output_buffer != []:
                for line in output_buffer:
                    o.write("%s\n" %(line))

            close(f,o)
            break
        output_chunk = Getnext(piece,n,f,o)
        if output_chunk is None:
            continue
        for line in output_chunk:
                    o.write("%s\n" %(line))
        output_buffer = []
    return time.time()-start_time


def Getnext( piece, n, f, o):
    for line in piece:
        line = line.strip()
        hash_value=hash(line)
        if hash_value not in hash_map:
            hash_map[hash_value] = 1
            if len(output_buffer)>=B:
                return output_buffer
            output_buffer.append(line)
    return None


def close(ip_file_object,op_file_object):
    ip_file_object.close()
    op_file_object.close()

def main( R, n, M):
    return hash_open(R,n,M)

    



        