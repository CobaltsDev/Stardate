from datetime import date, timedelta
d = date.today()
ys = int(d.year) - 1
ystart = date(ys, 12, 31)
dstart = date(1999, 12,31)
td = d - dstart
tdn = d - ystart
sd = str(d.year) + "." + str(tdn)[:3]
cent = int(d.year/100) + 1
c = str(cent)[1]
ysd = (d - dstart).days
yq = 0
if ysd <= 9999:
    yq = 1
elif ysd > 9999 and ysd <= 19998:
    yq = 2
    ysd -= 9999
elif ysd > 19998 and ysd <= 29997:
    yq = 3
    ysd -= 19998
elif ysd > 29997 and ysd <= 39996:
    yq = 4
    ysd -= 29997
sdng = c + str(yq) + str(ysd)[:3] + "." + str(ysd)[3:]
print("Stardate:")
print(sdng)
print("---OR---")
print(sd)
