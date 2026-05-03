---
title: "Designing User Experience for Virtual Reality (VR) applications"
source: "https://uxplanet.org/designing-user-experience-for-virtual-reality-vr-applications-fc8e4faadd96"
author:
  - "[[Sourabh Purwar]]"
published: 2019-03-04
created: 2026-05-02
description: "Designing User Experience for Virtual Reality (VR) applications Virtual Reality (VR) infers a total inundation experience that closes out the physical world. Utilizing VR gadgets, for example, HTC …"
tags:
  - "clippings"
---
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*2hLo9x2HpI6o1AEL.jpg)

Difference between AR, VR and Mmixed Reality | Image Source

**Virtual Reality (VR)** infers a total inundation experience that closes out the physical world. Utilizing VR gadgets, for example, HTC Vive, Oculus Rift or Google Cardboard. Users can be transported into a various genuine world and envisioned situations, for example, the center of a screeching penguin state or even the back of a monster.

There are other reality experiences that exist like Augmented Reality, Mixed Reality, and Extended Reality which provide the user with different experiences

**Augmented reality (AR)** adds digital elements to a live view often by using the camera on a smartphone. Examples of augmented reality experiences include Snapchat lenses and the game Pokemon Go.

In a **mixed reality (MR)** experience, which combines elements of both AR and VR, real-world and digital objects interact. Mixed reality technology is just now starting to take off with Microsoft’s HoloLens one of the most notable early mixed reality apparatuses.

### Relating Conventional Design to 3D experience

The market has furnished designers with a lot if reliable work over the past few decades and is going to move towards a new paradigm of vivid 3D content. Sound, touch, depth, and feeling will all be fundamental to the VR experience, making even the most novel 2D screen encounters feel exhausting and dated.

VR provides many of the same benefits of training in a physical environment — but without the accompanying safety risks. If a subject becomes overwhelmed, they can easily take off the headset or adjust the experience to be less overwhelming. This simple fact makes means specific industries like healthcare, military, police, and so on should prioritize finding ways to use VR for training.

Think Skype for Business on steroids. VR has the potential to bring digital workers together in digital meetings and conferences. There will be real-time event coverage, something like Facebook Live with VR. Rather than merely seeing the other person on a screen, you’ll be able to feel as if you are in the same room with them, despite being miles away.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*ybGE13_z6Z3j9iQi)

Image Source

Think about how you collaborate with a touchscreen screen today. There are various examples that we have all developed to understand, for example, swiping, squeezing to zoom, and long tapping to raise more choices. These are altogether contemplation's that ought to be made in VR also. I’m sure that as more creators come into the VR field, there will be more personalities to make and vet new UI designs, helping the business to push ahead.

Interactivity in virtual reality is composed of three elements. These are speed, range, and mapping. Speed is the response time of the virtual world. If the virtual world responses to user actions as quickly as possible, it is considered an interactive simulation since immediacy of responses affect the vividness of the environment. Many researchers try to determine the characteristics and components of interactivity of Virtual reality in different ways. However, in order to do this perfectly, the designers have to acquire a thorough real-world understanding, meaning that they need to visualize the typical physical space surrounding the user and then build on the elements that they’ve perused. This is so because at no point you want your users to feel uncomfortable and feel like the newly introduced elements are invading their personal space.

## So, What all kind of apps are we going to design

Generally speaking from a designer’s perspective, VR applications are made up of two types of components: environments and interfaces.

You can think of an environment as the world that you enter when you put on a VR headset — the virtual planet you find yourself on, or the view from the roller-coaster that you’re riding.

An interface is the set of elements that users interact with to navigate an environment and control their experience. All VR apps can be positioned along two axes according to the complexity of these two components.

- In the top-left quadrant are things like simulators, such as the roller-coaster experience linked to above. These have a fully formed environment but no interface at all. You’re simply locked in for the ride.
- In the opposite quadrant are apps that have a developed interface but little or no environment. Samsung’s Gear VR home screen is a good example.
![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*QAHx7nr3e7DI56XN)

## How to start designing the user experience for virtual reality

Before you start designing for your VR app, considering some of these fundamental questions may help you:

- How do people get started?
- What affordances are provided to guide people without overwhelming them?
- Do you want to err on the side of providing too much guidance or create a minimalist environment that doesn’t overload the user with too many choices?

Don’t expect people to know what to do and where to go. Slow and progressive familiarization, visual clues, and guidance from the software should all be used to help the user. When you’re designing for VR, you’re designing for the capabilities of people as much as you’re designing for the capabilities of the system. So it’s essential that you understand your users and the issues that may come up while they experience VR.

VR experience isn’t too different than the process for designing a web or mobile product. You will need user personas, conceptual flows, wire-frames, and an interaction model.

## The Process for Designing User Experience for Virtual Reality

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*zOmzlD08f0AFpMRs)

Whereas most designers have figured out their own workflow or design process for designing mobile apps, processes for designing VR interfaces are yet to be defined globally. For designing your first VR app you should start your process with the logical first step which is to devise a strategy or plan.

## USER RESEARCH INSIDE OF VR:

As a matter of first importance, before you even begin considering structuring for VR, you need to consider what sort of Experience you need to make? There is certainly not a one-measure fits-all. Most ethnographic research strategies are totally open within VR, including:

Client Interviews, Fly-on-the-Wall, Usability Testing, Touchstone Tours, Simulation Exercises, Shadowing, Participant Observation, Heuristic Evaluation, Focus Groups, Eye Tracking, Exploratory Research, and Diary Studies.

## WIRE-FRAMES:

Generally, as designers do, we’ll go through rapid iterations, defining the interactions and general layout.

## VISUAL DESIGN

At this stage, after the features and interactions have been approved. Brand guidelines are now applied to the wire-frames, and a beautiful interface is crafted.

The Design Process for VR apps would not change dramatically apart considering few usability issues from our normal design process.

## Setting up the environment for designing

## Canvas size

To apply mobile app workflow to VR UIs, you first have to figure out a canvas size that makes sense.

Below is what a 360-degree environment looks like when flattened. This representation is called an **equirectangular projection**. In a 3D virtual environment, these projections are wrapped around a sphere to mimic the real world.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*KYYxqfSCZyTtFEvF)

Image Source

The full width of the projection represents 360 degrees horizontally and 180 degrees vertically. We can use this to define the pixel size of the canvas: 3600 × 1800. Working with such a big size can be a challenge. But because we’re primarily interested in the interface aspect of VR apps, we can concentrate on a segment of this canvas.

Building on Mike Alger’s early research on comfortable viewing areas, we can isolate a portion where it makes sense to present the interface.

The area of interest represents the one-ninth of the 360-degree environment. It’s positioned right at the center of the equirectangular image and is 1200 × 600 pixels in size.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*aX_2K32N3lNzB4Ol)

Let’s sum up:

“360 View“: 3600 × 1800 pixels

## Get Sourabh Purwar’s stories in your inbox

Join Medium for free to get updates from this writer.

==“UI View“: 1200 × 600 pixels==

## Pencil & Paper

Before getting into any software, it’s crucial to get your ideas out on paper. It’s fast, cheap, and helps you express ideas that may take hours in software. This is especially important because moving from sketches to hi-fidelity can cost much more in 3D than in 2D.

## Software

Some designers start with tools they already know like Sketch, others use it as an opportunity to learn new tools. It really depends on what engine you are going to use to build your app. If you are building a 3D game, you’ll want to use Unity or Unreal Engine. Cinema 4D and Maya are also widely used, but mostly for complex animations and renderings.

## PRINCIPLES TO CONSIDER WHILE DESIGNING

## TEXT READABILITY

Because of the display’s resolution, all of your beautifully crisp UI elements will look pixelated. This means, first, that text will be difficult to read and, secondly, that there will be a high level of aliasing on straight lines. Try to avoid using big text blocks and highly detailed UI elements.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*UnTgVEjp24n7hoLs)

Image source

Intended viewing distance: how far away we have designed these to be viewed. What is the optimal distance that these screens were intended to be viewed from and that intended viewing distance will inform the size of the screen in addition to the size and density of the content therein.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*RgNriPKt6pN7kMhx)

Distance-independent millimeter or A dmm can be described as one millimeter at a meter away. So it’s an angular unit that just follows a millimeter as it scales off into the distance. Let’s look at a concrete example. In the upper left-hand corner of this diagram, I have a screen space layout that I have measured in dmm’s, All of my UI elements are measured in dmms. It is 400x480 dmms tall and then I have applied that layout in world space to three separate virtual screens.

All of these virtual screens have different intended viewing distance. From the vantage point, that all of these screens are intended to be viewed from, they will look same to the user, they will have same angular size and text would be just as readable, buttons would be just as clickable and motion will appear to move same as well.

## Ergonomics

When first designing for VR it’s exciting to think about creating futuristic interfaces like we’ve seen from Hollywood blockbusters like Iron Man or Minority Report, but the reality is those UIs would be exhausting if used for more than a few minutes. The following diagrams help to illustrate the comfortable range of motion zones:

![](https://miro.medium.com/v2/resize:fit:2800/format:webp/0*GZyeo20pAGMBxJ6s.png)

![](https://miro.medium.com/v2/resize:fit:2800/format:webp/0*KNbrH1lphLZdZi2C.png)

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*wYVDGwmGx7uuHEkL.jpeg)

Image Source

We’ve all been affected by some sort of “text neck” syndrome at some point (the soreness felt from looking down at our smart phones for extended periods). Depending on how far you lean over, poor posture can create up to 60 pounds of pressure on your spine. This can lead to permanent nerve damage in your spine and neck.

## AVOIDING SIMULATOR SICKNESS

Virtual reality introduces a new set of physiological considerations for design. Like flight simulators used by pilots in training, virtual reality has the potential to present mismatches between physical and visual motion cues. This mismatch can produce nausea known as “simulator sickness,” when your eyes think you’re moving, but your body does not.

Understanding the physiological effects of virtual reality design, and following these guidelines, is critical to making your app success and ensuring that users avoid simulator sickness.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*9q7DY-xq8ujvijza)

## BRIGHTNESS CHANGES

Be mindful of sudden changes in brightness. Given the proximity of the screen to the user’s eyes, transitioning the user from a dark scene to a bright scene may cause discomfort as they acclimate to the new level of brightness. It is similar to stepping out of a dark room into the sun.

## BUTTON PLACEMENT

Avoid placing fuse buttons in close proximity to each other. Fuse buttons work best if they are large targets that are sufficiently far apart from each other.

If multiple smaller fuse buttons are placed near each other, the user could accidentally click on the wrong button. Smaller buttons that are close to each other should require a direct click to activate.

> “Instead of trying to adapt ourselves to fit the limited interactions supported by our existing technologies, our interactions with VR platforms will need to be as natural and intuitive as possible.”

## Tools for Designing VR Experience

## Sketch

Sketch to VR is a sketch plugin that uses another tool called A-Frame. The Sketch to VR plugin automatically creates an A-Frame website, but all we need to worry about is creating our design in the sketch.

## Google Blocks

Use simple 3D geometry to simulate a sense of scale and depth. If you have a rift or vive, you can use Google Blocks to prototype your ideas. This isn’t something you’d put in front of a user, but you can begin to see how your 3D environment might look and feel.

## Photoshop

Photoshop lets us use core image editing tools like the pen and brush tool, to draw elements that appear to be in 3D space.

## Designing VR apps on Sketch

## SET UP “360 VIEW”

First things first. Let’s create a canvas that will represent the 360-degree view. Open a new document in Sketch, and create an artboard: 3600 × 1800 pixels. Import the file and place it in the middle of the canvas. If you’re using your own equirectangular background, make sure its proportions are 2:1, and resize it to 3600 × 1800 pixels.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*mM1wMtDvKP7DwZ5P)

## SET UP ARTBOARD

As mentioned above, the “UI View” is a cropped version of the “360 View” and focuses on the VR interface only. Create a new artboard next to the previous one: 1200 × 600 pixels. Then, copy the background that we just added to our “360 View,” and place it in the middle of our new artboard. Don’t resize it! We want to keep a cropped version of the background here.

## DESIGN THE INTERFACE

We’re going to design our interface on the “UI View” canvas. We’ll keep things simple for the sake of this exercise and add a row of tiles. Duplicate it, and create a row of three tiles.

## MERGE ARTBOARDS AND EXPORT

Drag the “UI View” artboard to the middle of the “360 View” artboard. Export the “360 View” artboard as a PNG; the “UI View” will be on top of it.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*TSL_-1_jjWqeYaVe)

Image Source

## TEST IT IN VR

Open the GoPro VR Player and drag the “360 View” PNG that you just exported into the window. Drag the image with your mouse to preview your 360-degree environment.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/0*8hTUvk0HudcphdVL)

## PROTOTYPING

Here, we’ll organize screens into flows, drawing links between screens and describing the interactions for each screen. We call this the app’s blueprint, and it will be used as the main reference for developers working on the project.

## Conclusion

As a Designer, I think this is the ripe time to start enhancing our skills to nurture the future of the Design industry and the important part it plays to enhance and improve the day to day life of application users. The best part of the lot is that the same concepts and ideation methods used in design thinking and ux methodology still remain the same with focus on some new principles of interaction as mentioned above.

> Thanks for Reading!!!  
> What are your thoughts about it?