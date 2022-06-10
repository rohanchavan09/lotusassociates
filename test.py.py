import qrcode
link1="https://www.google.com/search?q=best+python+book&source=lnms&tbm=bks&sa=X&ved=2ahUKEwit_-X2kNT3AhVJy4sBHU7ZBwUQ_AUoAXoECAIQCw&biw=1366&bih=657&dpr=1"
link2="ka hi hi pan"

img1=qrcode.make(link1)
img2=qrcode.make(link2)

img1.save("D:\python_class\new python class\link1.png")
img2.save("D:\python_class\new python class\link2.png")
