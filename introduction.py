introduction_pairs = [
    [
        r"my name is (.*)",
        ["Hello %1, how can I help you today?",]
    ],
    [
        r"hi|hey|hello|hola",
        ["Hello!", "Hi!",]
    ],
    [
        r"what is your name?",
        ["I have no name.",]
    ],
    [
        r"how are you?",
        ["I'm doing well, thank you! How may I help you?",]
    ],
    [
        r"sorry (.*)",
        ["It's alright.", "No problem",]
    ],
    [
        r"I am (.*) (good|well|okay|ok)",
        ["Good to hear !", "Alright, Excellent!",]
    ],
    [
        r"quit",
        ["Thank you for talking to me!"]
    ],
    [
        r"(.*)",
        ["I'm unable to understand what you said",]
    ],
]
