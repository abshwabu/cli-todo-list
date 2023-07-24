#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	actions = input("what do you want todo? \nadd\nshow\nexit")
	match actions:
		case 'add':
			task = input(userInput)
			todoList.append(task)
		case 'show':
			for todo in todoList:
				print(todo)
		case 'exit':
			break
		
		
		
		
		
