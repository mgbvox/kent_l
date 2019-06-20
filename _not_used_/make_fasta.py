import pandas as pd

def write_fasta(f_name,seqs,ID=''):
    with open(f_name+'.txt', "w") as out_handle:
        for seq in seqs:
            out_handle.write('>{}\n'.format(ID))
            out_handle.write(str(seq)+'\n')


data = pd.concat([pd.read_csv('training_data.csv'),pd.read_csv('test_data.csv')])
data = data[data['Resp']!=1].dropna(how='any')

pr_zeros = data['PR Seq']
rt_zeros = data['RT Seq']

write_fasta('files/pr_fasta',pr_zeros)
write_fasta('files/rt_fasta',rt_zeros)

