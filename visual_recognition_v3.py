from __future__ import print_function
import json
from os.path import abspath
from watson_developer_cloud import VisualRecognitionV3, WatsonApiException
import os


clothes = []

visual_recognition = VisualRecognitionV3(
    '2018-03-19',
    url='https://gateway.watsonplatform.net/visual-recognition/api',
    iam_apikey='_rTi9ExzLh2F_cNt6NRksfQz_sAJ7NhdlXchff5poiF0')

filelist = os.listdir("assets/images/")
for i in filelist:
    if i.endswith(".jpg") or i.endswith(".jpeg"):
        print("...")
        with open("assets/images/" + i, 'rb') as images_file:
            classes = visual_recognition.classify(
                #[cv2.imread(img) for img in glob.glob("assets/images/*.jpg")],
                images_file,
                threshold='0.5',
                classifier_ids='DefaultCustomModel_2095219532').get_result()
            #print(json.dumps(classes, indent=2))
            thisItem = classes['images'][0].get('classifiers')[0].get('classes')
            if len(thisItem) > 1:
                print("!!!")
                macks = 0
                thing = {}
                for d in thisItem:
                    macks = max(macks, d['score'])
                    if macks == d['score']:
                        thing = d
                thisItem = [thing]
            clothes.append(thisItem)
            #clothes.append([])

for c in clothes:
    print(c)
