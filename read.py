# Function to read the input Property File
def readInput(filename):
    # Open a file
    fp= open(filename,'r')
    line = fp.readline()
    url = ""
    while line:
        line = line[:-1]
        # Splitting each line into the Category and its inputs
        # data[0] contains the category
        # data[1] contains the values given by user in property file
        data = line.split(':')
        # Check for the category and whether it has any value associated by calculating the length
        if data[0]=="Location" and len(data[1])>0:
            url = url + ',"locations":['
            innerData = data[1].split(',')
            for i in range(0,len(innerData)):
                url = url + '"'+innerData[i]+'",'
            url = url[:-1]
            url = url + ']'    
        if data[0]=="JobType" and len(data[1])>0:
            innerData = data[1].split(',')
            # Check if Remote OK is present then change the url and remove from the list
            if "Remote OK" in innerData:
                url = url + ',"remote":true'
                innerData.remove("Remote OK")
            if len(innerData)>0:
                if  "Full Time" or "Contract" or "Internship" or "Cofounder" in innerData:
                    print "hello"
                    url = url + ',"types":['
                    innerData = data[1].split(',')
                    for i in range(0,len(innerData)):
                        if innerData[i] != "Remote OK":
                            if innerData[i] == "Full Time":
                                url = url + '"full-time",'
                            else:
                                url = url + '"' +innerData[i].lower()+'",'
                    url = url[:-1]
                    url = url + ']'
        if data[0]=="Role" and len(data[1])>0:
            url = url + ',"roles":['
            innerData = data[1].split(',')
            for i in range(0,len(innerData)):
                # Replace '/' with its unicode
                url = url + '"'+innerData[i].replace('/','%2F')+'",'
            url = url[:-1]
            url = url + ']'
            
        if data[0]=="Salary" and len(data[1])>0:
            url = url + ',"salary":{'
            innerData = data[1].split(',')
            url = url + '"min":' + innerData[0] +',"max":' + innerData[1] + '}'
            
        if data[0]=="Equity" and len(data[1])>0:
            url = url + ',"equity":{'
            innerData = data[1].split(',')
            url = url + '"min":' + innerData[0] + ',"max":' + innerData[1] + '}'
            
        if data[0]=="Size" and len(data[1])>0:
            url = url + ',"company_size":"' + data[1] + '"'

        if data[0]=="Funding" and len(data[1])>0:
            url = url + ',"company_stage":['
            innerData = data[1].split(',')
            for i in range(0,len(innerData)):
                url = url + '"'+innerData[i]+'",'
            # Trim the last ','
            url = url[:-1]
            # Add an eding bracket
            url = url + ']'
            
        if data[0]=="LastActive" and len(data[1])>0:
            url = url + ',"last_active":"' + data[1] + '"'
            
        if data[0]=="TopMarkets" and len(data[1])>0:
            url = url + ',"markets":['
            innerData = data[1].split(',')
            for i in range(0,len(innerData)):
                url = url + '"'+innerData[i]+'",'
            url = url[:-1]
            url = url + ']'

        if data[0]=="TopSkills" and len(data[1])>0:
            url = url + ',"skills":['
            innerData = data[1].split(',')
            for i in range(0,len(innerData)):
                url = url + '"'+innerData[i]+'",'
            url = url[:-1]
            url = url + ']'
        # Read next LIne
        line = fp.readline()

    # Because first character is ',' so remove it
    url = url[1:]
    # Create the final url
    url = 'https://angel.co/jobs#find/f!{' + url + '}'
    return url
