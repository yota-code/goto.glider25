#!/usr/bin/env python3

import glider25

u = glider25.Glider25()

for i in range(2000) :
	u.step()

for i in range(1000) :
	u.step(rol=i / 1000.0)

for i in range(4000) :
	u.step(rol=1.0)

for i in range(1000) :
	u.step(rol=(1000 -i) / 1000.0)

for i in range(2000) :
	u.step()

u.save("test.tsv")