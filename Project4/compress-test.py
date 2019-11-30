#!/usr/bin/env python3

import compress as c


data = c.load_data('./Project4/Data/ToCompare')
c.compress_images(data,100)

