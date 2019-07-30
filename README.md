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

## Create new galleries

In order to add a gallery named `my_gallery`:

1) In the folder `_details` create a new file named `my_gallery.md` with the following content:
    ```
    ---
    layout: detail
    name: my_gallery  # This must be the gallery name chosen
    ---

    Lorem ipsum dolor sit amet, consectetur adipiscing elit. Maecenas hendrerit rhoncus ipsum...
    ```

2) Now go to `/assets/images/galleries/` and create a new folder named `my_gallery`;

    2.1) Put all the images do you want;

    2.2) One image must be the displayed image in the gallery showcase. Name it (you can copy an image already inside and rename it) `my_gallery.png`. (Only `png` support for now);

3) Build the site:
    ```bash
    bundle exec jekyll build
    ```