import Image, ImageEnhance

def main():

    filename ='BMP.jpg'
    image = Image.open( filename )
    size = width, height = image.size

    # Brightness, Contrast, Sharpness, Color

    enhancer = ImageEnhance.Contrast( image )
    image = enhancer.enhance( 2 )


    image.save( 'modified_' + filename)
    del image

if ( __name__ == '__main__'):
    main()

