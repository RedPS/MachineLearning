#!/usr/bin/env python3

import compress as c


data = c.load_data('./Project4/Data/ToCompare')
Final_Result = c.compress_images(data,100)

print(Final_Result)
