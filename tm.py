

s = "https://www.transfermarkt.co.in/premier-league/formtabelle/wettbewerb/GB1?saison_id=2017&min=1&max=1"
for i in range(1,38):

    print(s[0:len(s) - 1] + str(i))
