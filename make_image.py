from PIL import Image

def main():
    l0 = Image.open('assets/H0.png')
    l1 = Image.open('assets/H1.png')
    l2 = Image.open('assets/H2.png')
    l3 = Image.open('assets/H3.png')
    l4 = Image.open('assets/H4.png')
    l5 = Image.open('assets/H5.png')
    l6 = Image.open('assets/H6.png')
    l7 = Image.open('assets/H7.png')
    l8 = Image.open('assets/H8.png')
    l9 = Image.open('assets/H9.png')
    # Assigns different opacities with the bottom layer having full opacity
    # and dropping the opacity down by 10% with each successive layer
    l1.putalpha(230)
    l2.putalpha(205)
    l3.putalpha(180)
    l4.putalpha(155)
    l5.putalpha(130)
    l6.putalpha(105)
    l7.putalpha(80)
    l8.putalpha(55)
    l9.putalpha(30)
    
    # Combine the layers into one image and save for the final result
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