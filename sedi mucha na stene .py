text = 'sedi mucha na stene, sedi a spi, sedi a buvinka potvora malinka'
samo='aeiouy'
schym=input('zadaj somohlasku kt tam chces: ')
nt=''
for i in text:
    if i in samo:
        nt=nt+schym
    else:
        nt=nt+i
print (nt)
