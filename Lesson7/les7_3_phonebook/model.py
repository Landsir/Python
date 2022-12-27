def write_txt(filename: str, data:list):
    with open(filename, 'w', encoding='UTF_8') as fout:
        
        for i in range(len(data)):
            s= ''
        for v in data[i].values():
            s+=v+','
        fout.write(f'{s[:-1]}\n')
        
        
def write_csv(filename: str, data:list):
    with open(filename, 'w', encoding='UTF_8') as fout:
        for i in range(len(data)):
            s =''
            for v in data[i].values():
                s += v+','
            fout.write(f'{s[:-1]}\n')



def read_csv(filename: str) -> list:
    data = []
    fields = ['Second_name', 'Name', 'Phonenumber', 'Info']
    with open (filename, 'r', encoding= 'UTF_8') as fin:
        for line in fin:
            record = dict(zip(fields, line.strip().split(',')))
            data.append(record)
    return data 
            
    # a={s:2,r:4}
    # a = dict((1,2),(b,5))
    
def find_by_name(data:list, last_name: str) -> str:
    for el in data:
        if el.get('Second_name') == last_name: 
            return el.get("Number")
    return "Can't find the record"

def find_by_number(data:list, phone_number: str) -> str:
    for el in data:
        if el.get('Phonenumber') == phone_number: 
            return f'{el.get("Second_name")}, {el.get("Name")}'
    return "Can't find the record"

def add_user(data: list, user_data: str):
    fields = ['Second_name', 'Name', 'Phonenumber', 'Info']
    record = dict(zip(fields, user_data.split(',')))
    data.append(record)
    
