import mapquesturl
import mapquestclass

def user_interface() -> None:
    '''
    User interface for MapQuest outputs
    '''
    print("Enter number of locations")
    locations = _handle_integer_input(1)
    
    print("Enter starting location")
    start = input()
    
    print("Enter stop locations, return after each location")
    stop_list= _handle_stops(locations-1)
     
    print("Enter number of outputs, between 1 and 4")    
    number_of_outputs = _handle_outputlist(0,4)
    
    Print('Enter steps, latlong,totaldistance, or totaltime. Return after each input')
    output_list = _handle_print_input(number_of_outputs)
    
    data=mapquesturl.get_result(mapquesturl.mapquest_search_url(start,stop_list))

    print()
    _handle_print_outputs(output_list,data)

def _handle_outputlist(x:int, y:int) -> int:
    '''
    Handles outputlist input
    '''
    while True:
        integer_input = input()
        try:
            integer_input = int(integer_input)
            if integer_input > x and integer_input <= y:
                
                return integer_input
        except:
            print('Please input a positive integer greater than '+str(x) +' and less than or equal to ' + str(y))

            
        else:
            print('Please input a positive integer greater than '+str(x) +' and less than or equal to ' + str(y))
    
def _handle_integer_input(x:int) -> int:
    '''
    Handles integer input
    '''
    while True:
        integer_input = input()
        try:
            integer_input = int(integer_input)
            if integer_input > x:
                
                return integer_input
        except:
            print('Please input a positive integer greater than '+str(x))
            
        else:
            print('Please input a positive integer greater than '+str(x))

def _handle_stops(x:int) -> list:
    '''
    Creates list of stops
    '''
    stop_list = []
    for i in range(0,x):
        stop= input()
        stop_list.append(stop)
    return stop_list
    
def _handle_print_input(x:int) ->list:
    '''
    Asks what outputs user wants and appends the user input to a list
    '''
    
    output_list =[]
    for i in range(0,x):
        while True:
            output= input()
            if output.upper().strip()=='STEPS':
                output= mapquestclass.Steps()
                output_list.append(output)
                break
            elif output.upper().strip() =='TOTALDISTANCE':
                output= mapquestclass.TotalDistance()
                output_list.append(output)
                break
            elif output.upper().strip()=='TOTALTIME':
                output= mapquestclass.TotalTime()
                output_list.append(output)
                break
            elif output.upper().strip()=='LATLONG':
                output= mapquestclass.LatLong()
                output_list.append(output)
                break
            else:
                print('Please enter valid output type')
    return output_list
            
            
        
def _handle_print_outputs(output_list:list, data:'json') -> None:
    '''
    Prints user outputs from json data
    '''
    try:
        
        mapquestclass.run_outputs(output_list, data)
        
    except:
        
        print('Response is missing route property; no route found.')
        print('The most common cause for this is one of your locations does not exist')
        print('or was not specified in a format that MapQuest supports.')

    else:

        print('Directions Courtesy of MapQuest; Map Data Copyright OpenStreetMap Contributors')
    

if __name__=='__main__':
    user_interface()
