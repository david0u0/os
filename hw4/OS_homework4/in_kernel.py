def test(output):
	global OUT
	output("u32 fp;")
	for i in range(0, 1024):
		output('fp = open("'+str(i)+'.txt", G_WRITE);')
		output('write(input, 1024, fp);')

	output("gsys(LS_D);")
	
	for i in range(0, 1024):
		if i%2 == 0:
			output('gsys(RM, "' + str(i) + '.txt");')
	
	output("gsys(LS_D);")