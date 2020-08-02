import json
import requests
import pprint
import os.path


def exists_data():
    exists = os.path.exists('courses2.json')
    if exists:
        with open("courses2.json" ,'r') as courses_file:
            data = courses_file.read()
            data_in_json = json.loads(data)
            
            # print(type(data_in_json)) #data in dict
            print("*****   WELCOME TO SARAL COURSES   *****","\n")
            s_no = 1
            for courses_index in (data_in_json["availableCourses"]):
                print(s_no,courses_index['name'])
                s_no = s_no + 1
            return data_in_json
            
            
    else:
        res = requests.get('http://saral.navgurukul.org/api/courses')
        with open('courses2.json', 'w') as courses_file:
            convert = res.json()
            json.dump(convert,courses_file)
courses = exists_data()
       

def select_course():
    select_index = int(input("select any index for course:- "))
    select_index = select_index - 1
    print(select_index,courses['availableCourses'][select_index]['name'])
    course_id = (courses['availableCourses'][select_index]['id'])
    return course_id
courseID = select_course()
# print(type(courseID))


def second_api():
    exists = os.path.exists("parents_child_exercise/parents"+courseID+'.json')
    if exists:
        with open("parents_child_exercise/parents"+courseID+'.json','r') as simple_file:
            data1 = simple_file.read()  # here data is in str
            data_file = json.loads(data1) # here data is changing str to dic
            return data_file
    else:
        
        res2 = requests.get("http://saral.navgurukul.org/api/courses/"+(courseID)+"/exercises")
        with open("parents_child_exercise/parents"+courseID+'.json', 'w') as simple_file:
            convert1 = res2.json()
            # print(type(convert1))
            json.dump(convert1,simple_file)
child_parents = second_api()
# pprint.pprint(child_parents)
    

def parents_child_exercise():
    s_no1 = 0
    print("#####   NOW YOU WILL GET PARENTS AND CHILD EXERCISE   #####")
    if len(child_parents['data']) > 0:
        for parents in child_parents['data']:
            my_child = parents['childExercises']
            print(s_no1,parents['name'])
            s_no1 = s_no1 + 1
            s_no2 = 0
            if len(my_child) > 0:
                for child in my_child:             
                    print((" ")*5,s_no2,child['name'])
                    s_no2 = s_no2 + 1
            else:
                print((" ")*5,"** child exercise is not here :- **")

        choice_exercise = int(input("enter your parent exercise with child exercise :- "))
        slug = []
        print(0,child_parents['data'][choice_exercise]['name'])
        parents_slug = (child_parents['data'][choice_exercise]['slug'])
        slug.append(parents_slug)
        s_no3 = 1
    
        for child_exercise in child_parents['data'][choice_exercise]['childExercises']:
            print((" ")*5,s_no3,child_exercise['name'])
            child_slug = (child_exercise['slug'])
            slug.append(child_slug)
            s_no3 = s_no3 + 1
        return(slug)
    else:
        print("sorry parents is not here:-")
exercise_slug = parents_child_exercise()


choice_slug = int(input("any slug "))
user_slug = (exercise_slug[choice_slug])


def content():
    if(not os.path.exists("parents_child_slug/slug"+user_slug.split('/')[0])):
        os.mkdir("parents_child_slug/slug"+user_slug.split('/')[0])
    exists = os.path.exists("parents_child_slug/slug"+user_slug+'.json')
    if exists:
        with open("parents_child_slug/slug"+user_slug+'.json', 'r') as slug_file:
            data2 = slug_file.read()
            data1_in_file = json.loads(data2) # here data is changing str to dic
            print(data1_in_file['content'])
            print(courseID)
    else:
        res3 = requests.get("http://saral.navgurukul.org/api/courses/"+(courseID)+"/exercise/getBySlug?slug="+(user_slug))
        with open("parents_child_slug/slug"+user_slug+'.json', 'w') as slug_file:
            convert2 = res3.json()
            json.dump(convert2,slug_file)
            # pprint.pprint(convert2)
content()
