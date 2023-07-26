#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	actions = input("what do you want todo? \nadd\nshow\nedit\ndone\nexit\n: ")
	match actions:
		case 'add':
			task = input(userInput) + '\n'
			file = open('list.txt','r')
			todoList = file.readlines()
			file.close()
			todoList.append(task)
			file = open('list.txt','w')
			file.writelines(todoList)
			file.close()
		case 'show':
			file = open('list.txt','r')
			todoList = file.readlines()
			file.close()
			for index, todo in enumerate(todoList):
				print(index+1,todo)
			file = open('list.txt','w')
			file.writelines(todoList)
			file.close()
		case 'edit':
			file = open('list.txt','r')
			todoList = file.readlines()
			file.close()
			for index, todo in enumerate(todoList):
				print(index+1,todo)
			num = int(input('which one do you want to edit \nEnter number: '))
			newTask = input('Enter the new task: ') + '\n'
			todoList[num-1]= newTask
			file = open('list.txt','w')
			file.writelines(todoList)
			file.close()
		case 'done':
			file = open('list.txt','r')
			todoList = file.readlines()
			file.close()
			for index, todo in enumerate(todoList):
				print(index+1,todo)
			num = int(input('which one do you finish \nEnter number: '))
			todoList.pop(num-1)
			
		case 'exit':
			break
		
		
		
		
		
