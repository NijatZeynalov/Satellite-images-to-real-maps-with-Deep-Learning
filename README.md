# Satellite Images to real maps with Deep Learning (and reverse)
In this project, I developed a Pix2Pix generative adversarial network for image-to-image translation. I have used the so-called maps dataset used in the Pix2Pix paper. The Pix2Pix model is a type of conditional GAN, or cGAN, where the generation of the output image is conditional on an input, in this case, a source image. The image translation problem involves converting satellite photos to Google maps format, or the reverse, Google maps images to Satellite photos.


After preparing dataset, I developed Pix2Pix model. The same model architecture and configuration described in the paper was used across a range of image translation tasks. 
Models are saved every 10 epochs and saved to a file with the training iteration number. Additionally, images are generated every 10 epochs and compared to the expected target images. In this case, we can see that the generated image captures large roads with orange and yellow as well as green park areas. The generated image is not perfect but is very close to the expected image.


<a href="https://static.wixstatic.com/media/c11292_aa019eb3a98b4f12ae443bc04d83afb4~mv2.png/v1/fill/w_740,h_553,al_c,lg_1,q_90/c11292_aa019eb3a98b4f12ae443bc04d83afb4~mv2.webp"><img src="https://static.wixstatic.com/media/c11292_aa019eb3a98b4f12ae443bc04d83afb4~mv2.png/v1/fill/w_740,h_553,al_c,lg_1,q_90/c11292_aa019eb3a98b4f12ae443bc04d83afb4~mv2.webp" title="made at imgflip.com"/></a>

We may also want to use the model to translate a given standalone image.I used Baku Central Park image as input and save the file as k.png in the current working directory. We must load the image as a NumPy array of pixels with the size of 256 × 256, rescale the pixel values to the range [-1,1], and then expand the single image dimensions to represent one input sample. 


<a href="https://static.wixstatic.com/media/c11292_30034af6cae44e82b09d1a96b62b2b51~mv2.png/v1/fill/w_740,h_292,al_c,q_90,usm_0.66_1.00_0.01/c11292_30034af6cae44e82b09d1a96b62b2b51~mv2.webp"><img src="https://static.wixstatic.com/media/c11292_30034af6cae44e82b09d1a96b62b2b51~mv2.png/v1/fill/w_740,h_292,al_c,q_90,usm_0.66_1.00_0.01/c11292_30034af6cae44e82b09d1a96b62b2b51~mv2.webp" title="made at imgflip.com"/></a>


The generated image appears to be a reasonable translation of the source image. The streets do not appear to be straight lines and the detail of the buildings is a bit lacking. __We have reduced the number of epochs on paper by 4 times and of course it is not right to expect great results. It is possible to generate very high quality images by making the number of epochs 150 or using different models.__

After this,  I developed a Pix2Pix model to translate Google Maps images to plausible satellite images. This requires that the model invent (or hallucinate) plausible buildings, roads, parks, and more. Image quality improves over the training process. For translating standalone Google Maps images to satellite images, I changed the order of the datasets.

I decided to convert unrealistic maps to satellite images to make my project more interesting. I used the oskarstalberg.com site to create unrealistic maps. Each time you tap the screen on this site, a city map is generated which is not exist in the real world. 


<a href="https://static.wixstatic.com/media/c11292_4b312377c1284cf5a142bfb80a979bcb~mv2.gif"><img src="https://static.wixstatic.com/media/c11292_4b312377c1284cf5a142bfb80a979bcb~mv2.gif"/></a>


After taking screenshot of random unrealistic map, I rescaled pixel values to 256 × 256. As before, we can load our saved Pix2Pix generator model and generate a translation of the loaded image. Finally, we can scale the pixel values back to the range [0,1] and plot the result.

![seher](https://user-images.githubusercontent.com/31247506/89767860-71de4b80-db03-11ea-96c0-b36f3085c75e.PNG)


We can continue training the model for another 100 epochs and evaluate whether the additional training results in further improvements in image quality.

You can read my [blog post](https://www.nijatzeynalov.com/post/d%C9%99rin-%C3%B6yr%C9%99nm%C9%99-il%C9%99-peykd%C9%99n-g%C9%99l%C9%99n-foto%C5%9F%C9%99kill%C9%99ri-real-x%C9%99rit%C9%99l%C9%99r%C9%99-%C3%A7evirm%C9%99-pix2pix-neyron-%C5%9F%C9%99b%C9%99k%C9%99-modeli) related to this project.
