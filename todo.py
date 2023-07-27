#!/bin/python3

userInput = "Enter a task: "

todoList = []

while True:
	actions = input("what do you want todo? \nadd\nshow\nedit\ndone\nclear all or \nexit\n: ")
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
			newTodo = []
			for item in todoList:
				newItem = item.strip('\n')
				newTodo.append(newItem)
			for index, task in enumerate(newTodo):
				print(index+1,task)
			file = open('list.txt','w')
			file.writelines(todoList)
			file.close()
		case 'edit':
			file = open('list.txt','r')
			todoList = file.readlines()
			file.close()
			for index, task in enumerate(todoList):
				task = task.strip('\n')
				print(index+1,task)
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
			file = open('list.txt','w')
			file.writelines(todoList)
			file.close()
		case 'clear all':
			file = open('list.txt','r')
			todoList = file.readlines()
			file.close()
			confirm = input('Are you sure[y/n]: ')
			match confirm:
				case 'y' | 'Y':
					todoList.clear()
					print('done')
				case 'n' | 'N':
					print('canceled')
			file = open('list.txt','w')
			file.writelines(todoList)
			file.close()
			
		case 'exit':
			break
		
		
		
		
		
