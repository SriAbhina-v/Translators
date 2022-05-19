import requests
def runCode():
    wordToTrans = input('Word: ')
    startLang = 'en'
    endLang = 'fr'
    finalURL = 'https://www.wordreference.com/' + startLang + endLang + '/' + wordToTrans.lower()
    req = requests.get(finalURL, 'html.parser')
    if (req.text.find('<meta name="description" content="')):
        ttx = req.text.split("<td class='ToWrd' >")[1]
        print('French Translation: ' + ttx.split('<')[0])
        x = req.text.split('<meta name="description" content="')[1]
        z = req.text.split("<span dir='ltr'>")[3]
        a = z.split("<")[0]
        print("\n")
        print('Example: ' + a)
    runCode()
runCode()