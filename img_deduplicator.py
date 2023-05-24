import os
import numpy as np
from PIL import Image
from tqdm import tqdm
import glob

class ImageDeduplicator:
    def __init__(self, reference_image = None, target_images = './'):
        self.target_images = glob.glob(target_images)
        self.reference_image = reference_image
        self.removed = 0

        if reference_image is not None:
            print(f'Attmepting to remove all images identical to {self.reference_image}.')
            self.reference_image = np.array(Image.open(self.reference_image))
            self.removeCopiesOf(self.reference_image)
            print(f'Succesfully removed {self.removed} duplicate images.')
        else:
            print(f'Attempting to remove all duplicate images.')
            self.deduplicateAll()
            print(f'Succesfully removed {self.removed} duplicate images.')

    def removeCopiesOf(self, reference_image, target_images = None):
        if target_images is None:
            target_images = self.target_images

        for img in tqdm(target_images):
            if np.array_equal(reference_image, np.array(Image.open(img))):
                os.remove(img)
                self.removed+=1
    
    def deduplicateAll(self):
        self.target_images
        while tqdm(len(self.target_images)):
            next_image = self.target_images.pop()
            print(f'Images left: {len(self.target_images)}')

            for idx, img in tqdm(enumerate(self.target_images)):
                if np.array_equal(np.array(Image.open(next_image)), np.array(Image.open(img))):
                    self.target_images.pop(idx)
                    os.remove(img)
                    self.removed+=1
        print(f'Succesfully removed {self.removed} duplicate images.')


ImageDeduplicator(target_images= './sprite/*.png')