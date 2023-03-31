def countEmail():
    # This first line is provided for you
    name = input("Enter file:")
    if len(name) < 1 : 
        name = "mbox-short.txt"
    handle = open(name)
    users = dict()
    
    for lines in handle:
        line = lines.split()
        
        if lines.startswith("From") and len(line) > 2 :
            user = line[1]
            users[user] = users.get(user, 0) + 1
    
    maxuser = None
    maxuseremails = None
    for sender,count in users.items():
        if maxuser is None or count > maxuseremails :
            maxuser = sender
            maxuseremails = count
    
    print(maxuser , maxuseremails)

## if you want to test locally run > python counter.py
if __name__ == "__main__":
    countEmail()
