---
title: "Unblurring Images - Deconvolution and the Frequency Domain"
source: "https://maxvanleeuwen.com/project/unblurring-images/"
author:
published: 2026-02-25
created: 2026-05-02
description: "Blurring is not safe. Very often, information underneath can be revealed. I'll explain how this works, and which blur types are best to use!"
tags:
  - "clippings"
---
![Unblurring Optical Defocus](https://maxvanleeuwen.com/wp-content/uploads/Unblurring-Optical-Defocus.gif) ![Mona Lisa - Deconvolution](https://maxvanleeuwen.com/wp-content/uploads/Mona-Lisa-Deconvolution.gif)

Don’t trust blurs to hide sensitive information. It is always (partially) reversible.

That doesn’t mean all blurs can be undone, but some information can be retrieved, making them unsuitable for anonymizing.

All experiments are my own, and I’ll go over the basics of deconvolution, Fourier transforms, and why some blur types are ‘safer’ than others!

My aim is to explain things in a simplified and intuitive way, with links to additional sources for those interested in diving deeper.

![](https://www.youtube.com/watch?v=8sTunOm3lJg)

*Debuting my new catchphrase: “if I can do this, imagine what a smart person can do”*

## Is It Real?

Yes – but the success rate depends on the type of blur.

Some are more difficult, like *Gaussian*, and the *Adobe AE Fast Box Blur* effect (at default settings).

Others can be unblurred surprisingly well. It’s eerie. For example: *Box Blur, Triangle/Hexagon/ $n$ -gon Blur*, *AE Camera Lens Blur*, and even optical defocus (depending on the lens).

Compression, noisiness and distortion make the deconvolution process more difficult, but these effects can often be mitigated.

![Unblurring Optical Defocus](https://maxvanleeuwen.com/wp-content/uploads/Unblurring-Optical-Defocus.gif) ![Optical Defocus - Wiener Deconvolution](https://maxvanleeuwen.com/wp-content/uploads/Optical-Defocus-Wiener-Deconvolution.jpg)

*Unblurring optically defocused video. Shot with my Fuji XT-3 (XC35mm F2)*

![iPhone Deconvolve - unblurring optical defocus](https://maxvanleeuwen.com/wp-content/uploads/iPhone-Deconvolve.jpg)

*Similar result with an out-of-focus iPhone 13 Pro.*

Some blurs destroy more information than others. In the age of surveillance software and machine learning, I think it’s best to assume some information will always be retrievable.

*![safely blurring a face](https://maxvanleeuwen.com/wp-content/uploads/Fake-Face-Underneath.gif)*

*If want to blur a face safely, just slide a fake one underneath:)*

![Captain Disillusion Unblur Challenge - Wiener Deconvolution](https://maxvanleeuwen.com/wp-content/uploads/Captain-Disillusion-Unblur-Challenge-Wiener-Deconvolution.jpg)

The Captain used *AE Fast Box Blur* (3 iterations), which is more difficult to deconvolve even with high-contrast text. More about this below.

Even if this example doesn’t give sharp unblurred results, I think it does demonstrate how insecure blurs are.

We’re not trying to restore the original image. This is about information retrieval, and we already know more than we did before, even with this being one of the most difficult blur types to work with.

On top of that, I’m just a guy. We don’t know what others are capable of! There are many advanced methods I haven’t tried yet.

![Captain Disillusion Unblur Challenge](https://maxvanleeuwen.com/wp-content/uploads/challenge.jpg)

*Another image blurred by the Captain, with two of my unblur attempts next to it. As you can see, this blur was very destructive. But it seems to be his face!*

*This challenge has not been solved yet (Feb 28th, 2026).*

## Image Convolution

To understand unblurring, let’s first look at what a blur actually is. A blur is created by *convolving* an image.

Simply put, convolution is the process of taking each pixel in an image and blending it with its neighbours. The shape and weights of this neighbourhood is called the *kernel*.

![Convolution with a kernel visualized, cross blur](https://maxvanleeuwen.com/wp-content/uploads/Kernel-Animation.gif)

When all weights in the kernel are positive, the result will be a blur of some kind. The shape dictates the look of the bokeh!

The kernel can be thought of as a stencil, similarly to how the aperture of a real-world camera creates bokeh shapes. Slightly unrelated, but [here’s](https://workmoreorless.com/blog-learn/techniques-custom-bokeh) a cool exploration into DIY camera apertures by photographer Jason Yang.

![Blur kernel shapes for different bokeh results](https://maxvanleeuwen.com/wp-content/uploads/Kernel-Shape-Bokeh.jpg)

Convolutions don’t always blur, though. If the kernel has negative values (like in the matrices shown below), they can do interesting things like edge detection or sharpening.

![Kernels](https://maxvanleeuwen.com/wp-content/uploads/Kernels-Wikipedia.jpg)

*Different kernels, from [wikipedia](https://en.wikipedia.org/wiki/Kernel_\(image_processing\))*

Go watch Captain Disillusion’s video on [blur](https://www.youtube.com/watch?v=xDLxFGXuPEc)!

And check out 3Blue1Brown’s video on [convolution](https://www.youtube.com/watch?v=KuXjwB4LzSA), for a mathematical deep-dive.

## The Frequency Domain

An image can be converted to the *frequency domain* by taking a *Fourier transform* of it.

The frequency domain is a different perspective of the same image. Instead of seeing it as a grid of pixels, we look at the image’s ‘rates of change’ and we deconstruct the image into a bunch of sine waves. Each individual wave now affects the entire image.

This is useful, because up until this point convolution was a per-pixel operation. When we convert our image to the frequency domain, it becomes a simple multiplication!

![2D Fourier Transform to visualize Frequency Domain in Nuke](https://maxvanleeuwen.com/wp-content/uploads/Frequency-Domain.jpg)

*The black areas in the frequency domain of a blurred image indicate suppressed high-frequency information.*

So in the frequency domain, ${Image}_{convolved} = {Image} * {Kernel}$. And afterwards, we simply convert back to the Spatial Domain to see the result.

Granted, this may all sound magical and made-up, so here’s a great [lecture](https://youtu.be/OOu5KP3Gvx0?si=lzrjPj-5EnMsEJdy&t=74) by Shree Nayar to prove it.

![freakuency](https://maxvanleeuwen.com/wp-content/uploads/freakuency.jpeg)

## Deconvolution

So blurring is a convolution, which is a multiplication in the frequency domain.

Unblurring (deconvolution) should then be the opposite: a division in the frequency domain! There is a lot more nuance to it, but this is the essence of the process. You take the Fourier transform of your image, and divide it by the Fourier transform of the kernel.

![Street deconvolution example camera lens blur](https://maxvanleeuwen.com/wp-content/uploads/Street-Deconvolve.gif)

*Deconvolving a blur made with a hexagonal kernel.*

To find out what the kernel of a specific blur looks like, you can just apply that blur effect to a single white pixel at the center of a black image and dial up the exposure.

For my tests, I rendered a bunch of white pixels with blur effect radii this way, so I can scroll through them and see which give the best results.

![Mona Lisa - Deconvolution](https://maxvanleeuwen.com/wp-content/uploads/Mona-Lisa-Deconvolution.gif) ![AE Camera Lens Blur - Wiener Deconvolution](https://maxvanleeuwen.com/wp-content/uploads/AE-Camera-Lens-Blur-Wiener-Deconvolution.jpg)

*Animating the kernel radius to find the perfect value.*

The nuances that make deconvolution so difficult with real-world images are mainly:

1. Knowing the exact kernel that was used (it can even be *space-variant*).
2. Soft kernels suppressing high-frequency information to below the noise floor.

Both require more complex solutions for better results, as well as some trial-and-error.

Soft kernels dampen high-frequency information more, because their frequency domain counterparts are smooth as well. They decay to a level below the noise floor very quickly, making the information nearly impossible to read. Hard kernels translate into ripples in the frequency domain, and those *sidelobes* let information leak through.

For this reason, it’s a good thing Gaussian blur is one of the most common blur types! But that standard has nothing to do with safety. Its kernel is mathematically separable, meaning it renders fast. And it looks pleasing because of its softness. [Here’s](https://www.youtube.com/watch?v=SiJpkucGa1o) a Computerphile video explaining kernel separability.

Other separable kernels usually produce less pleasant-looking blurs (like Box Blur). A hexagonal kernel, which looks more like a true lens defocus than Gaussian does, is not separable and thus expensive – it scales quadratically with its radius: $O(r^2)$.

![Directional Blur Deconvolution](https://maxvanleeuwen.com/wp-content/uploads/Directional-Blur-Deconvolution.gif)

*A directional blur can be deconvolved using a line.  
Stock photo by [Daniel Thürler](https://unsplash.com/photos/a-blurry-photo-of-a-man-walking-down-the-street-GlS43oGlUgY) on Unsplash.*

Two well-known methods of deconvolution are *Wiener* and *Richardson-Lucy*.

Wiener Deconvolution uses a noise-to-signal ratio to suppress noise, Richardson-Lucy Deconvolution is an iterative process.

## In Conclusion

Use black boxes instead of blurs.

Other common censoring techniques have their own issues. For example, pixelation (mosaic) can be safe, but is problematic when the [view is stationary](https://www.youtube.com/watch?v=acKYYwcxpGk). Or when you know [it’s text](https://bishopfox.com/blog/unredacter-tool-never-pixelation).

*![guessing text under mosaic censoring by Dan Petro](https://maxvanleeuwen.com/wp-content/uploads/wow_such_secrets.gif)*

*Guessing the text under a mosaic censor  
By [Dan Petro](https://bishopfox.com/blog/unredacter-tool-never-pixelation)*

I’m a bit cautious about sharing my project files for these experiments. While I didn’t invent the processes, my setup (created with the compositing software Nuke) might make it easier to do this at scale, and I don’t want to facilitate the collecting of sensitive information. Reach out if you’re a researcher looking to verify my results.