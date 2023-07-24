#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	task = input(userInput)
	if task == './end':
		break
	else:
		
		
		todoList.append(task)
		
		for todo in todoList:
			print(todo)
