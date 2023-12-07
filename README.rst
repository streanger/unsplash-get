unsplash_get
======================
Script for scraping unsplash. Only for educational purposes.

Install
**************************

from pypi

.. code-block:: bash

    pip install unsplash-get

from github

.. code-block:: bash

    pip install git+https://github.com/streanger/unsplash-get.git

Usage from command line
**************************

.. code-block:: bash

    # as module
    python -m unsplash_get <word>
    python -m unsplash_get orange

    # as entry point
    unsplash <word>
    unsplash orange

    # as script
    python unsplash_get.py <word>
    python unsplash_get.py orange

Usage from Python (save images)
**************************

.. code-block:: python

    from pathlib import Path
    from unsplash_get import search, save_img

    # get list of urls
    word = 'orange'
    urls = search(word)

    # create directory
    directory = Path(word)
    directory.mkdir(exist_ok=True)

    # save images
    for index, url in enumerate(urls, start=1):
        path = str(directory / f'{word}_{index:03}.jpg')
        status = save_img(url, path)
        print(f"{index:03}.{url} -> {path} ({status})")

Usage from Python (load image to variable)
**************************

it requires additional libraries (*PIL* and/or *numpy*), which could be installed with

.. code-block:: bash

    pip install Pillow numpy

example code

.. code-block:: python

    import io
    import numpy as np
    from PIL import Image
    from unsplash_get import search, get_image

    def load_img_to_pil(data):
        img = Image.open(io.BytesIO(data))
        return img

    def load_image_to_numpy(data):
        img = np.array(Image.open(io.BytesIO(data)))
        return img

    # get list of urls
    word = 'orange'
    urls = search(word)
    url = urls[4]

    # read image
    data = get_image(url)
    pil_img = load_img_to_pil(data)
    numpy_img = load_image_to_numpy(data)

Screenshots
**************************

.. image:: https://raw.githubusercontent.com/streanger/unsplash-get/master/images/unsplash1.png
