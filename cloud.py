'''pip install matplotlib
pip install pandas
pip install wordcloud
pip install fileupload
pip install ipywidgets
jupyter nbextension install --py --user fileupload
jupyter nbextension enable --py fileupload'''

import wordcloud
from PIL import Image
import numpy as np
from matplotlib import pyplot as plt
from wordcloud import ImageColorGenerator
from IPython.display import display
#import fileupload
import io
import sys

'''def _upload():

    _upload_widget = fileupload.FileUploadWidget()

    def _cb(change):
        global file_contents
        decoded = io.StringIO(change['owner'].data.decode('utf-8'))
        filename = change['owner'].filename
        print('Uploaded `{}` ({:.2f} kB)'.format(
            filename, len(decoded.read()) / 2 **10))
        file_contents = decoded.getvalue()

    _upload_widget.observe(_cb, names='data')
    display(_upload_widget)

_upload()'''
#str=input("Enter name of file : ")
file_contents=open("pandp.txt", "r").read()
def similar_color_func(word=None, font_size=None, position=None, orientation=None,font_path=None, random_state=None):
	h = 275 # use values within (0 - 360)
	s = 86 # use values within (0 - 100)
	l = random_state.randint(20, 70) #values defining the darkness of shades varying in the range (0 - 100)
	return "hsl({}, {}%, {}%)".format(h, s, l)
def calculate_frequencies(file_contents):
    # Here is a list of punctuations and uninteresting words that are omitted from wordcloud text. Feel free to add more words here
    punctuations = '''!()-[]{};:'"<>./?@#$%^&*_~'''
    uninteresting_words = ["the", "a", "to", "if", "is", "it","so","see","most","would","i","in","you","mr","mrs", "of", "and","on","for", "or", "an", "as", "i", "me", "my", \
    "we", "our", "ours", "you", "your", "yours", "he", "she", "said","say","told","tell","him", "his", "her", "hers", "its", "they", "them", \
    "their", "what", "which", "who", "whom", "this", "that", "am", "are", "was", "were", "be", "been", "being", \
    "have", "has", "had", "do", "does", "did", "but", "at","much","there","one","two", "by", "with", "from", "here", "when", "where", "how", \
    "all", "any", "both","must","know", "each", "few", "more", "some", "not","such", "no", "nor", "too", "very", "can", "will", "just"]
    lst=file_contents.split()
    freq={}
    #the loop moves through every word in file and removes puctuation signs and then adds them to dictionary
    for word in lst:
        new_word=""
        for letter in word:
            if letter.isalpha():
                new_word=new_word+letter
        if new_word.lower() in uninteresting_words:
            continue
        elif new_word in freq:
            freq[new_word]=freq[new_word]+1
        else:
            freq[new_word]=0
    #provide the path to the image whose outline is to be used inside "Image.open" 
    mask=np.array(Image.open('heart.jpg'))
    #for the font, make sure you have this font downloaded or it'll show an error. Use this site to download fonts for personal use #for the font, make sure you have this font downloaded or it'll show an error. Use this site to download fonts for personal use (https://www.dafont.com/) and copy the path of the downloaded file under font_path
    #you can set h,s values of colour in similar_color_func to change the shade
    #or use ImageColorGenerator(mask) in that place to set the color to the color of image in use
    #set background color to liking  
    cloud = wordcloud.WordCloud(font_path='BrightlyCrushShine.otf',color_func= similar_color_func,background_color="white",mask=mask)
    cloud.generate_from_frequencies(freq)
    return cloud.to_array()

myimage = calculate_frequencies(file_contents)
plt.imshow(myimage, interpolation = 'bilinear')
plt.axis('off')
plt.show()
