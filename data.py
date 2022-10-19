import csv
# create lists to store different types of self care techniques
# source: 
# https://www.buzzfeed.com/stephhallett/how-to-calm-down-when-angry
# https://eugenetherapy.com/article/50-self-care-ideas-for-a-bad-day/

happy = [
    "create something, maybe paint something?", 
    "cook yourself or your loved ones food to express your love to them",
    "dance along with your favorite songs",
    "do some workout to feel more alive",
    "hang out with friends",
    "make a playlist of your favorite songs",
    "write down 5 things you’re grateful for"
    ]

overwhelmed = [
    "get some rest, take a nap maybe?",
    "write your feelings out, get them out from your head to paper",
    "reach out for help, is there anyone who is able to help you in this situation?",
    "meditate with your favorite crystals",
    "get into your body and do some yoga",
    "take some deep breaths to sooth your nervous system",
    "call or text your trusted friends and express how you feel",
    "change your channel, maybe accomplish something different?",
    "do a digital detox"
 ]

stressed = [
    "go for a long walk in nature",
    "go to the beach and listen to the waves",
    "watch the sunset",
    "sit and be still for 10 minutes",
    "do a full-body scan",
    "spend some time with your animal",
    "take a few deep breaths",
    "plan a vacation or a short getaway trip"

]
anxious = [
    "take some deep breaths",
    "light your favorite candle",
    "read a book",
    "turn on a diffuser with your favorite essential oils",
    "sleep with a weighted blanket",
    "distance yourself from the news",
    "do some yoga or just move your body"
]

sad = [
    "watch your favorite show",
    "go for a drive (no destination required)",
    "practice yoga",
    "let yourself have a good cry (sometimes we need it)",
    "take a break from the news",
    "cuddle with your animal",
    "do something that'll make you happy",
    "write down your feelings"
]

angry = [
    "journal about how you’re feeling",
    "find a pillow and yell all the terrible things in your head into the pillow",
    "go running or do your favorite exercise",
    "do a body scan and release the tension in your body",
    "check in with yourself",
    "watch something funny",
    "identify other emotions that your anger may be masking"
]

tired = [
    "turn your phone off for a bit and try a new face mask",
    "do some stretching",
    "get some sleep",
    "take a bath or shower",
    "implement a morning and night routine you enjoy",
    "sleep with a weighted blanket",
    "go for a long walk in nature",
    "burn your favorite herb/incense"
]

depressed = [
    "go to your favorite place",
    "consider a walk around the block",
    "organize or rearrange your space",
    "put on an outfit that makes you feel good",
    "get some fresh air and drink some water",
    "do the opposite of what the 'depression voice' suggests",
    "implement a morning and night routine you enjoy",
]

excited = [
    "cook or order in your favorite meal",
    "try learning something new",
    "bake a delicious treat",
    "share your excitement with your loved ones",
    "dance with your favorite song",
    "sing!",
    "watch a good movie",
    "go for a drive (no destination required)"
]

# add movies from csv
movies = []

with open("WATCHLIST.csv") as file:
    reader = csv.DictReader(file)
    for row in reader:
        movies.append(row["Title"])


