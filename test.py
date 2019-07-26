from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import statistics

chromedriver_Path = "./chromedriver.exe"

test_number = 10
reading_file = "strings.txt"
result_file = "Result.txt"

# Test function
def Test(text):
    # Open chrome driver
    driver = webdriver.Chrome(chromedriver_Path)
    driver.get("https://www.google.com")
    assert "Google" in driver.title # Check if the title is google

    print("Test ediliyor -> " + text + "\n")

    # Do searching
    element = driver.find_element_by_name("q") 
    element.clear()
    element.send_keys(text)
    element.send_keys(Keys.RETURN)
    
    # Take result string
    rn = driver.find_element_by_id("resultStats").text.split()

    # Separate string into meaningful information 
    result_number = ""
    result_time = ""
    for i in rn:
        if i[0].isdigit() : result_number = i # 1.111.111
        if i[0] == "(" : result_time = i[1:] # (0,11
            
    driver.close()

    return [int(result_number.replace('.', '')), int(result_time.replace(',', ''))*10] # [number of results(int) , search time(int)(ms)]

# Read searching strings line by line
read_File = open(reading_file,"r")
searchList = []

searchList = read_File.read().splitlines()

read_File.close()


result = []
# Test for each string
for text in searchList:
    
    # Test
    f = []
    for i in range(test_number):
        f.append(Test(text))

    s_time = []
    for i in f:
        s_time.append(i[1]) # search time
    
    r = []
    r.append(f[0][0]) # number of results
    r.append(min(s_time))
    r.append(max(s_time))
    r.append(statistics.mean(s_time))

    result.append(r) # [results, min_time, max_time, ave_time]

open(result_file, 'w').close() # clear file
r_File = open(result_file,"a", encoding='utf-8') # open file

# write result array to new file
for i in result:
    r_File.write(str(i[0]) + " \t-> " + str(i[1]) + " " + str(i[2]) + " " + str(i[3]) + "\n")

r_File.close()
