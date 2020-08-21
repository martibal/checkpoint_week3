def to_camel_case(text):
    text = ' '.join(word[0].upper() + word[1:] for word in text.split())
    text = text.replace(' ', '')
    return(to_camel_case)

