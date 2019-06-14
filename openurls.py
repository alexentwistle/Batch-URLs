import webbrowser

websites = [input("Please enter your first URL: \n"),input("Please enter your second URL: \n")]

for url in websites:
    webbrowser.open(url)