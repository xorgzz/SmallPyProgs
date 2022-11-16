from bs4 import BeautifulSoup
import requests
done = []
currs = ["PLN", "GBP", "EUR", "RUB"]

def curr_swap():
	for i in range(len(currs)):
		html_file =  requests.get("https://themoneyconverter.com/USD/%s"%(currs[i])).text
		soup = BeautifulSoup(html_file, "lxml")
		done.append(round(float(str(soup.find_all("h3")[1]).split()[-2]), 2))

curr_swap()

html_value = requests.get("https://coinmarketcap.com/currencies/bitcoin/").text
soup = BeautifulSoup(html_value, "lxml")
value = soup.find_all("div", attrs={"class" : "priceValue"})

btc_value = round(float(str(str(str(value[0]).split("<")[2]).split("$")[1]).split(",")[0] + str(str(str(value[0]).split("<")[2]).split("$")[1]).split(",")[1]), 2)

print("""
  ____    _______    _____ 
 |  _ \  |__   __|  / ____|
 | |_) |    | |    | |     
 |  _ <     | |    | |     
 | |_) |    | |    | |____ 
 |____/     |_|     \_____|
""")

print("\t╔══════════════════╗")
print("\t║%s\tUSD║"%(str(btc_value)))
for i in range(len(done)):
	print("\t╠══════════════════╣")
	print("\t║%s\t%s║"%(str(round(done[i] * btc_value, 2)), currs[i]))

print("\t╚══════════════════╝")


'''
╔═╗
║ ║
╚═╝
╠╣
'''