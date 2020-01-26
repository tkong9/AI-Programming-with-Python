# HINT: modify the headlines list to verify your loop works with different inputs
headlines = ["Local Bear Eaten by Man",
             "Legislature Announces New Laws",
             "Peasant Discovers Violence Inherent in System",
             "Cat Rescues Fireman Stuck in Tree",
             "Brave Knight Runs Away",
             "Papperbok Review: Totally Triffic"]

news_ticker = ""
i = 0
j = 0
# write your loop here
while len(news_ticker) < 140:
    if len(news_ticker) + len(headlines[i]) > 140:
        while len(news_ticker) < 140:
            news_ticker = news_ticker + headlines[i][j]
            j += 1
    else:
        news_ticker = news_ticker + headlines[i] + " "
        i += 1
print(news_ticker)