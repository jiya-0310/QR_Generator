import qrcode as qr
a = input("enter your link:")
img = qr.make(a)
savename = input("enter name for file (use .png) :",a,".png")
img.save(savename)
