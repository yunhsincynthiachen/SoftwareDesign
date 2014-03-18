# -*- coding: utf-8 -*-
"""
Created on Thu Feb 27 21:18:00 2014

@author: ychen1
"""

""" Goal of the project: To use python and pattern.web to parse through news articles
from google that state oscar predictions, in order to use sentiment analysis to extract data
and predict the oscars based off of all of the oscar predictions. If this doesn't work,
we will use twitter stream to use sentiment analysis on all of the twitters related to the
oscars, in order to predict what will be the best picture, best actress, best actor and best
director! 
"""

from pattern.web import *
from pattern.en import *
import matplotlib.pyplot as plt

oscarmovies = {'\"12 years a slave\"':'\"oscars\"will\"win',
               '\"wolf of wall street\"':'\"oscars\"will\"win', 
               '\"nebraska\"':'\"oscars\"will\"win', 
               '\"captain phillips\"':'\"oscars\"will\"win', 
               '\"dallas buyers club\"':'\"oscars\"will\"win',
               '\"american hustle\"':'\"oscars\"will\"win',
               '\"gravity\"':'\"oscars\"will\"win',
               '\"#her\"':'\"oscars\"will\"win',
               '\"philomena\"':'\"oscars\"will\"win'}
               
om = oscarmovies    #initializes a dictionary that we can use to search through Twitter for

	# I'll mention up here that you have done a beautiful job in terms of formatting here - your code
	# looks very clean and nice and is easy to read. You also did a very good job at breaking everything
	# down into small, modular functions, so kudos on that. I will mention, and Paul hasn't really talked about this
	# that much yet, but when you have a project this large it often makes sense to put groups of
	# associated functions in seperate scripts that are imported by your main script.

def oscarmoviestwittersearch():
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    	# This is a wonderfully helpful docstring, but the critical thing that you are missing in all of these
    	# is that a docstring should always specify what arguments it takes and what it returns. Be sure to
    	# do that in future
    L = []
    L2 = []
    t = Twitter()
    for key in om:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + om[key]):
            L.append(tweet.text)
            L2.append(sentiment(tweet.text))

    file = open('bestoscarmovietweets.txt','w') #opens a new file, writes all of our tweets to this file, and closes file
    # Be careful with this - file is a python type, and you don't want to use types or other keywords as variable names. It worked
    # out alright for you here, but avoid this in future.
    for i in L:
        file.write(str(i)+'\n')
    file.close()

def openbestoscarmoviefiletweets():
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    with open('bestoscarmovietweets.txt','r') as myfile:
    	# Good use of the with statement!
    	# Honestly, if you know how to use it I'm not sure why you didn't in the last function.
        data = myfile.readlines()
    return data
    
def makingtweetslowercase(data):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets = []
    for i in range(len(data)):
        tweets.append(data[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets

def finding_sentiment_analysis(index, lower_case_list):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index = []
    for j in index: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index.append((sentiment(lower_case_list[j])))
    return sent_index

def finding_tot_sentiment_for_movie(sent_index):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index:
        tot_sent += i[0]
    return tot_sent
    
##############################################################################################################

if __name__ == "__main__":
    
    lower_case_list = makingtweetslowercase(openbestoscarmoviefiletweets()) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    index_12yearsaslave = []
    index_wolf = []
    index_nebraska = []
    index_captainphillips = []
    index_dallas = []
    index_ah = []
    index_gravity = []
    index_her = []
    index_philomena = []
        
    for i in range(len(lower_case_list)):
        if '12 years a slave' in lower_case_list[i]:
            index_12yearsaslave.append(i)
        if 'wolf of wall street' in lower_case_list[i]:
            index_wolf.append(i)
        if 'nebraska' in lower_case_list[i]:
            index_nebraska.append(i)
        if 'gravity' in lower_case_list[i]:
            index_gravity.append(i)
        if 'captain phillips' in lower_case_list[i]:
            index_captainphillips.append(i)
        if 'dallas buyers club' in lower_case_list[i]:
            index_dallas.append(i)
        if 'american hustle' in lower_case_list[i]:
            index_ah.append(i)
        if '#her' in lower_case_list[i]:
            index_her.append(i)
        if 'philomena' in lower_case_list[i]:
            index_philomena.append(i)

    #we chose to do this outside of a function so that we have access to all of these lists individually, without appending them all into one huge list

    # Why? - instead of storing individual lists for each movie, you might have been able to make each movie's index list part of
    # a list and run functions on each element of that overall list. You can store lists in lists. Yes, it would mean that each movie's name then
    # is just an index in that list, but you could unpack the movies' lists at the end and reassociate their names with the data that you have crunched.
    # In fact, it looks like you are already effectively doing that with the labels at the end.
    # It would save you a fair amount of typing. Certainly, if you'd been dealing with more movies a solution like this would be worthwhile.
    # Also functionalizing parts of this may have saved you some code when running best actor and made your overall code much more compact.
    
    sent_12yearsaslave = finding_sentiment_analysis(index_12yearsaslave, lower_case_list)
    sent_wolfofwallstreet = finding_sentiment_analysis(index_wolf, lower_case_list)
    sent_nebraska = finding_sentiment_analysis(index_nebraska, lower_case_list)
    sent_captainphillips = finding_sentiment_analysis(index_captainphillips, lower_case_list)
    sent_dallas = finding_sentiment_analysis(index_dallas, lower_case_list)
    sent_ah = finding_sentiment_analysis(index_ah, lower_case_list)
    sent_gravity = finding_sentiment_analysis(index_gravity, lower_case_list)
    sent_her = finding_sentiment_analysis(index_her, lower_case_list)
    sent_philomena = finding_sentiment_analysis(index_philomena, lower_case_list)

    a = finding_tot_sentiment_for_movie(sent_12yearsaslave)
    b = finding_tot_sentiment_for_movie(sent_wolfofwallstreet)
    c = finding_tot_sentiment_for_movie(sent_nebraska)
    d = finding_tot_sentiment_for_movie(sent_captainphillips)
    e = finding_tot_sentiment_for_movie(sent_dallas)
    f = finding_tot_sentiment_for_movie(sent_ah)
    g = finding_tot_sentiment_for_movie(sent_gravity)
    h = finding_tot_sentiment_for_movie(sent_her)
    k = finding_tot_sentiment_for_movie(sent_philomena)
    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sumofsentiments = (a+b+c+d+e+f+g+h+k)/100
    sizes = [a/sumofsentiments,
             b/sumofsentiments,
             c/sumofsentiments,
             d/sumofsentiments,
             e/sumofsentiments,
             f/sumofsentiments,
             g/sumofsentiments,
             h/sumofsentiments,
             k/sumofsentiments]
    
    labels = ['12 Years a Slave','The Wolf of Wall Street','Nebraska','Gravity',
              'Captain Phillips','Dallas Buyers Club','American Hustle','Her','Philomena']
    colors = ['yellowgreen','gold','orange','red','lightskyblue','blue','lightcoral','purple','magenta']
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes,labels=labels,colors=colors,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()

################################

bestactor = {'\"Leonardo\"Dicaprio\"':'\"oscars\"best actor\"will win',
            '\"Matthew\"Mcconaughey\"':'\"oscars\"best actor\"will win',
            '\"Christian\"Bale\"': '\"oscars\"best actor\"will win',
            '\"Bruce\"Dern\"':'\"oscars\"best actor\"will win',
            '\"Chiwetel\"Ejiofor\"':'\"oscars\"best actor\"will win'}
ba = bestactor

def bestactortwittersearch():
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    # This seems redundant with your oscar movie twitter search function - you could take in a different
    # list (om or ba) and a filename to write, and then just use the exact same file twice. This is the point
    # of making your functions modular, and its already perfectly set up except for those two particular arguments.
    L3 = []
    L4 = []
    t = Twitter()
    for key in ba:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + ba[key]):
            L3.append(tweet.text)
            L4.append(sentiment(tweet.text))

    file = open('bestactortweets.txt','w') #opens a new file, writes all of our tweets to this file, and closes file
    for i in L3:
        file.write(str(i)+'\n')
    file.close()

def openbestactorfiletweets():
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    # Woah! This is definately the same function as above with a different name, just like above. For all of the functions in this
    # section you're doing exactly what functions are designed to allow you not to do: repeating yourself! Save yourself some work
    # and use modular functions to take in the one or two arguments here that need to change between the functions. That's why we
    # use functions!
    with open('bestactortweets.txt','r') as myfile2:
        data2 = myfile2.readlines()
    return data2
    
def makingactortweetslowercase(data2):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets2 = []
    for i in range(len(data2)):
        tweets2.append(data2[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets2
    
def findingactor_sentiment_analysis(index2, lower_case_list2):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index2 = []
    for j in index2: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index2.append((sentiment(lower_case_list2[j])))
    return sent_index2

def findingactor_tot_sentiment_for_movie(sent_index2):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent2 = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index2:
        tot_sent2 += i[0]
    return tot_sent2
    
##############################################################################################################

if __name__ == "__main__":
    lower_case_list2 = makingactortweetslowercase(openbestactorfiletweets()) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    index_leonardo = []
    index_matthew = []
    index_christian = []
    index_bruce = []
    index_chiwetel = []

    for i in range(len(lower_case_list2)):
        if 'leonardo' in lower_case_list2[i]:
            index_leonardo.append(i)
        if 'matthew' in lower_case_list2[i]:
            index_matthew.append(i)
        if 'christian' in lower_case_list2[i]:
            index_christian.append(i)
        if 'bruce' in lower_case_list2[i]:
            index_bruce.append(i)
        if 'chiwetel' in lower_case_list2[i]:
            index_chiwetel.append(i)

    
    #we chose to do this outside of a function so that we have access to all of these lists individually, without appending them all into one huge list
    
    sent_leonardo = findingactor_sentiment_analysis(index_leonardo, lower_case_list2)
    sent_matthew = findingactor_sentiment_analysis(index_matthew, lower_case_list2)
    sent_christian = findingactor_sentiment_analysis(index_christian, lower_case_list2)
    sent_bruce = findingactor_sentiment_analysis(index_bruce, lower_case_list2)
    sent_chiwetel = findingactor_sentiment_analysis(index_chiwetel, lower_case_list2)


    l = findingactor_tot_sentiment_for_movie(sent_leonardo)
    m = findingactor_tot_sentiment_for_movie(sent_matthew)
    n = findingactor_tot_sentiment_for_movie(sent_christian)
    o = findingactor_tot_sentiment_for_movie(sent_bruce)
    p = findingactor_tot_sentiment_for_movie(sent_chiwetel)

    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sumofsentiments2 = (l+m+n+o+p)/100
    sizes2 = [l/sumofsentiments2,
             m/sumofsentiments2,
             n/sumofsentiments2,
             o/sumofsentiments2,
             p/sumofsentiments2]
    
    labels2 = ['Leonardo Dicaprio','Matthew Mcconaughey','Christian Bale','Bruce Dern','Chiwetel Ejiofor']
    colors = ['yellowgreen','gold','orange','red','lightskyblue']
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes2,labels=labels2,colors=colors,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    
#################################

bestactress = {'\"Amy Adams\"':'\"oscars\"best actress\"will win',
              '\"Cate Blanchett\"':'\"oscars\"best actress\"will win',
              '\"Sandra Bullock\"':'\"oscars\"best actress\"will win',
              '\"Judi Dench\"':'\"oscars\"best actress\"will win',
              '\"Meryl Streep\"':'\"oscars\"best actress\"will win'}
             
bas = bestactress


def bestactresstwittersearch():
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    L5 = []
    L6 = []
    t = Twitter()
    for key in bas:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + bas[key]):
            L5.append(tweet.text)
            L6.append(sentiment(tweet.text))

    file = open('bestactresstweets.txt','w') #opens a new file, writes all of our tweets to this file, and closes file
    for i in L5:
        file.write(str(i)+'\n')
    file.close()

def openbestactressfiletweets():
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    with open('bestactresstweets.txt','r') as myfile3:
        data3 = myfile3.readlines()
    return data3
    
def makingactresstweetslowercase(data3):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets3 = []
    for i in range(len(data3)):
        tweets3.append(data3[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets3
    
def findingactress_sentiment_analysis(index3, lower_case_list3):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index3 = []
    for j in index3: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index3.append((sentiment(lower_case_list3[j])))
    return sent_index3

def findingactress_tot_sentiment_for_movie(sent_index3):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent3 = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index3:
        tot_sent3 += i[0]
    return tot_sent3
    
##############################################################################################################

if __name__ == "__main__":
    lower_case_list3 = makingactresstweetslowercase(openbestactressfiletweets()) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    index_amy = []
    index_cate = []
    index_sandra = []
    index_judi = []
    index_meryl = []

    for i in range(len(lower_case_list3)):
        if 'amy' in lower_case_list3[i]:
            index_amy.append(i)
        if 'cate' in lower_case_list3[i]:
            index_cate.append(i)
        if 'sandra' in lower_case_list3[i]:
            index_sandra.append(i)
        if 'judi' in lower_case_list3[i]:
            index_judi.append(i)
        if 'meryl' in lower_case_list3[i]:
            index_meryl.append(i)

    
    #we chose to do this outside of a function so that we have access to all of these lists individually, without appending them all into one huge list
    
    sent_amy = findingactress_sentiment_analysis(index_amy, lower_case_list3)
    sent_cate = findingactress_sentiment_analysis(index_cate, lower_case_list3)
    sent_sandra = findingactress_sentiment_analysis(index_sandra, lower_case_list3)
    sent_judi = findingactress_sentiment_analysis(index_judi, lower_case_list3)
    sent_meryl = findingactress_sentiment_analysis(index_meryl, lower_case_list3)


    q = findingactress_tot_sentiment_for_movie(sent_amy)
    r = findingactress_tot_sentiment_for_movie(sent_cate)
    s = findingactress_tot_sentiment_for_movie(sent_sandra)
    t = findingactress_tot_sentiment_for_movie(sent_judi)
    u = findingactress_tot_sentiment_for_movie(sent_meryl)

    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sumofsentiments3 = (q+r+s+t+u)/100
    sizes3 = [q/sumofsentiments3,
             r/sumofsentiments3,
             s/sumofsentiments3,
             t/sumofsentiments3,
             u/sumofsentiments3]
    
    labels3 = ['Amy Adams','Cate Blanchett','Sandra Bullock','Judi Dench','Meryl Streep']
    colors = ['yellowgreen','gold','orange','red','lightskyblue']
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes3,labels=labels3,colors=colors,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
    
####################################

bestdirector = {'\"David O\'Russell\"':'\"oscars\"best director\"will win',
               '\"Alfonso Cuaron\"': '\"oscars\"best director\"will win',
               '\"Alexander Payne\"':'\"oscars\"best director\"will win',
               '\"Steve McQueen\"':'\"oscars\"best director\"will win',
               '\"Martin Scorsese\"':'\"oscars\"best director\"will win'}
               
bd = bestdirector

def bestdirectortwittersearch():
    """ This function, which we only run once, produces a set of tweets that we can work with in a plaintext
    file. The output of this function is a file containing all of our tweets, separated by /n """
    L7 = []
    L8 = []
    t = Twitter()
    for key in bd:  #loops through all the keys in the dictionary, searching tweets for movie titles and words "Oscars", "will", and "win"
        for tweet in t.search(key + ' ' + bd[key]):
            L7.append(tweet.text)
            L8.append(sentiment(tweet.text))

    file = open('bestdirectortweets.txt','w') #opens a new file, writes all of our tweets to this file, and closes file
    for i in L7:
        file.write(str(i)+'\n')
    file.close()

def openbestdirectorfiletweets():
    """ This function opens the plaintext file and outputs it as a varaible that can be called"""
    with open('bestdirectortweets.txt','r') as myfile4:
        data4 = myfile4.readlines()
    return data4
    
def makingdirectortweetslowercase(data4):
    """This helps us search through all of the tweets by making all of the text in the tweets lowercase. The 
    function also creates a list of all our tweets which makes it easy for us to loop through them and search
    for the relevant information we need"""
    tweets4 = []
    for i in range(len(data4)):
        tweets4.append(data4[i].lower())  #so we simultaneously make all of the tweets lowercase while appending them to a list
    return tweets4
    
def findingdirector_sentiment_analysis(index4, lower_case_list4):
    """ This function takes as input a list of all the indices for the tweets which mentioned the relevant movie
    and the full data-set of tweets. Then, using the indices it has found, it produces the indvidual sentiments
    of each relevant tweet. """
    sent_index4 = []
    for j in index4: #loops through all the relevant tweets that pertain to each movie, find the sentiment analysis, and append it to a list
        sent_index4.append((sentiment(lower_case_list4[j])))
    return sent_index4

def findingdirector_tot_sentiment_for_movie(sent_index4):
    """ This function takes as input the list of all of the sentiments, takes only the first sentiment value which
    indicates the postivity or negatviity of the tweet, and sums all of the sentiments """
    tot_sent4 = 0    #initializes starting value for total sentiment for each movie at 0
    for i in sent_index4:
        tot_sent4 += i[0]
    return tot_sent4
    
##############################################################################################################

if __name__ == "__main__":
    bestdirectortwittersearch()
    lower_case_list4 = makingdirectortweetslowercase(openbestdirectorfiletweets()) #lower_case_list contains all of the tweets, in lowercase, in a list
    
    #we initialize a bunch of empty lists to store the indices of each tweet that contain any of these movie names
    index_david = []
    index_alfonso = []
    index_alexander = []
    index_steve = []
    index_martin = []

    for i in range(len(lower_case_list4)):
        if 'david' in lower_case_list4[i]:
            index_david.append(i)
        if 'alfonso' in lower_case_list4[i]:
            index_alfonso.append(i)
        if 'alexander' in lower_case_list4[i]:
            index_alexander.append(i)
        if 'steve' in lower_case_list4[i]:
            index_steve.append(i)
        if 'martin' in lower_case_list4[i]:
            index_martin.append(i)

    
    #we chose to do this outside of a function so that we have access to all of these lists individually, without appending them all into one huge list
    
    sent_david = findingdirector_sentiment_analysis(index_david, lower_case_list4)
    sent_alfonso = findingdirector_sentiment_analysis(index_alfonso, lower_case_list4)
    sent_alexander = findingdirector_sentiment_analysis(index_alexander, lower_case_list4)
    sent_steve = findingdirector_sentiment_analysis(index_steve, lower_case_list4)
    sent_martin = findingdirector_sentiment_analysis(index_martin, lower_case_list4)


    v = findingdirector_tot_sentiment_for_movie(sent_david)
    w = findingdirector_tot_sentiment_for_movie(sent_alfonso)
    x = findingdirector_tot_sentiment_for_movie(sent_alexander)
    y = findingdirector_tot_sentiment_for_movie(sent_steve)
    z = findingdirector_tot_sentiment_for_movie(sent_martin)

    
    #using matplotlib to produce a pie chart of the probabilities of each movie to win Best Picture for the Oscars
    sumofsentiments4 = (v+w+x+y+z)/100
    sizes4 = [v/sumofsentiments4,
             w/sumofsentiments4,
             x/sumofsentiments4,
             y/sumofsentiments4,
             z/sumofsentiments4]
    
    labels4 = ['David O\'Russell','Alfonso Cuaron','Alexander Payne','Steve Mcqueen','Martin Scorsese']
    colors = ['yellowgreen','gold','orange','red','lightskyblue']
    font = {'size':12}    
    plt.rc('font',**font)
    plt.pie(sizes4,labels=labels4,colors=colors,autopct='%1.1f%%')
    plt.axis('equal')
    plt.show()
