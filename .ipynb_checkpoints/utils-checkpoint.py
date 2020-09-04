from PIL import Image
import glob
import matplotlib.pyplot as plt
import math
import os

def create_gif(image_folder, output_file, img_type='png',):
    # Create the frames
    frames = []

    # files need to be sorted from 1...n so that the video is played in correct sequence
    imgs = sorted(glob.glob(f'{image_folder}/*.{img_type}'))
    for i in imgs:
        new_frame = Image.open(i)
        frames.append(new_frame)
    
    # Save into a GIF file that loops forever
    frames[0].save(output_file, format='gif',
                append_images=frames[1:],
                save_all=True,
                duration=120, loop=0)

def plot_image(image):
    '''if image is a file, then open the file first'''
    image = Image.open(image)
    plt.imshow(image, cmap=plt.cm.gray, interpolation='nearest')
    plt.axis("off")
    
def display_images(images, max_per_row=5):
    nrows = math.ceil(len(images)/max_per_row)
    #fig = plt.figure(figsize=(max_per_row * 1.5, 3))
    for index, image in enumerate(images):
        plt.subplot(nrows, max_per_row, 1 + index)
        plot_image(image)
    #fig.save('fig.png')
    plt.show()
        
if __name__ == '__main__':
    print('hello')
    image_folder = r'C:\Users\kheng\.keras\datasets\UCSD_Anomaly_Dataset.v1p2\UCSDped1\Test\Test024'
    #create_gif(image_folder, 'mygif.gif', img_type='tif')

    images = []
    for i in range(10):
        images.append(os.path.join(image_folder, '{:03d}.tif'.format(i+1)))
    
    print(images)

    display_images(images, 2)