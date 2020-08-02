import requests,json
import os.path
import pprint

def requests_get(link_of_api):  
    url = requests.get(link_of_api)
    data_in_json = url.json()
    return data_in_json
requests_get("http://saral.navgurukul.org/api/courses")

url = requests.get("http://saral.navgurukul.org/api/courses")

exists = os.path.exists("/home/ravina/Documents/python_rinki1/courses.json")
if exists:
    file1 = open("courses.json",'r')
    data_in_json = url.json()
    json.dump(data_in_json,file1,sort_keys = True,indent = 4)
    
else:
    url = requests.get("http://saral.navgurukul.org/api/courses")
    file1 = open("courses.json",'w')
    data_in_json = url.json()
    json.dump(data_in_json,file1,sort_keys = True,indent = 4)

def courses_list():
    
    print("******* WELCOME TO COURSES OF SARAL *******","\n")

    i = 0
    while i<len(data_in_json["availableCourses"]):
        courses_name = data_in_json["availableCourses"][i]["name"]
        print(i,courses_name)
        i=i+1       
courses_list()

print(" ")
id = int(input("enter your any courses id then you will get that course name: "))

id_list = []
def id_courses():
    
    for index_of_course in range(len(data_in_json["availableCourses"])):
        courses_id = data_in_json["availableCourses"][index_of_course]["id"]
        id_list.append(courses_id)
    id_courses_name = data_in_json["availableCourses"][id]["name"]
    courses_user_id = data_in_json["availableCourses"][id]["id"]
    print(id,id_courses_name)
id_courses()


def id_courses1():
    
    for courses_index in range(len(data_in_json["availableCourses"])):
        courses_id = data_in_json["availableCourses"][courses_index]["id"]
    courses_user_id = data_in_json["availableCourses"][id]["id"]
    
    res =requests.get ("http://saral.navgurukul.org/api/courses/"+(courses_user_id)+"/exercises")
    api_data = res.json()
    # pprint.pprint(api_data)
    list_parents_slug = []
    
    print("#####  NOW WE WILL GET PARENTS AND CHILD EXERCISE:  #####)")
    def child_parents():

        id = int(input("enter your any courses id then you will get that course name: "))
        s_no = 0
        for parents in api_data['data']:
            child = parents['childExercises']
            print("\n")
            list_parents_slug.append(parents['slug'])
            print(s_no,parents['name'])
        
            s_no2 = 0
            slug_of_child = []
            for my_child in child:
                slug_of_child.append(my_child['slug'])
                print((5*(" ")),s_no2,my_child['name'])   
                s_no2 = s_no2 + 1    
            s_no = s_no + 1
    child_parents()

    up_user = input("enter your choice where you want to go UP/DOWN  if you will enter any thing except up so means you want to go down: ")
    if up_user == "up" or up_user == 'UP':
        courses_list()
        child_parents()
    
         
    normal_list = []
    user_slug = int(input("any index for parents "))
    parents_slug = api_data['data'][user_slug]['name']
    normal_list.append(api_data['data'][user_slug]['slug'])
    print(0,parents_slug)
    sNo = 1
    
   
    for child_slug in api_data['data'][user_slug]['childExercises']:
        print(((" ")*5),sNo,child_slug['name'])
        normal_list.append(child_slug['slug'])
        sNo=sNo+1
    
    choice = int(input("do you want content of child/parents if ha so enter your index for content "))
    
    print(" *******  NOW WE WILL GET CONTENT OF CHILD/PARENTS  ******* ","\n")
    
    slug_of_childParents = normal_list[choice]
   
    link_for_content = requests.get ("http://saral.navgurukul.org/api/courses/"+(courses_user_id)+"/exercise/getBySlug?slug="+(slug_of_childParents))
    content_in_json = link_for_content.json()
    print(content_in_json["content"])

    while True:
        user_choice = input("enter your choice previous page/next page P/N ")
        if user_choice == 'N' or user_choice == 'n':
            if (choice+1) < len(normal_list):
                slug_of_childParents = normal_list[choice+1]
                link_for_content = requests.get ("http://saral.navgurukul.org/api/courses/"+(courses_user_id)+"/exercise/getBySlug?slug="+( slug_of_childParents))
                content_in_json = link_for_content.json()
                print(content_in_json["content"])
                choice = choice + 1
            else:
                print(" SORRY, page is not able to find ")
                break
        elif user_choice == 'P' or user_choice == 'p':
            if choice >0 and choice < len(normal_list):
                slug_of_childParents = normal_list[choice-1]
                link_for_content = requests.get ("http://saral.navgurukul.org/api/courses/"+(courses_user_id)+"/exercise/getBySlug?slug="+( slug_of_childParents))
                content_in_json = link_for_content.json()
                print(content_in_json["content"])
                choice = choice - 1
            else:
                print("\n")
                print(" SORRY, page is not able to find ")
                break
        else:
            print("you entered wrong input not P and not N ")
            break

id_courses1()