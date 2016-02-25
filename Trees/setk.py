total_driving_time = 0

for log_num in range(driver_log(ID)):
	driving_time = driver_log(ID)[log_num]["end"] - driver_log(ID)[log_num]["start"]
	break_time = driver_log(ID)[log_num+1]["start"] - driver_log(ID)[log_num]["end"]

	total_driving_time += driving_time

	if total_driving_time == 12 and break_time < 8:
		time.time() - driver_log(ID)[log_num]["end"]
		return ("You've driven for 12 hours without taking an 8 hour break in between, log back in %d hours and %d minutes" %(hours, minutes))
