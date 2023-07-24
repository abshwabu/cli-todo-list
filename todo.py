#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	task = input(userInput)
	
	todoList.append(task)
	for todo in todoList:
		print(todo)
