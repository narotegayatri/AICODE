from unicodedata import name
import nltk
from nltk.chat.util import Chat, reflections

reflections = {
  "i am"       : "you are",
  "i was"      : "you were",
  "i"          : "you",
  "i'm"        : "you are",
  "i'd"        : "you would",
  "i've"       : "you have",
  "i'll"       : "you will",
  "my"         : "your",
  "you are"    : "I am",
  "you were"   : "I was",
  "you've"     : "I have",
  "you'll"     : "I will",
  "your"       : "my",
  "yours"      : "mine",
  "you"        : "me",
  "me"         : "you"
}

pairs = [
    [
        r"about college",
        ["for  which college are you looking for? \n 1]D.Y.PATIL COLLEGE OF ENGINEERING \n 2]D. Y. Patil International University \n 3]Dr. D. Y. Patil College of Pharmacy, Akurdi, Pune \n 4]Dr. D. Y. Patil Institute of Engineering, Management and Research, Pune",]
    ],
    [
        r"my name is (.*)",
        ["Hello %1, How can i help you today ?",]
    ],
    [
        r"hi|hey|hello",
        ["Hello ,Let me know what you are looking for?"]
    ], 
    [
        r"D.Y.PATIL COLLEGE OF ENGINEERING|DYPCOE|dypcoe",
        ["choose one of the following 1.campus \n 2.placement \n 3.fees structure  \n 4.address  \n 5.courses",]
    ],
    [
        r"1",
        ["Campus and college are two words that have become almost synonyms these days. People talk about an educational institution and the physical premises where classes are held in a manner that suggests as if campus and college are one and the same thing. For those who believe they are the same, this description clarifies the differences",]
    ],
    [
        r"2",
        ["about x placements are done till now and still counting",]
    ],
    [
        r"3",
        ["please,select the course for which you are  interested! \n 1. B.E \n 2. ME",]
    ],
    
    [
        r"B.E |BE",
        ["Great, for which course \n 1]COMPUTER ENGINEERING \n 2]IT \n 3] ENTC \n 4]AI DS \n 5] MECHANICAL \n  6] CIVIL  ",]
    ],
    [
        r"COMPUTER ENGINEERING",
        ["fees of Cs is about 1,23,000rs",]
    ],
    [ 
        r"thank you",
        ["you are welcome!!,Have a nice day!",]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) ","It was nice talking to you. See you soon :)",]
    ],
]

def chat():
    print("Hii! your virtual assistance here ,how an i help you? ")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == '__main__':
    chat()