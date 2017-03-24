import Image, ImageEnhance

def main():

    filename ='BMP.jpg'
    image = Image.open( filename )
    size = width, height = image.size

    sized_image = image.resize((int(width * 2), int(height * 2)))


    sized_image.save( 'modified_size' + filename)
    del image

if ( __name__ == '__main__'):
    main()

