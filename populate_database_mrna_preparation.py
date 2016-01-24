

cancers=['BLCA','BRCA','CESC','COAD','ESCA','GBM','HNSC','KIRC','KIRP','LAML','LGG','LIHC','LUAD','LUSC','OV','PAAD',\
               'READ','SARC','SKCM','STAD','UCEC']

##f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\for_oncolnc\all_mrna_ids.txt')

all_data={}

for cancer in cancers:
    print cancer
    f=open(r'C:\Users\Jordan Anaya\Desktop\omnesres\oncolnc\database\mrna'+'\\'+cancer+'mrnadata.txt')
    data=[eval(i.strip()) for i in f]
    for j in data:
        all_data[j[0].upper()+'_'+j[1]]=all_data.get(j[0].upper()+'_'+j[1],[])+[{'cox':str(j[2]),'p_value':j[3],'fdr':j[4],'rank':j[5],'median':j[6],\
                                                          'mean':j[7],'cancer':cancer,}]


f=open('for_oncolnc_mrna.txt','w')
for i in all_data:
    f.write(i)
    f.write('\t')
    f.write(str(all_data[i]))
    f.write('\n')
f.close()
