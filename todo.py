#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	actions = input("what do you want todo? \nadd\nshow\nedit\ndone\nexit\n: ")
	match actions:
		case 'add':
			task = input(userInput)
			todoList.append(task)
		case 'show':
			for index, todo in enumerate(todoList):
				print(index+1,todo)
		case 'edit':
			num = int(input('which one do you want to edit \nEnter number: '))
			newTask = input('Enter the new task: ')
			todoList[num-1]= newTask
		case 'done':
			num = int(input('which one do you finish \nEnter number: '))
			todoList.pop(num-1)
			
		case 'exit':
			break
		
		
		
		
		
