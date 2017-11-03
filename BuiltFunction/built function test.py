#built function test
print "Example01:"
def word_leght(sentence):
    return list(map(len, sentence.split()))
p = word_leght("How can we learn Python immediately?")
print "the length of words: ", p

print "\nExample01:\n"
def filter_words(word_list, letter):
    return filter(lambda word: word[0] == letter, l)
l = ["hello", "hi", "has", "one", "your", "excellent"]
x = filter_words(l, "h")
print "The word begins from 'h' : ", x
