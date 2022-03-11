from nltk.chat.util import Chat, reflections

pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"(.*) morning",
        ["A very good morning :)",]
    ],
    [
        r"(.*) evening",
        ["A very good evening :)",]
    ],
    [
        r"(.*) afternoon",
        ["A very good afternoon :)",]
    ],
    [
        r"(.*) night",
        ["Have a peaceful night :)",]
    ],
    [
        r"name is (.*)",
        ["Hello %1, How are you today ?",]
    ],
    [
        r"hi|hey|hello|hola",
        ["Hello, What's your name?", "Hey there, What's your name?", "Ciao, What's your name?","Hola, What's your name?","annyeong, What's your name?"]
    ], 
    [
        r"what is your name?",
        ["I am AIUTO, your friendly neighborhood bot.",]
    ],
    [
        r"how are you?",
        ["I'm doing good and How about You?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright pal","It's Okay",]
    ],
    [
        r"I am good",
        ["Great to hear that!","Wonderful!"]
    ],
    [
        r"I am fine",
        ["Great to hear that!","Wonderful!"]
    ],
    [
        r"i'm (.*) doing good",
        ["Nice to hear that :)","That's good :)",]
    ],
    [
        r"i'm (.*) good",
        ["Nice to hear that :)","That's good :)",]
    ],
    [
        r"I am (.*) sad",
        ["What happened? you can share it with me. I might be of some help maybe?",]
    ],
    [
        r"I am sad",
        ["What happened? you can share it with me. I might be of some help maybe?",]
    ],
    [
        r"What’s up?",
        ["I'm afraid it might come as a shock but the sky is up :)",]
    ],
    [
        r"Yes",
        ["Please Elaborate :)",]
    ],
    [
        r"No",
        ["Please Elaborate :)",]
    ],
    [
        r"(.*) age?",
        ["I am wayyy younger than you are but i'll help you as a companion.",]
    ],
    [
        r"what (.*) want ?",
        ["Make me an offer I can't refuse",]
    ],
    [
        r"(.*) created ?",
        ["ummm ","top secret ;)",]
    ],
    [
        r"(.*) (location|city) ?",
        ['Indore, Madhya Pradesh',]
    ],
    [
        r"how is weather in (.*)?",
        ["Weather in %1 is awesome like always","Too hot man here in %1","Too cold man here in %1","Never even heard about %1"]
    ],
    [
        r"i work in (.*)?",
        ["%1 is an Amazing company, I have heard about it.",]
    ],
    [
        r"(.*)raining in (.*)",
        ["No rain since last week here in %2","Damn its raining too much here in %2"]
    ],
    [
        r"how (.*) health(.*)",
        ["I'm a computer program, so I'm always healthy ",]
    ],
    [
        r"(.*) (sports|game) ?",
        ["I'm a very big fan of Basketball",]
    ],
    [
        r"who (.*) sportsperson ?",
        ["Chris Paul","Kevin Durant","Mivhael Jordan"]
    ],
    [
        r"who (.*) (moviestar|actor)?",
        ["Jhonny Depp","Robert Downey Jr.","Will Smith","Ryan Reynolds"]
    ],
    [
        r"i am looking for some help",
        ["yes, i'll help you as much as i can, please tell me what kind of help do you need?"]
    ],
    [
        r"today is my birthday",
        ["heyyy! happy birthdayyy! why didn't you tell me yesterday? i would've planned a party for you :) "]
    ],
    [
        r"(.*) quote",
        ["life is better when you are laughing :) "]
    ],
    [
        r"(.*) anime",
        ["Yes! my first one was beelzebub","Yes! I love the sci-fi ones"]
    ],
    [
        r"(.*) music",
        ["Chap! I love music of every genre ^-^"]
    ],
    [
        r"(.*) joke",
        ["How do you get reluctant Pokemon to get on a bus? You Poke-em-on.","What is common between Light from 'Death Note' and a lift? They are both L-evaders.","Why you would be in deep trouble if 'Tokyo Ghoul' would have been real? Because, in this world, you Ken-run, but you Ken-not hide.","Why does nobody joke about rock type or ground type Pokemon? Because their jokes have reached rock bottom."]
    ],
    [
        r"quit",
        ["Bye take care. See you soon :) "]
    ],
    [
        r"later|bye|ttyl|gtg",
        ["It was nice talking to you. See you soon :)"]
    ],
]

def chat():
    print("Ciao! I am a AIUTO, your personal rescue companion! \nType quit to exit :)")
    chat = Chat(pairs, reflections)
    chat.converse()
#initiate the conversation
if __name__ == "__main__":
    chat()
