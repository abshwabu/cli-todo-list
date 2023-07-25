#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	actions = input("what do you want todo? \nadd\nshow\nexit\n: ")
	match actions:
		case 'add':
			task = input(userInput)
			todoList.append(task)
		case 'show':
			for index, todo in enumerate(todoList):
				print(index,todo)
		case 'edit':
			num = int(input('which one do you want to edit \nEnter number: '))
			newTask = input('Enter the new task: ')
			todoList[num-1]= newTask
			
		case 'exit':
			break
		
		
		
		
		
