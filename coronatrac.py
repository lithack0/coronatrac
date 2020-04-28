import requests
import os
from pyfiglet import figlet_format
from termcolor import cprint
from pprint import pprint
cprint(figlet_format("\tCORONATRAC",font="standard"),"green",attrs=["bold","dark"])

u="https://api.covid19api.com/world/total"
r=requests.get(u)
count=0
j=r.json()

c=j["TotalConfirmed"]
s=str("                   "  +str(c))

cprint(figlet_format(s ,font="standard"),"red",attrs=["bold"])
print()			
print("\033[32;1m \t\t What You Want To Doo..!!!!" )
print()
print("\033[38;1m [1].Stats of Country[Last few updates(json)]")
print()
print("\033[35;1m [2].Stats of world(It will take more time)")
print()
print("\033[36;1m [3].Summary of New cases daily[World Wide]")
print()
print("\033[31;1m [4].All country Effect With this pandemic")
print()
print("\033[33;1m [5].Number of cases in World ")
print()
print("\033[32;1m [6].Current Stats of Country")
print()
print("\033[36;1m [7].Specific Data of Covid-19")
print()
print("\033[33;1m [8].Stats in Ascii Format!!")
print()
print("\033[35;1m [9].About Covid-19")
print()
print("\033[33;1m [*].ForAmerica it will show states")
print()
m=input("\033[32;1m Enter Your Input !! : ")
if m=="1" :
	print()
	c=input("\033[32;1mEnter the name of Country: " )
	
	u="https://api.covid19api.com/live/country/{}".format(c)
	r=requests.get(u)
	j=r.json()
	print()
	pprint( j)
elif m=="2":
	print()
	r=requests.get("https://api.covid19api.com/all")
	print()
	pprint(r.json())
elif m=="3":
	print()
	r=requests.get("https://api.covid19api.com/summary")
	print()
	pprint(r.json())
elif m=="4":
	print()
	r=requests.get(" https://api.covid19api.com/countries" )
	print()
	pprint(r.json())
elif m=="5":
	print()
	r=requests.get("https://api.covid19api.com/world/total")
	print()
	pprint(r.json())
elif m=="6":
	print()
	print("Enter the name of country")
	c=input(" ")
	u="https://api.covid19api.com/live/country/{}".format(c)
	r=requests.get(u)
	j=r.json()
	count=0
	for i in j:
		count+=1
	print()
	pprint(j[count-1])
elif m=="7":
	print()
	print("[1].Country Wise ")
	print()
	print("[2].World ")	
	a=input(" ")
	if a=="1":
		print("Enter the name of country")
		c=input(" ")
		print("\033[33;1m[a]Confirmed Case")
		print()
		print("\033[32;1m[b] Recovered Patient")
		print()
		print("\033[31;1m[c]Deaths")
		print()
		print("\033[33;1m[d]Active")
		ch=input("\033[32;1m ")
		if ch=="a":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print("\033[33;1m")
			pprint(j[count-1]["Confirmed"])
			
		elif ch=="b":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print("\033[32;1m")
			p=(j[count-1]["Recovered"])
			print(p)
			
		elif ch=="c":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print("\033[31;1m")
			pprint(j[count-1]["Deaths"])
		elif ch=="d":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print("\033[33;1m")
			pprint(j[count-1]["Active"])
	elif a=="2":
			print("[a]Confirmed Case")
			print()
			print("[b] Recovered Patient")
			print()
			print("[c]Deaths")
			print()
			ch=input(" ")
			if ch=="a":
				count=0
				r=requests.get("https://api.covid19api.com/world/total")
				j=r.json()
				for i in j:
					count+=1
				print("\033[33;1m")
				pprint(j["TotalConfirmed"])
			elif ch=="b":
				count=0
				r=requests.get("https://api.covid19api.com/world/total")
				j=r.json()
				for i in j:
					count+=1
				print("\033[32;1m")
				pprint(j["TotalRecovered"])
			elif ch=="c":
				count=0
				r=requests.get("https://api.covid19api.com/world/total")
				j=r.json()
				for i in j:
					count+=1
				print("\033[31;1m")
				pprint(j["TotalDeaths"])
elif m=="8":
	print()
	print("[1].Country Wise ")
	print()
	print("[2].World ")	
	a=input(" ")
	if a=="1":
		print("Enter the name of country")
		c=input(" ")
		print("\033[33;1m[a]Confirmed Case")
		print()
		print("\033[32;1m[b] Recovered Patient")
		print()
		print("\033[31;1m[c]Deaths")
		print()
		print("\033[33;1m[d]Active")
		print("\033[32;1m")
		ch=input(" ")
		if ch=="a":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print()
			cn=j[count-1]["Confirmed"]
			s=str("                   "  +str(cn))
			cprint(figlet_format(s,font="standard"),"yellow",attrs=["bold"])
			
		elif ch=="b":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print()
			rec=j[count-1]["Recovered"]
			s=str("                   "  +str(rec))
			cprint(figlet_format(s,font="standard"),"green",attrs=["bold"])
			
		elif ch=="c":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print()
			d=j[count-1]["Deaths"]
			s=str("                   "  +str(d))
			cprint(figlet_format(s,font="standard"),"red",attrs=["bold"])
		elif ch=="d":
			u="https://api.covid19api.com/live/country/{}".format(c)
			r=requests.get(u)
			count=0
			j=r.json()
			for i in j:
				count+=1
			print()
			a=j[count-1]["Active"]
			s=str("                   "  +str(a))
			cprint(figlet_format(s,font="standard"),"yellow",attrs=["bold"])
	elif a=="2":
			print("\033[33;1m[a]Confirmed Case")
			print()
			print("\033[32;1m[b] Recovered Patient")
			print()
			print("\033[31;1m[c]Deaths")
			print("\033[32;1m")
			ch=input(" ")
			if ch=="a":
				count=0
				r=requests.get("https://api.covid19api.com/world/total")
				j=r.json()
				for i in j:
					count+=1
				print()
				cn=j["TotalConfirmed"]
				s=str("                   "  +str(cn))
				cprint(figlet_format(s,font="standard"),"yellow",attrs=["bold"])
			elif ch=="b":
				count=0
				r=requests.get("https://api.covid19api.com/world/total")
				j=r.json()
				for i in j:
					count+=1
				print()
				rec=j["TotalRecovered"]
				s=str("                   "  +str(rec))
				cprint(figlet_format(s,font="standard"),"green",attrs=["bold"])
			elif ch=="c":
				count=0
				r=requests.get("https://api.covid19api.com/world/total")
				j=r.json()
				for i in j:
					count+=1
				print()
				d=j["TotalDeaths"]
				s=str("                   "  +str(d))
				cprint(figlet_format(s,font="standard"),"red",attrs=["bold"])
if m=="9":
	print("\033[32;1m ")
	print("\033[33;1m[1]Information about Covid-19[scientific]")
	print()
	print("\033[35;1m[2]Best Tracking map in gui of Covid-19")
	print("\033[32;1m")
	ch=input(" ")
	if ch=="1":
		print("\033[33;1m[a]Basic information")
		print("\033[35;1m")
		print("[b] Best YouTube videos")
		print()
		print("\033[32;1m[c]MythBuster !!")
		ch1=input("\033[32;1m ")
		if ch1=="a":
			print("\033[33;1m")
			o=os.system("echo The virus that causes covid-19 is known as SARS-CoV-2. It appears to have first emerged in Wuhan, China, in late 2019. The outbreak has since spread across China to other countries around the world. By the end of January, the new coronavirus had been declared a public health emergency of international concern by the WHO.The most commonly reported symptoms include a fever, dry cough and tiredness, and in mild cases people may get just a runny nose or a sore throat. In the most severe cases, people with the virus can develop difficulty breathing, and may ultimately experience organ failure. Some cases are fatal.Coronaviruses replicate their RNA genomes using enzymes called RNA-dependent RNA polymerases, which are prone to errors, but genomic analysis so far suggests that covid-19 is mutating slowly, reducing the chance of it changing to become more deadly.There are currently no vaccines or specific drug treatments for coronaviruses, but efforts to develop a vaccine are underway and HIV and Ebola drugs are being tested in people with covid-19.On 18 March, the World Health Organization [WHO] said they had begun a trial of the most promising drugs, including the long-used antimalarial drugs chloroquine and hydroxychloroquine, a new antiviral drug called remdesivir and a combination of two HIV drugs called lopinavir and ritonavir. The HIV drugs will also be tested in combination with an antiviral called interferon beta.On 22 March, several countries in Europe, including the UK, launched a collaborative trial of the same drugs, which will complement the WHO effort.Many other potential treatments are being explored, particularly the possibility of giving people a dose of antibodies against covid-19, a strategy being explored with a clinical trial run by Johns Hopkins University. | pv -qL 10")
		elif ch1=="b":
			print()
			print("\033[33;1mhttps://m.youtube.com/watch?v=fgBla7RepXU&t=5s")
			print("https://m.youtube.com/watch?v=ls8P68lqwWQ")
			print("https://m.youtube.com/watch?v=wfPF6_KRR_U")
			print("https://m.youtube.com/watch?v=qf3Ih0kNvlU&t=184s")
			print("https://m.youtube.com/watch?v=va6j4JITJoE")
		elif ch1=="c":
			print("\033[32;1m")
			o=os.system("echo *WHO Myth-busters*There is a lot of false information around. These are the facts.People of all ages CAN be infected by the coronavirus. Older people, and people with pre-existing medical conditions [such as asthma, diabetes, heart disease] appear to be more vulnerable to becoming severely ill with the virus. Cold weather and snow CANNOT kill the coronavirus.The coronavirus CAN be transmitted in areas with hot and humid climatesThe coronavirus CANNOT be transmitted through mosquito bites.There is NO evidence that companion animals/pets such as dogs or cats can transmit the coronavirus.Taking a hot bath DOES NOT prevent the coronavirus Hand dryers are NOT effective in killing the coronavirus.Ultraviolet light SHOULD NOT be used for sterilization and can cause skin irritation.Thermal scanners CAN detect if people have a fever but CANNOT detect whether or not someone has the coronavirus. Spraying alcohol or chlorine all over your body WILL NOT kill viruses that have already entered your body.Vaccines against pneumonia, such as pneumococcal vaccine and _Haemophilus influenzae_ type b [Hib] vaccine, DO NOT provide protection against the coronavirus.There is NO evidence that regularly rinsing the nose with saline has protected people from infection with the coronavirus. Garlic is healthy but there is NO evidence from the current outbreak that eating garlic has protected people from the coronavirus.Antibiotics DO NOT work against viruses, antibiotics only work against bacteria.To date, there is NO specific medicine recommended to prevent or treat the coronavirus.| pv -qL 10")
	elif ch=="2":
		print("\033[33;1m")
		print("https://thenextweb.com/corona/2020/03/10/best-coronavirus-dashboards-map-spread-covid-19/")
		print("https://www.google.com/amp/s/www.geospatialworld.net/blogs/here-are-some-of-the-best-maps-tracking-coronavirus-updates/amp/")
