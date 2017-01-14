import urllib

def read_text() :
    quotes = open("C:\Python27\exercise\profanity_check\movies_quotes.txt")
    contents_of_file = quotes.read()
    print(contents_of_file)
    quotes.close()
    prafanity_check(contents_of_file)

def prafanity_check(text_to_check) :
    connection = urllib.urlopen("http://www.wdylike.appspot.com/?q="+text_to_check)
    output = connection.read()
    print(output)
    connection.close()
read_text()
