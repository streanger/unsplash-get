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

Usage from Python
**************************

.. code-block:: python

    from unsplash_get import search, save_img
    
    # get list of urls
    word = 'orange'
    urls = search(word)
    
    # save images
    for index, url in enumerate(urls, start=1):
        file = f'{word}_{index:03}.jpg'
        save_img(url, file)

Load image to variable
**************************

it requires additional libraries (`PIL` and/or `numpy`), which could be installed with:

.. code-block:: bash

    pip install Pillow numpy

.. code-block:: python

    import io
    import numpy as np
    from PIL import Image
    from unsplash_get import search, load_img

    def load_img_to_pil(data):
        img = Image.open(io.BytesIO(data))
        return img

    def load_image_to_numpy(data):
        img = np.array(Image.open(io.BytesIO(data)))
        return img

    # get list of urls
    word = 'orange'
    urls = search(word)
    url = url[4]

    # read image
    pil_img = load_img_to_pil(url)
    numpy_img = load_image_to_numpy(url)

Screenshots
**************************

.. image:: https://raw.githubusercontent.com/streanger/unsplash-get/master/images/unsplash1.png
