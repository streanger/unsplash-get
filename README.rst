unsplash_get
======================
Script for scraping unsplash. Only for educational purposes.

Install
======================

.. code-block:: python

    pip install unsplash_get

General usage
======================

.. code-block:: python

    from unsplash_get import search, save_img
    
    # get list of urls
    word = 'orange'
    urls = search(word)
    
    # store images if needed
    for key, url in enumerate(urls[:10]):
        file = '{}_{:03}.jpg'.format(word, key)
        save_img(url, file)

Load image to variable
======================

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

    # read image
    img = load_img(urls[0])
    print(img.shape)
