from serpapi import GoogleSearch

try:
    framedID = int(input("Paste video link here: (Use ctrl+shift+v)\n").split("=")[1]) + 5
except:
    print("Something went wrong. Please try again later.")

params = {
  "engine": "google_lens",
  "country": "us",
  "num": '50',
  "url": "",
  "api_key": "YOUR API KEY HERE",
  "output": 'JSON'
}

attnum = 1
maxatt = 5
def attemptSearch(attnum,framedID):
    params["url"] = "https://framed.wtf/images/" + str(framedID) + "/00" + str(attnum) + ".jpeg?w=1920&q=75"
    search = GoogleSearch(params)
    results = search.get_dict()
    visual_matches = results["visual_matches"]
    guess = ""
    for e in visual_matches:
        if ("bluscreens") in e['link'] or "imdb" in e['link'].lower() or "fancaps" in e['link'].lower() or "fandom" in e['link'] or "fanpop" in e['link'].lower():
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
attemptSearch(attnum,framedID)
