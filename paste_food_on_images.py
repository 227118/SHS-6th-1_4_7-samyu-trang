import PIL
import matplotlib.pyplot as plt # single use of plt is commented out
import os.path  
import PIL.ImageDraw            

def get_images(directory=None):
    """ Returns PIL.Image objects for all the images in directory.
    
    If directory is not specified, uses current directory.
    Returns a 2-tuple containing 
    a list with a  PIL.Image object for each image file in root_directory, and
    a list with a string filename for each image file in root_directory
    """
    
    if directory == None:
        directory = os.getcwd() # Use working directory if unspecified

        
    image_list = [] # Initialize aggregaotrs
    file_list = []
    
    directory_list = os.listdir(directory) # Get list of files
    for entry in directory_list:
        absolute_filename = os.path.join(directory, entry)
        try:
            image = PIL.Image.open(absolute_filename)
            file_list += [entry]
            image_list += [image]
        except IOError:
            pass # do nothing with errors tying to open non-images
    return image_list, file_list
   
def paste_all_images(foodType='noodles', directory='none'):
    directory = os.getcwd()
    #new modified directory
    new_directory = os.path.join(directory, 'modified')
    try:
        os.mkdir(new_directory)
    except OSError:
        pass # if the directory already exists, proceed.
        
    #load all the images
    image_list, file_list = get_images(directory)
    
    #go through the images and save the odified versions
    for n in range(len(image_list)):
        #parse the filename
        filename, filetype = os.path.splitext(file_list[n])
        
        #frame the images~/Documents/GitHub/SHS-6th-1_4_7-samyu-trang/Background pic
        new_image = paste_food(image_list[n], foodType)
        #save altered image
        new_image_filename = os.path.join(new_directory, filename + '.png')
        new_image.save(new_image_filename)
        

def paste_food(original_image, foodType):
    width, height = original_image.size #get size of image
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0)) #create new image starting w blank image
    result.paste(original_image, (0,0)) #paste background img
    food = PIL.Image.open(os.path.join(os.getcwd(), foodType + '.png')) #open food image desired by user
    food = food.resize((width, height)) #resize food img
    result.paste(food, (0,0), mask=food) #paste food img over background
    
  
    return result #return new picture
    
    result = PIL.Image.new('RGBA', original_image.size, (0,0,0,0))
    