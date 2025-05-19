word_list = [
    # Fruits
    "apple", "banana", "cherry", "grape", "orange", "strawberry", "blueberry", "pineapple", "mango", "watermelon",
    
    # Animals
    "elephant", "giraffe", "kangaroo", "dolphin", "tiger", "lion", "cheetah", "panda", "zebra", "crocodile",
    
    # Musical Instruments
    "guitar", "piano", "violin", "trumpet", "drums", "flute", "saxophone", "harp", "cello", "trombone",
    
    # Nature
    "mountain", "ocean", "valley", "desert", "forest", "river", "waterfall", "glacier", "volcano", "canyon",
    
    # Programming Languages
    "python", "java", "javascript", "ruby", "swift", "csharp", "kotlin", "golang", "rust", "typescript",
    
    # Countries
    "canada", "brazil", "germany", "france", "italy", "japan", "india", "mexico", "australia", "china"
]

stages = ['''
     +_______+
     |       |
     |      (_)
     |      /|\\
     |       |
     |      / \\
     |
       ''','''
     +_______+
     |       |
     |      (_)
     |      /|\\
     |       |
     |      /
     |
        ''','''
     +_______+
     |       |
     |      (_)
     |      /|\\
     |       
     |      
     |
       ''',''' 
     +_______+
     |       |
     |      (_)
     |      /|
     |       
     |      
     |
        ''',''' 
      +_______+
     |       |
     |      ( )
     |      
     |       
     |      
     |
        ''','''
     +_______+
     |       |
     |      
     |      
     |       
     |      
     |
       ''']

logo = "....HANGMAN GAME 🧔‍♂️🪂...."

hint_map = {
    "apple": "Fruit", "banana": "Fruit", "cherry": "Fruit", "grape": "Fruit", "orange": "Fruit",
    "strawberry": "Fruit", "blueberry": "Fruit", "pineapple": "Fruit", "mango": "Fruit", "watermelon": "Fruit",

    "elephant": "Animal", "giraffe": "Animal", "kangaroo": "Animal", "dolphin": "Animal", "tiger": "Animal",
    "lion": "Animal", "cheetah": "Animal", "panda": "Animal", "zebra": "Animal", "crocodile": "Animal",

    "guitar": "Musical Instrument", "piano": "Musical Instrument", "violin": "Musical Instrument",
    "trumpet": "Musical Instrument", "drums": "Musical Instrument", "flute": "Musical Instrument",
    "saxophone": "Musical Instrument", "harp": "Musical Instrument", "cello": "Musical Instrument",
    "trombone": "Musical Instrument",

    "mountain": "Nature", "ocean": "Nature", "valley": "Nature", "desert": "Nature", "forest": "Nature",
    "river": "Nature", "waterfall": "Nature", "glacier": "Nature", "volcano": "Nature", "canyon": "Nature",

    "python": "Programming Language", "java": "Programming Language", "javascript": "Programming Language",
    "ruby": "Programming Language", "swift": "Programming Language", "csharp": "Programming Language",
    "kotlin": "Programming Language", "golang": "Programming Language", "rust": "Programming Language",
    "typescript": "Programming Language",

    "canada": "Country", "brazil": "Country", "germany": "Country", "france": "Country", "italy": "Country",
    "japan": "Country", "india": "Country", "mexico": "Country", "australia": "Country", "china": "Country"
}

__all__ = ["word_list", "stages", "logo", "hint_map"]