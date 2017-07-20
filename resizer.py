import PIL
from PIL import Image
import os
path = '/home/gul/data/train/'
files = os.listdir(path)
i = 1
basewidth = 128

hsize = 128
arr=["Barnett Newman", "Ernst Ludwig Kirchner","Ferdinand Hodle","Ferdinand Hodler","Franz Richard Unterberger","Heinrich Schonfeld","Hieronymus Bosch","Hiroshige","Ivan Aivazovsky","Judith Leyster","Koloman Moser", "Konstantin Vasilyev","Lorenzo Lotto","Mario Tozzi","Nicolas Poussin","Rembrandt","Titian", "Utagawa Kunisada","Utagawa Kunisada II","William-Adolphe Bouguereau","Wolfgang Paalen"]
print len(arr)
# for file in files:
# 	img = Image.open(path+file)..convert('RGB')

    
# 	img = img.resize((basewidth, hsize), PIL.Image.ANTIALIAS)
# 	img.save('/home/gul/data/resized/'+file);
