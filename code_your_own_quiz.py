
answer_list1 = ['world','python','print','HTML']
input_list1 = ["___1___","___2___","___3___","___4___"]

answer_list2 = ['function','arguments','none','lists']
input_list2 = ["___1___","___2___","___3___","___4___"]

answer_list3 = ['class','method','__init__','instance','__repr__','__add__','__sub__','__lt__','__gt__','__eq__']
input_list3 = ["___1___","___2___","___3___","___4___","___5___","___6___","___7___","___8___","___9___","___10___"]

sentence1 =  '''
A common first thing to do in a language is display
"Hello ___1___!"  In ___2___ this is particularly easy; all you have to do is type in:
___3___ "Hello ___1___!"
Of course, that isn't a very useful thing to do. However, it is an example of how to output to the user using the ___3___ command, and produces a program which does something, so it is useful in that capacity.

It may seem a bit odd to do something in a Turing complete language that
can be done even more easily with an ___4___ file in a browser, but it's
a step in learning ___2___ syntax, and that's really its purpose.
'''

sentence2 = '''
A ___1___ is created with the def keyword. You specify the inputs a ___1___ takes by
adding ___2___ separated by commas between the parentheses. ___1___s by default return ___3___ if you
don't specify the value to return. ___2___ can be standard data types such as string, number, dictionary,
tuple, and ___4___ or can be more complicated such as objects and lambda functions.
'''

sentence3 = '''
When you create a ___1___, certain ___2___s are automatically generated for you if you don't make them manually. 
These contain multiple underscores before and after the word defining abs. 
When you write a ___1___, you almost always include at least the ___3___ ___2___, defining variables for when ___4___s of the ___1___ get made. Additionally, you generally want to create a ___5___ ___2___, which will allow a string representation of the 
method to be viewed by other developers.

You can also create binary operators, like ___6___ and ___7___, which
allow + and - to be used by ___4___s of the ___1___.  Similarly, ___8___,
___9___, and ___10___ allow ___4___s of the ___1___ to be compared with <, >, and ==.

'''


user_ans_list = []


def valid_select(difficulty):
	"""
		Checking user's input is valid or not.
		
		Args:
			difficulty: What the user inputs.
		
		Behavior:
			judge whether input is true or not
		
		Returns:
			Return value. valid or unvalid.
	"""
	
	if difficulty == "easy":
		choice = "valid"  
	elif difficulty == "medium":
		choice = "valid"   
	elif difficulty == "hard":
		choice = "valid"    
	else:
		choice = "unvalid"
		
	return choice


def is_input_list(sentence_word,input_list):
	"""
		Checking sentence_word is in input_list.
		
		Args:
			sentence_word: The word that will compare with input_list.
			input_list: The list that should be inputed by user.
		
		Behavior:
			Define whether the sentence_word is in input_list.
		
		Returns:
			If sentence_word is in input_list, return True. Otherwise, return False.
	"""
	
	for input_word in input_list:
		if input_word in sentence_word:
			return input_word
		
	return "none"


def correct_or_not(user_ans,ans_list):
	"""
		Checking user's answer is correct.
		
		Args:
			user_ans: What the user inputs.
			ans_list: The answer list.
		
		Behavior:
			Define whether user's answer is correct.
		
		Returns:
			If user_ans is correct, return True. Otherwise, return False.
	"""
	for ans_word in ans_list:
		if user_ans == ans_word:
			return True
	return False


def replace_all(sentence_string_list,input_word, user_ans):
	"""
		Replacing all the input_word to user_ans.
		
		Args:
			sentence_string_list: Consists of problem sentence word.
			input_word: The word that should be inputed by user.
			user_ans: What the user inputs.
			
		Behavior:
			Replace all the input_word to user_ans if the answer is correct.
		
		Returns:
			Nothing
	"""
	index = 0
	while index < len(sentence_string_list):
		if input_word in sentence_string_list[index]:
			sentence_string_list[index] = sentence_string_list[index].replace(input_word, user_ans)
		index += 1


def while_repeat(sentence_string_list,input_word,answer_list):
	"""
		Repeating user inputs the answer.
		
		Args:
			sentence_string_list: Consists of problem sentence word.
			input_word: The word that should be inputed by user.
			answer_list: The answer list.
		
		Behavior:
			While chances are left, user inputs the answer that they think it is right.
			
		Returns:
			If chances are left, return the string 'valid'. If not, return the string 'unvalid'.
	"""
	chance = 5
	Repeat = "Repeat"
	
	while Repeat == "Repeat":
		print " ".join(sentence_string_list)+"\n"
		user_ans = raw_input("Your answer of " + input_word + " is : ")

		if correct_or_not(user_ans,answer_list):

			user_ans_list.append(user_ans)
			replace_all(sentence_string_list,input_word, user_ans)
			print "/////Corrent!/////\n"
			Repeat = "Stop"

		else:
			chance -= 1
			print "/////Worng! You've got " + str(chance) + "chances left!/////\n"
			Repeat = "Repeat"

		if chance == 0:
			return "unvalid"
		
	return "valid"

def mad_libs_generator(sentence,answer_list,input_list):
	"""
		The main function.
		
		Args:
			sentence: The poblem sentence.
			answer_list: Literally, the answer list.
			input_list: The list that should be inputed by user.
		
		Behavior:
			First, split the sentence and judge that the sentence word should be entered.
			And then, recieve a input from users. If it is correct, replace all the sentence string to correct answer.
			All the splited sentence word will be collected in user_ans_list.
			Finally, the function will return user_ans_list's complete sentence.
		
		Returns:
			If the user solve the problem, it will returns complete sentence. Otherwise, it will return part of the sentence.
	"""
	sentence_string_list = sentence.split()
	your_chance = "valid"
	for sentence_word in sentence_string_list:
		
		input_word = is_input_list(sentence_word,input_list)
		
		if input_word != "none":
			
			your_chance = while_repeat(sentence_string_list,input_word,answer_list)
			
		else:
			user_ans_list.append(sentence_word)
		
		if your_chance == "unvalid":
			print "/////Try next time. This is what you've figured out./////"
			return " ".join(sentence_string_list)
		
	print "Nicely done."
	return " ".join(user_ans_list)

    
difficulty = raw_input("Select the game difficulty! You can choose easy, medium, and hard : ")

choice = valid_select(difficulty)


while choice == "unvalid":
    
    print "Wrong choice!"
	
    difficulty = raw_input("Select the game difficulty! You can choose easy, medium, and hard : ")
	
    choice = valid_select(difficulty)

if difficulty == "easy":
    print mad_libs_generator(sentence1,answer_list1,input_list1)	
	
if difficulty == "medium":
    print mad_libs_generator(sentence2,answer_list2,input_list2)
	
if difficulty == "hard":
	print mad_libs_generator(sentence3,answer_list3,input_list3)

