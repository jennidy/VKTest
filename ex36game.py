from sys import exit

def office_space():
	print "You are in your office and your phone starts ringing. Do you answer the phone or ignore the phone?"
	
	choice = raw_input("> ")
	if choice == "answer phone":
		print "A voice tells you that your presence is required in Psychological Services."
		print "You know the way since you were just recently there for an IQ test."
		test_room()
	elif choice == "ignore phone":
		execution_room()
	else:
		print "I'm not sure why you'd do that to a telephone. How about trying 'answer phone' or 'ignore phone'?"
		print "Let's try this again."
		office_space() 
		
def execution_room():
	print "You have made a very bad choice, Leon."
	print "We know the truth about you, Leon"
	print "We are retiring your replicant ass, Leon."
	exit(0)
	
def test_room():
	print "A well-dressed man invites you to sit down. A odd machine sits on the table."
	print "You don't know why you're here again."
	print "You try to make small talk to break the tension."
	print "The well-dressed man takes a drag off of his cigarette."
	print "You don't like the looks of this. Do you stay or do you stand up and leave?"
	
	choice = raw_input("> ")
	if choice == "stay":
		print "Good. Let's begin."
	if "leave" in choice:
		execution_room() 
	
office_space () 

	


		