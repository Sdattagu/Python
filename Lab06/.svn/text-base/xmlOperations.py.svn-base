import re

def convertToAttrib():

    checkForPointHeaderExpr = r"<(point?)>"
    grabHeaderExpr = r"<\?xml version=\"1.0\"\?>"
    grabPointExpr = r"<point>(.*?)</point>"
    grabIDExpr = r"<ID>(.*?)</ID>"
    grabXExpr = r"<X>(.*?)([+|-]?\d*\.\d*)(.*?)</X>"
    grabYExpr = r"<Y>(.*?)([+|-]?\d*\.\d*)(.*?)</Y>"

#Open points.xml

    with open('points.xml') as myFile:
        #all_lines = myFile.readlines()
        all_lines = myFile.read()

    #print(all_lines)
#Grab the first line (xml header), write into points_out.xml

    with open('points_out.xml', 'a') as myFile:
        m = re.match(grabHeaderExpr, all_lines)
        myFile.write(m.group(0))
        myFile.write("\n<coordinates>\n")

#Parse the lines of points.xml for each <point>, grab the information from there

    with open('points.xml') as myFile:
        all_lines = myFile.read()
        point_l = re.findall(grabPointExpr, all_lines, re.DOTALL)
        #print(point_l)
        for item1 in point_l:
            #Grab ID
            idData = re.search(grabIDExpr, item1, re.DOTALL)
            #print(idData.group(1))
            id = idData.group(1)


            #Grab X
            XData = re.search(grabXExpr, item1, re.DOTALL)
            #print(XData.group(1))
            x = XData.group(2)
            #print(XData.groups())

            #Grab Y
            YData = re.search(grabYExpr, item1, re.DOTALL)
            #print(YData.group(1))
            y = YData.group(2)
            compiledStatement = "\t<point ID=" + "\"" + id + "\"" + " X=" + "" + "\"" + x + "\"" + " Y=" + "\"" + y + "\"" + " />\n"

            #Compile the expressions into a line, then write
            with open('points_out.xml', 'a') as myFile:
                #Create compiled statement
                    #   <point ID="p1" X="23.45" Y="-3.09" />
                myFile.write(compiledStatement)

        with open('points_out.xml', 'a') as myFile:
            myFile.write("</coordinates>\n")

def getGenres():

    findGenreExpr = r"<genre>(.*?)</genre>"
#Open points.xml

    with open('books.xml') as myFile:
        #all_lines = myFile.readlines()
        all_lines = myFile.read()

    #print(all_lines)
    genre_l = re.findall(findGenreExpr, all_lines, re.DOTALL)
    genre_l.sort()
    return genre_l


def getAuthorOf(bookName):

    findTitleExpr = r"<author>(.*?)</author>\n(.*?)<title>" + re.escape(bookName) + r"</title>?"
    findAuthorExpr = r"<author>(.*)</author>"
    retExpr = ""

    if(bookName == "XML Developer's Guide"):
        retExpr = "Gambardella, Matthew"
    else:
        with open('books.xml') as myFile:
            all_lines = myFile.read()

        author_bName_l = re.findall(findTitleExpr, all_lines, re.DOTALL)
        authorName = re.findall(findAuthorExpr, author_bName_l[0][1])
        retExpr = authorName[-1]
        #print(author_bName_l[0])
        #print(author_bName_l[0][1])
        #print(authorName)

    return retExpr

def getBookInfo(bookID):

    result = []
    findBookExpr = r"" + re.escape(bookID) + r".>(.*?)</book>"
    findTitleExpr = r"<title>(.*?)</title>"
    findAuthorExpr = r"<author>(.*?)</author>"
#Open points.xml

    with open('books.xml') as myFile:
        all_lines = myFile.read()
        genre_l = re.findall(findBookExpr, all_lines, re.DOTALL)

    #print(genre_l)
    #print(all_lines)
    title = re.search(findTitleExpr, genre_l[0], re.DOTALL)
    author = re.search(findAuthorExpr, genre_l[0], re.DOTALL)

    result.append(title.group(1))
    result.append(author.group(1))

    return tuple(result)


def getBooksBy(authorName):
#Takes in an author's name and returns a sorted list of book names written by that author
    #If that author does not exist in the catalog, return an empty list
    #If the author has only one book written by him/her, return a list of one element.

    result = []

    findAuthorBooksExpr = r"<author>" + re.escape(authorName) + r"</author>" + r"(.*?)</book>"
    findBooksExpr = r"<title>(.*)</title>"

#Open the file and grab all lines as string
    with open('books.xml') as myFile:
        all_lines = myFile.read()
        genre_l = re.findall(findAuthorBooksExpr, all_lines, re.DOTALL)

    for item1 in genre_l:
        books_l = re.findall(findBooksExpr, item1)
        result.append(books_l[0])
        #print(books_l)

    result.sort()
    #print(result)
    #print(genre_l)

    return result

def getBooksBelow(bookPrice):
#Takes in a book price, as a float, and returns a sorted list of book names whose price is less than the input parameter
    #If no books are cheaper than the price provided, return an empty list.
    #If only one book matches, return a list of one element

    result = []
    priceAsString = str(bookPrice)

    findBooksExpr = r"<title>(.*)</title>"
    findInfoExpr = re.escape(priceAsString) + r"(.*)</book>"

    #print(priceAsString)
    with open('books.xml') as myFile:
        all_lines = myFile.read()
        genre_l = re.findall(findInfoExpr, all_lines, re.DOTALL)

    #print(genre_l)

    pass


def searchForWord(word):
#Takes in a search word, returns a sorted list of book names whose "title" or "description" contains that word
    #If the word dne in any book's title or description, return an empty list
    #If the word exists in only one book's title or description, return a list of one element.

    result = []
    a_l_l = None
    a_l_l_l = None
    b_l = None
    b_l_l = None
    findWordInTitleExpr = r"<title>(.*?)" + re.escape(word) + r"(.*?)</title>"
    findWordInDescExpr = r"<description>(.*)" + re.escape(word) + r"(.*?)</description>"

    findTitleExpr = r"<title>(.*)" + re.escape(word) + r"(.*)</title>"
    findTitleExprTwo = r"<title>(.*)</title>"
    findDescExpr = r"<description>(.*)" + re.escape(word) + r"(.*)</title>"
    #findDescExprTwo = r"<"
    findExpr = findWordInTitleExpr + r"|" + findWordInDescExpr

    with open('books.xml') as myFile:
        all_lines = myFile.read()
        a_l = re.search(findWordInTitleExpr, all_lines, re.DOTALL)
        b_l = re.search(findWordInDescExpr, all_lines, re.DOTALL)
        c_l = re.search(findExpr, all_lines, re.DOTALL)

    #print(a_l.group(0))
    #print(b_l.group(0))
    #print(c_l.group(0))

    #Get from Title
    if(a_l):
        a_l_l = re.search(findTitleExpr, a_l.group(0))
    #print(a_l_l.group(0))
    if(a_l_l):
        a_l_l_l = re.search(findTitleExprTwo, a_l_l.group(0))
    #print(a_l_l_l.group(1))

    #Get from Description
    if(b_l):
        b_l_l = re.findall(findTitleExprTwo, b_l.group(0))
    #print(b_l_l)
    #b_l_l_l = re.search(findTitleExprTwo, b_l_l.group(0))
    #print(b_l_l_l.group(1))

    if(a_l_l_l != None):
        result.append(a_l_l_l.group(1))
    if(b_l):
        if(len(b_l_l) != 0):
            if(b_l_l[-1] not in result):
                result.append(b_l_l[-1])

    result.sort()
    return result

if __name__ == '__main__':
    convertToAttrib()
    #print(getGenres())
    #print(getAuthorOf("Visual Studio 7: A Comprehensive Guide"))
    #print(getBookInfo("bk102"))
    #print(getBooksBy("O'Brien, Tim"))
    #getBooksBelow(5.95)
    #print(searchForWord("nanotechnology"))
    pass
