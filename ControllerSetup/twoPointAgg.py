import random

def goForTwoAgg(ourScore, oppScore, quarter, timeOnClock, quarterLength):

	goForTwo = False
	scoreDiff = ourScore - oppScore

	if scoreDiff < -9:
		goForTwo = True
	elif scoreDiff == -9:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			80/20
		elif quarter == 3:
			if timeOnClock > (quarterLength/2):
				goForTwo = True
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == -8:
		if quarter == 1:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True

		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11110')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('11110')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		else:
			goForTwo = True


	elif scoreDiff == -7:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('1111000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			ran = random.choice('1100000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == -6:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/3):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('11000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == -5:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11110')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True
		elif quarter == 3:
			if timeOnClock > (quarterLength/3) and timeOnClock < (2*quarterLength/3):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True
		elif quarter == 4:
			goForTwo = True

	elif scoreDiff == -4:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('11110')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 4:
			goForTwo = True

	elif scoreDiff == -3:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('1111000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == -2:
		if quarter == 1:
			ran = random.choice('11110')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/3):
				goForTwo = True
			else:
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 3:
			goForTwo = True
		elif quarter == 4:
			goForTwo = True

	elif scoreDiff == -1:
		if quarter == 1:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			if timeOnClock >= (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			elif timeOnClock > (quarterLength/4) and timeOnClock < (quarterLength/2):
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == 0:
		if quarter == 1:
			if timeOnClock > (2*quarterLength/3):
				goForTwo = True
			else:
				ran = random.choice('1111000000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		else:
			goForTwo = False

	elif scoreDiff == 1:
		if quarter == 1:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True
		elif quarter == 2:
			ran = random.choice('1111111100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			if timeOnClock > (2*quarterLength/3):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True
		elif quarter == 4:
			goForTwo = True

	elif scoreDiff == 2:
		if quarter == 1:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('1111000000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('1111000000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11110')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == 3:
		if quarter == 1:
			if timeOnClock > (quarterLength/3) and timeOnClock < (2*quarterLength/3):
				goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 3:
			goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == 4:
		if quarter == 1:
			if timeOnClock > (quarterLength/3) and timeOnClock < (2*quarterLength/3):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 3:
			ran = random.choice('11110')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == 5:
		if quarter == 1:
			goForTwo = True
		elif quarter == 2:
			goForTwo = True
		elif quarter == 3:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			goForTwo = True

	elif scoreDiff == 6:
		if quarter == 1:
			if timeOnClock > (quarterLength/3) and timeOnClock < (2*quarterLength/3):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('1111000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == 7:
		if quarter == 1:
			if timeOnClock > (quarterLength/3):
				goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 2:
			ran = random.choice('11000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/2):
				goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == 8:
		goForTwo = False
	elif scoreDiff == 9:
		if quarter == 1:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 2:
			ran = random.choice('11000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == 10:
		if quarter == 1:
			if timeOnClock > (quarterLength/2):
				goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/3):
				goForTwo = False
			else:
				ran = random.choice('11110')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == 11:
		if quarter == 1:
			if timeOnClock > (quarterLength/3):
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('11000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True

		elif quarter == 3:
			if timeOnClock > (quarterLength/3):
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == 12:
		if quarter == 1:
			ran = random.choice('1111111100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				ran = random.choice('1111111100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				ran = random.choice('1111000000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 3:
			if timeOnClock > (quarterLength/3):
				ran = random.choice('11000')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
			else:
				goForTwo = True
		elif quarter == 4:
			goForTwo = True

	elif scoreDiff == 13:
		if quarter == 1:
			ran = random.choice('1111000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			goForTwo = False
		elif quarter == 3:
			ran = random.choice('1111000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == 14:
		if quarter == 1:
			goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				goForTwo = False
			else:
				goForTwo = True
		elif quarter == 3:
			goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff == 15:
		if quarter == 1:
			goForTwo = True
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			ran = random.choice('1111111100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			goForTwo = False

	elif scoreDiff == 16:
		if quarter == 1:
			ran = random.choice('1111000000')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 2:
			if timeOnClock > (quarterLength/2):
				goForTwo = False
			else:
				ran = random.choice('11100')
				if ran == '1':
					goForTwo = True
				else:
					goForTwo = False
		elif quarter == 3:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	elif scoreDiff >= 17:
		if quarter == 1:
			goForTwo = False
		elif quarter == 2:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False
		elif quarter == 3:
			goForTwo = False
		elif quarter == 4:
			ran = random.choice('11100')
			if ran == '1':
				goForTwo = True
			else:
				goForTwo = False

	return goForTwo
