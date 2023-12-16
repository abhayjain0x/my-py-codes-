import os 
from dotenv import load_dotenv
print("Welcomne to The Auction Program Bois , Let the Best Bet Win ! ")

hammer = '''

           __      Silence, please!
          (_()  Watch very closely, now....
           ||           /
      \__/ /)     \__/ /
      (_o)//      (oo)
      ( \\/_     //~~\\
       \_\__)____\\__//______
       ||| |                 |
   __  ||| |                 | _______
   ___(_(_)|_________________|______jro


'''

print(hammer)

import requests




load_dotenv()

bid_is_on = True 
bids = {}
while bid_is_on:
    name = input("What is your name ? ")
    bid = int(input("What is your bid ? $"))

    bids[name] = bid

    continue_bid = input("Are there any other bidders ? (y/n) ").lower()

    if continue_bid == "n":
        highest_bid = 0 
        for bidder in bids:
            bid_amount = bids[bidder]
            if bid_amount > highest_bid:
                highest_bid = bid_amount
                winner = bidder
        print(f"The winner is {winner} with a bid of ${highest_bid}")

        CHUNK_SIZE = 1024
        url = "https://api.elevenlabs.io/v1/text-to-speech/21m00Tcm4TlvDq8ikWAM"

        headers = {
        "Accept": "audio/mpeg",
        "Content-Type": "application/json",
        "xi-api-key": os.getenv("API_KEY")
        }

        data = {
            "text": f"The winner is {winner} with a bid of ${highest_bid}",
            "model_id": "eleven_monolingual_v1",
            "voice_settings": {
            "stability": 0.5,
            "similarity_boost": 0.5
            }
        }

        import pygame 
        
        pygame.mixer.init()

        response = requests.post(url, json=data, headers=headers)
        with open('output.mp3', 'wb') as f:
            for chunk in response.iter_content(chunk_size=CHUNK_SIZE):
                if chunk:
                    f.write(chunk)

        pygame.mixer.music.load("output.mp3")
        pygame.mixer.music.play()
        while pygame.mixer.music.get_busy() == True:
            continue
        bid_is_on = False

    elif continue_bid == "y":
        os.system("clear")



