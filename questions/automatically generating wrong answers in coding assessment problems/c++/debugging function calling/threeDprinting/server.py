import random
import string
import copy

# ----------------------------------------------------------------
# PROBLEM DESCRIPTION
# ----------------------------------------------------------------

# This is a debugging problem about calling functions. Students need to both correctly choose the bug from a list of commonly seen bugs, AND correctly select how to fix the bug.

# This problem is about 3D printing. The original function was part of a multiple choice problem in either the F20 or W21 exam. Laura can't remember :) 


def generate(data):

    # ----------------------------------------------------------------
    # IMPORT FUNCTIONS FOR GENERATING ANSWERS
    # ----------------------------------------------------------------


    import sys
    sys.path.append(data["options"]["server_files_course_path"])
    from generatingAnswersCplusplus import make_parameters
    from generatingAnswersCplusplus import buggy_func_call_answers



    # get characters to use to generate random "id numbers" later
    letters = string.ascii_letters



    # ------------------------------------------------------------------------
    # DATA FOR THE PROBLEM -- JUST CHANGE THIS PART TO MAKE A NEW PROBLEM! :)
    # ------------------------------------------------------------------------

    # this is a super short "what's this function about" phrase 
    function_topic = "3D printing"

    # Here's a bunch of reasonable names we could pick for this function
    functionName = ["printEstimate","costEstimate","approxCost","costCalculation","printCost"]
    random.shuffle(functionName)

    # Here's a bunch of sets of parameters/arguments to choose from later

    # These are pass by value sets
    p_and_a_set_1 = [
        {
        "name": "volume",
        "type": "double",
        "pass_by_reference": False,
        "argument": "V",
        "description": "the volume of the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "volAmount",
        "type": "double",
        "pass_by_reference": False,
        "argument": "V_total",
        "description": "the volume of the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "printVol",
        "type": "double",
        "pass_by_reference": False,
        "argument": "printV",
        "description": "the volume of the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        }
    ]
    p_and_a_set_2 = [
        {
        "name": "filament_type",
        "type": "string",
        "pass_by_reference": False,
        "argument": "t",
        "description": "the type of filament to be used in the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "filament_option",
        "type": "string",
        "pass_by_reference": False,
        "argument": "opt",
        "description": "the option of filament to be used in the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "filament_id",
        "type": "string",
        "pass_by_reference": False,
        "argument": "ID_num",
        "description": "the ID number of the filament to be used in the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        }
    ]
    p_and_a_set_3 = [
        {
        "name": "weight",
        "type": "double",
        "pass_by_reference": False,
        "argument": "W",
        "description": "the weight per unit length of the filament to be used in the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "mass",
        "type": "double",
        "pass_by_reference": False,
        "argument": "M",
        "description": "the mass per unit length of the filament to be used in the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        },
        {
        "name": "density",
        "type": "double",
        "pass_by_reference": False,
        "argument": "D",
        "description": "the density of the filament to be used in the 3D print",
        "argument_value": str(round(random.uniform(2,8)*1.17,2))
        }
    ]
    p_and_a_set_4 = [
        {
        "name": "machine_type",
        "type": "string",
        "pass_by_reference": False,
        "argument": "machine_choice",
        "description": "the type of machine that will create the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "machine",
        "type": "string",
        "pass_by_reference": False,
        "argument": "choice",
        "description": "the type of machine that will create the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "printer_type",
        "type": "string",
        "pass_by_reference": False,
        "argument": "printer_choice",
        "description": "the type of printer that will create the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
        {
        "name": "printer",
        "type": "string",
        "pass_by_reference": False,
        "argument": "printer_option",
        "description": "the type of printer that will create the 3D print",
        "argument_value": "\"" + ''.join(random.choice(letters) for i in range(5)) + "\""
        },
    ]

    # Pass by reference sets
    p_and_a_set_5 = [
        {
        "name": "capacity",
        "type": "double",
        "pass_by_reference": True,
        "argument": "how_busy",
        "description": "how busy the 3D print lab currently is, as a percentage of full capacity (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
        {
        "name": "how_busy",
        "type": "double",
        "pass_by_reference": True,
        "argument": "capacity",
        "description": "how busy the 3D print lab currently is, as a percentage of full capacity (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
        {
        "name": "availability",
        "type": "double",
        "pass_by_reference": True,
        "argument": "percent_in_use",
        "description": "how many 3D printers are available to use, as a percentage of the total number of printers in the lab (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
        {
        "name": "percent_in_use",
        "type": "double",
        "pass_by_reference": True,
        "argument": "availability",
        "description": "how many 3D printers are available to use, as a percentage of the total number of printers in the lab (this value should be between 0 and 100)",
        "argument_value": str(random.randrange(0,10)*10)
        },
    ]


    # Here's a bunch of return variables to choose from later
    # For this type of question, let the assignment variables be the same
    # name as the return variables, since this is a "Level 1" type question
    return_variable_set_1 = [
        {
            "name": "filament",
            "type": "double",
            "description": "an estimate of the length of filament the 3D print will require",
            "assignment": "filament",
        },
        {
            "name": "lengthFil",
            "type": "double",
            "description": "an estimate of the length of filament the 3D print will require",
            "assignment": "lengthFil",
        },
        {
            "name": "filamentLength",
            "type": "double",
            "description": "an estimate of the length of filament the 3D print will require",
            "assignment": "filamentLength",
        },
        {
            "name": "filLength",
            "type": "double",
            "description": "an estimate of the length of filament the 3D print will require",
            "assignment": "filLength",
        }
    ]
    return_variable_set_2 = [
        {
            "name": "cost",
            "type": "double",
            "description": "how much the filament will costs for the 3D print",
            "assignment": "cost",
        },
        {
            "name": "customerCost",
            "type": "double",
            "description": "how much the filament will costs for the 3D print",
            "assignment": "customerCost",
        },
        {
            "name": "estCost",
            "type": "double",
            "description": "how much the filament will costs for the 3D print",
            "assignment": "estCost",
        },
        {
            "name": "filCost",
            "type": "double",
            "description": "how much the filament will costs for the 3D print",
            "assignment": "filCost",
        }
    ]
    return_variable_set_3 = [
        {
            "name": "printTime",
            "type": "double",
            "description": "the estimated time for the 3D print",
            "assignment": "printTime",
        },
        {
            "name": "time2print",
            "type": "double",
            "description": "the estimated time for the 3D print",
            "assignment": "time2print",
        },
        {
            "name": "print_time",
            "type": "double",
            "description": "the estimated time for the 3D print",
            "assignment": "print_time",
        },
        {
            "name": "time_to_print",
            "type": "double",
            "description": "the estimated time for the 3D print",
            "assignment": "time_to_print",
        }
    ]






    # ----------------------------------------------------------------
    # CREATE THE PROBLEM -- DON'T CHANGE ANYTHING FROM HERE ON DOWN
    # ----------------------------------------------------------------


    # shuffle all the specified information above; it helps with randomizing the problem variants
    random.shuffle(functionName)

    # shuffle the parameters/arguments and combine them into one set
    random.shuffle(p_and_a_set_1)
    random.shuffle(p_and_a_set_2)
    random.shuffle(p_and_a_set_3)
    random.shuffle(p_and_a_set_4)
    random.shuffle(p_and_a_set_5)

    p_and_a_set_all_PBV = [
        p_and_a_set_1,
        p_and_a_set_2,
        p_and_a_set_3,
        p_and_a_set_4
    ]
    random.shuffle(p_and_a_set_all_PBV)

    p_and_a_set_all_PBR = [
        p_and_a_set_5
    ]
    random.shuffle(p_and_a_set_all_PBR)

    # shuffle the random variables and combine them into one set
    random.shuffle(return_variable_set_1)
    random.shuffle(return_variable_set_2)
    random.shuffle(return_variable_set_3)
    return_variable_set_all = [return_variable_set_1,return_variable_set_2,return_variable_set_3]
    random.shuffle(return_variable_set_all)



    # Determine number of parameters and return variables for this question variant
    numParamsPBV = random.randint(1,2)
    numParamsPBR = random.randint(1,1)
    numReturnVars = random.randint(1,1) # make them all return a value for Assessment 3

    # Create the set of parameters and return variables
    parameter_set = []
    i = 0
    while i < numParamsPBV:
        parameter_set.append(p_and_a_set_all_PBV[i][0])
        i += 1
    i = 0
    while i < numParamsPBR:
        parameter_set.append(p_and_a_set_all_PBR[i][0])
        i += 1


    # shuffle the parameters
    random.shuffle(parameter_set)

    # now get the randomly chosen return variable, if there is one
    return_variable_set = []
    i = 0
    while i < numReturnVars:
        return_variable_set.append(return_variable_set_all[i][0])
        i += 1





    # Create a scenario so that random function headers can be created
    # all the ways to make variants have already been shuffled, so select the first one 
    # (or first N) of each thing

    # set up the parameter/argument information
    parameters = []
    parameter_types = []
    parameter_descriptions = []
    arguments = []
    argument_values = []
    j = 0
    while j < len(parameter_set):
        parameters.append(parameter_set[j]["name"])
        parameter_types.append(parameter_set[j]["type"])
        parameter_descriptions.append(parameter_set[j]["description"])
        arguments.append(parameter_set[j]["argument"])
        argument_values.append(parameter_set[j]["argument_value"])
        j += 1

    # set up the return variable information
    return_variables = []
    return_variable_types = []
    return_variable_descriptions = []
    assignments = []
    j = 0
    functionType = "void" # assume there are no return values and this is a void function
    while j < len(return_variable_set):
        return_variables.append(return_variable_set[j]["name"])
        return_variable_types.append(return_variable_set[j]["type"])
        return_variable_descriptions.append(return_variable_set[j]["description"])
        assignments.append(return_variable_set[j]["assignment"])
        functionType = return_variable_set[j]["type"] # if there is a return value, change the function type
        j += 1


    scenarios = [
        {
            "function_name": functionName[0],
            "function_type": functionType,
            "topic": function_topic,
            "parameters": parameter_set,
            "parameter_descriptions": parameter_descriptions,
            "return_variables": return_variable_set,
            "return_variable_descriptions": return_variable_descriptions,
            "arguments": arguments,
            "argument_values": argument_values,
            "assignments": assignments,
            "distractor_functions": ["func", "another_func" ],
            "distractor_types":[
                "string","char","int","double","bool", 
            ],
            "distractor_rvs":[
                "x",
                "isReliable" 
            ]
        }
    ]



    # Get the buggy answers
    buggy_answers = buggy_func_call_answers(scenarios[0])



    



    # ----------------------------------------------------------------
    # SAVE THE DATA FOR PRAIRIELEARN TO USE
    # ----------------------------------------------------------------

    # function description
    data['params']['functionName'] = scenarios[0]["function_name"]
    data['params']['topic'] = scenarios[0]["topic"]

    # create the parameter list of descriptions and the code to declare the arguments
    j = 0
    parameterList = ""
    argumentList = ""
    while j < len(parameter_set):
        parameterList += str(j+1) + ". " + scenarios[0]["parameter_descriptions"][j] + " \r\n"
        argumentList += scenarios[0]["parameters"][j]["type"] + " " + scenarios[0]["arguments"][j] + " = " + scenarios[0]["argument_values"][j] + "; \r\n"
        j += 1

    # create the return value list of descriptions
    j = 0
    returnVarList = ""
    while j < len(return_variable_set):
        returnVarList += str(j+1) + ". " + scenarios[0]["return_variable_descriptions"][j] + " \r\n"
        j += 1

    data['params']['parameterList'] = parameterList
    data['params']['argumentList'] = argumentList
    data['params']['returnVarList'] = returnVarList

    # create the function header
    functionHeader = scenarios[0]["function_type"] + " "
    functionHeader += scenarios[0]["function_name"]
    functionHeader += make_parameters(scenarios[0],True)
    functionHeader += " {"

    data['params']['functionHeader'] = functionHeader


    # list all the bugs
    ALL_BUGS  = []
    i = 0
    while i < len(buggy_answers):
        ALL_BUGS.append({'tag': 'false', 'ans': buggy_answers[i]["bug"]})
        i += 1


    # list all the fixes
    ALL_FIXES  = []
    i = 0
    while i < len(buggy_answers):
        ALL_FIXES.append({'tag': 'false', 'ans': buggy_answers[i]["fix"]})
        i += 1



    # shuffle random integers to correspond to the different wrong calls
    index_numbers = []
    i = 0
    while i < len(buggy_answers):
        index_numbers.append(i)
        i += 1
    random.shuffle(index_numbers)



    # Create the questions, but need to coordinate the void vs. non-void functions

    i = 1
    numProblems = 3
    iBug = 0
    while i <= numProblems:
        
        bug = buggy_answers[index_numbers[iBug]]["bug"]
        if numReturnVars == 0 and bug == "forgotten to store the return value from a non-void function":
            iBug += 1
            continue
        elif numReturnVars == 1 and bug == "tried to store a return value from a void function":
            iBug += 1
            continue
        else:
            questionName = "call" + str(i)
            data['params'][questionName] = buggy_answers[index_numbers[iBug]]["ans"]
            bugs = copy.deepcopy(ALL_BUGS)
            bugs[index_numbers[iBug]]['tag'] = 'true'
            bugsAnswers = "bugs" + str(i)
            data['params'][bugsAnswers] = bugs
            fixes = copy.deepcopy(ALL_FIXES)
            fixes[index_numbers[iBug]]['tag'] = 'true'
            fixesAnswers = "fixes" + str(i)
            data['params'][fixesAnswers] = fixes
            iBug += 1
            i += 1



    # # FUNCTION CALL 1
    # data['params']['call1'] = buggy_answers[index_numbers[0]]["ans"]
    # q1bugs = copy.deepcopy(ALL_BUGS)
    # q1bugs[index_numbers[0]]['tag'] = 'true'
    # data['params']['bugs1'] = q1bugs
    # q1fixes = copy.deepcopy(ALL_FIXES)
    # q1fixes[index_numbers[0]]['tag'] = 'true'
    # data['params']['fixes1'] = q1fixes

    # # FUNCTION CALL 2
    # data['params']['call2'] = buggy_answers[index_numbers[1]]["ans"]
    # q2bugs = copy.deepcopy(ALL_BUGS)
    # q2bugs[index_numbers[1]]['tag'] = 'true'
    # data['params']['bugs2'] = q2bugs
    # q2fixes = copy.deepcopy(ALL_FIXES)
    # q2fixes[index_numbers[1]]['tag'] = 'true'
    # data['params']['fixes2'] = q2fixes

    # # FUNCTION CALL 3
    # data['params']['call3'] = buggy_answers[index_numbers[2]]["ans"]
    # q3bugs = copy.deepcopy(ALL_BUGS)
    # q3bugs[index_numbers[2]]['tag'] = 'true'
    # data['params']['bugs3'] = q3bugs
    # q3fixes = copy.deepcopy(ALL_FIXES)
    # q3fixes[index_numbers[2]]['tag'] = 'true'
    # data['params']['fixes3'] = q3fixes

    # # FUNCTION CALL 4
    # data['params']['call4'] = buggy_answers[index_numbers[3]]["ans"]
    # q4bugs = copy.deepcopy(ALL_BUGS)
    # q4bugs[index_numbers[3]]['tag'] = 'true'
    # data['params']['bugs4'] = q4bugs
    # q4fixes = copy.deepcopy(ALL_FIXES)
    # q4fixes[index_numbers[3]]['tag'] = 'true'
    # data['params']['fixes4'] = q4fixes



