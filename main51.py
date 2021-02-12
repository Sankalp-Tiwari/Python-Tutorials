def searcher():
    import time
    time.sleep(2)
    book = "Kabhi-Kabhi lagta hai ki apunich bhagwaana hai"

    while True:
        text = (yield)
        if text in book:
            print("Text is in the book")
        else:
            print("Text is not in the book")

search = searcher()
next(search)
search.send("Kabhi")
input()
search.send("lagta")