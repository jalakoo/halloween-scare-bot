def AI_PI_Transform(w,h,x,y):
	""" A function to translate x,y coordinates from Always AI screen
	to a Pyeye screen given the AI screen w,h,x and y 
	Input: 4 ints, return 2 ints """

	PI_w, PI_h = 60,60
	# The PI screen has 0,0 in the center; the translate values
	# shift the AI x,y coordiate to the correct location.
	PI_translate_y = 30 
	PI_translate_x = 30

	new_y = ((PI_h/h)*y)+PI_translate_y
	new_x = ((PI_w/w)*w)+PI_translate_x

	return new_x, new_y

