#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	actions = input("what do you want todo? \nadd\nshow\nedit\ndone\nclear all or \nexit\n: ")
	match actions:
		case 'add':
			task = input(userInput) + '\n'
			with open('list.txt','r') as file:
				todoList = file.readlines()
			
			todoList.append(task)
			with open('list.txt','w') as file:
				file.writelines(todoList)
			
		case 'show':
			with open('list.txt','r') as file:
				todoList = file.readlines()
			
			newTodo = []
			for item in todoList:
				newItem = item.strip('\n')
				newTodo.append(newItem)
			for index, task in enumerate(newTodo):
				print(index+1,task)
			with open('list.txt','w') as file:
				file.writelines(todoList)
		
		case 'edit':
			with open('list.txt','r') as file:
				todoList = file.readlines()
			
			for index, task in enumerate(todoList):
				task = task.strip('\n')
				print(index+1,task)
			num = int(input('which one do you want to edit \nEnter number: '))
			newTask = input('Enter the new task: ') + '\n'
			todoList[num-1]= newTask
			with open('list.txt','w') as file:
				file.writelines(todoList)
			
		case 'done':
			with open('list.txt','r') as file:
				todoList = file.readlines()
			
			for index, todo in enumerate(todoList):
				task = task.strip('\n')
				print(index+1,todo)
			num = int(input('which one do you finish \nEnter number: '))
			todoList.pop(num-1)
			with open('list.txt','w') as file:
				file.writelines(todoList)
			
		case 'clear all':
			with open('list.txt','r') as file:
				todoList = file.readlines()
			
			confirm = input('Are you sure[y/n]: ')
			match confirm:
				case 'y' | 'Y':
					todoList.clear()
					print('done')
				case 'n' | 'N':
					print('canceled')
			with open('list.txt','w') as file:
				file.writelines(todoList)
			
			
		case 'exit':
			break
		
		
		
		
		
