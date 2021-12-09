### Q1: create 4 blocks (list of lists) with 5 transactions.
### Utilize the website shown in class to create block hashs. 
### Each block should verify that the prior block is valid
### Create logic using loops, functions, and if statements to achieve this
### Transactions should have 4 elements in the list added to the list of lists. 
### REMEBER BLOCK LIMITS


blockchain = []

hash_value = ['0000f727854b50bb95c054b39c1fe5c92e5ebcfa4bcb5dc279f56aa96a365e5a','a7017a7e606f012b019a0ea1bcf55f274744a1b3f3f520fb416a730fa23b141f','9a955b1869aa03d9e29fe3b586bded284caad26da89194951cce5c6eb95871d9','91ac21893ed0bb98ee1200cc60f8a7aa01b0368014bd9cdf3fbb79071454a58f']
names = ['Dummmy_1','Dummmy_2','Dummmy_3','Dummy_4','Dummy_5',
         'Dummmy_6','Dummmy_7','Dummmy_8','Dummy_9','Dummy_10',
         'Dummmy_11','Dummmy_12','Dummmy_13','Dummy_14','Dummy_15',
         'Dummmy_16','Dummmy_17','Dummmy_18','Dummy_19','Dummy_20']
time = ['12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00',
        '12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00',
        '12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00',
        '12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00','12/8/2021 00:00:00',]
currency = ['ETH','ETH','ETH','ETH','ETH',
            'ETH','ETH','ETH','ETH','ETH',
            'ETH','ETH','ETH','ETH','ETH',
            'ETH','ETH','ETH','ETH','ETH']
value = [1,1.5,10,15,4,
         2,3,3.5,5.5,5,
         6,7.5,9.1,2,3,
         1,1,1,1.2,1.5]
block = []

for i in range(len(value)+1):
    if len(blockchain)==0:
        if len(block) == 5:
            blockchain.append(block)
            blockchain[len(blockchain)-1][4].append(hash_value[0])
            block = []
            block.append([names[i],time[i],currency[i],value[i]])
        else:
            block.append([names[i],time[i],currency[i],value[i]])
    else:
        if (len(block) == 5) and (blockchain[len(blockchain)-1][4][4] == hash_value[int((i+1)/5)-2]):
            blockchain.append(block)
            blockchain[len(blockchain)-1][4].append(hash_value[int(i/5)-1])
            block = []
            if i ==20:
                pass
            else:
                block.append([names[i],time[i],currency[i],value[i]])
        else:
            block.append([names[i],time[i],currency[i],value[i]])
            
        


len(blockchain)

### Q2: Create a class object to define a block. 
### Using your class object create a mini blockchain. 
### Assume a block now accepts 10 transactions and 15 blocks are created.

hash_value = ['0000f727854b50bb95c054b39c1fe5c92e5ebcfa4bcb5dc279f56aa96a365e5a','a7017a7e606f012b019a0ea1bcf55f274744a1b3f3f520fb416a730fa23b141f','9a955b1869aa03d9e29fe3b586bded284caad26da89194951cce5c6eb95871d9','91ac21893ed0bb98ee1200cc60f8a7aa01b0368014bd9cdf3fbb79071454a58f',
              'ba62cdcd5251c2f30ff882a003425ef22418fa24b7e8c04069c114607f160d4e','54183ca72a9f899b054aa37c08c6c54f27fd9100889acc9f4eb83983aa9046e7','bcd2b7a5ffd9083f41e1030b64945aa510a4501091b73256b2410915d4cd206a','273ff9ca9e31c4b813b24f238d6be97ab789d8b8c5b7257949a21451f16fb917',
              '64c83df872d808a1820aab72aa20bf2cf33b96fff4933e691e30f7646dfcc1be','20af2e45e35866cd1f34e50fd5eafda74d788071bf14617e65e375692704c7a7','426c8c87303d9b4d51b43edd4abf73071de8bdde07771c4711caec5249dbc87b','54e351832275f113db1968b3a782faab1dbe7898f7d0f824792928f8b2dae4c3',
              'ed9a7791b3d7975f28818518ebf962b2aaf7cf80dd42ea3c58b00390632a5144','8ef0b6e3f09b2153d2d46b47ffd62cfe9ebd4ba8d346c6d704af2c901099fd27','64c83df872d808a1820aab72aa20bf2cf33b96fff4933e691e30f7646dfcc1be']


names = []
time = []
currency = []
value = []


for i in range(150):
    time.append('12/8/2021 00:00:00')
    currency.append('ETH')
    value.append(i+1)
    names.append("Dummy_"+str(i))


class blockchainconstructor:
    def blockchainconst(names,time,currency,value,hash_value):
        names = names
        time = time
        currency = currency
        value = value
        hash_value = hash_value
        blockchain = []
        block = []
    
        for i in range(len(value)+1):
            if len(blockchain)==0:
                if len(block) == 10:
                    blockchain.append(block)
                    blockchain[len(blockchain)-1][9].append(hash_value[0])
                    block = []
                    block.append([names[i],time[i],currency[i],value[i]])
                else:
                    block.append([names[i],time[i],currency[i],value[i]])
            else:
                if (len(block) == 10) and (blockchain[len(blockchain)-1][9][4] == hash_value[int((i+1)/10)-2]):
                    blockchain.append(block)
                    blockchain[len(blockchain)-1][9].append(hash_value[int(i/10)-1])
                    block = []
                    if i == 150:
                        pass
                    else:
                        block.append([names[i],time[i],currency[i],value[i]])
                else:
                    block.append([names[i],time[i],currency[i],value[i]])
        return blockchain
        
    
bc = blockchainconstructor.blockchainconst(names,time,currency,value,hash_value)
len(bc)