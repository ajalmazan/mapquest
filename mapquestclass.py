class Steps:
    def print_output(self, json_data):
        """Print out directions"""
        print('DIRECTIONS')
        for item in json_data['route']['legs']:
            for x in item['maneuvers']:
                print(x['narrative'])
    
class TotalDistance:
    def print_output(self, json_data):
        """Print out distance"""
        distance= json_data['route']['distance']
        print('Total Distance: '+str(int(distance))+' miles')

class TotalTime:
    def print_output(self, json_data):
        """Print out time"""
        time = int(json_data['route']['time'])/60
        print('Total Time: '+str(int(time))+' minutes')

class LatLong:
    def print_output(self, json_data):
        """Print out latitutde and longitude"""
        for item in json_data['route']['locations']:
            lat = item['latLng']['lat']
            lng = item['latLng']['lng']
            if lat > 0:
                lat = str('{:.2f}'.format(lat))+'N'
            else:
                lat = str('{:.2f}'.format(abs(lat)))+'S'
            if lng > 0:
                lng = str('{:.2f}'.format(lng))+'E'
            else:
                lng = str('{:.2f}'.format(abs(lng)))+'W'
            print(lat, lng)
 
def run_outputs(outputs:['output'], data):
    """Print output for each element in list"""
    for element in outputs:
        element.print_output(data)
        print()


