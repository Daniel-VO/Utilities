"""
Created 21. January 2020 by Daniel Van Opdenbosch, Technical University of Munich

This program is free software: you can redistribute it and/or modify it under the terms of the GNU General Public License as published by the Free Software Foundation, either version 3 of the License, or (at your option) any later version. It is distributed without any warranty or implied warranty of merchantability or fitness for a particular purpose. See the GNU general public license for more details: <http://www.gnu.org/licenses/>
"""

import glob
import os
import ray

files=glob.glob('*.pdf')

ray.init()
funcs=[]

@ray.remote
def pdfcrop(i):
	return os.system('pdfcrop --hires '+i+' '+i)

for i in files:
	funcs.append(pdfcrop.remote(i))

ray.get(funcs)
