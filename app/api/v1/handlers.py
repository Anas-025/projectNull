def transformTextHandler(form):
    value = int(form['formatting'])
    if(value == 1):
        return form['text'].upper()
    elif(value == 2):
        return form['text'].lower()
    elif(value == 3):
        return ", ".join([word + ": " + str(len(word)) for word in form['text'].split(" ")]) 
