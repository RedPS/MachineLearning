#!/usr/bin/env python3

import compress as c


data = c.load_data('Data/Train/')
c.compress_images(data,10)

