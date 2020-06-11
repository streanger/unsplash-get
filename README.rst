unsplash_get
===========
Script for scraping unsplash. Only for educational purposes.

Install
===========

.. code-block:: python

    pip install unsplash_get

Usage from python
===========

.. code-block:: python

    from unsplash_get import search, save_img
    
    # get list of urls
    word = 'orange'
    urls = search(word)
    
    # store images if needed
    for key, url in enumerate(urls[:10]):
        file = '{}_{:03}.jpg'.format(word, key)
        save_img(url, file)
