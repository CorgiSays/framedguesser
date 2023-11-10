from serpapi import GoogleSearch
from datetime import datetime

params = {
  "engine": "google_lens",
  "country": "us",
  "num": '50',
  "url": "",
  "api_key": "c148c9b52dfc8b81ff1106fed45c116c22567c1be73753ac8a98134f5c83c81c",
  "output": 'JSON'
}

attnum = 1
maxatt = 5
def attemptSearch(attnum,framedID):
    params["url"] = "https://framed.wtf/images/" + str(framedID) + "/00" + str(attnum) + ".jpeg?w=1920&q=75"
    search = GoogleSearch(params)
    print("Loaded image from link: " + params["url"] + "\n")
    results = search.get_dict()
    visual_matches = results["visual_matches"]
    guess = ""
    for e in visual_matches:
        if ("bluscreens") in e['link'] or ("imdb" in e['link'].lower() and "list" not in e['link'] and "thread" not in e['link'] and "name" not in e['link']) or "fancaps" in e['link'].lower() or "fandom" in e['link'] or "fanpop" in e['link'].lower():
            guess = e['title']
            break
    if guess == "":
        print("I am not sure what the movie is. (Attempt " + str(attnum) + " of " + str(maxatt) + ")")
        if attnum <= maxatt:
            attemptSearch(attnum+1,framedID)
        else:
            print("I am not sure what the movie is.")
    else:
        print("I believe the movie is: " + guess.strip("- bluscreens").strip("Image Gallery of").strip("| Fancap"))
        if input("Was this correct? (Y/N)\n") == "N":
            attemptSearch(attnum+1,framedID)

try:
    val = input("Paste video link here: (Use ctrl+shift+v)\n")
    if val == "https://framed.wtf/":
        dateNow = datetime.now().date()
        refDate = datetime(year=2023, month=11, day=9).date()
        diffAdj = dateNow - refDate
        framedID = 613 + (int(str(diffAdj).split(" ")[0]))
    else:
        framedID = int(val.split("=")[1]) + 5
    attemptSearch(attnum,framedID)
except:
    print("Unable to identify movie at this time.")
