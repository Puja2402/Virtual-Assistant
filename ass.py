import wolframalpha
import wikipedia
while True:
    i=input("Question?")
    try:
        app_id="48YTK8-XKQ88L97YK"
        client=wolframalpha.Client(app_id)
        res=client.query(i)
        answer=next(res.results).text
        print(answer)
    except:
        print(wikipedia.summary(i,sentences=2))
