# Extract the domain name from a URL
def domain_name(url):
    domain = url.replace('http://', "").replace('https://', "").replace('www.', "")
    domain = domain.split('.')
    return domain[0]


# Encrypt this!
def encrypt_this(text):
    result = []
    
    for word in text.split():
        word = list(word)
        word[0] = str(ord(word[0]))
        if (len(word) > 2):
            word[1], word[-1] = word[-1], word[1]
        result.append(''.join(word))
        
    return ' '.join(result)


# Find The Parity Outlier
def find_outlier(integers):
    odds = [n for n in integers if n % 2 != 0]
    evens = [n for n in integers if n % 2 == 0]
    return odds[0] if len(odds) < len(evens) else evens[0]
