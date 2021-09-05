#- รับ h m s --> คำนวณวินาที
print("*** Converting hh.mm.ss to seconds ***")
h,m,s = map(int,input("Enter hh mm ss : ").split())
if m >= 60 or m < 0:
    print("mm("+str(m)+") is invalid!")
else:
    second = int(h) * 3600 + int(m) * 60 + int(s)
    print('{:02d}:{:02d}:{:02d} = {:,d} seconds'.format(h,m,s,second))
