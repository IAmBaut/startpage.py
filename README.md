# Startpage

A small script to generate a startpage written in Python.

## Preview with filters
![Screenshot with filters enabled](https://gitlab.com/Baut/readme-images/-/raw/master/StandaloneImages/Startpage%20with%20overlays.png)

The sizes of the pixels are rendered fitting to the display resolution the final startpage is displayed at. Since this preview is just a downscaled screenshot some of it won't display correctly here.

## Preview without filters (except background blur): 
![Screenshot of default startpage](https://gitlab.com/Baut/readme-images/-/raw/master/StandaloneImages/Startpage.png)

# Index

 * [Requirements](#requirements)
 * [How to generate a startpage with this script](#how-to-generate-a-startpage-with-this-script)
 * [The `hourOffset` variable](#the-houroffset-variable)
 * [Effect overlays](#effect-overlays)
 * [Known issues/warnings](#known-issueswarnings)
 * [Asset sources](#asset-sources)


# Requirements

You can technically just download this and use it as is (and make changes to the html and css manually), but the way it is intended is for you to use the `startpage.py` file. To run this file you need to have [python3](https://www.python.org/downloads/) installed on your system. That is the only requirement.

# How to generate a startpage with this script

## - Download this repository

If you are viewing this repo on **gitlab** click on the small download arrow button next to the **clone** button in the upper right of this site. If you are viewing this repo on **github** click on the **code** button in the upper right of this site directly. Then navigate to "Download Zip". You can of course also just clone the repo via command line.

Using the software of your choice decompress this archive if you did not clone the repo via command line.

## - Using the editor of your choice, change some values. There are 3 places that can accept changes: `startpage.py`, `main.css` and `content.txt`.

* `startpage.py` - For changing window strings, file paths and the clock.
    * (optional) Change the `TabTitle`,`TitleText` & `SubText` strings to change these on the final startpage. 
    * (required) Change the `importPath` and `outputPath` values. If you are on windows you need to escape the backslashes windows has in paths (or use raw strings). If you are on Linux, just use the normal path.
    * (optional) Change `hourOffset` if your time is wrong. For first setup keep it at 0. If your clock is wrong after generating the startpage, change this value to adjust it. (Positive numbers to increase the hours, negative to decrease.)
* `main.css` - For changing colors, images, effects and fonts.
    * All values in the root{} area are optional to change. To load other images change the image URLS in this section or replace the files (with the same name as the old file).
    * The variables in the root{} area have comments next to them with a short explanation what they do.
    * You can also activate or deactivate overlay effects like the blur, crt pixel effect and vignette from this root{} area.
    * If you want to change the font used, scroll to the bottom of the file and change the path to the font file.
* `content.txt` - For changing the actual content of the startpage.
    * This is where you change the actual content of the window of the startpage. The format is simple: 
        * Every category is seperated by one **empty** line (That means no whitespaces in that line either). 
        * The first line of each category is its title, while every line after that is considered a link. 
        * A link line consists of three parts: A name (what the link should be displayed as), a seperator (a dash surrounded by a space on each side) and a hyperlink. The hyperlink is optional, but required to make the link work later. In the example file most links are left empty intentionally, in your version you should change all of them. 
        * If a category has too many entries to fit them into one line on the startpage it will automatically add another line to the category.

## - Run `startpage.py`. 

You need python installed for that. How you run it is up to you. If you do not know what that means and are on Windows, double click it. A python window should open for a splitsecond before closing again and the index.html file in the folder should be updated.

## - Use as startpage

The index.html file is the new startpage you generated. To use it as a page for a new tab in your browser, look up a browser specific tutorial on how to set it as default for new tabs.

That's all.

# The `hourOffset` variable

The `startpage.py` file has a `hourOffset` variable that you can change. This variable should be changed if the clock is displaying the wrong time for you. 

Normally the clock should be accurate, but some browser configurations can create issues - for example if you run Firefox and have `privacy.resistFingerprinting` set to true, the timezone that the clock is displated in can be wrong since the browser refuses to tell the script the timezone you are in. This offset is a blanket solution to adjust the time if you run into any such issues without requiring you to change your browser settings or compromising your security. Just change the value and regenerate the startpage.

# Effect overlays

Currently there are 3 effect overlays that you can turn off or on for the startpage: a background blur, a "crt pixel" effect and a vignette overlay. These can be adjusted and toggled on/off in the `main.css` file. Explanations for them are in the comments to every setting. 

That being said the "crt pixel" effect might profit from explanation. It is an overlay that repeats every 3 pixels in each direction: Horizontally every 3 pixel group is overlayed with the colors that the RGB cells of a crt used to have. Vertically every third pixel is darkened to simulate "gaps" between the cells. This means the effect suggests that every 3*3=9 pixel group is 1 crt pixel. It is simply a overlay though, so alignment is not taken into account and the real image is still below in default resolution.

The `--pixeloverlay-resolution` is a multiplier that defines how big each cell is, at 1 it is a 3\*3 cell, at 2 it's a 6\*6 cell, etc. Floating point numbers (1.5 etc.) can be used, but will most likely cause [moiré patterns](https://en.wikipedia.org/wiki/Moir%C3%A9_pattern). Feel free to experiment with these settings, but if you want to avoid these patterns it is probably a good idea to stick to multipliers that result in whole numbers. In contrast the `--pixeloverlay-itensity` setting just defines the opacity of the overlay. 

# Known issues/warnings

## Scaling

The distances between divs in the html document are hardcoded in the form of pixel distances. Scaling can be bad if vastly different aspect ratios or resolutions other than 1920 x 1080 are used. From some quick testing it seems to behave decently with different aspect ratios, but you have been warned.

## Content overflow

Content overflow happens when the script encounters either more data than expected or unusually large strings. It will make content on the page appear to go outside the intended areas and make it look worse.

Currently there are two ways to trigger content overflow:

* The script automatically adds linebreaks if you are adding more content into one category than there is space in one line. If however you add very long strings (around 60 symbols with default font size), it will still overflow.

* If you add too much content overall, the script just adds category after category. There is no horizontal overflow check built in, so it will eventually flow out of the window. Limit the amount of links/categories you add to avoid this.

## White border around background image

The background image has a blur filter over it. You can adjust the intensity of this blur filter by changing the `--backgroundBlur` variable in the `main.css` file. Due to the way this blur is calculated, the very edges of the background image will have a blurry colored border equal to the background color of the document. This effect gets stronger the more blurry the background is set. This can be unintended in terms of appearance especially if you have dark backgrounds.

As of now there are two ways to avoid it:

* Disable the blur by changing it to `0px`
* Change the `backgroundBorder` property in `main.css` to a color that fits the image you are using better.

# Asset sources
The licences of the external assets do not require attribution, but in case you were wondering where they were from I decided to link the sources here anyways.

These assets are only used for the default look of the startpage and can be replaced at will.

## Inspiration

The original default appearance of this startpage is inspired by a startpage by [jamesNWT](https://github.com/jamesNWT). 

## Images

There are 3 images used, 2 of which are from [Pixabay](https://pixabay.com/) and are licenced under their [Pixabay licence](https://pixabay.com/service/terms/#license).

* The first image is the [background image with the tree blossom](https://pixabay.com/photos/blossom-pink-garden-nature-4151081/).
* The second image is the [painting "The Great Wave off Kanagawa"](https://pixabay.com/illustrations/picture-woodblock-printing-woodcut-1247354/).([Additional Wikipedia link](https://en.wikipedia.org/wiki/The_Great_Wave_off_Kanagawa))

The third image is a cut out and edited version of the window from an image that inspired this startpage script, the source of which has been lost.

## Font
The font used is the [W95FA font by FontsArena](https://fontsarena.com/w95fa-by-fontsarena/) and is licenced under a SIL OpenFont licence.
