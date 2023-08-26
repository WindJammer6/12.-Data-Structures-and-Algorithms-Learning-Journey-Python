#Question 1:
#Below is the management hierarchy of a company.
    # Nilupul (CEO)
    #   |__Chinmay (CTO)
    #       |__Vishwa (Infrastructure Head)
    #       |__Dhaval (Cloud Manager)
    #       |__Abhijit (App Manager)
    #   |__Aamir (Application Head)
    #|__Gels (HR Head)
    #   |_Peter (Recruitment Manager)
    #   |__Waqas (Policy Manager)

#Extend tree class built in our main tutorial so that it takes name and designation in data part of 
#'GeneralTreeNode' class. Now extend print_tree function such that it can print either name tree, 
#designation tree or name and designation tree as shown below:

    #CEO
    #   |__CTO
    #       |__Infrastructure Head
    #           |__Cloud Manager
    #           |__App Manager
    #       |__Application Head
    #   |__HR Head
    #       |__Recruitment Manager
    #       |_ Policy Manager

    #OR

    #Nilupul
    #   |__Chinmay
    #       |__Vishwa
    #           |__Dhaval
    #           |__Abhijit
    #       |__Aamir
    #   |_ Gels
    #       |_ Peter
    #       |__Waqas

    #OR

    #Nilupul (CEO)
    #   |__Chinmay (CTO)
    #       |__Vishwa (Infrastructure Head)
    #           |__Dhaval (Cloud Manager)
    #           |__Abhijit (App Manager)
    #       |__Aamir (Application Head)
    #   |__Gels (HR Head)
    #       |_ Peter (Recruitment Manager)
    #       |__Waqas (Policy Manager)

#Here is how your main function should will look like,

    #if __name__ == '__main__':
    #    root_node = build_management_tree()
    #    root_node.print_tree("name")            # prints only name hierarchy
    #    root_node.print_tree("designation")     # prints only designation hierarchy
    #    root_node.print_tree("both")            # prints both (name and designation) hierarchy
    #starting point of our General Tree being at the Root Node (since 'root_node' variable is initially set as only


#About Python's 'copy' Library:
#It contains 2 functions, 'copy()' for shallow copy of an object, and 'deepcopy()'. for deep copy of an object.
#I used shallow copy, 'copy()' in this Excercise.

#Sometimes, shallow copy may not be enough to create a completely independent copy of an object (such as those with 
#class Instances). In these cases, you might want to consider using deep copying.

#From documentation:
#-> A shallow copy constructs a new compound object and then (to the extent possible) inserts references into it to 
#   the objects found in the original.
#-> A deep copy constructs a new compound object and then, recursively, inserts copies into it of the objects found 
#   in the original.

#There are some issues that may arise, but I feel they are a little advanced.
#From documentation:
#-> Recursive objects (compound objects that, directly or indirectly, contain a reference to themselves) may cause 
#   a recursive loop.
#-> Because deep copy copies everything it may copy too much, such as data which is intended to be shared between 
#   copies.


from copy import copy

class GeneralTreeNode:
    def __init__(self, data):
        self.data = data
        self.children = []
        self.parent = None              

    def add_child_node(self, child_node_data):
        child_node_data.parent = self
        return self.children.append(child_node_data)

    def get_level_of_node(self):
        level = 0
        p = self.parent
        while p:
            level += 1
            p = p.parent
        return level
    
    def only_designation_of_employee(self):
        #'find()' function finds the first occurrence of the specified value, and returns its index. Accepted 
        #parameters: 'string.find(value, start, end)' (see documentation). It is quite similar as the 'index()' 
        #function, the only difference is that the index() method raises an exception if the value is not found
        #while 'find()' returns -1 if value is not found
        first_character_in_parenthesis = self.data.find("(")
        last_character_in_parenthesis = self.data.find(")")
        #Need the '+ 1', as indexing always starts from plus one index after the start index
        self.data = self.data[first_character_in_parenthesis + 1:last_character_in_parenthesis]
        return self.data

    def only_name_of_emloyee(self):
        start_of_parenthesis = self.data.find("(")
        self.data = self.data[:start_of_parenthesis]
        return self.data

    def print_general_tree(self, desired_general_tree_output):
        if desired_general_tree_output == "both":
            number_of_spaces = ' ' * self.get_level_of_node() * 3
            prefix = number_of_spaces + "|__" if self.parent else ""
            print(prefix + self.data)
            if self.children:
                for child in self.children:
                    child.print_general_tree("both")

        if desired_general_tree_output == "name":
            #Usage of Python's 'copy' Library's 'copy()' function here
            general_tree_with_just_employee_names = copy(self)
            number_of_spaces = ' ' * general_tree_with_just_employee_names.get_level_of_node() * 3
            prefix = number_of_spaces + "|__" if general_tree_with_just_employee_names.parent else ""
            print(prefix + general_tree_with_just_employee_names.only_name_of_emloyee())
            if general_tree_with_just_employee_names.children:
                for child in general_tree_with_just_employee_names.children:
                    child.print_general_tree("name")

        if desired_general_tree_output == "designation":
            #Usage of Python's 'copy' Library's 'copy()' function here
            general_tree_with_just_employee_designation = copy(self)
            number_of_spaces = ' ' * general_tree_with_just_employee_designation.get_level_of_node() * 3
            prefix = number_of_spaces + "|__" if general_tree_with_just_employee_designation.parent else ""
            print(prefix + general_tree_with_just_employee_designation.only_designation_of_employee())
            if general_tree_with_just_employee_designation.children:
                for child in general_tree_with_just_employee_designation.children:
                    child.print_general_tree("designation")


def build_management_tree():

    root_node = GeneralTreeNode("Nilupul (CEO)")

    chieftechnologyofficer_cto = GeneralTreeNode("Chinmay (CTO)")

    infrastructure_head = GeneralTreeNode("Vishwa (Infrastructure Head)")
    infrastructure_head.add_child_node(GeneralTreeNode("Dhaval (Cloud Manager)"))
    infrastructure_head.add_child_node(GeneralTreeNode("Abhijit (App Manager)"))

    application_head = GeneralTreeNode("Aamir (Application Head)")

    chieftechnologyofficer_cto.add_child_node(infrastructure_head)
    chieftechnologyofficer_cto.add_child_node(application_head)


    humanresource_HR_head = GeneralTreeNode("Gels (HR Head)")
    humanresource_HR_head.add_child_node(GeneralTreeNode("Peter (Recruitment Manager)"))
    humanresource_HR_head.add_child_node(GeneralTreeNode("Waqas (Policy Manager)"))

    root_node.add_child_node(chieftechnologyofficer_cto)
    root_node.add_child_node(humanresource_HR_head)

    return root_node


if __name__ == '__main__':
    root_node = build_management_tree()
    root_node.print_general_tree("name")            # prints only name hierarchy
    root_node.print_general_tree("designation")     # prints only designation hierarchy
    root_node.print_general_tree("both")            # prints both (name and designation) hierarchy


#//////////////////////////////////////////////


#Analysis of my own answer, and comparing it to Solution:

#Printed output is the expected output, but my answer looks quite messy and uses a lot of brute force. My answer 
#works by using Python's 'find()' function (explanation of what it does above), to search for the parenthesis 
#within 'self.data' attributte of each 'GeneralTreeNode' object to extract the words in the parenthesis (for the 
#"designation" General Tree)/remove the parenthesis and the words within it (for the "name" General Tree) which will
#be the designation and name of the particular employee respectively and replacing the 'self.data' with only the 
#employee's designation/name that I extracted using other Instance Method created, 
#'only_designation_of_employee(self)' and 'only_name_of_employee(self)'.

#However, I later realised by making 
#'self.data = self.data[first_character_in_parenthesis+1:last_character_in_parenthesis]' 
#(for 'only_designation_of_employee(self)') or 'self.data = self.data[:start_of_parenthesis-1]' 
#(for 'only_name_of_employee(self)'), I am changing the original copy of my management General Tree Data Structure, so
#I thought I should first make a seperate copy of my original managament General Tree Data Structure, and modify them
#as well as return (to print them) seperately using the Instance Methods 'only_designation_of_employee(self)' and 
#'only_name_of_employee(self)' so that if I had to print the management General Tree Data Structure in my main 
#function more than once, there won't be any issue. (cuz if I didn't make a copy, and lets say I want to print a 
#"name" management General Tree, then a "both" management General Tree, the initial printing of "name" management
#General Tree would have modified my original management General Tree by deleting/removing the parenthesis containing
#the employee's designation of the 'GeneralTreeNode' Nodes to print just the "name" of the employees in the "name" 
#management General Tree. Then later, when I want to print the "both" management General Tree, I would only get the 
#"name" of the employee's since their designations no longer exist as they were deleted in the printing of the "name"
#management General Tree)

#Initially, to make I copy of my management General Tree Data Structure, I tried to do the usual 
#'general_tree_with_just_employee_names = self', but the returned, printed copy of my management General Tree Data 
#Structure became weird and wrong. So I tried using Python's 'copy' Library to import its '.copy()' function, which 
#seems to solve this problem. (explanation of what it does above)