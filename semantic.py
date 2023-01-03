#this program looks at the examples of similarities

#Example Code 1
import spacy
nlp = spacy.load('en_core_web_md')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#It's interesting the Cat and monkey have such high similarity.
#But for humans Monkey and banana would seem to be more obvious a similarity

#My Example for Code 1
word1 = nlp("bat")
word2 = nlp("man")
word3 = nlp("cave")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#its interesting that the highest similarity is between man and cave
#rather than bat and cave which is a common habitat for many bats

#Example Code 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Example Code 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",similarity)

#Simpler version of the model code

#These versions of the code are run with the sm version of the model

#Example Code 1
import spacy
nlp = spacy.load('en_core_web_sm')
word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#It's interesting the Cat and monkey have such high similarity.
#But for humans Monkey and banana would seem to be more obvious a similarity

#My Example for Code 1
word1 = nlp("bat")
word2 = nlp("man")
word3 = nlp("cave")
print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))
#its interesting that the highest similarity is between man and cave
#rather than bat and cave which is a common habitat for many bats

#Example Code 2
tokens = nlp('cat apple monkey banana ')
for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Example Code 3
sentence_to_compare = "Why is my cat on the car"
sentences = ["where did my dog go",
"Hello, there is my car",
"I\'ve lost my car in my car",
"I\'d like my boat back",
"I will name my dog Diana"]
model_sentence = nlp(sentence_to_compare)
for sentence in sentences:
    similarity = nlp(sentence).similarity(model_sentence)
    print(sentence + " - ",similarity)

#Using the sm model results in a warning from the terminal about lack of word vectors
#additionally the similarity numbers seem to be overall higher but less differentiated between them
