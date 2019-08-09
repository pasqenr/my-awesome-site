# My Awesome Site

This site is built with [Jekyll](https://jekyllrb.com/).

## Prerequisites

In order to build the site you need:

* [Jekyll](https://jekyllrb.com/) (deps: Ruby, RubyGems, GCC, Make)
* Make sure that ruby gems directory is in PATH
* Add _Bundler_ gems: 
    ```bash
    gem install jekyll bundler
    ```

## Build and running

Before anything you need to install the npm dependencies:
```bash
npm install
```

Build the site (found it in the `_site` directory):
```bash
bundle exec jekyll build
```

To keep watching over file changes with a local webserver (useful for developers):
```bash
bundle exec jekyll serve
```
And browse to `http://localhost:4000`.

## Create new worlds, galleries and characters

To assist the user in the process of creating worlds, galleries and characters there is a tool: `CREATOR.py`.

### Prerequisites for CREATOR.py:

```
Python >= 3

wxPython
python-slugify
```

You can install those via `pip` using the command: `pip install -r requirements.txt`. Note that in Arch based distro it's better install them using `pacman`.

To start the tool simply use `python CREATOR.py` (or `python3 CREATOR.py` if the command `python` refers at version 2). Using the tool you can choose already existing worlds and galleries or creating new folders.

The worlds created are found in `assets/images/worlds` and, inside one of them, you can find the relative galleries as folders.

### Customize

* In a _gallery_ folder there is the default gallery image named as `gallery_name.png`. Replace it with the your image;
* In a _character_ folder there is the default character image named as `character_name.png`. Replace it with the your image. Every other image placed in this folder will be shown in the bottom of the page.
* To edit the description of a character open the file `_characters/character_name.md` and change the text `DESCRIPTION HERE (MARKDOWN ALLOWED)`. [Markdown is allowed (and recommended)](https://www.markdownguide.org/basic-syntax/).
* You can use a image named `frontpage.png` placed in `assets/images/` that will be shown in the homepage.

### Build the site:
 ```
bash
bundle exec jekyll build
```