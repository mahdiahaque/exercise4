import re


def parse_name(text):
    

    pattern = r'^(\w+\s\w+)'
    regex = re.compile(pattern)

    name = regex.findall(text)
    print(name)
    return name


def parse_address(text):
    
    #pattern = r'(\d+)\s(\w+)\s(\w+)\s(\w+)\s(\w+)'
    pattern = r'(\d{1,}[\w\s]+)\s(\w+)\s([A-Z]{2})'
    regex = re.compile(pattern)

    address = regex.finditer(text)
    
    for match in address:
        street = (match.group(1))
        city = (match.group(2))
        state = (match.group(3))
        print(street)
        print(city)
        print(state)
        
        return street,city,state
    

    


def parse_email(text):

    pattern = r'[\w+.?_?]+@\w+.\w+'
    regex = re.compile(pattern)

    email = regex.findall(text)
    print(email)
    
    return email









if __name__ == "__main__":
    # #parse_name("Jazmine Holcomb 3212 Adams Avenue Washington MD eluir.azevedo.7o@lucidmode.com")
    # parse_address("Jazmine Holcomb 3212 Adams Avenue Washington MD eluir.azevedo.7o@lucidmode.com")
    # parse_email("Jazmine Holcomb 3212 Adams Avenue Washington MD eluir.azevedo.7o@lucidmode.com")

    f = open("people.txt", "r")
    all = f.read()

    parse_name(all)
    parse_address(all)
    parse_email(all)

    f.close()