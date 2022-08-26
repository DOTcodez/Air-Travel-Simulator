from time import sleep
from geopy.distance import distance

def convert(seconds):
    seconds = seconds % (24 * 3600)
    hour = seconds // 3600
    seconds %= 3600
    minutes = seconds // 60
    seconds %= 60
    return "{}hrs {}mins {}secs".format(hour, minutes, seconds)

def navigate(lat1,lon1,lat2,lon2):

    dist = distance((lat1,lon1),(lat2,lon2)).km #total distance (km)
    
    speed = 0.222222 #Average aircraft speed = 800 km/hr = 0.222222km/sec
    
    time = convert(round(dist/speed)) #how long the journey will take (secs)
    
    refresh_rate = 10 #how much delay before each refresh (secs)

    if(dist > 0):
        dist_ratio = (refresh_rate * speed) / dist #ratio of total distance covered per refresh(km)
        refresh_distance = ((dist_ratio * dist)/111) #actual distance covered on earths surface per refresh (degrees)

    print('\nMoving from lat{}`/lon{}` to lat{}`/lon{}. Distance = {}km. Time = {}secs. refresh at {}secs` \n'.format(lat1,lon1,lat2,lon2,dist,time,refresh_rate))

    if(dist > 0):

        if((lon1 <= -60) and (lon2 >= 120)):
            
            print('lat{}`/lon{}`'.format(lat1,lon1))
            if(lat1 == lat2):
                while(lon1 < lon2):
                    # sleep(refresh_rate)
                    lon1 = round(lon1 - refresh_distance,4)
                    if(lon1 <- 180):
                        lon1 = round(180 - refresh_distance,4) 
                        break
                    print('lat{}`/lon{}`'.format(lat1,lon1)) 
                while(lon1 >= lon2):
                    # sleep(refresh_rate)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                    lon1 = round(lon1 - refresh_distance,4)
                print('\n Arrived...')

            elif(lat1 > lat2):
                londiff = (lon1 - (-180)) + (180 - lon2)
                latdiff = abs(lat1 - lat2)
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                print(lat_rate)
                while(lon1 < lon2):
                    # sleep(refresh_rate)
                    lon1 = lon1 - lon_rate
                    lat1 = lat1 - lat_rate
                    if(lon1 < -180):
                        lon1 = 180 - lon_rate
                        lat1 = lat1 - lat_rate
                        break
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))   
                while((lon1 >= lon2) and (lat1 >= lat2)):
                    # sleep(refresh_rate)
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))
                    lon1 = lon1 - lon_rate
                    lat1 = lat1 - lat_rate
                print('\n Arrived...')
            
            else:
                londiff = (lon1 - (-180)) + (180 - lon2)
                latdiff = lat2 - lat1
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                while(lon1 < lon2):
                    # sleep(refresh_rate)
                    lon1 = lon1 - lon_rate
                    lat1 = lat1 + lat_rate
                    if(lon1 < -180):
                        lon1 = 180 - lon_rate 
                        break
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))    
                while((lon1 >= lon2) and (lat1 <= lat2)):
                    # sleep(refresh_rate)
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))
                    lon1 = lon1 - lon_rate
                    lat1 = lat1 + lat_rate
                print('\n Arrived...')

        elif((lon1 >= 120) and (lon2 <= -60)):
        
            print('lat{}`/lon{}`'.format(lat1,lon1))
            if(lat1 == lat2):
                while(lon1 > lon2):
                    # sleep(refresh_rate)
                    lon1 = round(lon1 + refresh_distance,4)
                    if(lon1 > 180):
                        lon1 = round(-180 + refresh_distance,4) 
                        break
                    print('lat{}`/lon{}`'.format(lat1,lon1))          
                while(lon1 <= lon2):
                    # sleep(refresh_rate)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                    lon1 = round(lon1 + refresh_distance,4)
                print('\n Arrived...')
            
            elif(lat1 > lat2):
                londiff = (180 - lon1) + (lon2 - (-180))
                latdiff = lat1 - lat2
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                while(lon1 > lon2):
                    # sleep(refresh_rate)
                    lon1 = lon1 + lon_rate
                    lat1 = lat1 - lat_rate
                    if(lon1 > 180):
                        lon1 = -180 + lon_rate 
                        break
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))   
                while((lon1 <= lon2) and (lat1 >= lat2)):
                    # sleep(refresh_rate)
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))
                    lon1 = lon1 + lon_rate
                    lat1 = lat1 - lat_rate
                print('\n Arrived...')
            
            else:
                londiff = (180 - lon1) + (lon2 - (-180))
                latdiff = lat2 - lat1
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                while(lon1 > lon2):
                    # sleep(refresh_rate)
                    lon1 = lon1 + lon_rate
                    lat1 = lat1 + lat_rate
                    if(lon1 > 180):
                        lon1 = -180 + lon_rate 
                        break
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))    
                while((lon1 <= lon2) and (lat1 <= lat2)):
                    # sleep(refresh_rate)
                    print('lat{}`/lon{}`'.format(round(lat1,4),round(lon1,4)))
                    lon1 = lon1 + lon_rate
                    lat1 = lat1 + lat_rate
                print('\n Arrived...')
        
        else:

            if ((lon1 > lon2) and (lat1 > lat2)):
                londiff = lon1 - lon2
                latdiff = lat1 - lat2
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while((lon1 >= lon2) and (lat1 >= lat2)):
                    sleep(refresh_rate)
                    lon1 = round(lon1 - lon_rate,4)
                    lat1 = round(lat1 - lat_rate,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            elif ((lon1 < lon2) and (lat1 < lat2)):
                londiff = lon1 - lon2
                latdiff = lat1 - lat2
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while((lon1 <= lon2) and (lat1 <= lat2)):
                    sleep(refresh_rate)
                    lon1 = round(lon1 + lon_rate,4)
                    lat1 = round(lat1 + lat_rate,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            elif ((lon1 < lon2) and (lat1 > lat2)):
                londiff = abs(lon2 - lon1)
                latdiff = abs(lat2 - lat1)
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while((lon1 <= lon2) and (lat1 >= lat2)):
                    sleep(refresh_rate)
                    lon1 = round(lon1 + lon_rate,4)
                    lat1 = round(lat1 - lat_rate,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            elif ((lon1 > lon2) and (lat1 < lat2)):
                londiff = abs(lon2 - lon1)
                latdiff = abs(lat2 - lat1)
                totdiff = londiff + latdiff
                lon_rate = ((londiff/totdiff)*refresh_distance)
                lat_rate = ((latdiff/totdiff)*refresh_distance)
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while((lon1 >= lon2) and (lat1 <= lat2)):
                    sleep(refresh_rate)
                    lon1 = round(lon1 - lon_rate,4)
                    lat1 = round(lat1 + lat_rate,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')
            

            elif ((lon1 == lon2) and (lat1 > lat2)):
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while(lat1 >= lat2):
                    # sleep(refresh_rate)
                    lat1 = round(lat1 - refresh_distance,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            elif ((lon1 == lon2) and (lat1 < lat2)):
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while(lat1 <= lat2):
                    # sleep(refresh_rate)
                    lat1 = round(lat1 + refresh_distance,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            elif ((lon1 > lon2) and (lat1 == lat2)):
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while(lon1 >= lon2):
                    # sleep(refresh_rate)
                    lon1 = round(lon1 - refresh_distance,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            elif ((lon1 < lon2) and (lat1 == lat2)):
                print('lat{}`/lon{}`'.format(lat1,lon1))
                while(lon1 <= lon2):
                    # sleep(refresh_rate)
                    lon1 = round(lon1 + refresh_distance,4)
                    print('lat{}`/lon{}`'.format(lat1,lon1))
                print('\n Arrived...')

            else:
                print('\n Co-ordinates are thesame...')
    
    else: print('\n Same location')
    

def redirect(current_lat,current_long,destination_lat,destination_long):
    navigate(current_lat,current_long,destination_lat,destination_long)



print('Enter the cordinates of country 1')
Lat1 = round(float(input('Latitude :')),4)
Lon1 = round(float(input('Longitude :')),4)

print('Enter the cordinates of country 2')
Lat2 = round(float(input('Latitude :')),4)
Lon2 = round(float((input('Longitude :'))),4)

navigate(Lat1,Lon1,Lat2,Lon2)