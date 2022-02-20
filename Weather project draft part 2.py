# for making get requests

import requests

# the method fetches the wetaher data and returns the result

def fetch_data(zip=None, city=None):

    # base url for fetching the weathre

    baseUrl = "http://api.openweathermap.org/data/2.5/weather"

    # api id for the site

    apiid = "9ce15d14e7da935370ed737856783cae"

    # check if the user gave the zip code or the city name

    if zip is not None:

        # us at the end id for usa country , change it as required

        baseUrl += "?zip="+str(zip)+",us"

    else:

        baseUrl += "?q="+str(city)+",us"

    # finally append the api id

    baseUrl += "&appid="+str(apiid)

    # make get requetss using requests module

    r = requests.get(baseUrl)

    # return the response

    return r

#this method shows teh result in readbale for,

def showResult(resp):

    #this means request was successfull

    if resp.status_code == 200:

        data= resp.json()

        print(data['name'])

        print(f"""{data['name']} Weather Forecast:

        There will be {data['weather'][0]['description']} with wind speed of {data['wind']['speed']}.

        Visibility will be {data['visibility']}.

        Min. Temp will be {data['main']['temp_min']} and max will be {data['main']['temp_max']}.

        """)

    else:

        print("Request Failed, Try Again Error Code : ",resp.status_code)

#main method , main drive rcode of teh progra,

def main():

    #until teh user eixtss keep runnign teh code

    while True:

        #show the user choices

        inp =int(input("Your options :\n1. By Zip Code\n2. By City Name\n3. Exit\n"))

        if inp == 1:

            #ask for zip code

            try:

                queryData=int(input("Enter zip code : "))

                #mak call to fetch fetch_data

                resp= fetch_data(queryData,None)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp == 2:

            try:

                queryData = input("Enter city name : ")

                #mak call to fetch fetch_data

                resp= fetch_data(None,queryData)

                showResult(resp)

            except Exception as ex:

                print("Error : ",ex)

        elif inp==3:

            break

        else:

            print("Invalid Choice..\n")





if __name__=="__main__":

    #call the main mtehod

    main()
