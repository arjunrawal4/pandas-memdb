import pandas as pd
import resource

def memory_limit():
    soft, hard = resource.getrlimit(resource.RLIMIT_AS)
    resource.setrlimit(resource.RLIMIT_AS, (1024 ,1024 ))


file = 'sales.csv'
df_empty = pd.DataFrame()


if __name__ == '__main__':
    memory_limit() # Limitates maximun memory usage to half
    try:
#         with open(file) as f:
#             chunk_iter = pd.read_csv(f, chunksize = 100000)
#             for chunk in chunk_iter:
#                 indices = chunk[ (chunk['Sales Channel'] == 'Offline') | (chunk['Units Sold'] > 1)].index
#                 chunk.drop(indices, inplace=True)
#                 df_empty = pd.concat([df_empty,chunk])
        for i in range(0,10):    
            with open(file) as f:
                df_empty = pd.concat([df_empty, pd.read_csv(f)])
        
    except MemoryError:
        sys.stderr.write('\n\nERROR: Memory Exception\n')
        sys.exit(1)
