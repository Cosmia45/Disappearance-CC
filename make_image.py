from PIL import Image

def main():
    l0 = Image.open('images/H0.png')
    l1 = Image.open('images/H1.png')
    l2 = Image.open('images/H2.png')
    l3 = Image.open('images/H3.png')
    l4 = Image.open('images/H4.png')
    l5 = Image.open('images/H5.png')
    l6 = Image.open('images/H6.png')
    l7 = Image.open('images/H7.png')
    l8 = Image.open('images/H8.png')
    l9 = Image.open('images/H9.png')
    l1.putalpha(230)
    l2.putalpha(205)
    l3.putalpha(180)
    l4.putalpha(155)
    l5.putalpha(130)
    l6.putalpha(105)
    l7.putalpha(80)
    l8.putalpha(55)
    l9.putalpha(30)
    
    l0.paste(l1, (0,0), l1)
    l0.paste(l2, (0,0), l2)
    l0.paste(l3, (0,0), l3)
    l0.paste(l4, (0,0), l4)
    l0.paste(l5, (0,0), l5)
    l0.paste(l6, (0,0), l6)
    l0.paste(l7, (0,0), l7)
    l0.paste(l8, (0,0), l8)
    l0.paste(l9, (0,0), l9)
    l0.save("examples/sample.png")
main()