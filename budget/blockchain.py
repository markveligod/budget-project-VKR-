__author__='by Mark Veligod'
import os
import json
import hashlib
import datetime
from kbk_basa import data_kbk
people_directory=os.curdir+'/block_people/'
statement_directory=os.curdir+'/block_statement/'



def record_block(
	directory,
	name_main, 
	name_section,  
	name_subsection,  
	name_pr,
	name_pod,
	name_event, 
	name_view,
	value, 
	data_time='', 
	hashing=''):
	files=sorting_file(directory)
	prev_file=files[-1]
	filename=str(prev_file+1)
	hashing=get_hashing(directory, str(prev_file))
	data_time=str(timer())
	kbk=assembly(name_main, name_section, name_subsection, name_pr, name_pod, name_event, name_view)
	data={
	"name_main": name_main,
	"name_section": name_section,
	"name_subsection": name_subsection,
	"name_pr": name_pr,
	"name_pod": name_pod,
	"name_event": name_event,
	"name_view": name_view,
	"value": value,
	"kbk": kbk,
	"data_time": data_time,
	"hashing": hashing
	}
	with open(directory + filename, 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=4, ensure_ascii=False)

def sorting_file(directory):
	file=os.listdir(directory)
	return sorted([int(i) for i in file])

def get_hashing(directory, filename):
	file=open(directory+filename, 'rb').read()
	return hashlib.md5(file).hexdigest()

def timer():
	time=datetime.datetime.now()
	return time

def check_block(directory):
	files=sorting_file(directory)
	result=[]
	for file in files[1:]:
		f=open(directory+str(file), encoding='utf-8')
		now_hash=json.load(f)['hashing']
		prev_file=str(file-1)
		prev_hash=get_hashing(directory, prev_file)
		if now_hash==prev_hash:
			res='Блок не поврежден'
		else:
			res='Блок поврежден'

		result.append({'Block': prev_file, 'Status': res})

	return result

def find_file(directory, name_request, data_find):
	result=[]
	data_result=[]
	data_not_result=[]
	files=os.listdir(directory)
	for file in files[1:]:
		with open(directory+str(file), encoding='utf-8') as o:
			name_ans=json.load(o)
			if name_request==name_ans[data_find]:
				result.append({'Status': 'Файл найден', 'Блок': file})
				data_result.append(name_ans)
			else:
				data_not_result.clear()
				data_not_result.append('Запрашиваемые данные отсутствуют. Введите корректные данные.')
	if result:
		return data_result
	else:
		return data_not_result


def assembly(name_main, name_section, name_subsection, name_pr, name_pod, name_event, name_view):
	result=[]
	result_not=[]
	x=[name_main, name_section, name_subsection, name_pr, name_pod, name_event, name_view]
	for i in x:
		if i in data_kbk:
			result.append(data_kbk[i])
		elif i == name_main not in data_kbk:
			result.append('000')
		elif i == name_section not in data_kbk:
			result.append('00')
		elif i == name_subsection not in data_kbk:
			result.append('00')
		elif i == name_pr not in data_kbk:
			result.append('00')
		elif i == name_pod not in data_kbk:
			result.append('0')
		elif i == name_event not in data_kbk:
			result.append('00')
		elif i == name_view not in data_kbk:
			result.append('00000 000')

	print(result)
	return result


def reg_user(name, password, directory):
	files=sorting_file(directory)
	prev_file=files[-1]
	filename=str(prev_file+1)
	hashing=get_hashing(directory, str(prev_file))
	data_time=str(timer())
	data={
	"name": name,
	"password": password,
	"data_time": data_time,
	"hashing": hashing,
	}
	with open(directory + filename, 'w', encoding='utf-8') as file:
		json.dump(data, file, indent=4, ensure_ascii=False)


# def main():
# 	record_block(directory=statement_directory,
# 	name_main='Министерство промышленности и торговли Российской Федерации', 
# 	name_section='Национальная экономика',  
# 	name_subsection='Общеэкономические вопросы',  
# 	name_pr='Государственная программа Российской Федерации "Развитие промышленности и повышение ее конкурентоспособности"',
# 	name_pod='Подпрограмма "Развитие системы технического регулирования, стандартизации и обеспечение единства измерений"',
# 	name_event='Основное мероприятие "Развитие системы технического регулирования и стандартизации"',
# 	name_view='Финансовое обеспечение выполнения функций федеральных государственных органов, оказания услуг и выполнения работ (Закупка товаров, работ и услуг для обеспечения государственных (муниципальных) нужд)', 
# 	value='58 439,8')
	# find_file(directory=statement_directory, name_request='Общегосударственные', data_find='name_section')
	# check_block(statement_directory)
	# assembly (
	# name_main='Федеральное агентство научных организаций', 
	# name_section='Общегосударственные вопросы',  
	# name_subsection='Международные отношения и международное сотрудничество',  
	# name_pr='Государственная программа Российской Федерации "Развитие культуры и туризма" на 2013 - 2020 годы',
	# name_pod='Подпрограмма "Искусство"',
	# name_event='Основное мероприятие "Организация и проведение мероприятий, а также работ по строительству, реконструкции, реставрации, посвященных значимым событиям российской культуры"',
	# name_view='Финансовое обеспечение выполнения функций федеральных государственных органов, оказания услуг и выполнения работ (Иные бюджетные ассигнования)')


# if __name__ == '__main__':
# 	main()







