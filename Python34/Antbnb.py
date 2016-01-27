import datetime
from collections import namedtuple
Reservation = namedtuple('Reservation','confirmation room arrival departure name')
def read_file(S:str)-> list:
    ''' Takes in a S that it uses to read  file then returns all line in that file as a list'''
    infile = open(S,'r')
    temp = []
    for line in infile:
        temp.append(line.replace('\n',''))
    return temp

def print_bedrooms(L:list)->None:
    ''' Takes in a list of bedrooms L and prints each one out per line'''
    for bedroom in L:
        print(bedroom)
def print_reservations(L:list)->None:
    ''' Takes in a list of reservations L and prints each one out per line'''
    print('Number of reservations:  '+str(len(L)))
    print('No. Rm. Arrive      Depart     Guest')
    print('------------------------------------------------')
    for res in L:
        temp = str.split(res.arrival,'/')
        temp2 = str.split(res.departure,'/')
        print('{:3d} {:3} {:2d}/{:2d}/{:4d} {:2d}/{:2d}/{:4d} {}'.format(res.confirmation,res.room,int(temp[0]),int(temp[1]),int(temp[2]),int(temp2[0]),int(temp2[1]),int(temp2[2]),res.name))
def return_int(s:str)->int:
    return int(s)
def return_int_arrival(R:Reservation)->int:
    temp = str.split(R.arrival,'/')
    return ((int(temp[2])-2000)*372+int(temp[0])*31+int(temp[1]))
def bedroom_only_one(B:list,s:str)->bool:
    for bed in B:
        if bed == s:
            return False
    return True
def process()->None:
    ''' Main process function, reads file and interprets it'''
    
    lines = read_file('input.txt')
    bedrooms = []
    reservations =  []
    conf = 1
    filename = input('Enter the file to where you want to save bedrooms and reservations: ')
    for line in lines:
        temp = str.split(line)
        command = temp[0].upper()
        if command == 'PL':
            print(line[3:])
        elif command == 'LB':
            bedrooms.sort(key=return_int)
            print('Number of bedrooms in service:  '+str(len(bedrooms)))
            print('------------------------------------')
            print_bedrooms(bedrooms)
        elif command == 'NB':
            if bedroom_only_one(bedrooms,temp[1]):
                bedrooms.append(temp[1])
        elif command == 'RB':
            bedrooms = remove_bedroom(temp[1],bedrooms)
            reservations = remove_reservations_bedroom(reservations,temp[1])
        elif command == 'NR':
            if check_if_open(bedrooms,temp[1]):
                holder = len(reservations)
                reservations = add_reservation(reservations,Reservation(conf,temp[1],temp[2],temp[3],' '.join(temp[4:])))
                if (holder < len(reservations)):
                    conf+=1
        elif command == 'LR':
            reservations.sort(key=return_int_arrival)
            print_reservations(reservations)
        elif command == 'RR':
            reservations = remove_reservation(int(temp[1]),reservations)
        elif command == 'BR':
            x = line.split()
            print('Reservations for room ' + x[1] + ':')
            for res in reservations:
                if res.room == x[1]:
                    print('   {:10} to {:10}:  {}'.format(res.arrival, res.departure, res.name))
        elif command == 'RG':
            print('Reservations for ' + line[3:] + ':')
            for res in reservations:
                if res.name == line[3:]:
                    print('   {:10} to {:10}:  room {:3}'.format(res.arrival, res.departure, res.room))
        elif command == 'LA':
            x = line.split()
            print('Guests arriving on ' + x[1] + ':')
            for res in reservations:
                if res.arrival == x[1]:
                    print('   ' + res.name + '(room ' + res.room + ')')
        elif command == 'LD':
            x = line.split()
            print('Guests departing on ' + x[1] + ':')
            for res in reservations:
                if res.departure == x[1]:
                    print('   ' + res.name + '(room ' + res.room + ')')
        elif command == 'LF':
            x = line.split()
            rooms = []
            reserved_rooms = []
            occupied_rooms = []
            print('Bedrooms free between ' + x[1] + ' to ' + x[2] + ':')
            for res in reservations:
                reserved_rooms.append(res.room)
                if check_if_available(res, x[1], x[2]):
                    rooms.append(res.room)
                else:
                    occupied_rooms.append(res.room)
            for bedroom in bedrooms:
                if bedroom not in reserved_rooms:
                    rooms.append(bedroom)
            for room_number in (set(rooms) - set(occupied_rooms)):
                print('   ' + room_number)
        elif command == 'LO':
            x = line.split()
            occupied_rooms = []
            print('Bedrooms occupied between ' + x[1] + ' to ' + x[2] + ':')
            for res in reservations:
                reserved_rooms.append(res.room)
                if check_if_available(res, x[1], x[2]) == False:
                    occupied_rooms.append(res.room)
            occupied_room_numbers = set(occupied_rooms)
            for room_number in occupied_room_numbers:
                print('   ' + room_number)
    print_to_new_file(filename,bedrooms,reservations)

def print_to_new_file(s:str,B:list,R:list)->None:
    outfile = open(s,'w')
    for bedroom in B:
        outfile.write('NB ' + bedroom + '\n')
    #outfile.write('LB\n')
    for reservation in R:
        outfile.write('NR ' + reservation.room + ' ' + reservation.arrival+' '+reservation.departure+ ' '+reservation.name +'\n')
    #outfile.write('LR\n')

def add_reservation(L:list,R:Reservation)->list:
    if check_dates(R):
        if check_dates3(L, R):
            L.append(R)
            print('Reserving room '+R.room+' for '+R.name+' -- Confirmation #'+str(R.confirmation))
            print('    (arriving '+R.arrival+', departing '+R.departure+')')
            return L
            
    #print("Sorry, can't reserve room "+ R.room+ " ("+R.arrival +' to ' + R.departure +");" + '\n' + '\t' + 'cant ')
    return L

def check_dates(R:Reservation)->bool:
    temp1 = str.split(R.arrival, '/')
    temp2 = str.split(R.departure, '/')
    token = True
    s = "Sorry, can't reserve room "+ R.room+ " ("+R.arrival +' to ' + R.departure +");" + '\n' + '\t'
    if int(temp1[2]) > int(temp2[2]):
          s +=  "can't leave before you arrive."
          token = False
    elif int(temp1[2]) < int(temp2[2]):
          return True
    elif int(temp1[0]) > int(temp2[0]):
          s +=  "can't leave before you arrive."
          token = False
    elif int(temp1[0]) < int(temp2[0]):
          return True
    elif int(temp1[1]) > int(temp2[1]):
          s +=  "can't leave before you arrive."
          token = False
    elif int(temp1[1]) == int(temp2[1]):
          s +=  "can't arrive and leave on the same day."
          token = False
    if token == False:
          print(s)
    return token

def check_dates2(s:str, s2:str)->bool:
    temp1 = str.split(s, '/')
    temp2 = str.split(s2, '/')
    #print(int(temp1[2]) > int(temp2[2]))
    #print(temp1,temp2)
    token = True
    if int(temp1[2]) >= int(temp2[2]):
        token = False
    elif int(temp1[2]) < int(temp2[2]):
        return True
    if int(temp1[0]) >= int(temp2[0]):
        token = False
    elif int(temp1[0]) < int(temp2[0]):
        return True
    if int(temp1[1]) > int(temp2[1]):
        token = False
    elif int(temp1[1]) <= int(temp2[1]):
        return True
    return token
def check_dates_equals(s:str,s2:str)->bool:
    temp1 = str.split(s, '/')
    temp2 = str.split(s2, '/')
    return temp1[2] == temp2[2] and temp1[0] == temp2[0] and temp1[1] == temp2[1]
def check_dates_less(s:str,s2:str)->bool:
    temp1 = str.split(s, '/')
    temp2 = str.split(s2, '/')
    if int(temp1[2]) < int(temp2[2]):
        return True
    elif int(temp1[2]) > int(temp2[2]):
        return False
    if int(temp1[0]) < int(temp2[0]):
        return True
    elif int(temp1[0]) > int(temp2[0]):
        return False
    if int(temp1[1]) < int(temp2[1]):
        return True
    return False
def check_dates_greater(s:str,s2:str)->bool:
    temp1 = str.split(s, '/')
    temp2 = str.split(s2, '/')
    if int(temp1[2]) > int(temp2[2]):
        return True
    elif int(temp1[2]) < int(temp2[2]):
        return False
    if int(temp1[0]) > int(temp2[0]):
        return True
    elif int(temp1[0]) < int(temp2[0]):
        return False
    if int(temp1[1]) > int(temp2[1]):
        return True
    return False

#print("Sorry, can't reserve room "+ R.room+ " ("+R.arrival +' to ' + R.departure +");" + '\n' + '\t' + "it's already booked (Conf. #" + str(R.confirmation) + ")")
def check_dates3(L:list, R:Reservation)->bool:
    for res in L:
        if res[1] == R[1]:
            if check_dates_less(R.arrival,res.arrival):
                if check_dates_greater(R.departure,res.arrival):
                    return False
            if check_dates_less(res.arrival,R.arrival):
                if check_dates_greater(res.departure,R.arrival):
                    return False
            if check_dates_equals(R.arrival,res.arrival):
                return False
                
    return True
           
def check_if_open(b:list,i:str)->bool:
    for room in b:
        if room == i:
            return True
    print("Sorry; can't reserve room "+i+"; room not in service")
    return False
def check_if_occupied(Reserve:list,R:Reservation)->bool:
    for res in Reserve:
        if res.room == R.room:
            if check_dates(R):
                if check_dates3(Reserve, R):
                    return True


        
    print("Sorry, can't reserve room "+ R.room+ " ("+R.arrival +' to ' + R.departure +");" + '\n' + '\t' + "it's already booked (Conf. #" + str(res.confirmation) + ")")
    return False
def remove_bedroom(s:str, b:list)-> list:
    for r in range(0,len(b)):
        if b[r] == s:
            temp = b[:r]
            temp.extend(b[r+1:])
            
    print("Sorry, can't delete room " + s + '; it is not in service now')
    return b

def remove_reservation(i:int, b:list)-> list:
    for r in range(0,len(b)):
        if b[r].confirmation == i:
            temp = b[:r]
            temp.extend(b[r+1:])
            return temp
    print("Sorry, can't cancel reservation; no confirmation number "+str(i))
    return b
def remove_reservations_bedroom(R:list,s:str)->list:
    temp = []
    for reserve in R:
        if reserve.room == s:
            temp.append(reserve)
    for gg in temp:
        print("Deleting room "+s+" forces cancellation of this reservation:")
        print("   "+gg.name + " arriving "+gg.arrival+" and departing " + gg.departure+ "(Conf. #"+str(gg.confirmation)+")")
        R = remove_reservation(gg.confirmation,R)
    return R



def check_if_available(r:Reservation, d1:str, d2:str)-> bool:
    a = datetime.datetime.strptime(d1, '%m/%d/%Y').date()
    b = datetime.datetime.strptime(d2, '%m/%d/%Y').date()
    token = True
    p = datetime.datetime.strptime(r.arrival, '%m/%d/%Y').date()
    q = datetime.datetime.strptime(r.departure, '%m/%d/%Y').date()
    if a < p < b:
        return False
    elif a < q < b:
        return False
    elif p < a < q:
        return False
    elif p < b < q:
        return False
    else:
        return True

process()
