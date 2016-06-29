from sys import exc_info
import re, urllib.request

# List of given Urls
galleryList = []
# List of open page sourcecodes
galleryPages = []
# List of image ids found in page sourcecode
imageId = []
# List of open image page sourcecode
imagePage = []
#List of image source urls
imageUrl = []

def getGalleryList():
    global galleryList
    queryGalleryId = re.compile('[0-9]+')
    while(True):
        choice = str(input("Enter the Gallery Url:   (Write 'Break' to continue.)\n"))
        if choice.lower() == "break":
            break
        else:
            url = "http://www.imagefap.com/pictures/"
            galleryId = queryGalleryId.findall(choice)[0]
            url = url + galleryId + "/?gid={}&view=2".format(galleryId)
            print(url)
            galleryList.append(url)

def loadGalleryPage():
    global galleryList, galleryPages
    print("Loading Gallery Page")
    try:
        for page in galleryList:
            with urllib.request.urlopen(page) as f:
                galleryPages.append(f.read())
    except Exception as e:
        print("Unexpected Error: ", exc_info()[0], e)
        print("Error at loadGalleryPage")

def loadImagePage(pageUrl):
    try:
        with urllib.request.urlopen(pageUrl) as f:
            imagePage = f.read()
            return imagePage
    except Exception as e:
        print("Unexpected Error: ", exc_info()[0], e)
        print("Error at loadGalleryPage")

def getImagesInGallery():
    global imageId, galleryPages
    print("Getting Images In Gallery")
    try:
        queryImgId = re.compile('<td id="[0-9]+" align="center"  ?valign="top">')
        for gallery in galleryPages:
            result = queryImgId.findall(str(gallery))
            for item in result:
                string = item
                string = string.replace("<td","{")
                string = string.replace(">","}")
                string = string.replace("=",":")
                string = string.replace("id","'id'")
                string = string.replace("align",",'align'")
                string = string.replace("height",",'height'")
                string = string.replace("v,'align'",",'valign'")
                tag = eval(string)
                imageId.append(tag["id"])
        
    except Exception as e:
        print("Unexpected Error: ", exc_info()[0], e)
        print("Error at getImagesInGallery")

def findImageUrl():
    global imageId, imagePage, imageUrl
    print("Finding Image Urls")
    try:
        for picId in imageId:
            imagePage.append(loadImagePage("http://www.imagefap.com/photo/{}/".format(picId)))
        query = re.compile('"contentUrl": "[-_A-Za-z0-9\/\.:]+",')
        for page in imagePage:
            result = str(query.findall(str(page)))
            result = result.replace("['","{")
            result = result.replace("']","}")
            result = eval(result)
            print(result)
            imageUrl.append(result["contentUrl"])
        print("The following files have been queued for download:")
        for url in imageUrl:
            print(url)
    except Exception as e:
        print("Unexpected Error: ", exc_info()[0], e)
        print("Error at findImageUrl")

def downloadImage():
    global imageUrl
    try:
        for image in imageUrl:
            name = image.split("/")[-1].capitalize()
            print("Image Downloading: {}".format(name))
            imageContent = 0
            with urllib.request.urlopen(image) as f:
                imageContent = f.read()
            with open(name, "wb") as f:
                f.write(imageContent)
    except Exception as e:
        print("Unexpected Error: ", exc_info()[0], e)
        print("Error at downloadImage")

if __name__=="__main__":
    getGalleryList()
    loadGalleryPage()
    getImagesInGallery()
    findImageUrl()
    downloadImage()
