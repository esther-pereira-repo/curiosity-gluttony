---
title: "Chinese Typographic Design"
source: "https://medium.com/@Hynuza/typographic-design-in-asian-language-4bb1035ebb7"
author:
  - "[[Hynuza]]"
published: 2015-05-22
created: 2026-05-03
description: "Hynuza highlighted"
tags:
  - "clippings"
---
From Gutenberg to Steve Jobs, from printing to screen display, typographic design has been committed to creating better user experience for the most important activity by which human beings acquire information — Reading. Calligraphers, typesetters and designers have been thinking about this for thousands of years, ever since writing system came into being. So it won’t be just as simple as legibility and readability, it’s about how we can read more comfortably. As a visual designer, I am fascinated by such a profound subject that closely combines art and technique.

Here in Hong Kong, designing for Asian languages, or more specifically, designing for Chinese is a part of our practice. Apart from some general rules, guidelines and best practices of overall typography, I would like to write about some must-knows, thoughts and trends about Chinese typography that I find worth sharing based on my personal experience.

## What font to use

When it comes to discussing about typography, the first question is always about what font to use. Although font type is only one of the major issues that designers need to concern about, but apparently it is the most easy part to be noticed.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*UcuotAGJal52T_CTSg0LZg.png)

Four major categories of Chinese font type

There are four major categories of Chinese font type. From top to bottom in the image shown above, the style varies from traditional to modern. Kai Ti and Fang Song are often used in traditional printed books and publications, they rarely appear in digital design nowadays. For Song Ti (or Minchō in Japanese) and Hei Ti (or Gothic in Japanese), we can roughly correspond them to Serif and Sans Serif typefaces of Latin language typography. Similar to English, Hei Ti typeface was believed to fit digital devices best since serifs of Song Ti / Roman / Serif typefaces can look terrible on low DPI screens, which will harm the legibility and readability. Thus, almost all the default font type of every Operating System are Hei Ti / Sans Serif. However, with the high DPI screen / Retina display coming into being, the problem of Serif fonts does not exist anymore, some Apps (like Readability, Circa), websites (like Medium) start to use Serif font again to provide a traditional, classic and prestigious reading experience. Yet since most screens are still non-Retina, it’s much safer for designers to use Hei Ti / Sans Serif fonts for digital design.

For designer, the biggest problem of Chinese font is, there’s not many font types to choose from. The reason is obvious, there are so many characters in Chinese / Japanese language. ==Within one Chinese font type, the smallest standard font contains 6763 characters.== A Japanese font type called Hanazono has 87791 characters. A typical Chinese font file size is usually at least 5MB, some times can be over 20MB. It takes years for font designers to draw every single character creating just one font type. What’s more, a mature font type should have a set of weight system, not only regular and bold. For example English fonts like Helvatica, Frutiger and Roboto Sans, each of them has more than 5 different weight which enables designers to create more levels of hierarchy yet keep a consistent style within one design project. Very few Chinese fonts can have such a “huge” system of weights due to the cost for same reason. Although for designer the safest way is always using system default font type of target OS / device, yet some popular OS are still using low-quality Chinese font type as their default. Designers would find restrictions when designing for Chinese interfaces.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*SOr6m9kEpGJvJ7d7Nj22-g.png)

Apple’s default Chinese font type ST Heiti is widely criticised. It only has Light and Regular, so Apple uses Light as normal weight and Regular as bold. But the difference between Light and Regular is too small that users can hardly realise. The structure and stroke design of ST Heiti is also considered as low-quality.

Recently a good news makes designers excited, that Google and Adobe released a new Chinese font type called [Source Han Sans](http://en.wikipedia.org/wiki/Source_Han_Sans). It’s a huge project cooperated by font type companies from China, Japan and Korea. Source Hans Sans has 65,535 characters and 7 different weights, it provides a consistent and systematic style for Simplified Chinese, Traditional Chinese, Japanese and Korean. This is the first font type ever that has almost all the features designers want. **And it’s open source, it’s free!**

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*2qwfJZZlV7NZQwH8NoXVIQ.png)

Source Han Sans & Roboto

An interesting point of Source Hans Sans is, there are two weights called Regular and Normal, which only have a tiny small difference between them that most people cannot even tell.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*Ae4FM-_Z8_tzzEbF8puDgA.png)

Difference between Normal & Regular of Source Han Sans

The purpose of having these two weight is visual compensation on different background. See the image below, text with same font weight will look bolder on dark background, so using Normal weight which is slightly thinner than Regular on dark background will offset the visual illusion due to human eyes’ innate nature. I was amazed that Source Han Sans considered such details.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*I4Wp9_nZX24jGAMTqR6kLg.png)

Visual compensation on different background

Another two Chinese font type that have multiple weight choices are [LanTingHei](http://zh.wikipedia.org/wiki/%E6%96%B9%E6%AD%A3%E5%85%B0%E4%BA%AD%E9%BB%91) by Founder Type and [XinGothic](http://www.vmtype.com/index_e.html) by Vmtype. With more high-quality Chinese font types being developed, designers are having more choices other than system default fonts.

June 9th, 2015, [Apple introduced whole new Chinese system font called PingFang](http://www.apple.com/osx/elcapitan-preview/). PingFang has 6 different weights in both simplified and traditional Chinese. This is an exciting news since it’s the first time a Chinese system font equips more than 3 weights. Also, Apple finally retired ST Heiti, which has been criticised for a long time. Let’s see how PingFang works when OS X El Capitan formally released this fall.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*8S6dkeiC8dNv76rCjRdf8A.png)

## Possibilities and latest technique of Chinese web font

Web font is developing fast since it enables designers and developers to choose from almost endless fonts regardless of whether the end user has installed these font or not. However, Chinese web fonts are still having challenges an not yet able to be widely used. We mentioned above that a typical Chinese font file size is usually at least 5MB, some times can be over 20MB. To use web fonts, the browser still needs to download the font file from server, it’s not a problem for alphabetic languages like English since most English font are only around 100KB, while for Chinese fonts, it will take an intolerably long time for loading the font file, which will ruin the user experience. [Fonts.com](http://www.fonts.com/search/all-fonts?searchText=chinese&SearchType=WebFonts&page=1&itemsPerPage=10) has provided such service, but as expected, the font file takes too long to load, which makes it not usable.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*s_7j7nr7DTMXZsMZ_grhWw.png)

Justfont, one of the pioneer service of Chinese webfont

However, problems are always meant to be solved. Some Chinese font service such as [JustFont](http://cn.justfont.com/) and [Youziku](http://www.youziku.com/) are making it possible for Chinese web fonts. The way they do are similar, these service can dynamically generate a smaller font file which is a subset based on what characters are used on current page, in that way, the user’s browser does not need to download the entire file of the font but a much smaller subset file. It saves quite a lot of time.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*XxU6o33OsOKzzwfeIVp4sw.png)

The technique of fontsubsetter by Monotype

But still, these services only provide a limited number of fonts. If you need to use other fonts as web font for your website, you may need to use services like [Fontsubsetter](http://fontsubsetter/) by Monotype, which allows you use whatever font you are authorised and customise the way how you want to use the web font. Also, another more simple choice is to manually create a subset font file which contains all the characters your website uses, and put it on your server. It can also save quite a lot of time, just like what [Apple.com/cn](http://www.apple.com/cn/) does.

## Get Hynuza’s stories in your inbox

Join Medium for free to get updates from this writer.

A recent update on 15th June, 2015, Source Han Sans font type family was available from Adobe Typekit. [Adobe Typekit finally announced east Asian web font support](http://blog.typekit.com/2015/06/15/announcing-east-asian-web-font-support/).

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*RoXiu9SYEug_LK0fpYpTBA.png)

Announcing East Asian web font support and new font browsing tools for Japanese customers

## Tips and recommended practices of Chinese and Western mixed text composition

Sometimes designers need to do typography for mixed languages especially in Hong Kong where English and Chinese are both official languages. There are a few tips and notes that need to concern about when doing mixed text composition design, here I would like to talk about only one that is the most widely discussed and controversial.

Adding a space between Chinese and English is highly suggested by a lot designers. The rationale behind is that English naturally has a space between words while Chinese does not, but Chinese has larger tracking between characters than English’s between letters. So ideally there should be a specially treated kerning between English words and Chinese characters. Actually some advanced editor does this by default, such as Microsoft Word and Adobe InDesign.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*wk24Rpra9THVnGdiOlWe1A.png)

How Microsoft Word and InDesign treats the kerning between English words and Chinese characters.

However, most text editor including your the browsers do not have such detailed concern. So what people suggest is to add a space manually in order to make it not so squeezed and most designers agree that it looks visually better have a space. Lots of famous companies have already practise this suggestion for a long time on their websites, such as Google, Apple, Microsoft and Adobe.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*ry1pcyzeg_s7FkpWmZcghQ.png)

Google, Apple, Microsoft and Adobe’s practice on adding a space between Chinese and English

But still, it’s a “trick”, it’s a compromising way of solving this problem. There is a famous saying about typography that “The space bar is not a design tool”. Also, text styles should always be done by rendering, whatever by software or CSS or other environment, it should not be done by any inputing conduct. Imaging if I copy a long text from the websites where the designer added extra spaces, and paste into Microsoft Word or InDesign, I have to manually remove those spaces one by one. Thus, the best way is still to wait for smarter rendering system. For now, you can choose what you think is the best. Personally I suggest designers to add a space for visual purpose, but it should never be standardised as a rule.

## W3C Requirements for Chinese Text Layout

W3C develops protocols, guidelines and standards that are widely followed by web designers and developers. However, there are no standards or guidelines for Chinese text layout until 2015. [W3C HTML5 Chinese Interest Group](http://www.w3.org/html/ig/zh/Overview.html) and [W3C Internationalisation Working Group](http://www.w3.org/International/core/) jointly published [Requirements for Chinese Text Layout (Draft)](http://www.w3.org/International/docs/chinese-layout/). This is the first time that Chinese text layout for web has an international guideline to follow.

> the document summarises the text composition requirements in the Chinese writing system. One of the goals of the task force is to describe the issues in the Chinese layout requirements, another one is to provide satisfactory equivalent to the current standards (i.e. Unicode), also to promote vendors to implement those relevant features correctly.

This document is meant to consider all the possible cases of Chinese text layout, I strongly recommend designers who are doing design for Chinese user interface read this document. However, this document is not a Bible, it is just a summary of relevant discussions and topics as well as best practices that are recommended by experiences designers / developers. Also, the document is still incomplete, final version will be released by 2016. If you are interested, there are two completed relevant document for reference: [Requirements for Latin Text Layout and Pagination](http://www.w3.org/TR/dpub-latinreq/) and [Requirements for Japanese Text Layout](http://www.w3.org/TR/jlreq/). The second document which had been developing for 5 years and was finally published in 2008, had a profound influence on Japanese and Chinese text layout for web, and promoted web practices on Asian languages greatly.

![](https://miro.medium.com/v2/resize:fit:1400/format:webp/1*GzjgMoxuxXLCtIxYcDFVVg.jpeg)

A sample image from Requirements for Japanese Text Layout

## Links mentioned above and other useful ones

[*Source Han Sans*](http://en.wikipedia.org/wiki/Source_Han_Sans)

[*JustFont*](http://cn.justfont.com/) *— Chinese web font service*

[*Fontsubsetter*](http://fontsubsetter/) *by Monotype*

[*Requirements for Chinese Text Layout (Draft)*](http://www.w3.org/International/docs/chinese-layout/)

[*Requirements for Japanese Text Layout*](http://www.w3.org/TR/jlreq/)

[*Chinese Punctuation*](http://en.wikipedia.org/wiki/Chinese_punctuation)

[*Chinese equivalence for italic type*](http://cargocollective.com/cliko/Chinese-equivalence-for-italic-type)

[The CSS typography framework optimised for Chinese](https://css.hanzi.co/)